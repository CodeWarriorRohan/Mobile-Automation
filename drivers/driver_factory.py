"""
Appium driver factory.
- Reads capabilities from Config
- Builds UiAutomator2Options
- Creates and returns webdriver.Remote connected to Appium server
Full implementation: Phase 4 (Step 4E)
"""
 
from appium import webdriver
from appium.options.android import UiAutomator2Options
from config.settings import Config
 
 
class DriverFactory:
 
    @staticmethod
    def get_driver() -> webdriver.Remote:
        """
        Builds Appium capabilities and creates a new Appium session.
 
        Flow:
          1. Load config (from .env + device_config.yaml)
          2. Build UiAutomator2Options with platform, app, device caps
          3. Connect to Appium server via webdriver.Remote
          4. Return ready-to-use driver
        """
        config = Config()
        caps = config.device_caps
        options = UiAutomator2Options()
 
        # Core capabilities
        options.platform_name          = caps['platformName']        # 'android'
        options.automation_name        = caps['automationName']      # 'uiautomator2'
        options.device_name            = caps['deviceName']
        options.platform_version       = caps.get('platformVersion')
        options.auto_grant_permissions = caps.get('autoGrantPermissions', True)
        options.no_reset               = caps.get('noReset', True)
        options.new_command_timeout    = caps.get('newCommandTimeout', 300)
 
        # Launch by package/activity (app already installed on emulator)
        # Falls back to APK install path if appPackage is not defined
        if caps.get('appPackage'):
            options.app_package  = caps['appPackage']   # io.cilio.cio.qa
            options.app_activity = caps['appActivity']  # io.cilio.cio.mobile.MainActivity
        elif config.app_path:
            options.app = config.app_path               # install from APK file
 
        # Emulator: Appium will auto-launch this AVD if it isn't already running
        if caps.get('avd'):
            options.avd = caps['avd']
 
        # Real device: target a specific device by UDID
        if caps.get('udid'):
            options.udid = caps['udid']
 
        # Hybrid app support: auto-downloads matching Chromedriver for WebView
        options.set_capability('appium:chromedriverAutodownload', True)
 
        # AFTER
        driver = webdriver.Remote(
            command_executor=config.appium_url,
            options=options
        )
        # Increase HTTP socket timeout to 600 s so long-running test loops
        # (e.g. multi-card expansion in TC-18) never drop the connection.
        driver.command_executor.set_timeout(600)
        driver.implicitly_wait(10)
        return driver