"""
My Work Page - Page Object for the My Work / Home screen.

Locator strategy (priority order):
  1. ACCESSIBILITY_ID  (content-desc from Appium Inspector - most stable)
  2. ANDROID_UIAUTOMATOR  (for dynamic text / count matching)
  3. XPATH  (fallback only)
"""
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import TimeoutException

from src.pages.base_page import BasePage
from utils.constants import CILIO_LOGO, BACK_ARROW, BACK_ARROW_X, BACK_ARROW_Y, PROFILE_ICON, USER_NAME_TEXT, USER_ROLE_TEXT, VIEW_ALL_WORK_BTN, MY_BADGE_BTN, NAV_HOME, NAV_SEARCH, NAV_SCHEDULE,PROFILE_ICON_X, PROFILE_ICON_Y
from utils.card_reader import read_cards_with_count


class MyWorkPage(BasePage):

    # ------------------------------------------------------------------ #
    #  HEADER
    #  CILIO_LOGO  : android.widget.ImageView — top-left, bounds [39,115][197,193]
    #  PROFILE_ICON: com.horcrux.svg.SvgView  — top-right, bounds [978,123][1041,186]
    # ------------------------------------------------------------------ #
    CILIO_LOGO = CILIO_LOGO
    BACK_ARROW = BACK_ARROW
    BACK_ARROW_X = BACK_ARROW_X
    BACK_ARROW_Y = BACK_ARROW_Y

    PROFILE_ICON = PROFILE_ICON
    _PROFILE_ICON_X = PROFILE_ICON_X
    _PROFILE_ICON_Y = PROFILE_ICON_Y

    # ------------------------------------------------------------------ #
    #  USER INFO CARD
    # ------------------------------------------------------------------ #
    USER_NAME_TEXT    = USER_NAME_TEXT
    USER_ROLE_TEXT    = USER_ROLE_TEXT
    VIEW_ALL_WORK_BTN = VIEW_ALL_WORK_BTN
    MY_BADGE_BTN      = MY_BADGE_BTN

    # ------------------------------------------------------------------ #
    #  REFRESH
    # ------------------------------------------------------------------ #
    REFRESH_BTN       = (AppiumBy.XPATH, '//*[@content-desc="Refresh" or @text="Refresh"]')

    # ------------------------------------------------------------------ #
    #  WORK CARDS
    #  content-desc includes count e.g. "Today's Work, 1"
    #  starts-with keeps locators stable regardless of count value
    # ------------------------------------------------------------------ #
    TODAY_CARD        = (AppiumBy.XPATH, '//android.view.ViewGroup[starts-with(@content-desc, "Today\'s Work")]/android.widget.ImageView[1]')
    TOMORROW_CARD     = (AppiumBy.XPATH, '//android.view.ViewGroup[starts-with(@content-desc, "Tomorrow\'s Work")]/android.widget.ImageView[1]')
    YESTERDAY_CARD    = (AppiumBy.XPATH, '//android.view.ViewGroup[starts-with(@content-desc, "Yesterday\'s Work")]/android.widget.ImageView[1]')

    # Single locator that matches all three work-card summary ViewGroups
    # ("Today's Work, N" / "Tomorrow's Work, N" / "Yesterday's Work, N")
    ALL_WORK_CARDS    = (AppiumBy.XPATH, '//android.view.ViewGroup[contains(@content-desc, "s Work,")]')
    # ------------------------------------------------------------------ #
    #  BOTTOM NAVIGATION  (imported from utils.constants)
    # ------------------------------------------------------------------ #
    NAV_HOME     = NAV_HOME
    NAV_SEARCH   = NAV_SEARCH
    NAV_SCHEDULE = NAV_SCHEDULE

    # ------------------------------------------------------------------ #
    #  SECTION HEADERS (appear below cards when count > 0)
    # ------------------------------------------------------------------ #
    SECTION_TODAY     = (AppiumBy.XPATH, '(//android.widget.TextView[@text="Yesterday\'s Work"])[2]')
    SECTION_TOMORROW  = (AppiumBy.XPATH, '(//android.widget.TextView[@text="Tomorrow\'s Work"])[2]')
    SECTION_YESTERDAY = (AppiumBy.XPATH, '(//android.widget.TextView[@text="Yesterday\'s Work"])[2]')

    # ------------------------------------------------------------------ #
    #  JOB DETAIL CARD
    # ------------------------------------------------------------------ #
    PICKUP_REPORT_BTN = (AppiumBy.XPATH, '//*[@text="Pickup Report"]')
    JOB_CARD_NAME     = (AppiumBy.XPATH, '//android.widget.TextView[contains(@text, ",")]')
    JOB_CREW_PAY      = (AppiumBy.XPATH, '//android.widget.TextView[contains(@text, "$")]')
    NAME          = (AppiumBy.XPATH, '//android.widget.TextView[@text="Name :"]')
    CREW_PAY      = (AppiumBy.XPATH, '//android.widget.TextView[@text="Crew Pay :"]')

    # Tappable job card row — content-desc contains both "Name :" and "Crew Pay :"
    JOB_SECTION_CARD = (AppiumBy.XPATH, '//android.view.ViewGroup[contains(@content-desc, "Name :") and contains(@content-desc, "Crew Pay :")]')

    # ------------------------------------------------------------------ #
    #  EXPANDED JOB DETAIL FIELDS
    # ------------------------------------------------------------------ #
    DROPDOWN_ICON  = (AppiumBy.XPATH, '//android.view.ViewGroup[contains(@content-desc, "Name :")]/android.view.ViewGroup[2]/android.view.ViewGroup[1]')
    LABOR_CATEGORY = (AppiumBy.XPATH, '//android.widget.TextView[@text="Labor Category :"]')
    CUSTOMER_CITY  = (AppiumBy.XPATH, '//android.widget.TextView[@text="Customer City :"]')
    COMPANY_FIELD  = (AppiumBy.XPATH, '//android.widget.TextView[@text="Company :"]')
    START_TIME     = (AppiumBy.XPATH, '//android.widget.TextView[@text="Start :"]')
    END_TIME       = (AppiumBy.XPATH, '//android.widget.TextView[@text="End :"]')
    DURATION_FIELD = (AppiumBy.XPATH, '//android.widget.TextView[@text="Duration :"]')
    SCOPE_OF_WORK  = (AppiumBy.XPATH, '//android.widget.TextView[@text="Scope of work"]')

    # ------------------------------------------------------------------ #
    #  ROUTE BUTTONS (dynamic — depend on which card has data)
    # ------------------------------------------------------------------ #
    ROUTE_TODAY     = (AppiumBy.XPATH, '//*[@text="Today\'s Route"]')
    ROUTE_TOMORROW  = (AppiumBy.XPATH, '//*[@text="Tomorrow\'s Route"]')
    ROUTE_YESTERDAY = (AppiumBy.XPATH, '//*[@text="Yesterday\'s Route"]')

    # Generic route button matched via content-desc (any day)
    ROUTE_BTN = (AppiumBy.XPATH, '//android.view.ViewGroup[contains(@content-desc, "Route")]')

    # ================================================================== #
    #  REUSABLE HELPERS
    # ================================================================== #

    def is_my_work_displayed(self) -> bool:
        """Confirm My Work screen is loaded by checking the Today's Work card."""
        return self.is_element_visible(self.TODAY_CARD)

    def get_work_card(self, card_name: str):
        """
        Return work card element whose content-desc starts with card_name.
        card_name: "Today's Work" | "Tomorrow's Work" | "Yesterday's Work"
        """
        locator = (AppiumBy.XPATH, f'//*[starts-with(@content-desc, "{card_name}")]')
        return self.wait_for_element(locator)

    def get_work_count(self, card_name: str) -> int:
        """
        Parse the numeric count from a work card's content-desc.
        e.g. "Today's Work, 3" -> 3
        """
        try:
            card = self.get_work_card(card_name)
            desc = card.get_attribute("content-desc")
            return int(desc.split(",")[-1].strip())
        except (ValueError, AttributeError, TimeoutException):
            return 0

    def any_card_has_jobs(self) -> bool:
        """Returns True if at least one work card has count > 0."""
        return any(
            self.get_work_count(n) > 0
            for n in ("Today's Work", "Tomorrow's Work", "Yesterday's Work")
        )

    def cards_with_jobs(self) -> list:
        """Returns list of card names whose count > 0."""
        return [
            n for n in ("Today's Work", "Tomorrow's Work", "Yesterday's Work")
            if self.get_work_count(n) > 0
        ]

    def is_job_section_visible(self, section_name: str) -> bool:
        """Check whether a named section header is visible below the cards.

        The card label at the top always matches the same text, so there is
        always at least 1 node. The section header below the cards adds a
        second node — >= 2 means the section is rendered.
        """
        locator = (AppiumBy.XPATH, f'//android.widget.TextView[@text="{section_name}"]')
        elements = self.driver.find_elements(*locator)
        return len(elements) >= 2

    def get_field_value(self, label_text: str) -> str:
        """
        Given a static label (e.g. "Labor Category"), return the adjacent
        dynamic value TextView rendered next to it in the expanded job card.

        Tries two XPath sibling strategies to cover different layout structures:
          1. following-sibling  — label and value are direct siblings
          2. parent TextView[2] — label and value share a parent ViewGroup
        Returns empty string if value element is not found.
        """
        strategies = [
            f'//android.widget.TextView[@text="{label_text}"]/following-sibling::android.widget.TextView[1]',
            f'//android.widget.TextView[@text="{label_text}"]/../android.widget.TextView[2]',
        ]
        for xpath in strategies:
            try:
                elements = self.driver.find_elements(AppiumBy.XPATH, xpath)
                if elements:
                    return elements[0].text.strip()
            except Exception:
                continue
        return ""

    def get_work_cards_info(self) -> list:
        """
        Return name + count for all three day-summary work cards.
        All three cards are always on screen so scrolling is disabled.
        Returns: [{"name": "Today's Work", "count": "2"}, ...]
        """
        return read_cards_with_count(self.driver, self.ALL_WORK_CARDS, scroll=False)

    def get_job_section_card_count(self) -> int:
        """Return the number of Job Detail cards currently rendered in the DOM."""
        return len(self.driver.find_elements(*self.JOB_SECTION_CARD))

    def expand_job_details_by_index(self, card_index: int):
        """
        Expand the job detail card at position card_index (1-based).
        Clicks the dropdown chevron for that specific card, waits for the
        animation, then scrolls the expanded fields into view.
        """
        locator = (
            AppiumBy.XPATH,
            f'(//android.view.ViewGroup[contains(@content-desc, "Name :")]'
            f'/android.view.ViewGroup[2]/android.view.ViewGroup[1])[{card_index}]',
        )
        self.click(locator)
        import time
        time.sleep(0.3)  # brief pause for expand animation
        self.scroll_down()

    def is_expanded_field_visible_for_card(self, card_index: int, label_text: str) -> bool:
        """
        Return True if the field label is visible inside job card at card_index (1-based).
        Uses a scoped XPath so it only matches within that specific card's subtree.
        """
        locator = (
            AppiumBy.XPATH,
            f'(//android.view.ViewGroup[contains(@content-desc, "Name :")'
            f' and contains(@content-desc, "Crew Pay :")])[{card_index}]'
            f'//android.widget.TextView[@text="{label_text}"]',
        )
        return self.is_element_visible(locator)

    def get_expanded_field_value_for_card(self, card_index: int, label_text: str) -> str:
        """
        Return the dynamic value text adjacent to label_text inside job card
        at card_index (1-based). Returns empty string if not found.
        """
        xpath = (
            f'(//android.view.ViewGroup[contains(@content-desc, "Name :")'
            f' and contains(@content-desc, "Crew Pay :")])[{card_index}]'
            f'//android.widget.TextView[@text="{label_text}"]'
            f'/following-sibling::android.widget.TextView[1]'
        )
        try:
            elements = self.driver.find_elements(AppiumBy.XPATH, xpath)
            if elements:
                return elements[0].text.strip()
        except Exception:
            pass
        return ""

    def expand_job_details(self):
        """Click the dropdown icon and scroll expanded section into view."""
        self.click(self.DROPDOWN_ICON)
        import time
        time.sleep(1)  # allow expand animation to complete
        try:
            self.scroll_to_text("Labor Category")
        except Exception:
            # scroll forward a step if UiScrollable cant find text yet
            self.scroll_down()

    def is_route_button_visible(self) -> bool:
        """Returns True if any route button (Today/Tomorrow/Yesterday) is visible."""
        for locator in (self.ROUTE_TODAY, self.ROUTE_TOMORROW, self.ROUTE_YESTERDAY):
            if self.is_element_visible(locator, timeout=3):
                return True
        return False
    def tap_refresh(self):
        self.click(self.REFRESH_BTN)

    def tap_view_all_work(self):
        self.click(self.VIEW_ALL_WORK_BTN)

    def tap_my_badge(self):
        self.click(self.MY_BADGE_BTN)

    def tap_todays_work(self):
        self.click(self.TODAY_CARD)

    def tap_tomorrows_work(self):
        self.click(self.TOMORROW_CARD)

    def tap_yesterdays_work(self):
        self.click(self.YESTERDAY_CARD)

    def tap_card_with_jobs(self) -> str:
        """
        Scroll to top, find the first work card with count > 0, tap it,
        and wait for the job section to appear.
        Returns the card name that was tapped, e.g. "Today's Work".
        Raises ValueError if no card has jobs.
        """
        self.scroll_up()
        import time
        time.sleep(1)
        tap_map = {
            "Today's Work":     self.tap_todays_work,
            "Tomorrow's Work":  self.tap_tomorrows_work,
            "Yesterday's Work": self.tap_yesterdays_work,
        }
        for name, tap_fn in tap_map.items():
            if self.get_work_count(name) > 0:
                tap_fn()
                # wait for section header to confirm navigation/render
                self.is_job_section_visible(name)
                return name
        raise ValueError("tap_card_with_jobs: no card has count > 0")

    def scroll_to_route_button(self):
        """Scroll until any route button (text contains 'Route') is visible. Returns element text or None."""
        try:
            element = self.driver.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiScrollable(new UiSelector().scrollable(true))'
                '.scrollIntoView(new UiSelector().textContains("Route"))'
            )
            return element.text
        except Exception:
            return None
        
    
    def tap_pickup_report(self):
        self.click(self.PICKUP_REPORT_BTN)

    def tap_job_section_card(self):
        """Tap the job card row (ViewGroup with Name/Crew Pay in content-desc)."""
        self.click(self.JOB_SECTION_CARD)

    def tap_route_button(self):
        """Tap whichever route button (Today/Tomorrow/Yesterday) is visible."""
        self.click(self.ROUTE_BTN)    

    def tap_nav_home(self):
        self.click(self.NAV_HOME)

    def tap_nav_search(self):
        self.click(self.NAV_SEARCH)

    def tap_nav_schedule(self):
        self.click(self.NAV_SCHEDULE)
