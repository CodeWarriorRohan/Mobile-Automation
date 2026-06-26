"""
Seller Info Tab Test Cases - Test suite for the Job Details screen UI components.

Prerequisites: User is logged in and navigated to the Job Details Screen (via My Work or any other screen).
"""
import pytest
import sys
import os
import random
import logging
from appium.webdriver.common.appiumby import AppiumBy
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class TestSellerInfoTab:
    """Tests for the Seller Info tab in Job Details screen."""

    def test_tc65_seller_info_tab_visible(self, seller_info_page):
        """TC-65: 'Seller info' tab is visible on Job Details screen."""
        assert seller_info_page.is_seller_info_tab_visible(), "'Seller info' tab should be visible on Job Details screen"
    
    def test_tc66_tap_seller_info_tab(self, seller_info_page):
        """TC-66: Tapping 'Seller info' tab displays store name and address."""
        seller_info_page.tap_seller_info_tab()
        assert seller_info_page.get_store_name() != "", "Store name should be displayed in Seller info tab"
        assert seller_info_page.get_store_address() != "", "Store address should be displayed in Seller info tab"
