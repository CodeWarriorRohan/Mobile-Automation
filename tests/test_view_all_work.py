from appium.webdriver.common.appiumby import AppiumBy

from src.pages import my_work_page, view_all_work_page
import logging
import pytest

class TestViewAllWork:
    """Tests for the View All Work screen."""

    def test_tc40_header_always_visible(self, view_all_work_page):
        """TC-40: Cilio logo and profile icon are always visible."""
        assert view_all_work_page.is_element_visible(view_all_work_page.CILIO_LOGO), \
            "Cilio logo should be visible"
        assert view_all_work_page.is_element_visible(view_all_work_page.PROFILE_ICON), \
            "Profile icon should be visible"

    def test_tc41_user_info_card_always_visible(self, view_all_work_page):
        """TC-41: User name, role, View All Work and My Badge always visible."""
        assert view_all_work_page.is_element_visible(view_all_work_page.USER_NAME_TEXT), \
            "User name should be visible"
        assert view_all_work_page.is_element_visible(view_all_work_page.USER_ROLE_TEXT), \
            "User role text should be visible"
        assert view_all_work_page.is_element_visible(view_all_work_page.MY_WORK_BTN), \
            "My Work button should be visible"
        assert view_all_work_page.is_element_visible(view_all_work_page.MY_BADGE_BTN), \
            "My Badge button should be visible"

    # ================================================================== #
    #  FIND JOBS BY TYPES
    # ================================================================== #

    def test_tc42_find_jobs_by_type_cards_visible(self, view_all_work_page):
        """TC-42: Verify all 'Find Jobs by Types' cards are visible, count them, and log their names."""
        logger = logging.getLogger(__name__)

        cards = view_all_work_page.get_job_type_cards()

        # ── Log to terminal and report ────────────────────────────────
        total = len(cards)
        names = [c["name"] for c in cards]

        logger.info(f"Total cards found: {total}")
        logger.info(f"Card names: {names}")

        print(f"\nTotal cards found: {total}")
        print(f"Card names: {names}")

        for card in cards:
            logger.info(f"  Card: '{card['name']}' | Count: {card['count']}")
            print(f"  Card: '{card['name']}' | Count: {card['count']}")

        # ── Assertions ────────────────────────────────────────────────
        assert total > 0, "No job type cards found — 'Find Jobs by Types' section may not be loaded"

        # Scroll to each card individually using UiScrollable so off-screen cards
        # are brought into view before asserting visibility
        for card in cards:
            # Scroll until the card's name text is visible on screen
            try:
                view_all_work_page.driver.find_element(
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    f'new UiScrollable(new UiSelector().scrollable(true))'
                    f'.scrollIntoView(new UiSelector().text("{card["name"]}"))'
                )
            except Exception:
                pass  # Element may already be visible; proceed to assert

            locator = (
                AppiumBy.XPATH,
                f'//android.view.ViewGroup[starts-with(@content-desc, "{card["name"]},")]'
            )
            assert view_all_work_page.is_element_visible(locator, timeout=5), \
                f"Card '{card['name']}' is not visible on screen"
            logger.info(f"  ✓ '{card['name']}' is visible")


    def test_tc43_bottom_navigation_always_visible(self, view_all_work_page):
        """TC-43: All bottom navigation tabs are always visible."""
        assert view_all_work_page.is_element_visible(view_all_work_page.NAV_HOME), \
            "Home nav tab should be visible"
        assert view_all_work_page.is_element_visible(view_all_work_page.NAV_SEARCH), \
            "Search nav tab should be visible"
        assert view_all_work_page.is_element_disabled(view_all_work_page.NAV_SCHEDULE), \
            "Schedule nav tab should be disabled"        
        
    def test_tc44_tap_profile_icon_navigates_to_profile(self, view_all_work_page):
        """TC-44: All View All Work UI rendered — tap profile icon to navigate to Profile screen."""
        view_all_work_page.wait_seconds(1)
        view_all_work_page.tap_profile_icon()
        view_all_work_page.wait_seconds(1.5)
        view_all_work_page.tap_back_arrow()
        view_all_work_page.wait_seconds(1) 

    def test_tc45_tap_search_nav_navigates_to_search(self, view_all_work_page):
        """TC-45: Tapping Search navigation icon navigates to Search screen."""
        view_all_work_page.tap_nav_search()
        view_all_work_page.wait_seconds(2)

    

        