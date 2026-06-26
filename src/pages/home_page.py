from appium.webdriver.common.appiumby import AppiumBy
from src.pages.base_page import BasePage


class HomePage(BasePage):
    # Update these locators with actual resource-ids from your APK via Appium Inspector
    HOME_CONTAINER = (AppiumBy.ID, "com.myapp:id/home_container")
    WELCOME_TEXT = (AppiumBy.ID, "com.myapp:id/welcome_text")
    MENU_BTN = (AppiumBy.ID, "com.myapp:id/menu_button")

    def is_home_displayed(self):
        return self.is_displayed(self.HOME_CONTAINER)

    def get_welcome_text(self):
        return self.get_text(self.WELCOME_TEXT)

    def open_menu(self):
        self.click(self.MENU_BTN)
