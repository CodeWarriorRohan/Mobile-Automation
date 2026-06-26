from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from utils.constants import DEFAULT_TIMEOUT,  CILIO_LOGO, BACK_ARROW, BACK_ARROW_X, BACK_ARROW_Y, PROFILE_ICON, USER_NAME_TEXT, USER_ROLE_TEXT, MY_WORK_BTN, MY_BADGE_BTN, NAV_HOME, NAV_SEARCH, NAV_SCHEDULE, PROFILE_ICON_Y, PROFILE_ICON_X
import logging


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator):
        """Find element immediately (relies on implicit wait)."""
        return self.driver.find_element(*locator)

    def wait_for_element(self, locator, timeout=DEFAULT_TIMEOUT):
        """Explicit wait until element is present in DOM."""
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )

    def wait_for_clickable(self, locator, timeout=DEFAULT_TIMEOUT):
        """Explicit wait until element is visible and enabled."""
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )

    def click(self, locator):
        self.wait_for_clickable(locator).click()

    def tap_element(self, locator):
        self.wait_for_element(locator).click()

    def send_keys(self, locator, text):
        element = self.wait_for_clickable(locator)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        return self.wait_for_element(locator).text

    def is_displayed(self, locator, timeout=DEFAULT_TIMEOUT):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(locator)
            )
            return True
        except TimeoutException:
            return False

    def scroll_to_text(self, text):
        """UiAutomator2 scroll using UiScrollable — Android only."""
        self.driver.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            f'new UiScrollable(new UiSelector().scrollable(true))'
            f'.scrollIntoView(new UiSelector().text("{text}"))'
        )

    def find_elements(self, locator):
        """Find all matching elements; returns empty list if none found."""
        return self.driver.find_elements(*locator)

    def is_element_visible(self, locator, timeout=DEFAULT_TIMEOUT):
        """Returns True if element is visible on screen, False otherwise."""
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
            return True
        except TimeoutException:
            return False
        
    def is_element_disabled(self, locator, timeout=DEFAULT_TIMEOUT) -> bool:
        """Returns True if element is disabled (enabled='false' or clickable='false')."""
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(locator)
            )
            el = self.driver.find_element(*locator)
            return (
                el.get_attribute("enabled") == "false" or
                el.get_attribute("clickable") == "false"
            )
        except TimeoutException:
            return False   

    def is_element_present(self, locator, timeout=DEFAULT_TIMEOUT):
        """Returns True if element exists in DOM, False otherwise."""
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(locator)
            )
            return True
        except TimeoutException:
            return False
        
    def scroll_down(self):
        """Scroll down one viewport using UiScrollable."""
        self.driver.find_element(
         AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiScrollable(new UiSelector().scrollable(true)).scrollForward()'
    )

    def scroll_up(self):
        """Scroll back to top using UiScrollable."""
        self.driver.find_element(
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiScrollable(new UiSelector().scrollable(true)).scrollToBeginning(10)'
    )    

    def wait_seconds(self, seconds: float):
        """Hard wait — use sparingly, prefer explicit waits."""
        import time
        time.sleep(seconds)

    def tap_profile_icon(self):
        """Tap the profile icon. Falls back to coordinates if parent XPath doesn't resolve."""
        try:
            self.click(self.PROFILE_ICON)
        except Exception:
            # Coordinate fallback using bounds center from Appium Inspector: [978,123][1041,186]
            self.driver.execute_script(
                "mobile: clickGesture",
                {"x": PROFILE_ICON_X, "y": PROFILE_ICON_Y}
            )

    def tap_back_arrow(self):
        # Coordinate fallback using bounds center from Appium Inspector: [60,133]
        self.driver.execute_script(
            "mobile: clickGesture",
            {"x": BACK_ARROW_X, "y": BACK_ARROW_Y}
        )          

       # AFTER
    def tap_nav_home(self):
        self.click(NAV_HOME)

    def tap_nav_search(self):
        self.click(NAV_SEARCH)

    def tap_nav_schedule(self):
        self.click(NAV_SCHEDULE)