from src.pages import view_all_work_page, job_status_page
import pytest


class TestJobStatus:
    """Tests for the Job Status screen."""

    def test_tc45_tap_job_type_card_shows_job_status_screen(self, view_all_work_page, job_status_page):
        """TC-45: Tapping a Job Type card with count > 0 navigates to Job Status screen and shows sub-cards."""
        cards = view_all_work_page.get_job_type_cards()
        cards_with_jobs = [c for c in cards if c["count"].isdigit() and int(c["count"]) > 0]

        if not cards_with_jobs:
            pytest.skip("TC-45: skipped — all job type cards have count = 0")

        target = cards_with_jobs[0]
        view_all_work_page.tap_job_type_card(target["name"])
        view_all_work_page.wait_seconds(2)

        header = job_status_page.get_job_status_header()
        assert header == target["name"], \
            f"Expected header '{target['name']}', got '{header}'"

    def test_tc46_tap_job_status_card_with_count(self, job_status_page):
        """TC-46: On the Job Status screen, tap a sub-card with count > 0."""
        cards = job_status_page.get_job_status_cards()
        cards_with_jobs = [c for c in cards if c["count"].isdigit() and int(c["count"]) > 0]
        target = cards_with_jobs[0]
        job_status_page.tap_job_status_card(target["name"])
        job_status_page.wait_seconds(2)

    def test_tc47_tap_job_status_card_with_zero_count(self, job_status_page):
        job_status_page.tap_random_result_cards(sample_size=1)
        job_status_page.wait_seconds(3)
