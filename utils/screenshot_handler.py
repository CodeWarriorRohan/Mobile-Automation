import os
from datetime import datetime
from utils.logger import get_logger

logger = get_logger(__name__)
SCREENSHOT_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "Screenshots")


def save_screenshot_for_report(driver, name: str = None, directory: str = None) -> str:
    """Save a PNG screenshot to disk on test failure. Returns the saved path."""
    target_dir = directory or SCREENSHOT_DIR
    os.makedirs(target_dir, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    safe_name = (name or "screenshot").replace(" ", "_").replace("::", "__")
    filename = f"FAILED_{safe_name}_{timestamp}.png"
    path = os.path.join(target_dir, filename)
    try:
        driver.save_screenshot(path)
        logger.info(f"Screenshot saved: {path}")
    except Exception as e:
        logger.warning(f"Failed to capture screenshot: {e}")
    return path


def save_screenshot(driver, name: str = None, directory: str = None) -> str:
    """Save a named screenshot to disk on demand. Returns the saved path."""
    return save_screenshot_for_report(driver, name=name, directory=directory)
