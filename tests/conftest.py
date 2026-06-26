import pytest
from src.pages.login_page import LoginPage
from src.pages.home_page import HomePage
from src.pages.profile_page import ProfilePage
from src.pages.view_all_work_page import ViewAllWorkPage
from src.pages.webview_page import WebViewPage
from src.pages.my_work_page import MyWorkPage
from src.pages.job_status_page import JobStatusPage
from src.pages.search_page import SearchPage
from src.pages.scheduler_page import SchedulerPage
from src.pages.JobDetails.job_base_page import JobBasePage
from src.pages.JobDetails.CustSiteTab.cust_info_page import CustomerPage
from src.pages.JobDetails.CustSiteTab.seller_info_page import SellerInfoPage
from src.pages.JobDetails.CustSiteTab.site_info_page import SiteInfoPage
from src.pages.JobDetails.CustSiteTab.related_orders_page import RelatedOrderPage
from src.pages.JobDetails.JobSchedTab.job_info_page import JobInfoPage
from src.pages.JobDetails.ActionsDocsTab.attachments_page import AttachmentsPage
from src.pages.JobDetails.ActionsDocsTab.notes_and_email_page import NotesAndEmailPage
from src.pages.JobDetails.ActionsDocsTab.q_and_a_page import QAndAPage
from src.pages.JobDetails.ActionsDocsTab.activities_page import ActivitiesPage

@pytest.fixture
def login_page(driver):
    return LoginPage(driver)


@pytest.fixture
def home_page(driver):
    return HomePage(driver)


@pytest.fixture
def webview_page(driver):
    return WebViewPage(driver)


@pytest.fixture
def my_work_page(driver):
    return MyWorkPage(driver)

@pytest.fixture
def profile_page(driver):
    return ProfilePage(driver)

@pytest.fixture
def view_all_work_page(driver):
    return ViewAllWorkPage(driver)

@pytest.fixture
def search_page(driver):
    return SearchPage(driver)   

@pytest.fixture
def scheduler_page(driver):
    return SchedulerPage(driver)

@pytest.fixture
def job_status_page(driver):
    return JobStatusPage(driver)   

@pytest.fixture
def job_details_page(driver):
    return JobBasePage(driver)

@pytest.fixture
def customer_page(driver):
    return CustomerPage(driver)

@pytest.fixture
def seller_info_page(driver):
    return SellerInfoPage(driver)

@pytest.fixture
def site_info_page(driver):
    return SiteInfoPage(driver)     

@pytest.fixture
def related_order_page(driver):
    return RelatedOrderPage(driver)

@pytest.fixture
def job_info_page(driver):
    return JobInfoPage(driver)

@pytest.fixture
def attachments_page(driver):
    return AttachmentsPage(driver)

@pytest.fixture
def notes_and_email_page(driver):
    return NotesAndEmailPage(driver)

@pytest.fixture
def q_and_a_page(driver):
    return QAndAPage(driver)

@pytest.fixture
def activities_page(driver):
    return ActivitiesPage(driver)