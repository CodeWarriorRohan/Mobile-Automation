"""
 Seller Info Page- Page Object for Seller Info Tab in Job Details Screen.

 Locator strategy (priority order):
  1. ACCESSIBILITY_ID  (content-desc from Appium Inspector - most stable)
  2. ANDROID_UIAUTOMATOR  (for dynamic text / count matching)
  3. XPATH  (fallback only)
"""
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import TimeoutException

from src.pages.base_page import BasePage

class SellerInfoPage(BasePage):
    # ------------------------------------------------------------------ #
    #  SELLER INFO TAB ELEMENTS
    # ------------------------------------------------------------------ #
    SELLER_INFO_TAB = (AppiumBy.XPATH, '//android.widget.TextView[@text="Seller info"]')
    STORE_NAME_FIELD = (AppiumBy.XPATH, '//android.widget.EditText[@hint="Store"]')
    STORE_ADDRESS_FIELD = (AppiumBy.XPATH, '//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[3]')

    def is_seller_info_tab_visible(self) -> bool:
        """Returns True if the 'Seller info' tab is visible on screen."""
        return self.is_element_visible(self.SELLER_INFO_TAB)
    
    def tap_seller_info_tab(self):
        """Tap the 'Seller info' tab to view seller details."""
        self.click(self.SELLER_INFO_TAB)
        self.wait_seconds(1)
    
    def get_store_name(self) -> str:
        """Return the displayed store name text."""
        return self.get_text(self.STORE_NAME_FIELD)
    
    def get_store_address(self) -> str:
        """Return the displayed store address text."""
        return self.is_element_present(self.STORE_ADDRESS_FIELD)