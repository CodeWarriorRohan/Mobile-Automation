import pytest
from src.pages.webview_page import WebViewPage


class TestHybridWebView:

    @pytest.mark.hybrid
    def test_switch_to_webview(self, driver):
        webview_page = WebViewPage(driver)

        contexts = webview_page.get_contexts()
        assert "NATIVE_APP" in contexts

        context = webview_page.switch_to_webview()
        assert "WEBVIEW_" in context

        webview_page.switch_to_native()
        assert webview_page.current_context() == "NATIVE_APP"

    @pytest.mark.hybrid
    def test_webview_current_context_is_native_by_default(self, driver):
        webview_page = WebViewPage(driver)
        assert webview_page.current_context() == "NATIVE_APP"
