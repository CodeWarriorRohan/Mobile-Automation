"""
Job Status Page - Page Object for the Job Status screen.

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
from utils.constants import BACK_ARROW, BACK_ARROW_X, BACK_ARROW_Y, PROFILE_ICON, NAV_HOME, NAV_SEARCH, NAV_SCHEDULE, PROFILE_ICON_Y, PROFILE_ICON_X
from utils.card_reader import read_cards_with_count

class JobStatusPage(BasePage):
    # ------------------------------------------------------------------ #
    #  HEADER
    #  JOB TYPE and COUNT
    #  PROFILE_ICON: com.horcrux.svg.SvgView  — top-right, bounds [978,123][1041,186]
    # ------------------------------------------------------------------ #
    PROFILE_ICON = PROFILE_ICON
    _PROFILE_ICON_X = PROFILE_ICON_X
    _PROFILE_ICON_Y = PROFILE_ICON_Y

    BACK_ARROW = BACK_ARROW
    BACK_ARROW_X = BACK_ARROW_X
    BACK_ARROW_Y = BACK_ARROW_Y

    # ------------------------------------------------------------------ #
    # Sub-cards shown after tapping a Job Type card
    # content-desc format: "New, (0)", "Active, (5)"  — count is in parentheses
    JOB_STATUS_CARDS = (
        AppiumBy.XPATH,
        '//android.view.ViewGroup'
        '[contains(@content-desc, ", (") and @clickable="true"]'
    )

    JOB_STATUS_HEADER = (
        AppiumBy.XPATH,
        '//android.widget.TextView[@index="3" and @clickable="false"]'
    )
    JOB_STATUS_COUNT = (
        AppiumBy.XPATH,
        '//android.widget.TextView[@index="4" and @clickable="false"]'
    )

    SEARCH_RESULT_CARDS = (
        AppiumBy.XPATH,
            '//android.view.ViewGroup[contains(@content-desc, "Name :") and @clickable="true"]'
    )
    # ------------------------------------------------------------------ #
    #  BOTTOM NAVIGATION  (imported from utils.constants)
    # ------------------------------------------------------------------ #
    NAV_HOME     = NAV_HOME
    NAV_SEARCH   = NAV_SEARCH
    NAV_SCHEDULE = NAV_SCHEDULE

    # ================================================================== #
    #  REUSABLE HELPERS
    # ================================================================== #

    def get_job_status_header(self) -> str:
        """Reads the header text of the Job Status screen (e.g. 'Assessment')."""
        try:
            return self.wait_for_element(self.JOB_STATUS_HEADER, timeout=2).text.strip()
        except TimeoutException:
            return ""
    
    def get_job_status_count(self) -> str:
        """Reads the count text of the Job Status screen (e.g. ' Job(71)')."""
        try:
            count_text = self.wait_for_element(self.JOB_STATUS_COUNT, timeout=2).text.strip()
            return count_text.strip("()")  # Remove parentheses if present
        except TimeoutException:
            return ""
        
    def get_search_result_cards(self) -> list:
        """Return all visible search result card elements."""
        return self.find_elements(self.SEARCH_RESULT_CARDS)
    
    def get_job_status_cards(self) -> list:
        """
        After tapping a Job Type card, collect the sub-cards shown on that screen.
        Returns list of dicts: [{"name": "Active", "count": "5"}, ...]
        """
        self.is_element_present(self.JOB_STATUS_CARDS, timeout=10)
        return read_cards_with_count(self.driver, self.JOB_STATUS_CARDS)

    def tap_job_status_card(self, name: str):
        """Tap a Job Status sub-card by name (e.g. 'Active', 'New')."""
        try:
            self.driver.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                f'new UiScrollable(new UiSelector().scrollable(true))'
                f'.scrollIntoView(new UiSelector().textContains("{name}"))'
            )
        except Exception:
            pass  # Card may already be visible
        locator = (
            AppiumBy.XPATH,
            f'//android.view.ViewGroup'
            f'[starts-with(@content-desc, "{name},")]',
        )
        self.click(locator)

    def tap_random_result_cards(self, sample_size: int = 3, wait_after_tap: int = 10, wait_after_back: int = 5):
        """
        Reusable helper: tap up to `sample_size` random result cards from the current search screen,
        navigate back after each using tap_back_arrow().
        """
        logger = logging.getLogger(__name__)

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


    