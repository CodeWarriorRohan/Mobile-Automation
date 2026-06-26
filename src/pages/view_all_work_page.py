"""
View All Work Page - Page Object for the View All Work screen.

Locator strategy (priority order):
  1. ACCESSIBILITY_ID  (content-desc from Appium Inspector - most stable)
  2. ANDROID_UIAUTOMATOR  (for dynamic text / count matching)
  3. XPATH  (fallback only)
"""
from appium.webdriver.common.appiumby import AppiumBy

from selenium.common.exceptions import TimeoutException

from src.pages.base_page import BasePage
from utils.constants import CILIO_LOGO, BACK_ARROW, BACK_ARROW_X, BACK_ARROW_Y, PROFILE_ICON, USER_NAME_TEXT, USER_ROLE_TEXT, MY_WORK_BTN, MY_BADGE_BTN, NAV_HOME, NAV_SEARCH, NAV_SCHEDULE, PROFILE_ICON_Y, PROFILE_ICON_X
from utils.card_reader import read_cards_with_count

class ViewAllWorkPage(BasePage):

    # ------------------------------------------------------------------ #
    #  HEADER
    #  CILIO_LOGO  : android.widget.ImageView — top-left, bounds [39,115][197,193]
    #  PROFILE_ICON: com.horcrux.svg.SvgView  — top-right, bounds [978,123][1041,186]
    # ------------------------------------------------------------------ #
    CILIO_LOGO = CILIO_LOGO
    PROFILE_ICON = PROFILE_ICON
    _PROFILE_ICON_X = PROFILE_ICON_X
    _PROFILE_ICON_Y = PROFILE_ICON_Y

    BACK_ARROW = BACK_ARROW
    BACK_ARROW_X = BACK_ARROW_X
    BACK_ARROW_Y = BACK_ARROW_Y

    # ------------------------------------------------------------------ #
    #  USER INFO CARD
    # ------------------------------------------------------------------ #
    USER_NAME_TEXT    = USER_NAME_TEXT
    USER_ROLE_TEXT    = USER_ROLE_TEXT
    MY_WORK_BTN       = MY_WORK_BTN
    MY_BADGE_BTN      = MY_BADGE_BTN

    # ------------------------------------------------------------------ #
    #  FIND JOBS BY TYPE CARDS
    #  Each card is a ViewGroup with content-desc = "CardName, Count"
    # ------------------------------------------------------------------ #
    JOB_TYPE_CARDS = (
        AppiumBy.XPATH,
        '//android.widget.ScrollView//android.view.ViewGroup'
        '[android.widget.TextView and contains(@content-desc, ",")]'
    )
    # AFTER
    # Sub-cards shown after tapping a Job Type card
    # content-desc format: "New, (0)", "Active, (5)"  — count is in parentheses
    JOB_STATUS_CARDS = (
        AppiumBy.XPATH,
        '//android.view.ViewGroup'
        '[contains(@content-desc, ", (") and @clickable="true"]'
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
        

    def tap_my_work(self):
        self.click(self.MY_WORK_BTN)

    def tap_my_badge(self):
        self.click(self.MY_BADGE_BTN)   

    def get_job_type_cards(self) -> list:
        """
        Scroll through the Find Jobs by Types section and collect all cards.
        Returns list of dicts: [{"name": "Assessment", "count": "71"}, ...]
        Delegates to the global read_cards_with_count utility.
        """
        # Wait for at least one card to appear before starting
        self.is_element_present(self.JOB_TYPE_CARDS, timeout=10)
        return read_cards_with_count(self.driver, self.JOB_TYPE_CARDS)

    def get_job_status_cards(self) -> list:
        """
        After tapping a Job Type card, collect the sub-cards shown on that screen.
        Returns list of dicts: [{"name": "Active", "count": "5"}, ...]
        """
        self.is_element_present(self.JOB_STATUS_CARDS, timeout=10)
        return read_cards_with_count(self.driver, self.JOB_STATUS_CARDS)

    def tap_job_type_card(self, name: str):
        """
        Tap the Job Type card whose content-desc starts with the given name.
        Scrolls the card into view first if it is off-screen.
        """
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
            f'//android.view.ViewGroup[starts-with(@content-desc, "{name},")]',
        )
        self.click(locator)

    def tap_nav_home(self):
        self.click(self.NAV_HOME)

    def tap_nav_search(self):
        self.click(self.NAV_SEARCH)

    def tap_nav_schedule(self):
        self.click(self.NAV_SCHEDULE)
