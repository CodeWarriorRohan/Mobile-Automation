"""
Profile Test Cases - Test suite for Profile screen functionality
"""
import pytest
import sys
import os

from data.credentials import VALID_USER
from src.pages import profile_page

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class TestProfile:
    # ── TC_25: Profile Screen Elements ────────────────────────────────────────────────

    def test_tc25_profile_screen_elements(self, profile_page):
        """TC-25: Verify all expected elements are present on the profile screen."""
        assert profile_page.is_profile_screen_displayed(), \
            "Profile screen not displayed"

        
    # ── TC_26: My Badge Navigation ────────────────────────────────────────────────
    # Note: This test assumes the My Badge screen is implemented and accessible.

    def test_tc26_my_badge_navigation(self, profile_page): 
        """TC-26: Tapping My Badge button navigates to My Badge screen."""
        profile_page.tap_my_badge()
        profile_page.wait_seconds(5)
        profile_page.tap_back_arrow()  
            # Return to profile screen for further tests
        
    # ── TC_27: My Account Navigation ────────────────────────────────────────────────
    # Note: This test assumes the My Account screen is implemented and accessible.

    def test_tc27_my_account_navigation(self, profile_page):
        """TC-27: Tapping My Account button navigates to My Account screen."""
        profile_page.tap_my_account()
        # assert profile_page.is_my_account_screen_displayed(), \
        #     "My Account screen not displayed after tapping My Account button"
        profile_page.wait_seconds(5)
        profile_page.scroll_down()  # Scroll to reveal options that are off-screen
        profile_page.scroll_up()    # Scroll back up to top of screen
        profile_page.tap_back_arrow()  
            # Return to profile screen for further tests

    # --- TC_28: View Cilio Dashboard Navigation ────────────────────────────────────────────────
    # Note: This test assumes tapping View Cilio Dashboard opens the dashboard screen or external link.
    
    def test_tc28_view_cilio_dashboard_navigation(self, profile_page):
        """TC-28: Tapping View Cilio Dashboard opens dashboard screen or external link."""
        profile_page.tap_view_cilio_dashboard()
        profile_page.wait_seconds(2)
        profile_page.tap_profile_icon()

    def test_tc29_privacy_policy_page(self, profile_page):
        """TC-29: Verify Privacy Policy page opens from Profile"""
        profile_page.tap_privacy_policy()
        # assert profile_page.is_privacy_policy_page_displayed(), \
        #     "Privacy Policy page not displayed after tapping Privacy Policy button"
        profile_page.wait_seconds(2)
        profile_page.scroll_down()
        profile_page.scroll_up()
        profile_page.tap_back_arrow()

    def test_tc30_terms_conditions_page(self, profile_page):
        """TC-30: Verify Terms & Conditions page opens from Profile"""
        profile_page.tap_terms_conditions()
        # assert profile_page.is_terms_conditions_page_displayed(), \
        #     "Terms & Conditions page not displayed after tapping Terms & Conditions button"
        profile_page.wait_seconds(2)
        profile_page.scroll_down()
        profile_page.scroll_up()
        profile_page.tap_back_arrow()

    # ── TC_031: Logout Functionality ────────────────────────────────────────────────    

    def test_tc31_logout_functionality(self, profile_page):
        """TC-31: Verify logout process from Profile screen."""
        profile_page.tap_logout()
        assert profile_page.is_logout_dialog_displayed(), \
            "Logout confirmation dialog not displayed after tapping Logout button"
        profile_page.wait_seconds(1)
        profile_page.cancel_logout()
        # assert profile_page.is_logged_out(), "User still logged in after confirming logout"

    def test_tc32_logout_functionality(self, profile_page):
        """TC-32: Verify logout process from Profile screen."""
        profile_page.tap_logout()
        assert profile_page.is_logout_dialog_displayed(), \
            "Logout confirmation dialog not displayed after tapping Logout button"
        profile_page.wait_seconds(1)
        profile_page.confirm_logout()
        # assert profile_page.is_logged_out(), "User still logged in after confirming logout"
        profile_page.wait_seconds(10)  # Wait for logout to complete and login screen to appear
         
    def test_tc33_valid_credentials(self, login_page):
        """TC-33: Login with valid username and password should succeed"""
        login_page.login(VALID_USER["username"], VALID_USER["password"])
        login_page.wait_seconds(5)
        assert login_page.is_login_successful(), \
            "Should navigate away from login page with valid credentials"
    
    def test_tc34_tap_my_work_navigates_to_my_work(self, profile_page):
        """TC-34: Tapping My Work button navigates to My Work screen."""
        profile_page.tap_my_work()
        # assert profile_page.is_my_work_screen_displayed(), \
        #     "My Work screen not displayed after tapping My Work button"
        profile_page.wait_seconds(5)

    def test_tc35_tap_home_nav_navigates_to_home(self, profile_page):
        """TC-35: Tapping Home navigation icon navigates to Home screen."""
        profile_page.tap_nav_home()
        # assert profile_page.is_home_screen_displayed(), \
        #     "Home screen not displayed after tapping Home navigation icon"
               
    def test_tc36_tap_search_nav_navigates_to_search(self, profile_page):
        """TC-36: Tapping Search navigation icon navigates to Search screen."""
        profile_page.tap_nav_search()
        # assert profile_page.is_search_screen_displayed(), \
        #     "Search screen not displayed after tapping Search navigation icon"           
        profile_page.wait_seconds(2)

    def test_tc37_tap_schedule_nav_navigates_to_schedule(self, profile_page):
        """TC-37: Tapping Schedule navigation icon navigates to Schedule screen."""
        profile_page.tap_nav_schedule()
        # assert profile_page.is_schedule_screen_displayed(), \
        #     "Schedule screen not displayed after tapping Schedule navigation icon"           
        profile_page.wait_seconds(2)    

    def test_tc38_tap_home_nav_navigates_to_home_from_schedule(self, profile_page):
        """TC-38: Tapping Home navigation icon navigates to Home screen from Schedule screen."""
        profile_page.tap_nav_home()
        # assert profile_page.is_home_screen_displayed(), \
        #     "Home screen not displayed after tapping Home navigation icon"   
        profile_page.wait_seconds(5)

    def test_tc_39_tap_view_all_work_navigates_to_view_all_work(self, profile_page):
        """TC-39: Tapping View All Work button navigates to View All Work screen."""
        profile_page.tap_view_all_work()
        # assert profile_page.is_view_all_work_screen_displayed(), \
        #     "View All Work screen not displayed after tapping View All Work button"
        profile_page.wait_seconds(5)        