import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.pages.base_page import BasePage
from utils.constants import DEFAULT_TIMEOUT, WEBVIEW_LOAD_TIMEOUT


class WebViewPage(BasePage):
    NATIVE_CONTEXT = "NATIVE_APP"

    def get_contexts(self):
        return self.driver.contexts

    def switch_to_webview(self, timeout=WEBVIEW_LOAD_TIMEOUT):
        """Wait for a WEBVIEW_ context to appear, then switch into it."""
        end_time = time.time() + timeout
        while time.time() < end_time:
            contexts = self.driver.contexts
            webview = next((c for c in contexts if c.startswith("WEBVIEW_")), None)
            if webview:
                self.driver.switch_to.context(webview)
                return webview
            time.sleep(1)
        raise TimeoutError("WebView context did not appear within timeout")

    def switch_to_native(self):
        self.driver.switch_to.context(self.NATIVE_CONTEXT)

    def current_context(self):
        return self.driver.current_context

    def find_web_element(self, css_selector, timeout=DEFAULT_TIMEOUT):
        """Find an HTML element inside the active WebView using CSS selector."""
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, css_selector))
        )

    def click_web_element(self, css_selector):
        self.find_web_element(css_selector).click()

    def get_web_text(self, css_selector):
        return self.find_web_element(css_selector).text
