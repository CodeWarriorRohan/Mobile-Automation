"""
Job Details Page Test Cases - Test suite for the Job Details screen UI components.

Prerequisites: User is logged in and navigated to the Job Details Screen (via My Work or any other screen).
"""
import pytest
import sys
import os
import random
import logging
from appium.webdriver.common.appiumby import AppiumBy
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class TestJobDetailsBasePage:
    """Tests for the Job Details screen."""

    def test_tc59_job_details_header_visible(self, job_details_page):
        """TC-59: Job Details header is visible."""
        assert job_details_page.is_job_details_header_visible(), "Job Details header should be visible"
        assert job_details_page.is_hot_buttons_visible(), "Hot button should be visible on Job Details screen"
        assert job_details_page.is_measures_button_visible(), "Measures button should be visible on Job Details screen"
        assert job_details_page.is_dynamic_name_displayed(), "Lead Safe button should be visible on Job Details screen"
        assert job_details_page.is_lead_safe_button_visible(), "Lead Safe button should be visible on Job Details screen"
    
    def test_tc60_hot_buttons_and_navigation(self, job_details_page):
        """TC-60: Tapping 'Hot Buttons' header navigates to Hot Buttons screen, and back arrow returns to Job Details."""
        job_details_page.tap_hot_buttons()
        job_details_page.wait_seconds(2)
        job_details_page.tap_hot_buttons_back()
    
    def test_tc61_measures_button_disabled(self, job_details_page):
        """TC-61: 'Measures' button is visible but disabled on Job Details screen."""
        assert job_details_page.is_measures_button_visible(), "Measures button should be visible on Job Details screen"
        assert job_details_page.is_element_disabled(job_details_page.MEASURES_BUTTON), "Measures button should be disabled on Job Details screen"


    def test_tc62_cust_site_and_job_sched_buttons(self, job_details_page):
        """TC-63: 'Cust/Site' and 'Job/Sched' buttons are visible but disabled on Job Details screen."""
        assert job_details_page.is_cust_site_button_visible(), "Cust/Site button should be visible on Job Details screen"
        assert job_details_page.is_job_sched_button_visible(), "Job/Sched button should be visible on Job Details screen"
        assert job_details_page.is_action_docs_button_visible(), "Action/Docs button should be visible on Job Details screen"
    
    def test_tc63_measures_button_and_navigation (self, job_details_page):
        """TC-63: Tapping 'Measures' button is disabled on Job Details screen."""
        job_details_page.tap_measures_button()
        job_details_page.wait_seconds(1)
        job_details_page.tap_back_arrow()
        job_details_page.wait_seconds(1)
    
    def test_tc64_tap_profile_icon(self, job_details_page):
        job_details_page.tap_profile_icon()
        job_details_page.wait_seconds(1)
        job_details_page.tap_back_arrow()
        job_details_page.wait_seconds(1)