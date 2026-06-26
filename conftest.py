import pytest
from dotenv import load_dotenv
from drivers.driver_factory import DriverFactory
from utils.screenshot_handler import save_screenshot_for_report

load_dotenv()


@pytest.fixture(scope="session")
def driver():
    drv = DriverFactory.get_driver()
    yield drv
    drv.quit()


@pytest.fixture(autouse=True)
def screenshot_on_failure(driver, request):
    yield
    if hasattr(request.node, "rep_call") and request.node.rep_call.failed:
        save_screenshot_for_report(driver, name=request.node.name)


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, f"rep_{rep.when}", rep)
