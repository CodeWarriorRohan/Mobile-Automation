from appium.webdriver.common.appiumby import AppiumBy

DEFAULT_TIMEOUT = 10
LONG_TIMEOUT = 30
WEBVIEW_LOAD_TIMEOUT = 15
RETRY_COUNT = 3

# Locators for Login Page (used in login_page.py)
USERNAME_FIELD = (AppiumBy.CLASS_NAME, "android.widget.EditText")    
PASSWORD_FIELD = (AppiumBy.CLASS_NAME, "android.widget.EditText")
SIGN_IN_BUTTON = (AppiumBy.XPATH, '//*[@text="Sign in"]')
ERROR_MESSAGE = (AppiumBy.CLASS_NAME, "android.widget.TextView")

# ------------------------------------------------------------------ #
#  HEADER
#  CILIO_LOGO  : android.widget.ImageView — top-left, bounds [39,115][197,193]
#  PROFILE_ICON: com.horcrux.svg.SvgView  — top-right, bounds [978,123][1041,186]
# ------------------------------------------------------------------ #
CILIO_LOGO = (
    AppiumBy.XPATH,
    '//android.widget.FrameLayout[@resource-id="android:id/content"]'
    '/android.widget.FrameLayout'
    '/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup'
    '/android.view.ViewGroup/android.view.ViewGroup'
    '/android.view.ViewGroup[2]/android.view.ViewGroup[2]'
    '/android.widget.FrameLayout/android.view.ViewGroup'
    '/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup'
    '/android.view.ViewGroup/android.view.ViewGroup[1]'
    '/android.widget.FrameLayout/android.view.ViewGroup'
    '/android.view.ViewGroup/android.view.ViewGroup'
    '/android.view.ViewGroup[1]/android.widget.FrameLayout'
    '/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup'
    '/android.view.ViewGroup/android.view.ViewGroup'
    '/android.view.ViewGroup[1]/android.widget.ImageView'
)
    
BACK_ARROW = (AppiumBy.XPATH, '//android.widget.ImageView[@index="0"]/parent::android.view.ViewGroup[@clickable="true"]')
BACK_ARROW_X = 60
BACK_ARROW_Y = 133

PROFILE_ICON = (AppiumBy.XPATH, '(//com.horcrux.svg.SvgView)[last()]')
PROFILE_ICON_X         = 1009
PROFILE_ICON_Y         = 154

# ------------------------------------------------------------------ #
#  USER INFO CARD
# ------------------------------------------------------------------ #
USER_NAME_TEXT    = (AppiumBy.XPATH, '//*[@text="David Brass"]')
USER_ROLE_TEXT    = (AppiumBy.XPATH, '//*[@text="Cilio Fabrication Administrators Role"]')
VIEW_ALL_WORK_BTN = (AppiumBy.XPATH, '//*[@text="View All Work"]')
MY_BADGE_BTN      = (AppiumBy.XPATH, '//*[@text="My Badge"]')

# Locators for My Work Page (used in my_work_page.py)
MY_WORK_BTN = (AppiumBy.XPATH, '//*[@text="My Work"]')


# ------------------------------------------------------------------ #
#  BOTTOM NAVIGATION  (shared across all screens)
# ------------------------------------------------------------------ #
NAV_HOME     = (AppiumBy.XPATH, '//*[@content-desc="Home" or @text="Home"]')
NAV_SEARCH   = (AppiumBy.XPATH, '//*[@content-desc="Search" or @text="Search"]')
NAV_SCHEDULE = (AppiumBy.XPATH, '//*[@content-desc="Schedule" or @text="Schedule"]')
