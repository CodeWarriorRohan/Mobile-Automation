"""
My Work Test Cases - Test suite for the My Work screen.

Scenario 1: All work cards have count = 0 (no jobs)
Scenario 2: At least one work card has count > 0 (jobs exist)

Tests that apply to BOTH scenarios: TC06 - TC10, TC15
Tests for Scenario 1 only (0 jobs):  TC11, TC12
Tests for Scenario 2 only (jobs exist): TC13, TC14, TC16 - TC24
"""
import sys
import os
import pytest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import logging
from appium.webdriver.common.appiumby import AppiumBy

class TestMyWork:

    # ================================================================== #
    #  COMMON UI — both scenarios (Scenario 1 + 2)
    # ================================================================== #

    def test_tc06_header_always_visible(self, my_work_page):
        """TC-06: Cilio logo and profile icon are always visible."""
        assert my_work_page.is_element_visible(my_work_page.CILIO_LOGO), \
            "Cilio logo should be visible"
        assert my_work_page.is_element_visible(my_work_page.PROFILE_ICON), \
            "Profile icon should be visible"

    def test_tc07_user_info_card_always_visible(self, my_work_page):
        """TC-07: User name, role, View All Work and My Badge always visible."""
        assert my_work_page.is_element_visible(my_work_page.USER_NAME_TEXT), \
            "User name should be visible"
        assert my_work_page.is_element_visible(my_work_page.USER_ROLE_TEXT), \
            "User role text should be visible"
        assert my_work_page.is_element_visible(my_work_page.VIEW_ALL_WORK_BTN), \
            "View All Work button should be visible"
        assert my_work_page.is_element_visible(my_work_page.MY_BADGE_BTN), \
            "My Badge button should be visible"

    def test_tc08_refresh_button_always_visible(self, my_work_page):
        """TC-08: Refresh button is always visible."""
        assert my_work_page.is_element_visible(my_work_page.REFRESH_BTN), \
            "Refresh button should be visible"

    def test_tc09_all_three_work_cards_visible(self, my_work_page):
        """TC-09: All three work cards are visible regardless of count value."""
        assert my_work_page.is_element_visible(my_work_page.TODAY_CARD), \
            "Today's Work card should be visible"
        assert my_work_page.is_element_visible(my_work_page.TOMORROW_CARD), \
            "Tomorrow's Work card should be visible"
        assert my_work_page.is_element_visible(my_work_page.YESTERDAY_CARD), \
            "Yesterday's Work card should be visible"

    def test_tc10_bottom_navigation_always_visible(self, my_work_page):
        """TC-10: All bottom navigation tabs are always visible."""
        assert my_work_page.is_element_visible(my_work_page.NAV_HOME), \
            "Home nav tab should be visible"
        assert my_work_page.is_element_visible(my_work_page.NAV_SEARCH), \
            "Search nav tab should be visible"
        assert my_work_page.is_element_visible(my_work_page.NAV_SCHEDULE), \
            "Schedule nav tab should be visible"

    # ================================================================== #
    #  SCENARIO 1 — All cards have count = 0 (NO JOBS)
    # ================================================================== #

    def test_tc11_no_job_sections_when_all_zero(self, my_work_page):
        """TC-11 [Scenario 1]: Job detail sections should NOT appear when all counts = 0."""
        if my_work_page.any_card_has_jobs():
            pytest.skip("Scenario 1 only: skipped because at least one card has jobs")

        assert not my_work_page.is_job_section_visible("Today's Work"), \
            "Today's Work section should not appear when count = 0"
        assert not my_work_page.is_job_section_visible("Tomorrow's Work"), \
            "Tomorrow's Work section should not appear when count = 0"
        assert not my_work_page.is_job_section_visible("Yesterday's Work"), \
            "Yesterday's Work section should not appear when count = 0"

    def test_tc12_no_route_button_when_all_zero(self, my_work_page):
        """TC-12 [Scenario 1]: Route button should NOT appear when all counts = 0."""
        if my_work_page.any_card_has_jobs():
            pytest.skip("Scenario 1 only: skipped because at least one card has jobs")

        assert not my_work_page.is_route_button_visible(), \
            "Route button should not appear when all work card counts are 0"

    # ================================================================== #
    #  SCENARIO 2 — At least one card has count > 0 (JOBS EXIST)
    # ================================================================== #

    def test_tc13_card_with_jobs_is_visible(self, my_work_page):
        """TC-13 [Scenario 2]: Work card with count > 0 shows correct count and is tappable."""
        if not my_work_page.any_card_has_jobs():
            pytest.skip("Scenario 2 only: skipped because no jobs exist")

        for name in my_work_page.cards_with_jobs():
            # Verify card is visible
            card = my_work_page.get_work_card(name)
            assert card.is_displayed(), f"{name} card should be visible"

            # Verify count > 0 is correctly read
            count = my_work_page.get_work_count(name)
            assert count > 0, f"{name} count should be > 0, got {count}"

        # Tap the first card that has jobs to open job details
        tapped = my_work_page.tap_card_with_jobs()
        assert tapped is not None, "Should be able to tap a card with jobs"

    def test_tc14_section_header_renders_only_for_cards_with_jobs(self, my_work_page):
        """TC-14 [Scenario 2]: Tap every card; section header appears only when count > 0."""
        if not my_work_page.any_card_has_jobs():
            pytest.skip("Scenario 2 only: skipped because no jobs exist")

        all_cards = ["Today's Work", "Tomorrow's Work", "Yesterday's Work"]
        tap_map = {
            "Today's Work":     my_work_page.tap_todays_work,
            "Tomorrow's Work":  my_work_page.tap_tomorrows_work,
            "Yesterday's Work": my_work_page.tap_yesterdays_work,
        }
        cards_with = set(my_work_page.cards_with_jobs())

        for name in all_cards:
            my_work_page.scroll_up()
            my_work_page.wait_seconds(1.5)
            tap_map[name]()
            my_work_page.wait_seconds(1.5)

            if name in cards_with:
                assert my_work_page.is_job_section_visible(name), \
                    f"Section '{name}' should be visible after tap (count > 0)"
            else:
                assert not my_work_page.is_job_section_visible(name), \
                    f"Section '{name}' should NOT appear after tap (count = 0)"
    
    def test_tc15_log_work_card_summary(self, my_work_page):
        """TC-15: Capture each day card's name and job count via global card-reader, log and assert."""
        logger = logging.getLogger(__name__)

        # Use the global card-reading utility via the page-object wrapper
        cards = my_work_page.get_work_cards_info()

        # ── Log to terminal and report ────────────────────────────────
        total = sum(int(c["count"]) for c in cards if c["count"].isdigit())
        logger.info(f"Total jobs across all cards: {total}")
        print(f"\nTotal jobs across all cards: {total}")
        for card in cards:
            logger.info(f"  Card: '{card['name']}' | Count: {card['count']}")
            print(f"  Card: '{card['name']}' | Count: {card['count']}")

        # ── Assertions ────────────────────────────────────────────────
        assert len(cards) > 0, "No work cards returned — get_work_cards_info() may have failed"

        for card in cards:
            # Scroll card name into view (off-screen cards on some devices)
            try:
                my_work_page.driver.find_element(
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    f'new UiScrollable(new UiSelector().scrollable(true))'
                    f'.scrollIntoView(new UiSelector().textContains("{card["name"]}"))'
                )
            except Exception:
                pass  # Card may already be visible

            work_card = my_work_page.get_work_card(card["name"])
            assert work_card.is_displayed(), f"'{card['name']}' card should be visible"
            logger.info(f"  ✓ '{card['name']}' is visible")
    
    def test_tc16_pickup_report_visible_when_jobs_exist(self, my_work_page):
        """TC-16 [Scenario 2]: Tapping a card reveals the Pickup Report button."""
        if not my_work_page.any_card_has_jobs():
            pytest.skip("Scenario 2 only: skipped because no jobs exist")

        my_work_page.tap_card_with_jobs()
        my_work_page.scroll_down()
        my_work_page.wait_seconds(1)

        assert my_work_page.is_element_present(my_work_page.PICKUP_REPORT_BTN), \
            "Pickup Report button should be visible after tapping card with jobs"

    def test_tc17_job_card_name_and_pay_visible(self, my_work_page):
        """TC-17 [Scenario 2]: Tapping a card shows job name and crew pay in the detail card."""
        if not my_work_page.any_card_has_jobs():
            pytest.skip("Scenario 2 only: skipped because no jobs exist")

        my_work_page.tap_card_with_jobs()
        my_work_page.scroll_down()
        my_work_page.wait_seconds(1)

        assert my_work_page.is_element_present(my_work_page.JOB_CARD_NAME), \
            "Job card name (e.g. 'Thomas, Wyatt') should be visible after tapping card"
        assert my_work_page.is_element_present(my_work_page.JOB_CREW_PAY), \
            "Job crew pay (e.g. '$6375.00') should be visible after tapping card"

    def test_tc18_expand_job_details_shows_all_fields(self, my_work_page):
        """TC-18 [Scenario 2]: For every work card (Today/Tomorrow/Yesterday) that has jobs,
        each Job Detail card is expanded, all labels asserted visible, and values logged.
        Empty values are allowed."""
        if not my_work_page.any_card_has_jobs():
            pytest.skip("Scenario 2 only: skipped because no jobs exist")

        logger = logging.getLogger(__name__)

        tap_map = {
            "Today's Work":     my_work_page.tap_todays_work,
            "Tomorrow's Work":  my_work_page.tap_tomorrows_work,
            "Yesterday's Work": my_work_page.tap_yesterdays_work,
        }

        expanded_label_texts = [
            "Name :",
            "Crew Pay :",
            "Labor Category :",
            "Customer City :",
            "Company :",
            "Start :",
            "End :",
            "Duration :",
            "Scope of work",
        ]

        for card_name in ["Today's Work", "Tomorrow's Work", "Yesterday's Work"]:
            job_count = my_work_page.get_work_count(card_name)
            if job_count == 0:
                logger.info(f"\n[SKIP] '{card_name}' — count = 0, no job details")
                print(f"\n[SKIP] '{card_name}' — count = 0, no job details")
                continue

            # Scroll to top, tap the work card to reveal its job detail cards
            my_work_page.scroll_up()
            my_work_page.wait_seconds(0.5)
            tap_map[card_name]()
            my_work_page.wait_seconds(0.5)
            my_work_page.scroll_down()
            my_work_page.wait_seconds(0.5)

            detail_count = my_work_page.get_job_section_card_count()
            assert detail_count > 0, \
                f"'{card_name}' has count={job_count} but no Job Detail cards were rendered"

            # ── Work card banner ──────────────────────────────────────
            logger.info(f"\n{'=' * 52}")
            logger.info(f"  Work Card : {card_name}  ({job_count} job(s))")
            logger.info(f"  Job Detail cards rendered : {detail_count}")
            logger.info(f"{'=' * 52}")
            print(f"\n{'=' * 52}")
            print(f"  Work Card : {card_name}  ({job_count} job(s))")
            print(f"  Job Detail cards rendered : {detail_count}")
            print(f"{'=' * 52}")

            # AFTER
            for i in range(1, detail_count + 1):
                logger.info(f"\n  ── Job Detail Card {i} of {detail_count} ──")
                print(f"\n  ── Job Detail Card {i} of {detail_count} ──")

                my_work_page.expand_job_details_by_index(i)

                for label in expanded_label_texts:
                    assert my_work_page.is_expanded_field_visible_for_card(i, label), \
                        f"'{card_name}' — Card {i}: label '{label}' should be visible"

                    value = my_work_page.get_expanded_field_value_for_card(i, label)
                    display_value = value if value else "(empty)"
                    logger.info(f"    {label:<20} {display_value}")
                    print(f"    {label:<20} {display_value}")

                my_work_page.expand_job_details_by_index(i)  # collapse before next card

    def test_tc19_scroll_down_reveals_job_detail_and_route_button(self, my_work_page):
        """TC-19 [Scenario 2]: Scrolling down shows job detail section and route button."""
        if not my_work_page.any_card_has_jobs():
            pytest.skip("Scenario 2 only: skipped because no jobs exist")

        # Tap a card to load job details into the DOM, then scroll down to reveal them
        my_work_page.tap_card_with_jobs()
        my_work_page.wait_seconds(1)

        my_work_page.scroll_down()
        my_work_page.wait_seconds(1)

        assert my_work_page.is_element_visible(my_work_page.JOB_CARD_NAME), \
            "Job detail card should be visible after scrolling down"

        # Dynamically finds whichever day's route button is rendered
        found = my_work_page.scroll_to_route_button()
        assert found is not None, \
            "Route button (Today's/Tomorrow's/Yesterday's Route) should be visible after scroll"

    def test_tc20_scroll_up_restores_header(self, my_work_page):
        """TC-20 [Scenario 2]: Scrolling back up brings header (Cilio logo) back into view."""
        my_work_page.scroll_up()
        my_work_page.wait_seconds(1)

        assert my_work_page.is_element_visible(my_work_page.CILIO_LOGO), \
            "Cilio logo should be visible after scrolling back to top"

    def test_tc21_tap_pickup_report_button(self, my_work_page):
        """TC-21 [Scenario 2]: Verify Pickup Report, Job Section Card and Route Button rendered, then tap Pickup Report."""
        if not my_work_page.any_card_has_jobs():
            pytest.skip("Scenario 2 only: skipped because no jobs exist")

        my_work_page.tap_card_with_jobs()
        my_work_page.scroll_down()
        my_work_page.wait_seconds(1)

        # Verify all three UI components are rendered before tapping
        assert my_work_page.is_element_visible(my_work_page.PICKUP_REPORT_BTN), \
            "Pickup Report button should be visible"
        assert my_work_page.is_element_visible(my_work_page.JOB_SECTION_CARD), \
            "Job section card (Name/Crew Pay) should be visible"
        assert my_work_page.is_element_present(my_work_page.ROUTE_BTN), \
            "Route button should be present in the DOM"

        my_work_page.tap_pickup_report()
        my_work_page.tap_nav_home()  # Navigate back to Home screen for test isolation
        my_work_page.wait_seconds(5)


    def test_tc22_tap_job_section_card(self, my_work_page):
        """TC-22 [Scenario 2]: Verify Job Section Card is rendered, then tap it."""
        if not my_work_page.any_card_has_jobs():
            pytest.skip("Scenario 2 only: skipped because no jobs exist")

        my_work_page.tap_card_with_jobs()
        my_work_page.scroll_down()
        my_work_page.wait_seconds(1)
        assert my_work_page.is_element_visible(my_work_page.JOB_SECTION_CARD), \
            "Job section card (Name/Crew Pay) should be visible"

        my_work_page.tap_job_section_card()
        my_work_page.wait_seconds(5)
        my_work_page.tap_back_arrow()  # Navigate back to previous screen for test isolation

    def test_tc23_tap_route_button(self, my_work_page):
        """TC-23 [Scenario 2]: Verify Route Button is rendered, then tap it."""
        if not my_work_page.any_card_has_jobs():
            pytest.skip("Scenario 2 only: skipped because no jobs exist")

        my_work_page.tap_card_with_jobs()
        my_work_page.wait_seconds(1)

        found = my_work_page.scroll_to_route_button()
        assert found is not None, \
            "Route button (Today's/Tomorrow's/Yesterday's Route) should be visible after scrolling"

        my_work_page.tap_route_button()
        my_work_page.wait_seconds(5)
        my_work_page.tap_back_arrow()  # Navigate back to previous screen for test isolation

    def test_tc24_tap_profile_icon_navigates_to_profile(self, my_work_page):
        """TC-24: All View All Work UI rendered — tap profile icon to navigate to Profile screen."""
        my_work_page.wait_seconds(1)
        my_work_page.tap_profile_icon()
        my_work_page.wait_seconds(3)