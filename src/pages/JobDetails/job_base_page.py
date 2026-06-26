"""
SEARCH Page - Page Object for the My Work / Home screen.

Locator strategy (priority order):
  1. ACCESSIBILITY_ID  (content-desc from Appium Inspector - most stable)
  2. ANDROID_UIAUTOMATOR  (for dynamic text / count matching)
  3. XPATH  (fallback only)
"""
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import TimeoutException

from src.pages.base_page import BasePage
from utils.constants import CILIO_LOGO, BACK_ARROW, BACK_ARROW_X, BACK_ARROW_Y, PROFILE_ICON, USER_NAME_TEXT, USER_ROLE_TEXT, VIEW_ALL_WORK_BTN, MY_BADGE_BTN, NAV_HOME, NAV_SEARCH, NAV_SCHEDULE,PROFILE_ICON_X, PROFILE_ICON_Y
from utils.field_reader import read_input_field_hints

class JobBasePage(BasePage):
    # ------------------------------------------------------------------ #
    #  HEADER
    #  USER INFO CARD
    #  FIND JOBS BY TYPES CARDS
    #  BOTTOM NAVIGATION  (imported from utils.constants)
    # ------------------------------------------------------------------ #
    JOB_DETAILS_HEADER = (AppiumBy.XPATH, '//android.widget.TextView[@text="Job details"]')
    HOT_BUTTONS = (AppiumBy.XPATH, '//android.widget.TextView[@text="Buttons"]')
    MEASURES_BUTTON = (AppiumBy.XPATH, '//android.widget.TextView[@text="Measures"]')
    # Dynamic name field — text varies per job (e.g. customer/tech name); located by bounds
    # bounds [137,204][389,263] → center X=263, Y=233
    DYNAMIC_NAME_FIELD = (AppiumBy.XPATH, '//android.widget.TextView[starts-with(@bounds, "[137,204]")]')
    LEAD_SAFE_BUTTON = (AppiumBy.XPATH, '//android.widget.TextView[@text="Lead Safe"]')
    START_MEASURES_BUTTON = (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="Start Measure"]')
    CUST_SITE_BUTTON = (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="Cust/Site"]')
    JOB_SCHED_BUTTON = (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="Job/Sched"]')
    ACTION_DOCS_BUTTON = (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="Actions/Docs"]')
    HOT_BUTTONS_BACK = (AppiumBy.XPATH, '//android.view.ViewGroup[@resource-id="TouchableOpacity"]')

    def is_job_details_header_visible(self) -> bool:
        """Returns True if the 'Job details' header is visible on screen."""
        return self.is_element_visible(self.JOB_DETAILS_HEADER)
    
    def is_hot_buttons_visible(self) -> bool:
        """Returns True if the 'Buttons' header is visible on screen."""
        return self.is_element_visible(self.HOT_BUTTONS)
    
    def is_measures_button_visible(self) -> bool:
        """Returns True if the 'Measures' header is visible on screen."""
        return self.is_element_visible(self.MEASURES_BUTTON)
    
    def get_dynamic_name(self) -> str:
        """Return the displayed name text without asserting a specific value."""
        return self.get_text(self.DYNAMIC_NAME_FIELD)

    def is_dynamic_name_displayed(self) -> bool:
        """Returns True if the name field is visible on screen."""
        return self.is_element_visible(self.DYNAMIC_NAME_FIELD)
    
    def is_lead_safe_button_visible(self) -> bool:
        """Returns True if the 'Lead Safe' button is visible on screen."""
        return self.is_element_visible(self.LEAD_SAFE_BUTTON)
    
    def is_start_measures_button_visible(self) -> bool:
        """Returns True if the 'Start Measure' button is visible on screen."""
        return self.is_element_visible(self.START_MEASURES_BUTTON)
    
    def is_cust_site_button_visible(self) -> bool:
        """Returns True if the 'Cust/Site' button is visible on screen."""
        return self.is_element_visible(self.CUST_SITE_BUTTON)
    
    def is_job_sched_button_visible(self) -> bool:
        """Returns True if the 'Job/Sched' button is visible on screen."""
        return self.is_element_visible(self.JOB_SCHED_BUTTON)   
    
    def is_action_docs_button_visible(self) -> bool:
        """Returns True if the 'Action/Docs' button is visible on screen."""
        return self.is_element_visible(self.ACTION_DOCS_BUTTON)
    
    def tap_hot_buttons(self):
        """Tap the 'Buttons' header to navigate to the Hot Buttons screen."""
        self.click(self.HOT_BUTTONS)
    
    def tap_hot_buttons_back(self):
        """Tap the back arrow on the Hot Buttons screen to return to Job Details."""
        self.click(self.HOT_BUTTONS_BACK)   
    

    def tap_lead_safe_button(self):        
        """Tap the 'Lead Safe' button to navigate to the Lead Safe screen."""
        self.is_element_disabled(self.LEAD_SAFE_BUTTON)

    def tap_cust_site_button(self):
        """Tap the 'Cust/Site' button to navigate to the Customer/Site screen."""
        self.is_element_disabled(self.CUST_SITE_BUTTON)
    
    def tap_job_sched_button(self):
        """Tap the 'Job/Sched' button to navigate to the Job/Schedule screen."""
        self.is_element_disabled(self.JOB_SCHED_BUTTON)
    
    def tap_action_docs_button(self):
        """Tap the 'Action/Docs' button to navigate to the Action/Docs screen."""
        self.is_element_disabled(self.ACTION_DOCS_BUTTON)
    
    def tap_measures_button(self):
        """Tap the 'Measures' button to navigate to the Measures screen."""
        self.click(self.START_MEASURES_BUTTON)

    def scroll_content_to_text(self, text: str):
        """Scroll the Job Details content area (second scrollable, instance(1))
        until an element with the given text is visible.
        Uses instance(1) to skip the tab bar (first scrollable) and target
        the content ScrollView directly. Scrolls up or down as needed."""
        self.driver.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            f'new UiScrollable(new UiSelector().scrollable(true).instance(1))'
            f'.scrollIntoView(new UiSelector().text("{text}"))'
        )

    def scroll_content_to_beginning(self):
        """Scroll the Job Details content area (instance(1)) back to the very top.
        Uses scrollToBeginning(10) — up to 10 scroll steps to reach the top."""
        self.driver.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiScrollable(new UiSelector().scrollable(true).instance(1))'
            '.scrollToBeginning(10)'
        )

    def scroll_to_end(self):
        """Scroll the attachment list down to the very last item."""
        self.driver.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            f'new UiScrollable(new UiSelector().scrollable(true).instance(1))'
            f'.scrollToEnd(10)'
        )
    