"""
SEARCH Page - Page Object for the My Work / Home screen.

Locator strategy (priority order):
  1. ACCESSIBILITY_ID  (content-desc from Appium Inspector - most stable)
  2. ANDROID_UIAUTOMATOR  (for dynamic text / count matching)
  3. XPATH  (fallback only)
"""
import logging
import random

from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import TimeoutException

from src.pages.base_page import BasePage
from utils.constants import CILIO_LOGO, BACK_ARROW, BACK_ARROW_X, BACK_ARROW_Y, PROFILE_ICON, USER_NAME_TEXT, USER_ROLE_TEXT, VIEW_ALL_WORK_BTN, MY_BADGE_BTN, NAV_HOME, NAV_SEARCH, NAV_SCHEDULE,PROFILE_ICON_X, PROFILE_ICON_Y
from utils.field_reader import read_input_field_hints

class SearchPage(BasePage):
    # ------------------------------------------------------------------ #
    #  HEADER
    #  USER INFO CARD
    #  FIND JOBS BY TYPES CARDS
    #  BOTTOM NAVIGATION  (imported from utils.constants)
    # ------------------------------------------------------------------ #
    CILIO_LOGO = CILIO_LOGO

    # ------------------------------------------------------------------ #
    #  SEARCH BAR
    #  ViewGroup (clickable) wraps a non-clickable TextView placeholder
    #  Tap the ViewGroup to open the search input
    # ------------------------------------------------------------------ #
    
    SEARCH_BAR         = (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="Search..."]')
    SEARCH_PLACEHOLDER = (AppiumBy.XPATH, '//android.widget.TextView[@text="Search..."]')
    
    # Active search input — appears after tapping SEARCH_BAR
    SEARCH_INPUT = (AppiumBy.XPATH, '//android.widget.EditText[@hint="Search here.."]')
    
    # Cross icon to clear typed text — bounds [964,166][1040,245] → center X=1002, Y=206
    CLEAR_SEARCH_BTN = (AppiumBy.XPATH, '//android.widget.ImageView[@index="0" and @clickable="false" and @bounds="[964,166][1040,245]"]')
    
    # Search result cards — ViewGroup with content-desc containing "Name :"
    # Pattern: "Status, Name :, JobName, StoreName, Store No :"
    SEARCH_RESULT_CARDS = (
        AppiumBy.XPATH,
            '//android.view.ViewGroup[contains(@content-desc, "Name :") and @clickable="true"]'
    )
    
    # ------------------------------------------------------------------ #
    #  FIND JOBS BY FILTERS SECTION
    # ------------------------------------------------------------------ #
    #  FIND JOBS BY FILTERS SECTION
    # ------------------------------------------------------------------ #
    
    FIND_JOBS_BY_FILTERS_LABEL = (AppiumBy.XPATH, '//android.widget.TextView[@text="Find Jobs by Filters"]')
    BASIC_SEARCH_BTN           = (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="Basic"]')
    ADVANCED_SEARCH_BTN        = (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="Advanced"]')
    
    # ------------------------------------------------------------------ #
    #  BASIC SEARCH SCREEN
    # ------------------------------------------------------------------ #
    
    BASIC_SEARCH_ENABLED_INPUTS   = (AppiumBy.XPATH, '//android.widget.EditText[@enabled="true"]')
    CUSTOMER_FIRST_NAME_INPUT     = (AppiumBy.XPATH, '//android.widget.EditText[contains(@hint, "First Name") or @hint="Customer First Name"]')
    CITY_INPUT = (AppiumBy.XPATH, '//android.widget.EditText[@text="City" or @hint="City"]')
    PHONE_NUMBER_INPUT = (AppiumBy.XPATH, '//android.widget.EditText[@text="Phone Number" or @hint="Phone Number"]')
    GO_BTN                        = (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="Go"]')
    CLEAR_BTN                     = (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="Clear"]')

    # ------------------------------------------------------------------ #
    #  ADVANCED SEARCH SCREEN - Sidebar Tabs
    # ------------------------------------------------------------------ #
    
    ADVANCED_STATUS_TAB   = (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="Status"]')
    ADVANCED_TYPE_TAB     = (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="Type"]')
    ADVANCED_CATEGORY_TAB = (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="Category"]')
    
    # Enabled items in the Advanced Search list (right-side ScrollView only)
    ADVANCED_ENABLED_ITEMS = (AppiumBy.XPATH, '//android.widget.ScrollView//android.view.ViewGroup[@content-desc and @clickable="true"]')

    # Individual selectable items for tap actions
    ADVANCED_STATUS_NEW_ITEM       = (AppiumBy.XPATH, '//android.widget.TextView[@text="New"]')
    ADVANCED_TYPE_ASSESSMENT_ITEM  = (AppiumBy.XPATH, '//android.widget.TextView[@text="Assessment"]')
    ADVANCED_CATEGORY_WINDOWS_ITEM = (AppiumBy.XPATH, '//android.widget.TextView[@text="Windows"]')

    
    # ── Clear Confirmation Dialog for Basic Search ───────────────────────────────────────────
    
    CLEAR_DIALOG_TITLE   = (AppiumBy.XPATH, '//android.widget.TextView[@text="Clear"]')
    CLEAR_DIALOG_MESSAGE = (AppiumBy.XPATH, '//android.widget.TextView[@text="Are you sure you want to clear?"]')
    CLEAR_CONFIRM_OK     = (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="Ok"]')
    CLEAR_CONFIRM_CANCEL = (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="Cancel"]')
    NAV_HOME     = NAV_HOME
    NAV_SEARCH   = NAV_SEARCH
    NAV_SCHEDULE = NAV_SCHEDULE
    # ================================================================== #
    #  REUSABLE HELPERS
    # GLOBAL SEARCH PAGE                                                     
    # ================================================================== #
       
    def is_search_screen_displayed(self) -> bool:
        """Returns True if the Search bar is visible."""
        return self.is_element_visible(self.SEARCH_BAR)
 
    def is_find_jobs_by_filters_displayed(self) -> bool:
        return self.is_element_visible(self.FIND_JOBS_BY_FILTERS_LABEL)
 
    def is_basic_filter_displayed(self) -> bool:
        return self.is_element_visible(self.BASIC_SEARCH_BTN)
 
    def is_advanced_filter_displayed(self) -> bool:
        return self.is_element_visible(self.ADVANCED_SEARCH_BTN)
    # ================================================================== #
    #  ACTIONS
    # ================================================================== #
 
    def tap_search_bar(self):
        self.click(self.SEARCH_BAR)
 
    def enter_search_text(self, text: str):
        """Type text in search — taps search bar only if input is not already open."""
        if not self.is_element_present(self.SEARCH_INPUT, timeout=2):
            self.tap_search_bar()
            self.wait_seconds(1)
        field = self.driver.find_element(*self.SEARCH_INPUT)
        field.clear()
        field.send_keys(text)
 
    def tap_clear_search(self):
        """Tap the cross icon to clear text from the search input."""
        self.driver.execute_script(
        "mobile: clickGesture",
        {"x": 1002, "y": 206}
    )
 
    def get_search_result_cards(self) -> list:
        """Return all visible search result card elements."""
        return self.find_elements(self.SEARCH_RESULT_CARDS)

    def tap_search_back_arrow(self):
        """Back arrow inside the search input screen — bounds [42,182][84,229] → center X=63, Y=206."""
        self.driver.execute_script(
        "mobile: clickGesture",
        {"x": 63, "y": 206}
    )
             
    def tap_basic_search(self):
        """Tap Basic filter button to navigate to Basic Search screen."""
        self.click(self.BASIC_SEARCH_BTN)

    def get_basic_search_filter_fields(self, max_scrolls: int = 5) -> list:
        """Delegate to utils.field_reader for multi-pass scroll field collection."""
        return read_input_field_hints(
            self.driver, self.BASIC_SEARCH_ENABLED_INPUTS, max_scrolls=max_scrolls
        )
    def enter_customer_first_name(self, text: str):
        field = self.driver.find_element(*self.CUSTOMER_FIRST_NAME_INPUT)
        field.clear()
        field.send_keys(text)

    def enter_city(self, text: str):
        field = self.driver.find_element(*self.CITY_INPUT)
        field.send_keys(text)

    def enter_phone_number(self, text: str):
        field = self.driver.find_element(*self.PHONE_NUMBER_INPUT)
        field.send_keys(text)     

    def tap_go_button(self):
        self.click(self.GO_BTN)

    # ================================================================== #
    #  REUSABLE HELPER: TAP RANDOM RESULT CARDS
    # ================================================================== #

    def tap_random_result_cards(self, sample_size: int = 3, wait_after_tap: int = 10, wait_after_back: int = 5):
        """
        Reusable helper: tap up to `sample_size` random result cards from the current search screen,
        navigate back after each using tap_back_arrow().
        """
        logger = logging.getLogger(__name__)

        cards = self.get_search_result_cards()
        if len(cards) == 0:
            self.enter_search_text("testing")
            self.wait_seconds(10)
            cards = self.get_search_result_cards()

        assert len(cards) > 0, "No search result cards found"
        logger.info(f"Total search result cards found: {len(cards)}")

        count = min(sample_size, len(cards))
        descs = []
        for c in random.sample(cards, count):
            try:
                descs.append(c.get_attribute("content-desc") or "")
            except Exception:
                pass  # skip stale elements
        selected_descs = [d for d in descs if d]

        assert len(selected_descs) > 0, "Could not read content-desc from any result card"

        for i, desc in enumerate(selected_descs, 1):
            logger.info(f"  Tapping card {i}: {desc}")
            print(f"\n  Tapping card {i}: {desc}")
            locator = (AppiumBy.XPATH, f'//android.view.ViewGroup[@content-desc="{desc}" and @clickable="true"]')
            self.driver.find_element(*locator).click()
            self.wait_seconds(wait_after_tap)
            self.tap_back_arrow()
            self.wait_seconds(wait_after_back)
    


    def tap_clear_button(self):
        self.click(self.CLEAR_BTN)

    def is_clear_dialog_displayed(self) -> bool:
        """Returns True if the clear confirmation dialog is visible."""
        return (
            self.is_element_visible(self.CLEAR_DIALOG_TITLE, timeout=2) and
            self.is_element_visible(self.CLEAR_DIALOG_MESSAGE, timeout=2) and
            self.is_element_visible(self.CLEAR_CONFIRM_OK, timeout=2)
        )        

    def tap_clear_ok(self):
        """Tap the OK button on the clear confirmation dialog."""
        self.click(self.CLEAR_CONFIRM_OK)

    def tap_clear_cancel(self):
        """Tap the Cancel button on the clear confirmation dialog."""
        self.click(self.CLEAR_CONFIRM_CANCEL)         

    def tap_advanced_search(self):
        """Tap the 'Advanced' filter button to navigate to Advanced Search screen."""
        self.click(self.ADVANCED_SEARCH_BTN)    

    def tap_status_tab(self):
        """Tap the 'Status' tab in Advanced Search sidebar."""
        self.click(self.ADVANCED_STATUS_TAB)

    def tap_type_tab(self):
        """Tap the 'Type' tab in Advanced Search sidebar."""
        self.click(self.ADVANCED_TYPE_TAB)

    def tap_category_tab(self):
        """Tap the 'Category' tab in Advanced Search sidebar."""
        self.click(self.ADVANCED_CATEGORY_TAB)

    def tap_status_new_item(self):
        """Tap the 'New' status checkbox item in Advanced Search."""
        self.click(self.ADVANCED_STATUS_NEW_ITEM)

    def tap_type_assessment_item(self):
        """Tap the 'Assessment' type checkbox item in Advanced Search."""
        self.click(self.ADVANCED_TYPE_ASSESSMENT_ITEM)

    def tap_category_windows_item(self):
        """Tap the 'Windows' category checkbox item in Advanced Search."""
        self.click(self.ADVANCED_CATEGORY_WINDOWS_ITEM)

    def _advanced_scroll_down(self):
        """Scroll down within the Advanced Search list area (bounds [416,247][1041,2152])."""
        self.driver.execute_script(
            "mobile: swipeGesture",
            {
                "left": 416, "top": 247, "width": 625, "height": 1905,
                "direction": "up",  # swipe up to scroll down
                "percent": 0.75
            }
        )

    def _advanced_scroll_up(self):
        """Scroll up within the Advanced Search list area (bounds [416,247][1041,2152])."""
        self.driver.execute_script(
            "mobile: swipeGesture",
            {
                "left": 416, "top": 247, "width": 625, "height": 1905,
                "direction": "down",  # swipe down to scroll up
                "percent": 0.75
            }
        )

    def get_advanced_search_items(self, max_scrolls: int = 5) -> list:
        """Scroll down then up to load all fields, capture and return enabled item names from Advanced Search list."""
        items = set()
        
        # First pass: scroll down to load all items
        for _ in range(max_scrolls):
            elements = self.find_elements(self.ADVANCED_ENABLED_ITEMS)
            for el in elements:
                try:
                    text = el.get_attribute("content-desc") or ""
                    # Exclude sidebar labels and buttons
                    if text and text not in ("Status", "Type", "Category", "Go", "Clear"):
                        items.add(text)
                except Exception:
                    pass
            
            try:
                # self._advanced_scroll_down()
                self.wait_seconds(1)
            except Exception:
                break  # No more scrollable content
        
        # Second pass: scroll back up to capture any missed items
        try:
            # self._advanced_scroll_up()
            self.wait_seconds(1)
        except Exception:
            pass
        
        for _ in range(max_scrolls):
            elements = self.find_elements(self.ADVANCED_ENABLED_ITEMS)
            for el in elements:
                try:
                    text = el.get_attribute("content-desc") or ""
                    if text and text not in ("Status", "Type", "Category", "Go", "Clear"):
                        items.add(text)
                except Exception:
                    pass
            
            try:
                # self._advanced_scroll_down()
                self.wait_seconds(1)
            except Exception:
                break
        
        return sorted(items) 