"""
card_reader.py — Global utility for reading card lists from the UI.

Usage:
    from utils.card_reader import read_cards_with_count

    cards = read_cards_with_count(driver, locator)
    # Returns: [{"name": "Assessment", "count": "7"}, ...]

Works on any screen whose cards are ViewGroups with content-desc formatted as
"Card Name, Count"  (e.g. "Today's Work, 2", "Assessment, 71", "Active, 5").
"""
import time
from appium.webdriver.common.appiumby import AppiumBy


def read_cards_with_count(
    driver,
    locator: tuple,
    scroll: bool = True,
    max_scrolls: int = 5,
) -> list:
    """
    Scroll through a card list and collect every card that has a name + count
    in its content-desc.

    Args:
        driver:      Appium WebDriver instance.
        locator:     (AppiumBy.*, selector) tuple that matches card ViewGroups.
        scroll:      If True, scroll forward after each pass to reveal off-screen cards.
        max_scrolls: Maximum number of scroll steps (guard against infinite loops).

    Returns:
        List of dicts: [{"name": str, "count": str}, ...]
        Duplicates (by name) are removed; order is insertion order (first seen).
    """
    seen_names: set = set()
    cards: list = []

    passes = max_scrolls if scroll else 1

    for _ in range(passes):
        elements = driver.find_elements(*locator)
        new_found = True  # Flag to track if new cards are found in this pass

        for el in elements:
            content_desc = (el.get_attribute("content-desc") or "").strip()
            parts = content_desc.split(", ", 1)
            if len(parts) == 2:
                name = parts[0].strip()
                # Normalize count: strip parentheses e.g. "(0)" → "0"
                count = parts[1].strip().strip("()")
                if name and name not in seen_names:
                    seen_names.add(name)
                    cards.append({"name": name, "count": count})
                    new_found = True
        if not scroll or not new_found:
            break  # No new cards after this pass — list is complete

        # Scroll forward one step to bring off-screen cards into view
        try:
            driver.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                "new UiScrollable(new UiSelector().scrollable(true)).scrollForward()",
            )
            time.sleep(1)
        except Exception:
            break  # Nothing left to scroll

    return cards
