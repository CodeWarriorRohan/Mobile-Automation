"""
Login Page - Page Object for Login Screen
"""
from appium.webdriver.webdriver import WebDriver
from appium.webdriver.common.appiumby import AppiumBy
from src.pages.base_page import BasePage
from utils.constants import USERNAME_FIELD, PASSWORD_FIELD, SIGN_IN_BUTTON, ERROR_MESSAGE

class LoginPage(BasePage):
    """Page Object for Login Screen"""

    # Locators for login page elements (defined in constants.py)
    
    USERNAME_FIELD = USERNAME_FIELD
    PASSWORD_FIELD = PASSWORD_FIELD
    SIGN_IN_BUTTON = SIGN_IN_BUTTON
    ERROR_MESSAGE = ERROR_MESSAGE

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def get_username_field(self):
        """Get username input field"""
        fields = self.find_elements(self.USERNAME_FIELD)
        return fields[0] if fields else None

    def get_password_field(self):
        """Get password input field"""
        fields = self.find_elements(self.PASSWORD_FIELD)
        return fields[1] if len(fields) > 1 else None

    def enter_username(self, username: str):
        """Enter username"""
        field = self.get_username_field()
        if field:
            field.clear()
            field.send_keys(username)

    def enter_password(self, password: str):
        """Enter password"""
        field = self.get_password_field()
        if field:
            field.clear()
            field.send_keys(password)

    def click_sign_in(self):
        """Click sign in button"""
        self.click(self.SIGN_IN_BUTTON)

    def login(self, username: str, password: str):
        """Perform login with given credentials"""
        self.enter_username(username)
        self.enter_password(password)
        self.click_sign_in()

    def clear_fields(self): 
        """Clear username and password fields"""
        username_field = self.get_username_field()
        password_field = self.get_password_field()
        if username_field:
            username_field.clear()
        if password_field:
            password_field.clear()

    def is_login_page_displayed(self) -> bool:
        """Check if login page is displayed"""
        return self.is_element_visible(self.SIGN_IN_BUTTON)

    def is_login_successful(self) -> bool:
        """Check if login was successful (Sign in button not visible)"""
        self.wait_seconds(2)
        return not self.is_element_present(self.SIGN_IN_BUTTON, timeout=3)

    def get_error_message(self) -> str:
        """Get error message if displayed"""
        try:
            error_elements = self.find_elements(self.ERROR_MESSAGE)
            for elem in error_elements:
                text = elem.text.lower()
                if any(word in text for word in ["error", "invalid", "incorrect", "required"]):
                    return elem.text
        except:
            pass
        return ""
