"""
Related Order Test Cases
"""
import logging
import pytest

from tests.conftest import customer_page

class TestRelatedOrder:
    
    def test_tc70_click_related_order_tab(self, related_order_page):
        """TC-70:
        1. Tap the Related Order tab.
        2. Verify the Related and Umbrella tabs are visible.
        3. Tap the Related tab, verify related job details are visible.
        4. Tap the Umbrella tab, verify umbrella job details are visible.
        """
        # Step 1 — tap Related Order tab
        related_order_page.click_related_order_tab()
        related_order_page.wait_seconds(1)

        # Step 2 — verify Related and Umbrella tabs are visible
        assert related_order_page.is_related_tab_visible(), \
            "Related tab should be visible on Related Order page"
        assert related_order_page.is_umbrella_tab_visible(), \
            "Umbrella tab should be visible on Related Order page"  
        
    def test_tc71_click_related_tab(self, related_order_page):
        """TC-71:
        1. Tap the Related tab.
        2. Tap the Related tab, verify related tab job cards are visible.
        3. if visible then click expend icon and log info if not visible then skip the test case.
        """
        # Step 1 — tap Related tab
        related_order_page.click_related_tab()
        related_order_page.wait_seconds(1)

        # Step 2 — verify related job cards are visible
        if not related_order_page.is_related_job_cards_visible():
            pytest.skip("No related job cards visible — skipping TC-71")

        # Step 3 — expand first card and log
        related_order_page.click_related_expand_icon()
        related_order_page.wait_seconds(1)
        logging.info("Expand icon tapped on first related job card")

    def test_tc72_click_umbrella_tab(self, related_order_page):
        """TC-72:
        1. Tap the Umbrella tab.
        2. Tap the Umbrella tab, verify umbrella job cards are visible.
        3. if visible then click expend icon and log info if not visible then skip the test case.
        """
        # Step 1 — tap Umbrella tab
        related_order_page.click_umbrella_tab()
        related_order_page.wait_seconds(1)

        # Step 2 — verify umbrella job cards are visible
        if not related_order_page.is_umbrella_job_cards_visible():
            pytest.skip("No umbrella job cards visible — skipping TC-72")

        # Step 3 — expand first card and log
        related_order_page.click_umbrella_expand_icon()
        related_order_page.wait_seconds(1)
        logging.info("Expand icon tapped on first umbrella job card")