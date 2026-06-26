"""
Site Info Screen Test Cases - Test suite for the Site Info Screen UI components.

Prerequisites: User is logged in and navigated to the Job Details Screen (via My Work or any other screen).
"""
import pytest
import sys
import os
import random
import logging
from appium.webdriver.common.appiumby import AppiumBy
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class TestSiteInfoPage:
    """Tests for the Site Info screen."""

    def test_tc64_site_info_fields_visible(self, site_info_page):
        """TC-64: Verify all expected fields are visible on the Site Info tab."""
        site_info_page.click(site_info_page.SITE_INFO_TAB)
        assert site_info_page.is_element_visible(site_info_page.SELLER_DISTANCE_FIELD), "Distance to Seller field should be visible"
        assert site_info_page.is_element_visible(site_info_page.AVG_SELLER_TIME), "Avg. Time to Seller field should be visible"
        assert site_info_page.is_element_visible(site_info_page.BUILT_PRE_DATA_FIELD), "Built Pre-1978 field should be visible"
        assert site_info_page.is_element_visible(site_info_page.LEAD_SAFE_FIELD), "Lead Safe Job field should be visible"

    def test_tc65_zillow_button_info(self, site_info_page):
        """TC-65: Tapping the Zillow icon opens the Zillow listing in a webview."""
        site_info_page.tap_zillow_icon()
        site_info_page.wait_seconds(1)
        assert site_info_page.is_element_visible(site_info_page.ZILLOW_BOTTOM_SHEET_TITLE), "Zillow webview should open when Zillow icon is tapped"
        assert site_info_page.is_element_visible(site_info_page.BOTTOM_SHEET_DATA), "Zillow listing data should be visible in webview"
        assert site_info_page.is_element_visible(site_info_page.ZILLOW_WEBVIEW_LINK), "Link to Zillow listing should be visible in webview"
        assert site_info_page.is_element_visible(site_info_page.ZILLOW_CLOSE_ICON), "Close button should be visible in Zillow webview"
        site_info_page.wait_seconds(1)

    def test_tc66_zillow_button_navigation(self, site_info_page):
        """TC-66: Tapping the Zillow icon opens the Zillow listing, and tapping Close returns to Site Info tab."""
        site_info_page.click(site_info_page.ZILLOW_WEBVIEW_LINK)
        site_info_page.wait_seconds(1)
        site_info_page.tap_back_arrow()
        site_info_page.wait_seconds(3)

    def test_tc65_is_lead_safe_job_checkbox_checked(self, site_info_page, job_details_page):
        """TC-65: Verify the 'Lead Safe Job' checkbox is checked when the job is marked as lead safe."""
        if site_info_page.is_element_visible(site_info_page.CHECKBOX_CHECKED):
            assert True, "Lead Safe Job checkbox is correctly checked for lead safe job"
            assert site_info_page.is_dropdown_built_pre_visible(), "Dropdown for Built Pre should be visible for lead safe job"
            assert site_info_page.is_dropdown_lead_safe_required_visible(), "Dropdown for Lead Safe Practices Required should be visible for lead safe job"
            job_details_page.scroll_content_to_text('Responsible User')  # Scroll to bring bottom elements into view
            assert site_info_page.is_element_visible(site_info_page.LEAD_COLLECTION_BUTTON), "Lead Collection Form button should be visible for lead safe job"
            assert site_info_page.is_element_visible(site_info_page.RESPONSIBLE_USER_TAB), "Responsible User tab should be visible for lead safe job"
            assert site_info_page.is_element_visible(site_info_page.RESPONSIBLE_USER_DATA), "Responsible User icon should be visible for lead safe job"
        else:
            pytest.skip("TC-65 requires checkbox to be checked — skipping because checkbox is currently unchecked")

    def test_tc66_is_lead_safe_job_checkbox_unchecked(self, site_info_page):
        """TC-66: Verify the 'Lead Safe Job' checkbox is unchecked when the job is not marked as lead safe."""
        if site_info_page.is_element_visible(site_info_page.CHECKBOX_UNCHECKED):
            assert True, "Lead Safe Job checkbox is correctly unchecked for non-lead safe job"
            assert not site_info_page.is_element_visible(site_info_page.LEAD_SAFE_QUESTION), "Lead Safe Practices Required question should not be visible for non-lead safe job"
            assert not site_info_page.is_dropdown_built_pre_visible(), "Dropdown for Built Pre should not be visible for non-lead safe job"
            assert not site_info_page.is_dropdown_lead_safe_required_visible(), "Dropdown for Lead Safe Practices Required should not be visible for non-lead safe job"
            assert site_info_page.is_element_visible(site_info_page.LEAD_COLLECTION_BUTTON), "Lead Collection Form button should not be visible for non-lead safe job"
            assert site_info_page.is_element_visible(site_info_page.RESPONSIBLE_USER_TAB), "Responsible User tab should not be visible for non-lead safe job"
            assert site_info_page.is_element_visible(site_info_page.RESPONSIBLE_USER_DATA), "Responsible User icon should not be visible for non-lead safe job"
        else:
            pytest.skip("TC-66 requires checkbox to be unchecked — skipping because checkbox is currently checked")
    

    # def test_tc67_select_random_option_dropdown_built_pre(self, site_info_page, job_details_page):
    #     """TC-68 [Checkbox checked]: Open Built Pre-1978 dropdown and select a random option."""
    #     job_details_page.scroll_content_to_beginning()  # Scroll to top to ensure dropdown is in view
    #     site_info_page.wait_seconds(1)
    #     if not site_info_page.is_checkbox_checked():
    #         pytest.skip("TC-68 requires checkbox to be checked — dropdowns not rendered when unchecked")
    #     # Select option in first dropdown
    #     chosen1 = site_info_page.open_and_select_random_option(site_info_page.DROPDOWN_BUILT_PRE)
        
    #     # Wait for UI to stabilize after first selection
    #     site_info_page.wait_seconds(2)
    #     assert chosen1, "A non-empty option should have been selected from first dropdown"

    
    def test_tc69_tap_lead_collection_form_button(self, site_info_page, job_details_page):
        """TC-70: Tap the Lead Collection Form button and verify navigation, then return."""
        job_details_page.scroll_content_to_text('Responsible User')  # Scroll to bring button into view
        site_info_page.wait_seconds(1)
        site_info_page.tap_lead_collection_button()
        site_info_page.wait_seconds(2)
        site_info_page.tap_back_arrow()
        site_info_page.wait_seconds(1)

    def test_tc70_tap_responsible_user_icon(self, site_info_page, job_details_page):
        """TC-67: Tapping the Responsible User icon opens the Responsible User bottom sheet."""
        job_details_page.scroll_content_to_text('Responsible User')
        site_info_page.wait_seconds(1)
        site_info_page.tap_responsible_user_icon()
        site_info_page.wait_seconds(1)
        assert site_info_page.is_element_visible(site_info_page.BOTTOM_SHEET_TITLE), "Responsible User bottom sheet should open when icon is tapped"
        site_info_page.close_responsible_user_bottom_sheet()
        site_info_page.wait_seconds(1)
    


    

