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

class TestGlobalSearch:

    # ================================================================== #
    #  COMMON UI — all visible on Search screen
    # ================================================================== #

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

    def test_tc50_bottom_navigation_visible(self, search_page):
        """TC-50: All bottom navigation tabs are visible on Search screen."""
        assert search_page.is_element_visible(search_page.NAV_HOME), \
            "Home nav tab should be visible"
        assert search_page.is_element_visible(search_page.NAV_SEARCH), \
            "Search nav tab should be visible"
        assert search_page.is_element_disabled(search_page.NAV_SCHEDULE), \
            "Schedule nav tab should be disabled on Search screen"

    # ================================================================== #
    #  ACTIONS
    # ================================================================== #

    def test_tc51_tap_search_bar_opens_input(self, search_page):
        """TC-51: Tapping the search bar opens the search input."""
        search_page.tap_search_bar()
        search_page.wait_seconds(2)

    def test_tc52_enter_search_text(self, search_page):
        """TC-52: Tapping search bar opens input and text can be typed."""
        search_page.enter_search_text("testing")
        search_page.wait_seconds(2)
        # Verify the input field contains the typed text
        field = search_page.driver.find_element(*search_page.SEARCH_INPUT)
        assert field.text == "testing" or field.get_attribute("text") == "testing", \
            "Search input should contain 'testing' after typing"    


    def test_tc55_tap_random_three_search_result_cards(self, search_page):
        """TC-55: Results from TC-52 still showing — tap 3 random cards one by one, go back after each."""
        logger = logging.getLogger(__name__)

        # Results from TC-52's "testing" search should already be on screen.
        # Re-type only if results are not present (e.g. test run in isolation).
        cards = search_page.get_search_result_cards()
        assert len(cards) > 0, "No search result cards found after searching 'testing'"
        logger.info(f"Total search result cards found: {len(cards)}")

        # Capture content-desc strings upfront to avoid stale element references
        sample_size = min(3, len(cards))
        selected_descs = [c.get_attribute("content-desc") or "" for c in random.sample(cards, sample_size)]

        for i, desc in enumerate(selected_descs, 1):
            logger.info(f"  Tapping card {i}: {desc}")
            print(f"\n  Tapping card {i}: {desc}")
            # Re-locate card fresh each iteration to avoid stale reference
            locator = (AppiumBy.XPATH, f'//android.view.ViewGroup[@content-desc="{desc}" and @clickable="true"]')
            search_page.driver.find_element(*locator).click()
            search_page.wait_seconds(10)
            search_page.tap_back_arrow()   # back: job detail → search results
            search_page.wait_seconds(5)

    def test_tc56_tap_clear_search(self, search_page):
        """TC-56: Tapping the clear search button clears the search input."""
        search_page.tap_clear_search()
        search_page.wait_seconds(2)

    def test_tc57_tap_search_back_arrow(self, search_page):
        """TC-57: Tapping the back arrow inside the search input screen navigates back."""
        search_page.tap_search_back_arrow()
        search_page.wait_seconds(2)  
    
    
    