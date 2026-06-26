from appium.webdriver.common.appiumby import AppiumBy
from src.pages.base_page import BasePage

class ActivitiesPage(BasePage):

    # SECTION HEADER
    ACTIVITIES_TAB = (
        AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="Activities"]'
    )

    # Actions

    def click_activities_tab(self):
        self.driver.find_element(*self.ACTIVITIES_TAB).click()