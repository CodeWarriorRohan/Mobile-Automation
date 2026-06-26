import pytest
from src.pages.home_page import HomePage


class TestHome:

    @pytest.mark.smoke
    def test_home_page_displays(self, driver):
        home_page = HomePage(driver)
        assert home_page.is_home_displayed()

    @pytest.mark.regression
    def test_welcome_text_present(self, driver):
        home_page = HomePage(driver)
        text = home_page.get_welcome_text()
        assert text is not None and len(text) > 0
