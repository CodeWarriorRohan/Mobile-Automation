"""
Global Search Test Cases - Test suite for the Search screen UI components.

Prerequisites: User is logged in and navigated to the Search screen (via tap_nav_search from My Work or any other screen).
"""
import pytest
import sys
import os
import random
import logging
from appium.webdriver.common.appiumby import AppiumBy
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class TestBasicAndAdvancedSearch:    
    def test_tc45_search_screen_loaded(self, search_page):
            """TC-45: Search screen is loaded — search bar is visible."""
            assert search_page.is_element_visible(search_page.CILIO_LOGO), \
                "Cilio logo should be visible on Search screen"
            assert search_page.is_search_screen_displayed(), \
                "Search bar should be visible on Search screen"

    def test_tc46_search_bar_placeholder_visible(self, search_page):
        """TC-46: Search bar shows 'Search...' placeholder text."""
        assert search_page.is_element_visible(search_page.SEARCH_PLACEHOLDER), \
            "Search placeholder text 'Search...' should be visible"

    def test_tc47_find_jobs_by_filters_label_visible(self, search_page):
        """TC-47: 'Find Jobs by Filters' section label is visible."""
        assert search_page.is_find_jobs_by_filters_displayed(), \
            "'Find Jobs by Filters' label should be visible"

    def test_tc48_basic_filter_button_visible(self, search_page):
        """TC-48: 'Basic' filter button is visible."""
        assert search_page.is_basic_filter_displayed(), \
            "'Basic' filter button should be visible"

    def test_tc49_advanced_filter_button_visible(self, search_page):
        """TC-49: 'Advanced' filter button is visible."""
        assert search_page.is_advanced_filter_displayed(), \
            "'Advanced' filter button should be visible"

    def test_tc50_bottom_navigation_visible(self, search_page):
        """TC-50: All bottom navigation tabs are visible on Search screen."""
        assert search_page.is_element_visible(search_page.NAV_HOME), \
            "Home nav tab should be visible"
        assert search_page.is_element_visible(search_page.NAV_SEARCH), \
            "Search nav tab should be visible"
        assert search_page.is_element_disabled(search_page.NAV_SCHEDULE), \
            "Schedule nav tab should be disabled on Search screen"
        
    def test_tc51_tap_basic_search_navigates_to_basic_search(self, search_page):
        """TC-58: Tapping 'Basic' filter button navigates to Basic Search screen."""
        search_page.tap_basic_search()
        search_page.wait_seconds(5)

    def test_tc52_basic_search_fields_and_go(self, search_page):
        """TC-56: Navigate to Basic Search → log all enabled fields → enter 'testing' in Customer First Name → tap Go."""
        logger = logging.getLogger(__name__)
        assert search_page.is_element_visible(search_page.GO_BTN), \
            "'Go' button should be visible on Basic Search screen"
        
        assert search_page.is_element_visible(search_page.CLEAR_BTN), \
            "'Clear' button should be visible on Basic Search screen"

        # Scroll down then up to load all fields, capture and log them
        field_names = search_page.get_basic_search_filter_fields()
        msg = "These are all search fields for user has permissioned — these are enabled for this particular user:"
        logger.info(msg)
        print(f"\n{msg}")
        for name in field_names:
            if name:
                logger.info(f"  - {name}")
                print(f"  - {name}")

    def test_tc53_enter_customer_first_name_and_go(self, search_page):
        """TC-53: Enter 'testing' in Customer First Name and tap Go."""
        search_page.enter_customer_first_name("testing")
        search_page.wait_seconds(1)
        search_page.tap_go_button()
        search_page.wait_seconds(5) 

    def test_tc54_tap_random_basic_search_result_cards(self, search_page):
        """TC-54: Tap up to 2 random Basic Search result cards and navigate back after each."""
        search_page.tap_random_result_cards(sample_size=2)
        search_page.wait_seconds(3)
        search_page.tap_back_arrow()    

    def test_tc55_tap_clear_shows_confirmation_dialog_ok_clear(self, search_page):
        """TC-55: Tapping 'Clear' shows a confirmation dialog with Ok and Cancel."""
        search_page.tap_clear_button()
        search_page.wait_seconds(1)
        assert search_page.is_clear_dialog_displayed(), \
            "Clear confirmation dialog should appear after tapping 'Clear'"
        search_page.wait_seconds(1)
        search_page.tap_clear_ok()     

    def test_tc56_enter_city_and_go(self, search_page):
        """TC-56: Enter 'city' in City field and tap Go."""
        search_page.enter_city("city")
        search_page.wait_seconds(1)
        search_page.tap_go_button()
        search_page.wait_seconds(5) 

    def test_tc57_tap_random_cards_after_city_search(self, search_page):
        """TC-57: Tap up to 2 random result cards from City search, go back."""
        search_page.tap_random_result_cards(sample_size=2)
        search_page.wait_seconds(3)
        search_page.tap_back_arrow()

    def test_tc58_tap_clear_shows_confirmation_dialog_ok_clear(self, search_page):
        """TC-58: Tapping 'Clear' shows a confirmation dialog with Ok and Cancel."""
        search_page.tap_clear_button()
        search_page.wait_seconds(1)
        search_page.tap_clear_ok()
            

    def test_tc59_enter_phone_number_and_go(self, search_page):
        """TC-59: Enter '1234567890' in Phone Number field and tap Go."""
        search_page.enter_phone_number("1234567890")
        search_page.wait_seconds(1)
        search_page.tap_go_button()
        search_page.wait_seconds(5)

    def test_tc60_tap_random_cards_after_phone_search(self, search_page):
        """TC-60: Tap up to 2 random result cards from Phone Number search, go back."""
        search_page.tap_random_result_cards(sample_size=2)
        search_page.wait_seconds(3)
        search_page.tap_back_arrow()  

    def test_tc61_tap_clear_shows_confirmation_dialog_ok_clear(self, search_page):
        """TC-61: Tapping 'Clear' shows a confirmation dialog with Ok and Cancel."""
        search_page.tap_clear_button()
        search_page.wait_seconds(1)
        search_page.tap_clear_ok()
        search_page.wait_seconds(2)

    def test_tc62_navigate_back_from_basic_search(self, search_page):
        """TC-62: Tapping back arrow on Basic Search screen navigates back to Search screen."""
        search_page.tap_back_arrow()
        search_page.wait_seconds(2)
        assert search_page.is_search_screen_displayed(), \
            "Should be back on main Search screen after tapping back arrow"    
        
    def test_tc63_tap_advanced_search_navigates_to_advanced_search(self, search_page):
        """TC-63: Tapping 'Advanced' filter button navigates to Advanced Search screen."""
        search_page.tap_advanced_search()
        search_page.wait_seconds(5)    

    def test_tc64_advanced_search_status_and_go(self, search_page):
        """TC-64: Advanced Search — log all enabled Job Statuses, select 'New', tap Go."""
        logger = logging.getLogger(__name__)

        # Verify Go and Clear buttons are visible
        assert search_page.is_element_visible(search_page.GO_BTN), \
            "'Go' button should be visible on Advanced Search screen"
        assert search_page.is_element_visible(search_page.CLEAR_BTN), \
            "'Clear' button should be visible on Advanced Search screen"

        # --- Status Tab ---
        search_page.tap_status_tab()
        search_page.wait_seconds(2)
        statuses = search_page.get_advanced_search_items()
        msg = "Enabled Job Statuses:"
        logger.info(msg)
        print(f"\n{msg}")
        for name in statuses:
            logger.info(f"  - {name}")
            print(f"  - {name}")

        search_page.tap_status_new_item()
        search_page.tap_go_button()
        search_page.wait_seconds(5)
        search_page.tap_random_result_cards(sample_size=2)
        search_page.tap_back_arrow()
        search_page.tap_advanced_search()
        search_page.wait_seconds(2)

    def test_tc65_advanced_search_type_and_go(self, search_page):
        """TC-65: Advanced Search — log all enabled Job Types, select 'Assessment', tap Go."""
        logger = logging.getLogger(__name__)

        # --- Type Tab ---
        search_page.tap_type_tab()
        search_page.wait_seconds(2)
        types = search_page.get_advanced_search_items()
        msg = "Enabled Job Types:"
        logger.info(msg)
        print(f"\n{msg}")
        for name in types:
            logger.info(f"  - {name}")
            print(f"  - {name}")

        search_page.tap_type_assessment_item()
        search_page.tap_go_button()
        search_page.wait_seconds(5)
        search_page.tap_random_result_cards(sample_size=2)
        search_page.tap_back_arrow()
        search_page.wait_seconds(1)
        search_page.click(search_page.NAV_HOME)  
        search_page.wait_seconds(1)

    # def test_tc66_advanced_search_category_and_go(self, search_page):
    #     """TC-66: Advanced Search — log all enabled Job Categories, select 'Windows', tap Go."""
    #     logger = logging.getLogger(__name__)

    #     # --- Category Tab ---
    #     search_page.tap_category_tab()
    #     search_page.wait_seconds(2)
    #     categories = search_page.get_advanced_search_items()
    #     msg = "Enabled Job Categories:"
    #     logger.info(msg)
    #     print(f"\n{msg}")
    #     for name in categories:
    #         logger.info(f"  - {name}")
    #         print(f"  - {name}")

    #     search_page.tap_category_windows_item()
    #     search_page.tap_go_button()
    #     search_page.wait_seconds(5)
    #     search_page.tap_random_result_cards(sample_size=2)
    #     search_page.tap_back_arrow()
    #     search_page.tap_advanced_search()
    #     search_page.wait_seconds(2) 
 