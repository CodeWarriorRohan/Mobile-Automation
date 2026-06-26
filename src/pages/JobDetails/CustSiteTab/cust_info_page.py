"""
Customer Page - Page Object for the Customer Contact Info section within a Job Details screen.

Locator strategy (priority order):
  1. XPATH  (text-based for labels/values, content-desc for groups)
  2. Coordinate-based tap  (for SVG icons without stable accessibility IDs)
"""
import logging

from appium.webdriver.common.appiumby import AppiumBy

from src.pages.JobDetails.job_base_page import JobBasePage
from utils.field_reader import read_input_field_hints


class CustomerPage(JobBasePage):

    # ------------------------------------------------------------------ #
    #  SECTION HEADER
    # ------------------------------------------------------------------ #

    FIRST_NAME_LABEL = (
        AppiumBy.XPATH, '//android.widget.TextView[@text="First Name"]'
    )

    LAST_NAME_LABEL = (
        AppiumBy.XPATH, '//android.widget.TextView[@text="Last Name"]'  
    )

    PHONE_LABEL = (
        AppiumBy.XPATH, '//android.widget.TextView[@text="Phone"]'
    )

    ALT_PHONE_LABEL = (
        AppiumBy.XPATH, '//android.widget.TextView[@text="Alt Phone"]'
    )

    ADDRESS_LABEL = (
        AppiumBy.XPATH, '//android.widget.TextView[@text="Address"]'
    )

    ADDRESS_TWO_LABEL = (
        AppiumBy.XPATH, '//android.widget.TextView[@text="Address Two"]'
    )

    CITY_LABEL = (
        AppiumBy.XPATH, '//android.widget.TextView[@text="City"]'
    )

    ZIP_LABEL = (
        AppiumBy.XPATH, '//android.widget.TextView[@text="ZIP"]'
    )

    # Address field container — ViewGroup[11] under the ScrollView root group.
    # (confirmed via Appium Inspector: contains Address label + value + Copy icon)
    ADDRESS_CONTAINER = (
        AppiumBy.XPATH,
        '//android.widget.TextView[@text="Address"]'
    )

    COUNTRY_PLACEHOLDER = "Select Country"

    SELECT_COUNTRY_DROPDOWN_LABEL = (
        AppiumBy.XPATH, f'//android.widget.TextView[@text="{COUNTRY_PLACEHOLDER}"]'
    )

    # ------------------------------------------------------------------ #
    #  COUNTRY DROPDOWN ARROW — Select Country
    #  bounds [949,2148][1014,2208]  →  center x=981, y=2178
    # ------------------------------------------------------------------ #

    COUNTRY_PARENT_CONTAINER = (
        AppiumBy.XPATH,
        f'(//android.widget.ScrollView//android.widget.TextView[@text="{COUNTRY_PLACEHOLDER}"]'
        '/ancestor::android.view.ViewGroup'
        '[.//android.view.ViewGroup[@clickable="true" and @content-desc]][1])[1]'
    )

    COUNTRY_DROPDOWN_OPTIONS = (
        AppiumBy.XPATH,
        '//android.view.ViewGroup[@clickable="true" and @content-desc and android.widget.TextView]'
    )
    COUNTRY_CLICKABLE_DESCENDANTS = (
        AppiumBy.XPATH,
        './/android.view.ViewGroup[@clickable="true" and @content-desc]'
    )

    EMAIL_LABEL = (
        AppiumBy.XPATH, '//android.widget.TextView[@text="Email Address"]'
    )


    CUSTOMER_EMAILS_LABEL = (
        AppiumBy.XPATH, '//android.widget.TextView[@text="Customer Emails"]'
    )

    CUSTOMER_CONTACT_INFO_LABEL = (
        AppiumBy.XPATH, '//android.widget.TextView[@text="Customer Contact Info"]'
    )

    # ------------------------------------------------------------------ #
    #  COPY ICON — Address field
    #  bounds [930,1790][993,1853]  →  center x=961, y=1821
    # ------------------------------------------------------------------ #

    COPY_ADDRESS_ICON = (
        AppiumBy.XPATH,
        '//android.widget.ScrollView/android.view.ViewGroup'
        '/android.view.ViewGroup[12]/com.horcrux.svg.SvgView'
    )
    _COPY_ADDRESS_X = 961
    _COPY_ADDRESS_Y = 1821

    # ------------------------------------------------------------------ #
    #  EDIT INFO ICON
    #  bounds [933,2062][996,2125]  →  center x=964, y=2093
    # ------------------------------------------------------------------ #

    EDIT_INFO_ICON = (
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
        '/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]'
        '/android.widget.FrameLayout/android.view.ViewGroup'
        '/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup'
        '/android.view.ViewGroup/android.view.ViewGroup'
        '/android.view.ViewGroup[11]/com.horcrux.svg.SvgView'
    )
    _EDIT_INFO_X = 964
    _EDIT_INFO_Y = 2093

    # ------------------------------------------------------------------ #
    #  EDIT MODE BUTTONS (visible after tapping Edit Info icon)
    # ------------------------------------------------------------------ #

    SAVE_CHANGES_BTN = (
        AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="Save Changes"]'
    )

    CANCEL_BTN = (
        AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="Cancel"]'
    )

    # EditText rows: ViewGroup with TextView (label) + EditText (value)
    _FIELD_ROWS = (
        AppiumBy.XPATH,
        '//android.widget.ScrollView//android.view.ViewGroup'
        '[android.widget.TextView and android.widget.EditText]'
    )

    # Dropdown rows: ViewGroup with TextView (label) + ViewGroup[@content-desc] (value)
    _DROPDOWN_ROWS = (
        AppiumBy.XPATH,
        '//android.widget.ScrollView//android.view.ViewGroup'
        '[android.widget.TextView and android.view.ViewGroup[@content-desc]]'
    )

    # Text-only rows: ViewGroup with 2 TextViews as label+value (e.g. Address field)
    # No EditText child, no content-desc ViewGroup child
    _TEXT_ROWS = (
        AppiumBy.XPATH,
        '//android.widget.ScrollView//android.view.ViewGroup'
        '[android.widget.TextView[2] and not(android.widget.EditText)'
        ' and not(android.view.ViewGroup[@content-desc])]'
    )

    # ================================================================== #
    #  VISIBILITY HELPERS
    # ================================================================== #

    def is_first_name_visible(self) -> bool:
        return self.is_element_visible(self.FIRST_NAME_LABEL)
    
    def is_last_name_visible(self) -> bool:
        return self.is_element_visible(self.LAST_NAME_LABEL)
    
    def is_phone_visible(self) -> bool:
        return self.is_element_visible(self.PHONE_LABEL)
    
    def is_alt_phone_visible(self) -> bool:
        return self.is_element_visible(self.ALT_PHONE_LABEL)
    
    def is_address_visible(self) -> bool:
        return self.is_element_visible(self.ADDRESS_LABEL)
    
    def is_address_two_visible(self) -> bool:
        return self.is_element_visible(self.ADDRESS_TWO_LABEL)
    
    def is_city_visible(self) -> bool:
        return self.is_element_visible(self.CITY_LABEL)
    
    def is_zip_visible(self) -> bool:
        return self.is_element_visible(self.ZIP_LABEL)
    
    def is_country_dropdown_label_visible(self) -> bool:
        try:
            return self.get_country_hint_element().is_displayed()
        except Exception:
            return False
    
    def is_country_dropdown_visible(self) -> bool: 
        try:
            return self.get_country_clickable_container().is_displayed()
        except Exception:
            return False
    
    def is_email_visible(self) -> bool:
        return self.is_element_visible(self.EMAIL_LABEL)
    
    def is_customer_emails_visible(self) -> bool:
        return self.is_element_visible(self.CUSTOMER_EMAILS_LABEL)

    def is_customer_contact_info_visible(self) -> bool:
        return self.is_element_visible(self.CUSTOMER_CONTACT_INFO_LABEL)

    def is_copy_address_icon_visible(self) -> bool:
        return self.is_element_visible(self.COPY_ADDRESS_ICON)

    def is_edit_info_icon_visible(self) -> bool:
        return self.is_element_visible(self.EDIT_INFO_ICON)

    def is_save_changes_visible(self) -> bool:
        return self.is_element_visible(self.SAVE_CHANGES_BTN)

    def is_cancel_visible(self) -> bool:
        return self.is_element_visible(self.CANCEL_BTN)

    # ================================================================== #
    #  ACTIONS
    # ================================================================== #

    def tap_copy_address_icon(self):
        """Tap copy icon for the Address field via XPath; falls back to coordinates."""
        try:
            self.click(self.COPY_ADDRESS_ICON)
        except Exception:
            self.driver.execute_script(
                "mobile: clickGesture",
                {"x": self._COPY_ADDRESS_X, "y": self._COPY_ADDRESS_Y}
            )

    @staticmethod
    def _country_dropdown_option_locator(option_text: str) -> tuple:
        return (
            AppiumBy.XPATH,
            f'//android.view.ViewGroup[@content-desc="{option_text}"]',
        )

    def _scroll_country_into_view(self):
        try:
            self.scroll_content_to_text(self.COUNTRY_PLACEHOLDER)
        except Exception:
            pass

    def _get_country_dropdown_option_values(self) -> list:
        values = []
        seen = set()

        for element in self.find_elements(self.COUNTRY_DROPDOWN_OPTIONS):
            value = (element.get_attribute("content-desc") or "").strip()
            if not value or value in seen:
                continue
            seen.add(value)
            values.append(value)

        return values

    def get_country_parent_container(self):
        """Return the parent ViewGroup for the country field row."""
        self._scroll_country_into_view()
        return self.wait_for_element(self.COUNTRY_PARENT_CONTAINER)

    def get_country_clickable_descendants(self) -> list:
        """Return clickable content-desc descendants inside the country row."""
        parent = self.get_country_parent_container()
        return parent.find_elements(*self.COUNTRY_CLICKABLE_DESCENDANTS)

    def _rank_country_clickable_candidates(self, candidates: list) -> list:
        """Rank clickable descendants so the country field wins over icons/buttons."""
        hint_rect = self.get_country_hint_element().rect
        ranked = []

        for element in candidates:
            rect = element.rect
            width = rect.get("width", 0)
            y_gap = rect.get("y", 0) - hint_rect.get("y", 0)
            x_gap = abs(rect.get("x", 0) - hint_rect.get("x", 0))

            if width < 200:
                continue
            if y_gap < -80 or y_gap > 220:
                continue

            ranked.append((abs(y_gap), x_gap, -width, element))

        ranked.sort(key=lambda item: item[:3])
        return ranked

    def get_country_clickable_container(self):
        """Return the single clickable child that opens the country dropdown."""
        descendants = self.get_country_clickable_descendants()
        if len(descendants) != 1:
            ranked = self._rank_country_clickable_candidates(descendants)
            if ranked:
                return ranked[0][3]
            raise AssertionError(
                "Could not resolve the country dropdown child from the parent row "
                f"(found {len(descendants)} clickable descendants)"
            )
        return descendants[0]

    def get_country_value(self) -> str:
        """Return the selected country value from the clickable child."""
        return (self.get_country_clickable_container().get_attribute("content-desc") or "").strip()

    def is_country_empty(self) -> bool:
        """Return True when the country dropdown still shows the placeholder."""
        return self.get_country_value() == self.COUNTRY_PLACEHOLDER

    def get_country_hint_element(self):
        """Return the Select Country hint element anchored inside the parent row."""
        parent = self.get_country_parent_container()
        return parent.find_element(
            AppiumBy.XPATH,
            f'.//android.widget.TextView[@text="{self.COUNTRY_PLACEHOLDER}"]'
        )

    def tap_country_dropdown(self):
        """Tap the parent-scoped clickable child for the country dropdown."""
        container = self.get_country_clickable_container()
        try:
            container.click()
        except Exception:
            rect = container.rect
            self.driver.execute_script(
                "mobile: clickGesture",
                {
                    "x": int(rect["x"] + (rect["width"] / 2)),
                    "y": int(rect["y"] + (rect["height"] / 2)),
                }
            )

    def select_first_available_country(self, exclude_current: bool = True) -> str:
        """Select the first non-placeholder option from the country dropdown."""
        current_value = self.get_country_value()
        existing_values = self._get_country_dropdown_option_values()

        self.tap_country_dropdown()
        self.wait_seconds(1)

        option_values = self._get_country_dropdown_option_values()
        candidates = [
            value for value in option_values
            if value != self.COUNTRY_PLACEHOLDER
            and value not in existing_values
            and (not exclude_current or value != current_value)
        ]

        if not candidates:
            candidates = [
                value for value in option_values
                if value != self.COUNTRY_PLACEHOLDER
                and (not exclude_current or value != current_value)
            ]

        if not candidates:
            raise ValueError(
                "No selectable country options were found after opening the dropdown "
                f"(current value: {current_value!r}, values seen: {option_values})"
            )

        chosen = candidates[0]
        self.click(self._country_dropdown_option_locator(chosen))
        return chosen

    def tap_edit_info_icon(self):
        """Tap the Edit Info icon via XPath; falls back to coordinates."""
        try:
            self.click(self.EDIT_INFO_ICON)
        except Exception:
            self.driver.execute_script(
                "mobile: clickGesture",
                {"x": self._EDIT_INFO_X, "y": self._EDIT_INFO_Y}
            )

    def tap_cancel(self):
        """Tap the Cancel button (visible after tapping Edit Info)."""
        self.click(self.CANCEL_BTN)

    def tap_save_changes(self):
        """Tap the Save Changes button (visible after tapping Edit Info)."""
        self.click(self.SAVE_CHANGES_BTN)

    # ================================================================== #
    #  EDIT FIELD INPUTS
    #  Anchored to each EditText's hint attribute — stable across scroll.
    # ================================================================== #

    FIRST_NAME_INPUT = (
        AppiumBy.XPATH, '//android.widget.EditText[@hint="First Name"]'
    )
    LAST_NAME_INPUT = (
        AppiumBy.XPATH, '//android.widget.EditText[@hint="Last Name"]'
    )
    PHONE_INPUT = (
        AppiumBy.XPATH, '//android.widget.EditText[@hint="Phone"]'
    )
    ALT_PHONE_INPUT = (
        AppiumBy.XPATH, '//android.widget.EditText[@hint="Alt Phone"]'
    )
    ADDRESS_INPUT = (
        AppiumBy.XPATH, '//android.widget.EditText[@hint="Address"]'
    )
    ADDRESS_TWO_INPUT = (
        AppiumBy.XPATH, '//android.widget.EditText[@hint="Address Two"]'
    )
    CITY_INPUT = (
        AppiumBy.XPATH, '//android.widget.EditText[@hint="City"]'
    )
    ZIP_INPUT = (
        AppiumBy.XPATH, '//android.widget.EditText[@hint="ZIP"]'
    )
    EMAIL_INPUT = (
        AppiumBy.XPATH, '//android.widget.EditText[@hint="Email Address"]'
    )
    CUSTOMER_EMAIL_INPUT = (
        AppiumBy.XPATH, '//android.widget.EditText[@hint="Customer Emails"]'
    )
    CUSTOMER_CONTACT_INFO_INPUT = (
        AppiumBy.XPATH, '//android.widget.EditText[@hint="Customer Contact Info"]'
    )


    def fill_customer_fields(self, data: dict):
        """Clear and fill each EditText field present in *data*.

        Keys in *data* must match field label text exactly:
            "First Name", "Last Name", "Phone", "Alt Phone",
            "Address", "Address Two", "City", "ZIP", "Email Address",
            "Customer Email Address", "Customer Contact Info"


        Scrolls into view before typing so off-screen fields are reached.
        """
        _field_map = {
            "First Name":    self.FIRST_NAME_INPUT,
            "Last Name":     self.LAST_NAME_INPUT,
            "Phone":         self.PHONE_INPUT,
            "Alt Phone":     self.ALT_PHONE_INPUT,
            "Address":       self.ADDRESS_INPUT,
            "Address Two":   self.ADDRESS_TWO_INPUT,
            "City":          self.CITY_INPUT,
            "ZIP":           self.ZIP_INPUT,
            "Email Address": self.EMAIL_INPUT,
            "Customer Email Address": self.CUSTOMER_EMAIL_INPUT,
            "Customer Contact Info": self.CUSTOMER_CONTACT_INFO_INPUT,
        }
        for field_name, value in data.items():
            locator = _field_map.get(field_name)
            if locator is None:
                continue
            try:
                self.scroll_content_to_text(field_name)
            except Exception:
                pass
            self.send_keys(locator, value)
            self.send_keys(locator, value)
            try:
                self.driver.hide_keyboard()
            except Exception:
                pass
 
