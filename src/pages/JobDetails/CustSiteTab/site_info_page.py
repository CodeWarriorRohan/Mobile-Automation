"""
 Site Info Page- Page Object for Site Info Tab in Job Details Screen.

 Locator strategy (priority order):
  1. ACCESSIBILITY_ID  (content-desc from Appium Inspector - most stable)
  2. ANDROID_UIAUTOMATOR  (for dynamic text / count matching)
  3. XPATH  (fallback only)
"""
import random

from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import TimeoutException

from src.pages.base_page import BasePage

class SiteInfoPage(BasePage):
    # ------------------------------------------------------------------ #
    #  SITE INFO TAB ELEMENTS
    # ------------------------------------------------------------------ #
    SITE_INFO_TAB = (AppiumBy.XPATH, '//android.widget.TextView[@text="Site Info"]')
    SELLER_DISTANCE_FIELD = (AppiumBy.XPATH, '//android.widget.TextView[@text="Distance to Seller"]')
    AVG_SELLER_TIME = (AppiumBy.XPATH, '//android.widget.TextView[@text="Avg. Time to Seller"]')
    BUILT_PRE_DATA_FIELD = (AppiumBy.XPATH, '//android.widget.TextView[@text="Built Pre-1978"]')
    LEAD_SAFE_FIELD = (AppiumBy.XPATH, '//android.widget.TextView[@text="Lead Safe Job"]')
    # Checkbox state detected via bounds — checked/unchecked render at different Y offsets
    CHECKBOX_CHECKED   = (AppiumBy.XPATH, '//android.widget.ImageView[@bounds="[991,1516][1038,1563]"]')
    CHECKBOX_UNCHECKED = (AppiumBy.XPATH, '//android.widget.ImageView[@bounds="[991,1511][1038,1558]"]')
    LEAD_SAFE_QUESTION = (AppiumBy.XPATH, '//android.widget.TextView[@text="Are Lead Safe Practices Required?"]')

    # ------------------------------------------------------------------ #
    # Zillow Info Bottom Sheet
    # ------------------------------------------------------------------ #

    ZILLOW_BUTTON = (AppiumBy.XPATH, '//android.widget.TextView[@text="View Zillow Info"]')

    ZILLOW_BOTTOM_SHEET_TITLE = (AppiumBy.XPATH, '//android.widget.TextView[@text="Zillow Information"]')

    BOTTOM_SHEET_DATA = (AppiumBy.XPATH, '//android.widget.TextView[@text="Year Built:"]')

    ZILLOW_WEBVIEW_LINK = (AppiumBy.XPATH, '//android.widget.TextView[@text="Terms of Service"]')

    ZILLOW_CLOSE_ICON = (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="Close"]')

    # ------------------------------------------------------------------ #
    #  DROPDOWN CONTAINERS
    #  Anchored by stable bounds from Appium Inspector (index 16 / 22)
    # ------------------------------------------------------------------ #
    DROPDOWN_BUILT_PRE = (
    AppiumBy.XPATH,
    '(//android.view.ViewGroup[@clickable="true" and @content-desc])[1]',
  )

    DROPDOWN_LEAD_SAFE_REQUIRED = (
        AppiumBy.XPATH,
        '(//android.view.ViewGroup[@clickable="true" and @content-desc])[2]',
    )
    # Overlay option rows — matched after the dropdown overlay opens.
    # Every selectable row has a content-desc AND a child TextView.
    ALL_DROPDOWN_OPTIONS = (
        AppiumBy.XPATH,
        '//android.view.ViewGroup[@content-desc and android.widget.TextView]',
    )

    LEAD_COLLECTION_BUTTON = (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="Lead Collection Form"]')

    RESPONSIBLE_USER_TAB = (AppiumBy.XPATH, '(//android.widget.TextView[@text="Responsible User"])[1]')

    RESPONSIBLE_USER_ICON = (
    AppiumBy.XPATH,
    '//android.widget.ImageView[@bounds="[951,1892][986,1945]"]/parent::android.view.ViewGroup',
)

    RESPONSIBLE_USER_DATA = (AppiumBy.XPATH, '(//android.widget.TextView[@text="Responsible User"])[2]') 
    # ------------------------------------------------------------------ #
    # Responsible User Bottom Sheet
    # ------------------------------------------------------------------ #
    
    BOTTOM_SHEET_TITLE = (AppiumBy.XPATH, '//android.widget.TextView[@text="Responsible User"]')

    BOTTOM_SHEET_CLOSE_BUTTON = (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="Close"]')

    # ------------------------------------------------------------------ #
    #  DYNAMIC LOCATOR BUILDERS
    # ------------------------------------------------------------------ #
    @staticmethod
    def _dropdown_option_locator(option_text: str) -> tuple:
        """Return a locator for a single option row in the open overlay."""
        return (
            AppiumBy.XPATH,
            f'//android.view.ViewGroup[@content-desc="{option_text}"]',
        )

    def get_dropdown_by_position(self, position: int = 1) -> tuple:
        """
        Get dropdown locator by position (1=1st unselected, 2=2nd unselected, etc).
        
        Handles index-shifting: When dropdown 1 is selected, dropdown 2's empty XPath
        changes from [2] to having no index at all.
        
        Strategy:
        1. If dropdown HAS selection → find "Select" label, use its parent clickable
        2. If dropdown has NO selection → find ViewGroup[@content-desc="Select"]
        
        Args:
            position: Which unselected dropdown to find (1, 2, 3, etc.)
        
        Returns:
            tuple: (By, locator_string) for the clickable dropdown
        """
        # Strategy 1: Try to find by "Select" label (indicates selection exists)
        select_label_xpath = f'(//android.widget.TextView[@text="Select"])[{position}]'
        
        try:
            self.wait_for_element((AppiumBy.XPATH, select_label_xpath), timeout=1)
            # Found label → dropdown has a selection
            # Get the parent clickable ViewGroup (ancestor, not direct parent)
            parent_xpath = f'({select_label_xpath})/ancestor::android.view.ViewGroup[@clickable="true"][1]'
            return (AppiumBy.XPATH, parent_xpath)
        except TimeoutException:
            pass
        
        # Strategy 2: No selection found → use ViewGroup with content-desc="Select"
        # First try with index (when multiple empty dropdowns exist)
        no_selection_indexed_xpath = f'(//android.view.ViewGroup[@content-desc="Select"])[{position}]'
        
        try:
            self.wait_for_element((AppiumBy.XPATH, no_selection_indexed_xpath), timeout=1)
            return (AppiumBy.XPATH, no_selection_indexed_xpath)
        except TimeoutException:
            pass
        
        # Fallback: Try without index (when other dropdowns are selected and index shifted)
        # This handles: [2] → no index when [1] has selection
        no_selection_no_index_xpath = f'//android.view.ViewGroup[@content-desc="Select"]'
        return (AppiumBy.XPATH, no_selection_no_index_xpath)

    # ------------------------------------------------------------------ #
    #  CHECKBOX STATE
    # ------------------------------------------------------------------ #
    def is_checkbox_checked(self) -> bool:
        """Return True if the Lead Safe checkbox is in its checked state."""
        return self.is_element_present(self.CHECKBOX_CHECKED)

    # ------------------------------------------------------------------ #
    #  VISIBILITY ASSERTIONS
    #  Both dropdowns are only rendered when the checkbox is checked.
    # ------------------------------------------------------------------ #
    def is_dropdown_built_pre_visible(self) -> bool:
        """Return True only when checkbox is checked AND the Built Pre-1978 dropdown is visible."""
        if not self.is_checkbox_checked():
            return False
        return self.is_element_visible(self.DROPDOWN_BUILT_PRE)

    def is_dropdown_lead_safe_required_visible(self) -> bool:
        """Return True only when checkbox is checked AND the Lead Safe Practices Required dropdown is visible."""
        if not self.is_checkbox_checked():
            return False
        return self.is_element_visible(self.DROPDOWN_LEAD_SAFE_REQUIRED)

    # ------------------------------------------------------------------ #
    #  READ SELECTED VALUE
    # ------------------------------------------------------------------ #

    def get_selected_dropdown_value(self, container_locator: tuple) -> str:
      """Return selected value — reads content-desc directly from the container."""
      container = self.wait_for_element(container_locator)
      return container.get_attribute("content-desc")
    
    def open_dropdown(self, container_locator: tuple):
      """Click the dropdown container (NOT the text)."""
      container = self.wait_for_element(container_locator)
      container.click()
   # ------------------------------------------------------------------ #
    #  COLLECT OPTIONS FROM OPEN OVERLAY
    # ------------------------------------------------------------------ #
    def get_all_dropdown_options(self) -> list:
        """Return all option labels visible in the currently open dropdown overlay."""
        elements = self.find_elements(self.ALL_DROPDOWN_OPTIONS)
        return [
            el.get_attribute("content-desc")
            for el in elements
            if el.get_attribute("content-desc")
        ]

    # ------------------------------------------------------------------ #
    #  SELECT A RANDOM OPTION
    # ------------------------------------------------------------------ #
    def select_random_dropdown_option(self, exclude_value: str = None) -> str:
        """Pick and tap a random option from the open overlay.

        Args:
            exclude_value: The label of the currently selected value — skipped so
                           the selection always changes.

        Returns:
            The label of the option that was tapped.
        """
        options = self.get_all_dropdown_options()
        candidates = [o for o in options if o != exclude_value] if exclude_value else options
        if not candidates:
            raise ValueError(
                f"No selectable options found in dropdown overlay "
                f"(all options: {options}, excluded: {exclude_value!r})"
            )
        chosen = random.choice(candidates)
        self.click(self._dropdown_option_locator(chosen))
        return chosen

    # ------------------------------------------------------------------ #
    #  ORCHESTRATION — open + random pick in one call
    # ------------------------------------------------------------------ #
    #  Placeholder text rendered when no option has been selected yet.
    _DROPDOWN_PLACEHOLDER = "Select"

    def open_and_select_random_option(self, container_locator: tuple) -> str:
        """
        Open dropdown and select random option.
        
        Handles dynamic dropdowns: empty dropdowns use content-desc="Select",
        selected dropdowns use TextView[@text="Select"] as label.
        
        Args:
            container_locator: Optional pre-defined locator tuple (legacy support)
            position: Dropdown position if no locator provided (1 = 1st, 2 = 2nd, etc.)
        
        Returns:
            str: The label of the option that was selected
        
        Example:
            chosen = site_info_page.open_and_select_random_option(position=1)  # 1st dropdown
            chosen = site_info_page.open_and_select_random_option(position=2)  # 2nd dropdown
        """
        # Step 1: Get current value (SAFE)
        current_value = self.get_selected_dropdown_value(container_locator)

        # Step 2: Open dropdown (FIXED — click container)
        self.open_dropdown(container_locator)

        self.wait_seconds(1)  # allow overlay animation

        # Step 3: Handle placeholder
        exclude = None if current_value == self._DROPDOWN_PLACEHOLDER else current_value

        # Step 4: Select option
        return self.select_random_dropdown_option(exclude_value=exclude)

 
    def tap_responsible_user_icon(self):
        """Tap the Responsible User icon to open the bottom sheet."""
        self.click(self.RESPONSIBLE_USER_ICON)

    def close_responsible_user_bottom_sheet(self):
        """Tap the Close button on the Responsible User bottom sheet."""
        self.tap_element(self.BOTTOM_SHEET_CLOSE_BUTTON)

    def tap_lead_collection_button(self):
        """Scroll to and tap the Lead Collection Form button."""
        self.scroll_to_text("Lead Collection Form")
        self.tap_element(self.LEAD_COLLECTION_BUTTON)

    def tap_zillow_icon(self):
        """Tap the Zillow icon to open the Zillow Information bottom sheet."""
        self.click(self.ZILLOW_BUTTON)
