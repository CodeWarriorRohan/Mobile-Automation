# Profile Page after clicking the profile icon in the bottom nav. Shows user info and app

from appium.webdriver.common.appiumby import AppiumBy
from .base_page import BasePage
from utils.constants import CILIO_LOGO, USERNAME_FIELD, PASSWORD_FIELD, SIGN_IN_BUTTON, ERROR_MESSAGE, MY_WORK_BTN, MY_BADGE_BTN, PROFILE_ICON, BACK_ARROW, BACK_ARROW_X, BACK_ARROW_Y, PROFILE_ICON_X, PROFILE_ICON_Y, NAV_HOME, NAV_SEARCH, NAV_SCHEDULE, USER_NAME_TEXT,USER_ROLE_TEXT,VIEW_ALL_WORK_BTN


class ProfilePage(BasePage):

    # ── Profile ───────────────────────────────────────────────────────────────
    # The profile icon is a non-clickable com.horcrux.svg.SvgView (React Native SVG).
    # We target its closest clickable ancestor (ViewGroup/View wrapping it).

    PROFILE_ICON            = PROFILE_ICON
    # Fallback coordinates derived from Appium Inspector bounds [978,123][1041,186]
    _PROFILE_ICON_X         = PROFILE_ICON_X
    _PROFILE_ICON_Y         = PROFILE_ICON_Y
    BACK_ARROW              = BACK_ARROW
    _BACK_ARROW_X           = BACK_ARROW_X
    _BACK_ARROW_Y           = BACK_ARROW_Y
    CILIO_LOGO              = CILIO_LOGO
    PROFILE_IMAGE           = (AppiumBy.XPATH, '//android.widget.ImageView[@index="2"]')
    MY_BADGE_BTN            = MY_BADGE_BTN
    PROFILE_USER_NAME       = USER_NAME_TEXT
    PROFILE_ROLE            = USER_ROLE_TEXT
    REFRESH_BTN = (AppiumBy.XPATH, '//*[@content-desc="Refresh" or @text="Refresh"]')
    MY_ACCOUNT_BUTTON       = (AppiumBy.XPATH, '//*[@text="My Account"]')
    VIEW_CILIO_DASHBOARD    = (AppiumBy.XPATH, '//*[contains(@text,"View")]')
    PRIVACY_POLICY_BUTTON   = (AppiumBy.XPATH, '//*[@text="Privacy Policy"]')
    TERMS_CONDITIONS_BUTTON = (AppiumBy.XPATH, '//*[@text="Terms & Condition"]')
    LOGOUT_BTN              = (AppiumBy.XPATH, '//*[@content-desc="Logout"]')

    # ── Logout Confirmation Dialog ───────────────────────────────────────────
    LOGOUT_DIALOG_TITLE   = (AppiumBy.XPATH, '//android.widget.TextView[@text="Logout"]')
    LOGOUT_DIALOG_MESSAGE = (AppiumBy.XPATH, '//android.widget.TextView[@text="Are you sure you want to logout?"]')
    LOGOUT_CONFIRM_YES    = (AppiumBy.XPATH, '//android.widget.TextView[@text="Yes"]')
    LOGOUT_CONFIRM_NO     = (AppiumBy.XPATH, '//android.widget.TextView[@text="Cancel"]')

    # Locators for login page elements (defined in constants.py)

    USERNAME_FIELD = USERNAME_FIELD
    PASSWORD_FIELD = PASSWORD_FIELD
    SIGN_IN_BUTTON = SIGN_IN_BUTTON
    ERROR_MESSAGE = ERROR_MESSAGE
    MY_WORK_BTN = MY_WORK_BTN
    NAV_HOME = NAV_HOME
    NAV_SEARCH = NAV_SEARCH
    NAV_SCHEDULE = NAV_SCHEDULE
    VIEW_ALL_WORK_BTN = VIEW_ALL_WORK_BTN


    # ── Profile Screen Checks ────────────────────────────────────────────────

    def is_profile_screen_displayed(self) -> bool:
        """Check if profile screen is displayed."""
        return (
            self.is_element_visible(self.PROFILE_IMAGE, timeout=5) or
            self.is_element_visible(self.PROFILE_USER_NAME, timeout=5)
        )

    def is_cilio_logo_displayed(self) -> bool:
        return self.is_element_visible(self.CILIO_LOGO, timeout=3)

    def is_profile_image_displayed(self) -> bool:
        return self.is_element_present(self.PROFILE_IMAGE, timeout=3)

    def is_profile_user_name_displayed(self) -> bool:
        return self.is_element_visible(self.PROFILE_USER_NAME, timeout=3)

    def is_profile_role_displayed(self) -> bool:
        return self.is_element_visible(self.PROFILE_ROLE, timeout=3)

    def is_my_badge_displayed(self) -> bool:
        return self.is_element_visible(self.MY_BADGE_BTN, timeout=3)

    def is_my_account_displayed(self) -> bool:
        return self.is_element_visible(self.MY_ACCOUNT_BUTTON, timeout=3)

    def is_view_cilio_dashboard_displayed(self) -> bool:
        return self.is_element_visible(self.VIEW_CILIO_DASHBOARD, timeout=3)

    def is_privacy_policy_displayed(self) -> bool:
        return self.is_element_visible(self.PRIVACY_POLICY_BUTTON, timeout=3)

    def is_terms_conditions_displayed(self) -> bool:
        return self.is_element_visible(self.TERMS_CONDITIONS_BUTTON, timeout=3)

    def is_logout_displayed(self) -> bool:
        return self.is_element_visible(self.LOGOUT_BTN, timeout=3)

    # ── Actions ──────────────────────────────────────────────────────────────

    def tap_my_badge(self):
        self.click(self.MY_BADGE_BTN)
       

    def tap_my_account(self):
        self.click(self.MY_ACCOUNT_BUTTON) 

    def tap_view_cilio_dashboard(self):
        self.click(self.VIEW_CILIO_DASHBOARD)
        self.wait_seconds(5)         

    def tap_privacy_policy(self):
        self.click(self.PRIVACY_POLICY_BUTTON)

    def tap_terms_conditions(self):
        self.click(self.TERMS_CONDITIONS_BUTTON)

    def tap_logout(self):
        self.scroll_down()
        self.wait_seconds(1)
        self.click(self.LOGOUT_BTN)

    def is_logout_dialog_displayed(self) -> bool:
        """Returns True if the logout confirmation dialog is visible."""
        return (
            self.is_element_visible(self.LOGOUT_DIALOG_TITLE, timeout=5) and
            self.is_element_visible(self.LOGOUT_DIALOG_MESSAGE, timeout=5) and
            self.is_element_visible(self.LOGOUT_CONFIRM_YES, timeout=5)
        )

    def confirm_logout(self):
        """Tap Yes on the logout confirmation dialog."""
        self.click(self.LOGOUT_CONFIRM_YES)

    def cancel_logout(self):
        """Tap Cancel on the logout confirmation dialog."""
        self.click(self.LOGOUT_CONFIRM_NO)

    def tap_my_work(self):
        self.click(self.MY_WORK_BTN)  

    def tap_refresh(self):
        self.click(self.REFRESH_BTN)    

    def tap_nav_home(self):
        self.click(self.NAV_HOME)

    def tap_nav_search(self):
        self.click(self.NAV_SEARCH)

    def tap_nav_schedule(self):
        self.click(self.NAV_SCHEDULE)
    def tap_view_all_work(self):
        self.click(self.VIEW_ALL_WORK_BTN)               