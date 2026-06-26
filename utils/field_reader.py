"""
field_reader.py — Global utility for reading enabled input field hints from the UI.

Usage:
    from utils.field_reader import read_input_field_hints

    fields = read_input_field_hints(driver, locator)
    # Returns: ["Customer First Name", "City", "Phone Number", ...]

Works on any screen whose enabled inputs are EditText elements with a hint or text
attribute. Mirrors the multi-pass scroll + deduplication logic of card_reader.py.
"""
from appium.webdriver.common.appiumby import AppiumBy
import time


def read_input_field_hints(
    driver,
    locator: tuple,
    max_scrolls: int = 5,
) -> list:
    """
    Scroll through an input form and collect every enabled field's hint/text.

    Args:
        driver:      Appium WebDriver instance.
        locator:     (AppiumBy.*, selector) tuple that matches enabled EditText elements.
        max_scrolls: Maximum number of forward scroll steps (guard against infinite loops).

    Returns:
        List of field name strings, deduplicated, in first-seen order.
        e.g. ["Customer First Name", "City", "Phone Number"]
    """
    seen_names: set = set()
    names: list = []

    for _ in range(max_scrolls):
        elements = driver.find_elements(*locator)
        new_found = False

        for el in elements:
            try:
                name = el.get_attribute("hint") or el.get_attribute("text") or ""
                if name and name not in seen_names:
                    seen_names.add(name)
                    names.append(name)
                    new_found = True
            except Exception:
                pass  # skip stale elements caused by async re-render

        if not new_found:
            break  # no new fields in this pass — list is complete

        try:
            driver.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                "new UiScrollable(new UiSelector().scrollable(true)).scrollForward()",
            )
            time.sleep(1)
        except Exception:
            break  # nothing left to scroll

    # Scroll back to the top after all passes so the screen is reset
    try:
        driver.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            "new UiScrollable(new UiSelector().scrollable(true)).scrollToBeginning(10)",
        )
        time.sleep(1)
    except Exception:
        pass  # screen may not be scrollable — safe to ignore

    return names
