# Cilio.Appium — Android Mobile Automation

End-to-end UI automation for the Cilio Android app, built on **Appium 2.x + Python + pytest** using the Page Object Model.

## Stack

| Area | Choice |
|---|---|
| Platform | Android (emulator or real device) |
| Language | Python 3.11+ |
| Test runner | pytest with HTML reports |
| Appium driver | UiAutomator2 |
| Design pattern | Page Object Model |
| App type | Native + Hybrid (WebView) |

## Project Layout

```
apps/                  APK under test
config/                device_config.yaml + settings loader
data/                  credentials & test data
drivers/               Appium driver factory
src/pages/             Page Object classes (login, home, job details, ...)
tests/                 pytest suites (login, profile, search, job status, ...)
utils/                 logger, waits, screenshots, field/card readers
reports/               HTML test reports
Screenshots/           failure screenshots
conftest.py            session driver fixture + screenshot-on-failure hook
pyproject.toml         pytest config (testpaths, markers, addopts)
```

## Prerequisites

- Node.js 18+ LTS
- Java JDK 17
- Android Studio + SDK (platform-tools, emulator, API 34+ system image)
- Python 3.11+
- Appium 2.x with UiAutomator2 driver

```bash
npm install -g appium
appium driver install uiautomator2
```

Environment variables: `JAVA_HOME`, `ANDROID_HOME`, and `PATH` entries for `platform-tools` and `emulator`.

See [Plan.md](Plan.md) for the full environment-setup walkthrough.

## Setup

```bash
python -m venv .venv
.venv\Scripts\activate        # Windows
pip install -r requirements.txt
```

Create a `.env` at the repo root (loaded by [conftest.py](conftest.py)):

```
APPIUM_HOST=127.0.0.1
APPIUM_PORT=4723
DEVICE_PROFILE=emulator
APP_PATH=apps/TuVDdtnOd.apk
```

Device capabilities are selected from [config/device_config.yaml](config/device_config.yaml) by `DEVICE_PROFILE`. Update `avd`, `platformVersion`, `appPackage`, and `appActivity` to match your setup.

## Running Tests

Start the emulator and Appium server first:

```bash
adb devices           # confirm device is listed
appium                # starts on http://127.0.0.1:4723
```

Run the suite:

```bash
pytest                           # run all testpaths from pyproject.toml
pytest tests/test_login.py       # single file
pytest -m smoke                  # marker filter
pytest -k "search"               # name filter
```

Reports are written to [reports/report.html](reports/report.html). Failure screenshots land in [Screenshots/](Screenshots/).

### Markers

- `smoke` — quick validation
- `regression` — full suite
- `hybrid` — tests that switch into WebView context

## Adding a Test

1. Add a page class under [src/pages/](src/pages/) extending `BasePage`.
2. Add a `test_*.py` file under [tests/](tests/) using the session-scoped `driver` fixture from [conftest.py](conftest.py).
3. Register the file in `testpaths` in [pyproject.toml](pyproject.toml) if you want it picked up by the default run.

## Troubleshooting

- **`adb devices` empty** — relaunch the AVD or `adb kill-server && adb start-server`.
- **Appium session fails to start** — verify `appPackage`/`appActivity` match the installed APK (`adb shell dumpsys package io.cilio.cio.qa`).
- **Hybrid tests can't find WebView** — ensure `chromedriver` matching the device's WebView version is available to Appium.
