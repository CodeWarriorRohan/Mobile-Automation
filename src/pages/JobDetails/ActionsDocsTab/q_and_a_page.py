from appium.webdriver.common.appiumby import AppiumBy
from src.pages.base_page import BasePage

class QAndAPage(BasePage):

    # SECTION HEADER

    Q_AND_A_TAB = (
        AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="Q/A\'s"]'
    )

    # First dropdown category row (resource-id=content-desc identifies Q&A rows)
    FIRST_DROPDOWN_CATEGORY = (
        AppiumBy.XPATH,
        '//android.view.ViewGroup[@clickable="false"]'
        '/android.view.ViewGroup[@clickable="true" and string-length(@content-desc) > 0'
        ' and @resource-id=@content-desc]'
    )

    # First option inside an opened dropdown container
    FIRST_DROPDOWN_OPTION = (
        AppiumBy.XPATH,
        '//android.view.ViewGroup[@clickable="false" and string-length(@content-desc) = 0]'
        '/android.view.ViewGroup[string-length(@content-desc) > 0]'
    )

    @staticmethod
    def dropdown_category_locator(category_desc):
        return (
            AppiumBy.XPATH,
            f'//android.view.ViewGroup[@clickable="false"]'
            f'/android.view.ViewGroup[@content-desc="{category_desc}"]'
        )

    @staticmethod
    def dropdown_option_locator(option_desc):
        return (
            AppiumBy.XPATH,
            f'//android.view.ViewGroup[@content-desc="{option_desc}"]'
        )

    # Actions

    def click_q_and_a_tab(self):
        self.click(self.Q_AND_A_TAB)

    def open_dropdown(self, category_desc):
        self.click(self.dropdown_category_locator(category_desc))

    def open_first_dropdown(self):
        el = self.wait_for_element(self.FIRST_DROPDOWN_CATEGORY)
        desc = el.get_attribute('content-desc')
        el.click()
        return desc

    def select_dropdown_option(self, option_desc):
        self.tap_element(self.dropdown_option_locator(option_desc))

    def select_first_dropdown_option(self):
        el = self.wait_for_element(self.FIRST_DROPDOWN_OPTION)
        desc = el.get_attribute('content-desc')
        el.click()
        return desc   