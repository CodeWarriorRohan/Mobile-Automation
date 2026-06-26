"""
Login Test Cases - Test suite for login functionality
"""
import pytest
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from data.credentials import VALID_USER, INVALID_USER


class TestLogin:
    """Test class for Login functionality"""

    def test_tc01_empty_credentials(self, login_page):
        """TC-01: Login with empty username and password should fail"""
        login_page.clear_fields()
        login_page.login("", "")
        login_page.wait_seconds(2)
        
        assert login_page.is_login_page_displayed(), \
            "Should remain on login page with empty credentials"
        login_page.clear_fields()

    def test_tc02_valid_username_invalid_password(self, login_page):
        """TC-02: Login with valid username and invalid password should fail"""
        login_page.login(VALID_USER["username"], "wrongPass123")
        login_page.wait_seconds(2)
        
        assert login_page.is_login_page_displayed(), \
            "Should remain on login page with wrong password"
        login_page.clear_fields()

    def test_tc03_invalid_username_valid_password(self, login_page):
        """TC-03: Login with invalid username and valid password should fail"""
        login_page.login("wrongadmin", VALID_USER["password"])
        login_page.wait_seconds(2)
        
        assert login_page.is_login_page_displayed(), \
            "Should remain on login page with wrong username"
        login_page.clear_fields()

    def test_tc04_invalid_credentials(self, login_page):
        """TC-04: Login with invalid username and password should fail"""
        login_page.login(INVALID_USER["username"], INVALID_USER["password"])
        login_page.wait_seconds(2)
        
        assert login_page.is_login_page_displayed(), \
            "Should remain on login page with invalid credentials"
        login_page.clear_fields()

    def test_tc05_valid_credentials(self, login_page):
        """TC-05: Login with valid username and password should succeed"""
        login_page.login(VALID_USER["username"], VALID_USER["password"])
        login_page.wait_seconds(5)
        
        assert login_page.is_login_successful(), \
            "Should navigate away from login page with valid credentials"
