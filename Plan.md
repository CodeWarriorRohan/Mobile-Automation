# Appium Android Automation — Project Plan

## Overview

**Goal**: Build a fully scaffolded mobile automation framework for Android using Python.

| Detail | Choice |
|---|---|
| Platform | Android only (emulator via Android Studio) |
| Language | Python 3.11+ |
| Test Framework | pytest + Allure reporting |
| Design Pattern | Page Object Model (POM) |
| App Type | Native + Hybrid (WebView) |
| Appium Driver | UiAutomator2 (via Appium 2.x) |
| App Under Test | Your own APK |

---

## Phase 1 — Prerequisites & Environment Setup

### Step 1 — Install Node.js 18+ LTS

- Download from [nodejs.org](https://nodejs.org) (Windows .msi installer)
- Verify:
  ```powershell
  node --version     # → 18.x+
  npm --version      # → 9.x+
  ```

### Step 2 — Install Java JDK 17 LTS

- Download Oracle JDK or [Adoptium Temurin](https://adoptium.net/)
- Set environment variables:
  - `JAVA_HOME` = `C:\Program Files\Java\jdk-17`
  - Add `%JAVA_HOME%\bin` to system `PATH`
- Verify:
  ```powershell
  java -version
  ```

### Step 3 — Install Android Studio + SDK

- Download from [developer.android.com](https://developer.android.com/studio)
- In SDK Manager, install:
  - SDK Platform: Android 14 (API 34) or latest
  - SDK Tools: Platform-Tools, Build-Tools, Android Emulator
  - System image: x86_64 with Google APIs (for emulator)
- Set environment variables:
  - `ANDROID_HOME` = `C:\Users\<YourName>\AppData\Local\Android\Sdk`
  - Add to `PATH`: `%ANDROID_HOME%\platform-tools` and `%ANDROID_HOME%\emulator`
- Verify:
  ```powershell
  adb --version
  emulator -list-avds
  ```

### Step 4 — Create an Android Emulator (AVD)

- Android Studio → Tools → Device Manager → Create Device
- Pick device profile: Pixel 7
- Pick system image: API 34, x86_64, Google APIs
- Launch emulator and verify:
  ```powershell
  adb devices        # → emulator-5554
  ```

### Step 5 — Install Python 3.11+

- Verify:
  ```powershell
  python --version
  pip --version
  ```

### Step 6 — Install Appium 2.x + UiAutomator2 Driver

```powershell
npm install -g appium
appium driver install uiautomator2
```

- Verify:
  ```powershell
  appium --version
  appium driver list   # → uiautomator2 [installed]
  ```

### Step 7 — Validate Environment with appium-doctor

```powershell
npm install -g @appium/doctor
appium-doctor --android
```

All **necessary** checks must pass before proceeding.

### Step 8 — Install Allure CLI

```powershell
# Install Scoop first if you don't have it:
irm get.scoop.sh | iex

scoop install allure
allure --version
```

---

## Phase 2 — Python Project Initialization

### Step 9 — Create Virtual Environment

```powershell
cd d:\AppiumProject
python -m venv venv
venv\Scripts\activate
```

### Step 10 — Install Python Dependencies

Create `requirements.txt`:

```
Appium-Python-Client>=4.0.0
pytest>=8.0.0
allure-pytest>=2.13.0
python-dotenv>=1.0.0
pytest-timeout>=2.3.1
pyyaml>=6.0.1
```

```powershell
pip install -r requirements.txt
```

---

## Phase 3 — Project Folder Structure

```
d:\AppiumProject\
├── .env                        ← secrets + env-specific config (never commit)
├── .gitignore
├── pyproject.toml              ← pytest configuration
├── requirements.txt
├── conftest.py                 ← GLOBAL fixtures: driver lifecycle, Allure hooks
│
├── apps/
│   └── my_app.apk             ← your APK file (in .gitignore)
│
├── config/
│   ├── __init__.py
│   ├── settings.py             ← reads .env + YAML → Config object
│   └── device_config.yaml      ← emulator & real device capability profiles
│
├── drivers/
│   ├── __init__.py
│   └── driver_factory.py       ← builds UiAutomator2Options → webdriver.Remote
│
├── src/pages/
│   ├── __init__.py
│   ├── base_page.py            ← parent class: find, wait, click, scroll
│   ├── login_page.py           ← example page object
│   ├── home_page.py            ← example page object
│   └── webview_page.py         ← hybrid app: context switching
│
├── utils/
│   ├── __init__.py
│   ├── wait_helpers.py         ← custom explicit waits
│   ├── screenshot_handler.py   ← capture + attach to Allure
│   ├── logger.py               ← logging utility
│   └── constants.py            ← timeouts, retry counts
│
├── tests/
│   ├── __init__.py
│   ├── conftest.py             ← test-level fixtures
│   ├── test_login.py           ← example test
│   ├── test_home.py            ← example test
│   └── test_hybrid_webview.py  ← hybrid/webview test
│
└── allure_reports/             ← generated at runtime (in .gitignore)
```

---

## Phase 4 — File-by-File Design

### 4A — `.env`

```env
APPIUM_HOST=127.0.0.1
APPIUM_PORT=4723
DEVICE_PROFILE=emulator
APP_PATH=d:/AppiumProject/apps/my_app.apk
```

- Loaded by `python-dotenv` in `conftest.py`
- **Never committed to git** — add to `.gitignore`

### 4B — `pyproject.toml`

```toml
[tool.pytest.ini_options]
testpaths = ["tests"]
python_files = ["test_*.py"]
python_classes = ["Test*"]
python_functions = ["test_*"]
markers = [
    "smoke: quick validation tests",
    "regression: full regression suite",
    "hybrid: tests involving webview context",
]
addopts = "-v --tb=short --timeout=120"
log_cli = true
log_cli_level = "INFO"
```

### 4C — `config/device_config.yaml`

Two profiles — switch between them via `DEVICE_PROFILE` in `.env`:

```yaml
emulator:
  platformName: android
  automationName: uiautomator2
  deviceName: Android Emulator
  avd: Pixel_7_API_34              # ← from `emulator -list-avds`
  platformVersion: "14"
  autoGrantPermissions: true
  noReset: false
  newCommandTimeout: 300

real_device:
  platformName: android
  automationName: uiautomator2
  deviceName: My Phone
  udid: XXXXXXXXXXXXXXXX           # ← from `adb devices`
  platformVersion: "14"
  autoGrantPermissions: true
  noReset: false
  newCommandTimeout: 300
```

### 4D — `config/settings.py`

- Calls `load_dotenv()` to read `.env`
- Reads `device_config.yaml` with PyYAML
- Exposes a `Config` class with properties:
  - `appium_url` → `http://{host}:{port}`
  - `device_caps` → the selected YAML profile dict (based on `DEVICE_PROFILE`)
  - `app_path` → full path to APK

### 4E — `drivers/driver_factory.py`

**Key Concept — `UiAutomator2Options`** (from `appium.options.android`):

This is the modern, typed replacement for the legacy `DesiredCapabilities` dict. Each capability is a Python property with autocomplete support.

**`DriverFactory.get_driver()` does:**
1. Reads config from `settings.py`
2. Builds `UiAutomator2Options`:
   - `platform_name` → `'android'`
   - `automation_name` → `'uiautomator2'`
   - `device_name`, `app` (APK path), `avd` (emulator name)
   - `auto_grant_permissions`, `no_reset`, `new_command_timeout`
   - For hybrid: `set_capability('appium:chromedriverAutodownload', True)`
3. Creates `webdriver.Remote(command_executor=appium_url, options=options)`
4. Sets `driver.implicitly_wait(10)`
5. Returns the driver

**What happens at runtime:**
1. HTTP POST to Appium server at `localhost:4723` with capabilities
2. UiAutomator2 driver installs helper apps on emulator
3. Your APK is installed and launched
4. Session established → driver ready for commands
5. Every subsequent command (find, click, type) = HTTP to Appium → forwarded to device

### 4F — `src/pages/base_page.py` — POM Foundation

BasePage is the **parent class** every page object inherits from. It wraps raw Appium driver calls into readable, reusable methods.

**Core methods:**

| Method | Purpose |
|---|---|
| `find_element(locator)` | Finds element; `locator = (AppiumBy.ID, 'com.app:id/btn')` |
| `wait_for_element(locator, timeout)` | Explicit wait with `WebDriverWait` + `EC.presence_of_element_located` |
| `wait_for_clickable(locator, timeout)` | Explicit wait for element to be clickable |
| `click(locator)` | Wait for clickable + click |
| `send_keys(locator, text)` | Wait + clear + type text |
| `get_text(locator)` | Wait + return `.text` |
| `is_displayed(locator, timeout)` | Returns True/False without throwing |
| `scroll_to_text(text)` | UiAutomator2-specific scroll using `UiScrollable` |

**Android Locator Strategies (`AppiumBy`):**

| Strategy | Example | When to use |
|---|---|---|
| `AppiumBy.ID` | `'com.myapp:id/username'` | **Best** — fastest, most stable |
| `AppiumBy.ACCESSIBILITY_ID` | `'Login Button'` | Great for cross-platform |
| `AppiumBy.XPATH` | `'//android.widget.TextView[@text="Login"]'` | **Slowest** — use as last resort |
| `AppiumBy.ANDROID_UIAUTOMATOR` | `'new UiSelector().text("Login")'` | Powerful for scroll & complex finds |
| `AppiumBy.CLASS_NAME` | `'android.widget.Button'` | Too generic, rarely useful alone |

### 4G — `src/pages/login_page.py` — Example Page Object

```
class LoginPage(BasePage):                   # ← inherits BasePage
    USERNAME = (AppiumBy.ID, 'com.myapp:id/username')   # locators as tuples
    PASSWORD = (AppiumBy.ID, 'com.myapp:id/password')
    LOGIN_BTN = (AppiumBy.ID, 'com.myapp:id/login_btn')

    def login(self, user, pwd):
        self.send_keys(self.USERNAME, user)   # ← calls BasePage method
        self.send_keys(self.PASSWORD, pwd)
        self.click(self.LOGIN_BTN)
```

**Call chain:** `test → LoginPage.login() → BasePage.send_keys() → WebDriverWait + driver.find_element().send_keys()`

### 4H — `src/pages/webview_page.py` — Hybrid App Context Switching

**How hybrid apps work in Appium:**
- Your app has **native UI** (buttons, text fields) AND **embedded WebViews** (mini browser inside the app)
- Appium exposes two **contexts**: `NATIVE_APP` and `WEBVIEW_com.yourpackage`
- In `NATIVE_APP` → use AppiumBy locators (ID, ACCESSIBILITY_ID, etc.)
- In `WEBVIEW_*` → use standard Selenium locators (CSS_SELECTOR, XPATH for HTML)
- **You must explicitly switch** before interacting with elements in the other context

**Key methods:**

| Method | What it does |
|---|---|
| `driver.contexts` | Returns list: `['NATIVE_APP', 'WEBVIEW_com.myapp']` |
| `driver.switch_to.context('WEBVIEW_com.myapp')` | Switch to webview |
| `driver.switch_to.context('NATIVE_APP')` | Switch back to native |
| `driver.current_context` | Returns current context name |

**Important capability for hybrid:** `chromedriverAutodownload: true` — auto-downloads matching Chromedriver for the WebView version.

### 4I — `conftest.py` (Root) — Driver Lifecycle & Allure Hooks

**This is the heart of the framework.** Three key components:

#### 1. `driver` fixture (`scope="function"`)
```
@pytest.fixture(scope="function")
def driver():
    drv = DriverFactory.get_driver()     # create session
    yield drv                             # test runs
    drv.quit()                            # teardown
```
- **function-scoped** = fresh app state per test (reliable but slower)
- Change to `scope="session"` for speed during development

#### 2. `allure_screenshot_on_failure` fixture (`autouse=True`)
- Runs automatically for **every test**
- After test completes: checks if it failed
- If failed → `driver.get_screenshot_as_png()` → attaches to Allure report as PNG

#### 3. `pytest_runtest_makereport` hook
- Makes test pass/fail result accessible in fixtures via `request.node.rep_call`
- Required by the screenshot fixture to know whether the test failed

**Lifecycle per test:**
```
1. pytest discovers test → sees it needs `driver` fixture
2. DriverFactory → HTTP to Appium → installs APK → launches app
3. Test body runs (find, click, assert)
4. yield → screenshot fixture checks result → captures if failed
5. driver.quit() → Appium session ends, app closes
```

### 4J — `tests/test_login.py` — Example Test

```python
@allure.feature("Login")
class TestLogin:

    @pytest.mark.smoke
    @allure.severity(allure.severity_level.CRITICAL)
    def test_valid_login(self, driver):
        login_page = LoginPage(driver)
        home_page = HomePage(driver)

        with allure.step("Enter credentials and login"):
            login_page.login("user@test.com", "pass123")

        with allure.step("Verify home page"):
            assert home_page.is_home_displayed()
```

**How it connects:** test receives `driver` from fixture → passes to `LoginPage(driver)` → `LoginPage` inherits `BasePage` → `BasePage` wraps all driver calls. `allure.step()` blocks create labeled sections in the Allure report.

---

## Phase 5 — Running & Debugging Tests

### Start Appium Server (separate terminal — must stay running)

```powershell
appium                                     # default: localhost:4723
appium --port 4724 --log appium.log        # custom port + log to file
```

### Run Tests

```powershell
# All tests with Allure
pytest tests/ --alluredir=allure_reports -v

# Single file
pytest tests/test_login.py -v

# Single test method
pytest tests/test_login.py::TestLogin::test_valid_login -v

# By marker
pytest -m smoke --alluredir=allure_reports -v

# With print() output visible
pytest -s tests/test_login.py -v
```

### View Allure Reports

```powershell
# Live browser report
allure serve allure_reports

# Static HTML export
allure generate allure_reports -o allure_reports/export --clean
```

### Debugging Toolkit

| Tool | Purpose |
|---|---|
| **Appium Inspector** | GUI to visually inspect app elements and find locators. Download from [github.com/appium/appium-inspector](https://github.com/appium/appium-inspector). Connect to running Appium server, paste capabilities as JSON, tap elements to see their IDs/XPaths. |
| `driver.page_source` | Returns full XML of current screen — use `print(driver.page_source)` when locators fail |
| `adb devices` | Verify emulator is connected |
| `adb shell dumpsys window \| findstr mCurrentFocus` | See which Activity is currently on screen |
| `adb shell pm list packages \| findstr myapp` | Check if your APK is installed |
| `adb logcat` | Android system logs (filter by tag for your app) |
| Appium server terminal | Full HTTP request/response log — **check here first** when tests fail |
| `pytest -s` | Shows `print()` output during test execution |

### Common Errors & Fixes

| Error | Cause | Fix |
|---|---|---|
| "Could not find a connected Android device" | Emulator not running or adb not in PATH | Launch emulator, verify `adb devices` |
| "An unknown server-side error occurred" | APK path wrong or incompatible with emulator API | Check `APP_PATH` in `.env`, ensure APK supports target API |
| `NoSuchElementException` | Wrong locator, element not loaded, or wrong context | Add explicit wait, verify locator in Appium Inspector, check native vs. webview context |
| `SessionNotCreatedException` | Appium not running or driver not installed | Start `appium`, verify `appium driver list` |
| `WebDriverException: Connection refused` | Appium server not started | Run `appium` in a separate terminal first |

---

## Verification Checklist

- [ ] `appium-doctor --android` → all necessary checks pass
- [ ] `adb devices` → emulator listed
- [ ] `appium` → server starts on port 4723 without errors
- [ ] `pytest tests/test_login.py -v` → test executes, app launches on emulator
- [ ] `allure serve allure_reports` → opens browser with results + screenshots

---

## Architecture Decisions

| Decision | Rationale |
|---|---|
| function-scoped driver | Clean app state per test — reliable over fast |
| `UiAutomator2Options` | Modern typed API; legacy `DesiredCapabilities` dict is deprecated |
| YAML device profiles | Easy to add real_device profile later — just change `.env` |
| `.env` for secrets, YAML for capabilities | Separation of sensitive vs. structural config |
| Allure `with allure.step()` in tests | Creates readable, labeled sections in reports |
| Appium Inspector for locator discovery | Visual element inspection is essential for Appium beginners |

## Implementation Order

```
Phase 1 (prereqs)      → MUST complete first, blocks everything
Phase 2 (venv + deps)  → depends on Phase 1
Phase 3 (folders)       → create all directories + __init__.py files
Phase 4 (files)         → .env → pyproject.toml → device_config.yaml → settings.py
                          → driver_factory.py → base_page.py → login_page.py
                          → conftest.py → test_login.py
Phase 5 (run)           → start Appium server, run first test, verify pytest report
```
