from appium.webdriver.common.appiumby import AppiumBy
from src.pages.base_page import BasePage
import re
import logging

logger = logging.getLogger(__name__)

class NotesAndEmailPage(BasePage):

    # SECTION HEADER

    NOTES_AND_EMAIL_TAB = (
        AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="Notes & Email"]'
    )

    ADD_NOTES_BUTTON = (
        AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="+,  Add Notes"]'
    )

    ENTER_TEXT_FIELD = (
        AppiumBy.XPATH, '//android.widget.EditText[@text="Note"]'
    )

    ADD_NOTE_BUTTON = (
        AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="Add Note"]'
    )

    # Filter icon
    FILTER_ICON = (
        AppiumBy.XPATH,
        '//android.widget.FrameLayout[@resource-id="android:id/content"]'
        '/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup'
        '/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup'
        '/android.view.ViewGroup[2]/android.view.ViewGroup[2]/android.widget.FrameLayout'
        '/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup'
        '/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]'
        '/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup'
        '/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout'
        '/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup'
        '/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[10]'
        '/android.widget.ImageView'
    )

    # Specific filter options
    FILTER_STANDARD_NOTE = (
        AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="Show Standard Note (4)"]'
    )

    # Filter badge showing count = 1
    FILTER_BADGE_ONE = (
        AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="1"]/android.view.ViewGroup'
    )

    CLEAR_ALL_BTN = (
        AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="Clear All"]'
    )

    # All filter option rows inside the filter sheet (content-desc contains count in parens)
    FILTER_OPTION_ITEM = (
        AppiumBy.XPATH,
        '//android.view.ViewGroup[contains(@content-desc, "Show ") and contains(@content-desc, "(")]'
    )

    # Apply Filters / Clear All buttons inside filter sheet
    APPLY_FILTERS_BTN = (
        AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="Apply Filters"]'
    )

    # Individual note / email items in the list
    NOTE_ITEM = (
        AppiumBy.XPATH,
        '//android.widget.ScrollView/android.view.ViewGroup'
        '/android.widget.ScrollView/android.view.ViewGroup'
        '/android.view.ViewGroup'
    )

    # Actions

    def click_notes_and_email_tab(self):
        self.driver.find_element(*self.NOTES_AND_EMAIL_TAB).click()

    def click_add_notes_button(self):
        self.driver.find_element(*self.ADD_NOTES_BUTTON).click()

    def enter_note_text(self, text):
        self.driver.find_element(*self.ENTER_TEXT_FIELD).send_keys(text)

    def click_add_note_button(self):
        self.driver.find_element(*self.ADD_NOTE_BUTTON).click()

    # ------------------------------------------------------------------
    #  SCROLL HELPERS
    # ------------------------------------------------------------------

    def scroll_to_end(self):
        """Scroll the notes and email list down to the very last item."""
        self.driver.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            f'new UiScrollable(new UiSelector().scrollable(true).instance(1))'
            f'.scrollToEnd(32)'
        )

    def scroll_to_beginning(self):
        """Scroll the notes and email list back up to the very first item."""
        self.driver.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiScrollable(new UiSelector().scrollable(true).instance(1))'
            '.scrollToBeginning(32)'
        )

    # ------------------------------------------------------------------
    #  FILTER HELPERS
    # ------------------------------------------------------------------

    def click_filter_icon(self):
        self.tap_element(self.FILTER_ICON)

    def click_standard_note_filter(self):
        el = self.wait_for_element(self.FILTER_STANDARD_NOTE)
        desc = el.get_attribute('content-desc')
        m = re.search(r'\((\d+)\)', desc)
        count = int(m.group(1)) if m else 0
        el.click()
        return desc, count

    def is_filter_badge_one(self) -> bool:
        """Return True when the filter badge shows exactly 1."""
        return self.is_displayed(self.FILTER_BADGE_ONE, timeout=5)

    def click_apply_filters(self):
        self.click(self.APPLY_FILTERS_BTN)

    def click_clear_all(self):
        self.click(self.CLEAR_ALL_BTN)
