from appium.webdriver.common.appiumby import AppiumBy
from src.pages.base_page import BasePage
from utils.constants import CILIO_LOGO, BACK_ARROW, BACK_ARROW_X, BACK_ARROW_Y, PROFILE_ICON, USER_NAME_TEXT, USER_ROLE_TEXT, MY_WORK_BTN, MY_BADGE_BTN, NAV_HOME, NAV_SEARCH, NAV_SCHEDULE, PROFILE_ICON_Y, PROFILE_ICON_X
import random

class SchedulerPage(BasePage):

    # Scheduler Tab
    SCHEDULER_TAB = (
        AppiumBy.XPATH, '//android.view.View[@content-desc="Schedule"]'
    )

    # ------------------------------------------------------------------ #
    #  HEADER
    # ------------------------------------------------------------------ #
    
    CILIO_LOGO = CILIO_LOGO

    MAP_ICON = (
        AppiumBy.XPATH,
        '//android.widget.FrameLayout[@resource-id="android:id/content"]'
        '/android.widget.FrameLayout'
        '/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup'
        '/android.view.ViewGroup/android.view.ViewGroup'
        '/android.view.ViewGroup[2]/android.view.ViewGroup[2]'
        '/android.widget.FrameLayout/android.view.ViewGroup'
        '/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup'
        '/android.view.ViewGroup/android.view.ViewGroup[1]'
        '/android.widget.FrameLayout/android.view.ViewGroup'
        '/android.view.ViewGroup/android.view.ViewGroup'
        '/android.view.ViewGroup[1]/android.widget.FrameLayout'
        '/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup'
        '/android.view.ViewGroup/android.view.ViewGroup'
        '/android.view.ViewGroup[2]/android.widget.ImageView'
    )

    MAP_ICON_X = 921
    MAP_ICON_Y = 154

    PROFILE_ICON = PROFILE_ICON
    _PROFILE_ICON_X = PROFILE_ICON_X
    _PROFILE_ICON_Y = PROFILE_ICON_Y

    # Map / Route screen (shown after tapping MAP_ICON)
    ROUTE_TEXT = (
        AppiumBy.XPATH, "//android.widget.TextView[contains(@text, \" Route\")]"
    )

    CALENDAR_ICON = (
        AppiumBy.XPATH,
        '//android.widget.FrameLayout[@resource-id="android:id/content"]'
        '/android.widget.FrameLayout'
        '/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup'
        '/android.view.ViewGroup/android.view.ViewGroup'
        '/android.view.ViewGroup[2]/android.view.ViewGroup[2]'
        '/android.widget.FrameLayout/android.view.ViewGroup'
        '/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup'
        '/android.view.ViewGroup/android.view.ViewGroup'
        '/android.widget.FrameLayout/android.view.ViewGroup'
        '/android.view.ViewGroup/android.view.ViewGroup'
        '/android.view.ViewGroup[1]/android.widget.FrameLayout'
        '/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup'
        '/android.view.ViewGroup/android.view.ViewGroup'
        '/android.view.ViewGroup[2]/android.view.ViewGroup/android.widget.ImageView'
    )
    CALENDAR_ICON_X = 921
    CALENDAR_ICON_Y = 154

    PICKUP_REPORT_BTN = (AppiumBy.XPATH, '//*[@text="Pickup Report"]')

    BACK_ARROW = (
        AppiumBy.XPATH,
        '//android.widget.FrameLayout[@resource-id="android:id/content"]'
        '/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup'
        '/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]'
        '/android.view.ViewGroup[2]/android.widget.FrameLayout/android.view.ViewGroup'
        '/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup'
        '/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout'
        '/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup'
        '/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup'
        '/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup'
        '/android.view.ViewGroup/android.view.ViewGroup[3]/android.widget.ImageView'
    )
    BACK_ARROW_X = 52
    BACK_ARROW_Y = 254

    # ------------------------------------------------------------------ #
    #  Calendar
    # ------------------------------------------------------------------ #

    LEFT_ARROW = (
        AppiumBy.XPATH, '(//android.widget.ImageView[@resource-id="undefined.leftArrow"])[2]'
    )

    RIGHT_ARROW = (
        AppiumBy.XPATH, '(//android.widget.ImageView[@resource-id="undefined.rightArrow"])[2]'
    )
    
    EXTEND_CALENDAR = (
        AppiumBy.XPATH, '//android.view.ViewGroup[@resource-id="undefined.knob"]' 
    )

    # Week calendar individual day buttons (resource-id: undefined.weekCalendar.day_YYYY-MM-DD)
    WEEK_CALENDAR_DAY = (
        AppiumBy.XPATH,
        '//*[contains(@resource-id, "undefined.weekCalendar.day_") and not(contains(@resource-id, ".text"))]'
    )

    # Any job card on the calendar (identified by time range in content-desc)
    CALENDAR_JOB_CARD = (
        AppiumBy.XPATH,
        '//android.view.ViewGroup[contains(@content-desc, "AM") or contains(@content-desc, "PM")]'
    )

    TODAY_BUTTON = (
        AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="Today"]'       
    )
    

    # Bottom sheet shown after tapping a job card
    BOTTOM_SHEET = (
    AppiumBy.XPATH, '(//android.widget.SeekBar[@content-desc="Bottom Sheet"])[2]'
    )
    
    BOTTOM_SHEET_TEXT = (
    AppiumBy.XPATH,
    '(//android.widget.SeekBar[@content-desc="Bottom Sheet"])[2]/parent::*/descendant::android.widget.TextView'
    )

    VIEW_JOB_BTN = (
    AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="View Job"]'
   )

    # ------------------------------------------------------------------ #
    #  BOTTOM NAVIGATION  (imported from utils.constants)
    # ------------------------------------------------------------------ #
    
    NAV_HOME     = NAV_HOME
    NAV_SEARCH   = NAV_SEARCH
    NAV_SCHEDULE = NAV_SCHEDULE

    # ------------------------------------------------------------------ #
    # Actions
    # ------------------------------------------------------------------ #

    def click_scheduler_tab(self):
        self.click(self.SCHEDULER_TAB)

    def tap_map_icon(self):
        try:
            self.click(self.MAP_ICON)
        except Exception:
            self.driver.execute_script(
                "mobile: clickGesture",
                {"x": self.MAP_ICON_X, "y": self.MAP_ICON_Y}
            )

    def tap_calendar_icon(self):
        try:
            self.click(self.CALENDAR_ICON)
        except Exception:
            self.driver.execute_script(
                "mobile: clickGesture",
                {"x": self.CALENDAR_ICON_X, "y": self.CALENDAR_ICON_Y}
            )

    def tap_profile_icon(self):
        self.click(self.PROFILE_ICON)

    def tap_pickup_report(self):
        self.click(self.PICKUP_REPORT_BTN)

    def tap_calendar_section_items(self):

        self.click(self.LEFT_ARROW)
        self.wait_seconds(1)
        self.click(self.RIGHT_ARROW)
        self.wait_seconds(1)
        self.click(self.EXTEND_CALENDAR)
        self.wait_seconds(1)
        self.click(self.EXTEND_CALENDAR)

    def tap_two_random_dates(self):
        cells = self.find_elements(self.WEEK_CALENDAR_DAY)
        assert len(cells) >= 2, 'Not enough day cells found in week calendar'
        idx = random.randint(0, len(cells) - 2)
        chosen = [cells[idx], cells[idx + 1]]
        for cell in chosen:
            desc = cell.get_attribute('content-desc') or cell.get_attribute('resource-id')
            cell.click()
            print(f'Tapped date cell: {desc}')
            self.wait_seconds(1)
        return chosen    
    
    def tap_back_arrow(self):
        try:
            self.click(self.BACK_ARROW)
        except Exception:
            self.driver.execute_script(
                "mobile: clickGesture",
                {"x": self.BACK_ARROW_X, "y": self.BACK_ARROW_Y}
            )

    def tap_random_job_card(self):
        cards = self.find_elements(self.CALENDAR_JOB_CARD)
        assert cards, 'No job cards found on calendar'
        chosen = random.choice(cards)
        print(f'Tapped job: {chosen.get_attribute("content-desc")}')
        chosen.click()

    def scroll_content_to_beginning(self):
        """Scroll the Job Details content area (instance(1)) back to the very top.
        Uses scrollToBeginning(10) — up to 10 scroll steps to reach the top."""
        self.driver.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiScrollable(new UiSelector().scrollable(true).instance(1))'
            '.scrollToBeginning(10)'
        )

    def scroll_content_to_text(self, text=None, max_swipes=10):
        """Scroll down by swiping until a CALENDAR_JOB_CARD (AM/PM in content-desc) is visible."""
        
        size = self.driver.get_window_size()
        w = size['width']
        h = size['height']
        for _ in range(max_swipes):
            cards = self.find_elements(self.CALENDAR_JOB_CARD)
            if cards:
                return
            self.driver.execute_script("mobile: swipeGesture", {
                "left": w // 2 - 50, "top": int(h * 0.25),
                "width": 100, "height": int(h * 0.5),
                "direction": "up", "percent": 1.0
            })
        
        self.wait_seconds(0.5)  

    def scroll_to_end(self):
        """Scroll the attachment list down to the very last item."""
        self.driver.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            f'new UiScrollable(new UiSelector().scrollable(true).instance(1))'
            f'.scrollToEnd(10)'
        )


    def log_bottom_sheet_details(self):
        """Wait for the bottom sheet, log and return all visible text fields."""
        self.wait_for_element(self.BOTTOM_SHEET)
        texts = self.find_elements(self.BOTTOM_SHEET_TEXT)
        details = [el.text for el in texts if el.text.strip()]
        for line in details:
            print(f'Bottom sheet detail: {line}')
        return details

    def tap_view_job(self):
        self.click(self.VIEW_JOB_BTN)    
        
    def tap_nav_home(self):
        self.click(self.NAV_HOME)

    def tap_nav_search(self):
        self.click(self.NAV_SEARCH)

    def tap_nav_schedule(self):
        self.click(self.NAV_SCHEDULE)

    