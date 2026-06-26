from appium.webdriver.common.appiumby import AppiumBy
import logging
from src.pages.JobDetails.job_base_page import JobBasePage

class RelatedOrderPage(JobBasePage):
    # ================================================================== #
    #  LOCATORS
    # ================================================================== #

    RELATED_ORDER_TAB = (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="Related Order"]')

    RELATED_TAB = (AppiumBy.XPATH, '//android.widget.TextView[@text="Related"]')

    UMBRELLA_TAB = (AppiumBy.XPATH, '//android.widget.TextView[@text="Umbrella"]')

    # Job cards inside the Related tab 
    JOB_CARDS = (
        AppiumBy.XPATH,
        '//android.widget.ScrollView/android.view.ViewGroup'
        '/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup'
    )

    # Expand icon for the first related job card
    EXPAND_ICON = (
        AppiumBy.XPATH,
        '//android.widget.FrameLayout[@resource-id="android:id/content"]'
        '/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup'
        '/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup'
        '/android.view.ViewGroup[2]/android.view.ViewGroup[2]/android.widget.FrameLayout'
        '/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup'
        '/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]'
        '/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup'
        '/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout'
        '/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup'
        '/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView'
        '/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup'
        '/android.view.ViewGroup[1]/android.view.ViewGroup[2]/android.view.ViewGroup[1]'
    )

    # ================================================================== #
    #  VISIBILITY HELPERS
    # ================================================================== #

    def is_related_order_tab_visible(self) -> bool:
        """Check if the 'Related Order' tab is visible on the screen."""
        return self.is_element_visible(self.RELATED_ORDER_TAB)

    def is_related_tab_visible(self) -> bool:
        """Check if the 'Related' tab is visible on the screen."""
        return self.is_element_visible(self.RELATED_TAB)

    def is_umbrella_tab_visible(self) -> bool:
        """Check if the 'Umbrella' tab is visible on the screen."""
        return self.is_element_visible(self.UMBRELLA_TAB)

    def is_related_job_cards_visible(self) -> bool:
        """Check if any job cards are visible in the Related tab."""
        return self.is_element_visible(self.JOB_CARDS)

    def is_umbrella_job_cards_visible(self) -> bool:
        """Check if any job cards are visible in the Umbrella tab."""
        return self.is_element_visible(self.JOB_CARDS)

    # ================================================================== #
    #  ACTIONS
    # ================================================================== #

    def click_related_order_tab(self):
        """Tap the 'Related Order' tab to view related order details."""
        self.driver.find_element(*self.RELATED_ORDER_TAB).click()

    def click_related_tab(self):
        """Tap the 'Related' tab to view related job details."""
        self.driver.find_element(*self.RELATED_TAB).click()

    def click_umbrella_tab(self):
        """Tap the 'Umbrella' tab to view umbrella job details."""
        self.driver.find_element(*self.UMBRELLA_TAB).click()

    def click_related_expand_icon(self):
        """Tap the expand icon on the first related job card."""
        self.click(self.EXPAND_ICON)

    def click_umbrella_expand_icon(self):
        """Tap the expand icon on the first umbrella job card."""
        self.click(self.EXPAND_ICON)