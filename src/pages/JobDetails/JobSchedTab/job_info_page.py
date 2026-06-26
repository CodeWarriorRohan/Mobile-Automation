import random
from appium.webdriver.common.appiumby import AppiumBy
from src.pages.JobDetails.job_base_page import JobBasePage


class JobInfoPage(JobBasePage):

    # ------------------------------------------------------------------ #
    #  SECTION HEADER
    # ------------------------------------------------------------------ #
    
    JOB_SCHED_TAB = (
        AppiumBy.XPATH, '//android.widget.TextView[@text="Job/Sched"]'
    )

    JOB_INFO_TAB = (
        AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="Job information"]' 
    )

    SOW_TAB = (
        AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="SOW"]' 
    )

    DIV_TAB = (
        AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="DIV"]' 
    )

    CREW_PAY_TAB = (
        AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="Crew Pay"]' 
    )

    EXTENDED_TAB = (
        AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="Extended"]' 
    )

    JOB_INFO_1_TAB = (
        AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="Job information 1"]'
    )

    # # ------------------------------------------------------------------ #
    # #  JOB STATUS DROPDOWN — tuple-based locators (mirrors Country pattern)
    # # ------------------------------------------------------------------ #

    JOB_STATUS_PLACEHOLDER = "Job Status"

    JOB_STATUS_LABEL = (
        AppiumBy.XPATH, '//android.widget.TextView[@text="Job Status"]'
    )

    JOB_STATUS_PARENT_CONTAINER = (
    AppiumBy.XPATH, '//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[1]'
    )

    JOB_STATUS_DROPDOWN_OPTIONS = (
        AppiumBy.XPATH,
        '//android.view.ViewGroup[@clickable="true" and @content-desc and android.widget.TextView]'
    )

    JOB_STATUS_CLICKABLE_DESCENDANTS = (
        AppiumBy.XPATH,
        './/android.view.ViewGroup[@clickable="true" and @content-desc]'
    )

    # ------------------------------------------------------------------ #
    #  JOB TYPE DROPDOWN
    # ------------------------------------------------------------------ #

    JOB_TYPE_PLACEHOLDER = "Job Type"

    JOB_TYPE_LABEL = (
        AppiumBy.XPATH, '//android.widget.TextView[@text="Job Type"]'
    )

    JOB_TYPE_PARENT_CONTAINER = (
    AppiumBy.XPATH,
    '//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[7]'
)

    JOB_TYPE_DROPDOWN_OPTIONS = (
        AppiumBy.XPATH,
        '//android.view.ViewGroup[@clickable="true" and @content-desc and android.widget.TextView]'
    )

    JOB_TYPE_CLICKABLE_DESCENDANTS = (
        AppiumBy.XPATH,
        './/android.view.ViewGroup[@clickable="true" and @content-desc]'
    )

    # ------------------------------------------------------------------ #
    #  LABOR CATEGORY DROPDOWN
    # ------------------------------------------------------------------ #

    LABOR_CATEGORY_PLACEHOLDER = "Labor Category"

    LABOR_CATEGORY_LABEL = (
        AppiumBy.XPATH, '//android.widget.TextView[@text="Labor Category"]'
    )

    LABOR_CATEGORY_PARENT_CONTAINER = (
    AppiumBy.XPATH, '//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[4]'
)

    LABOR_CATEGORY_DROPDOWN_OPTIONS = (
        AppiumBy.XPATH,
        '//android.view.ViewGroup[@clickable="true" and @content-desc and android.widget.TextView]'
    )

    LABOR_CATEGORY_CLICKABLE_DESCENDANTS = (
        AppiumBy.XPATH,
        './/android.view.ViewGroup[@clickable="true" and @content-desc]'
    )

    # ================================================================== #
    #  EDIT FIELD INPUTS
    #  Anchored to each EditText's hint attribute — stable across scroll.
    # ================================================================== #

    JOB_NUMBER_INPUT = (
        AppiumBy.XPATH, '//android.widget.EditText[@hint="Job Number"]'
    )
    PROJECT_NUMBER_INPUT = (
        AppiumBy.XPATH, '//android.widget.EditText[@hint="Project Number"]'
    )
    PURCHASE_ORDER_NUMBER_INPUT = (
        AppiumBy.XPATH, '//android.widget.EditText[@hint="Purchase Order Number"]'
    )

    JOB_INFO_2_TAB = (
        AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="Job information 2"]'
    )
    

    JOB_INFO_3_TAB = (
        AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="Job information 3"]'
    )

    # ================================================================== #
    #  JOB INFO 2 — EDIT FIELD INPUTS
    #  Anchored to the label TextView's following-sibling EditText.
    # ================================================================== #

    INVOICE_NUMBER_INPUT = (
        AppiumBy.XPATH,
        '//android.widget.TextView[@text="Invoice Number"]/following-sibling::android.widget.EditText'
    )
    PURCHASE_ORDER_AMOUNT_INPUT = (
        AppiumBy.XPATH,
        '//android.widget.TextView[@text="Purchase Order Amount"]/following-sibling::android.widget.EditText'
    )
    BUDGETED_YEAR_INPUT = (
        AppiumBy.XPATH,
        '//android.widget.TextView[@text="Budgeted Year"]/following-sibling::android.widget.EditText'
    )
    BUDGETED_AMOUNT_INPUT = (
        AppiumBy.XPATH,
        '//android.widget.TextView[@text="Budgeted Amount"]/following-sibling::android.widget.EditText'
    )
    INVOICE_COMMENT_INPUT = (
        AppiumBy.XPATH,
        '//android.widget.TextView[@text="Invoice Comment"]/following-sibling::android.widget.EditText'
    )
    YEAR_BUILT_INPUT = (
        AppiumBy.XPATH,
        '//android.widget.TextView[@text="Year Built"]/following-sibling::android.widget.EditText'
    )
    COD_INPUT = (
        AppiumBy.XPATH,
        '//android.widget.TextView[@text="COD"]/following-sibling::android.widget.EditText'
    )
    PAYMENT_TERMS_INPUT = (
        AppiumBy.XPATH,
        '//android.widget.TextView[@text="Payment Terms"]/following-sibling::android.widget.EditText'
    )
    PERMIT_NUMBER_INPUT = (
        AppiumBy.XPATH,
        '//android.widget.TextView[@text="Permit Number"]/following-sibling::android.widget.EditText'
    )
    SALES_ORDER_NUMBER_INPUT = (
        AppiumBy.XPATH,
        '//android.widget.TextView[@text="Sales Order Number"]/following-sibling::android.widget.EditText'
    )

    # ================================================================== #
    #  JOB INFO 3 — EDIT FIELD INPUTS
    # ================================================================== #

    PRODUCT_AMOUNT_INPUT = (
        AppiumBy.XPATH,
        '(//android.widget.TextView[@text="Product Amount"]/parent::android.view.ViewGroup//android.widget.EditText)[1]'
    )
    LABOR_AMOUNT_INPUT = (
        AppiumBy.XPATH,
        '(//android.widget.TextView[@text="Labor Amount"]/parent::android.view.ViewGroup//android.widget.EditText)[1]'
    )
    SALES_TAX_INPUT = (
        AppiumBy.XPATH,
        '(//android.widget.TextView[@text="Sales Tax"]/parent::android.view.ViewGroup//android.widget.EditText)[1]'
    )
    LOWS_CHECK_NUMBER_INPUT = (
        AppiumBy.XPATH,
        '(//android.widget.TextView[@text="Lows Check Number"]/parent::android.view.ViewGroup//android.widget.EditText)[1]'
    )
    LOWS_PR_NUMBER_INPUT = (
        AppiumBy.XPATH,
        '(//android.widget.TextView[@text="Lows PR Number"]/parent::android.view.ViewGroup//android.widget.EditText)[1]'
    )
    LOWS_PAYMENT_AMOUNT_INPUT = (
        AppiumBy.XPATH,
        '(//android.widget.TextView[@text="Lows Payment Amount"]/parent::android.view.ViewGroup//android.widget.EditText)[1]'
    )
    LOWS_PAYMENT_TYPE_INPUT = (
        AppiumBy.XPATH,
        '(//android.widget.TextView[@text="Lows Payment Type"]/parent::android.view.ViewGroup//android.widget.EditText)[1]'
    )
    ADDITIONAL_LABOR_AMOUNT_INPUT = (
        AppiumBy.XPATH,
        '(//android.widget.TextView[@text="Additional Labor Amount"]/parent::android.view.ViewGroup//android.widget.EditText)[1]'
    )



    # ================================================================== #
    #  VISIBILITY HELPERS
    # ================================================================== #

    def is_job_info_tab_visible(self):
        return self.is_element_visible(self.JOB_INFO_TAB)   
    
    def is_job_info_1_tab_visible(self):
        return self.is_element_visible(self.JOB_INFO_1_TAB)
    
    def is_job_info_2_tab_visible(self):
        return self.is_element_visible(self.JOB_INFO_2_TAB)
    
    def is_job_info_3_tab_visible(self):
        return self.is_element_visible(self.JOB_INFO_3_TAB)
    

    # ================================================================== #
    #  ACTIONS
    # ================================================================== #
    
    def click_job_sched_tab(self):
        self.click(self.JOB_SCHED_TAB)                
    
    def click_job_info_tab(self):
        self.click(self.JOB_INFO_TAB)

    def click_sow_tab(self):
        self.click(self.SOW_TAB)

    def click_div_tab(self):
        self.click(self.DIV_TAB) 

    def click_crew_pay_tab(self):
        self.click(self.CREW_PAY_TAB)

    def click_extended_tab(self):
        self.click(self.EXTENDED_TAB)               

    def click_job_info_1_tab(self):
        self.click(self.JOB_INFO_1_TAB)

    def click_job_info_2_tab(self):
        self.click(self.JOB_INFO_2_TAB)

    def click_job_info_3_tab(self):
        self.click(self.JOB_INFO_3_TAB)   


    # ================================================================== #
    #  GENERIC DROPDOWN OPTION LOCATOR
    # ================================================================== #

    @staticmethod
    def _dropdown_option_locator(option_text: str) -> tuple:
        """Locator for any open-state dropdown option by content-desc."""
        return (
            AppiumBy.XPATH,
            f'//android.view.ViewGroup[@clickable="true" and @content-desc="{option_text}"]',
        )

    @staticmethod
    def _dropdown_trigger_locator(label_text: str) -> tuple:
        """Navigate from the label UP one level to its parent row, then DOWN
        to the clickable trigger in that row only.
        Avoids ancestor:: which escapes the row boundary when multiple
        dropdowns share the same form section.
        """
        return (
            AppiumBy.XPATH,
            f'(//android.widget.ScrollView//android.widget.TextView[@text="{label_text}"]'
            f'/following-sibling::android.view.ViewGroup[@clickable="true" and @content-desc])[1]',
        )

    # ================================================================== #
    #  JOB STATUS DROPDOWN
    # ================================================================== #

    def _scroll_job_status_into_view(self):
        try:
            self.scroll_content_to_text(self.JOB_STATUS_PLACEHOLDER)
        except Exception:
            pass

    def _get_job_status_option_values(self) -> list:
        values, seen = [], set()
        for el in self.find_elements(self.JOB_STATUS_DROPDOWN_OPTIONS):
            v = (el.get_attribute("content-desc") or "").strip()
            if v and v not in seen:
                seen.add(v)
                values.append(v)
        return values

    def get_job_status_parent_container(self):
        self._scroll_job_status_into_view()
        return self.wait_for_element(self.JOB_STATUS_PARENT_CONTAINER)

    def get_job_status_clickable_descendants(self) -> list:
        return self.get_job_status_parent_container().find_elements(
            *self.JOB_STATUS_CLICKABLE_DESCENDANTS
        )

    def get_job_status_clickable_container(self):
        descendants = self.get_job_status_clickable_descendants()
        if len(descendants) == 1:
            return descendants[0]
        if not descendants:
            raise AssertionError("No clickable descendants found inside the Job Status parent row")
        return max(descendants, key=lambda el: el.rect.get("width", 0))

    def get_job_status_value(self) -> str:
        self._scroll_job_status_into_view()
        return (
            self.wait_for_element(self._dropdown_trigger_locator(self.JOB_STATUS_PLACEHOLDER))
                .get_attribute("content-desc") or ""
        ).strip()

    def tap_job_status_dropdown(self):
        self._scroll_job_status_into_view()
        el = self.wait_for_element(self._dropdown_trigger_locator(self.JOB_STATUS_PLACEHOLDER))
        try:
            el.click()
        except Exception:
            rect = el.rect
            self.driver.execute_script("mobile: clickGesture", {
                "x": int(rect["x"] + rect["width"] / 2),
                "y": int(rect["y"] + rect["height"] / 2),
            })

    def select_random_job_status(self) -> str:
        current_value = self.get_job_status_value()
        self.tap_job_status_dropdown()
        self.wait_seconds(1)
        candidates = [v for v in self._get_job_status_option_values() if v != current_value]
        if not candidates:
            raise ValueError(
                f"No alternative Job Status options found "
                f"(current: {current_value!r}, seen: {self._get_job_status_option_values()})"
            )
        chosen = random.choice(candidates)
        self.click(self._dropdown_option_locator(chosen))
        return chosen

    # ================================================================== #
    #  JOB TYPE DROPDOWN
    # ================================================================== #

    def _scroll_job_type_into_view(self):
        try:
            self.scroll_content_to_text(self.JOB_TYPE_PLACEHOLDER)
        except Exception:
            pass

    def _get_job_type_option_values(self) -> list:
        values, seen = [], set()
        for el in self.find_elements(self.JOB_TYPE_DROPDOWN_OPTIONS):
            v = (el.get_attribute("content-desc") or "").strip()
            if v and v not in seen:
                seen.add(v)
                values.append(v)
        return values

    def get_job_type_parent_container(self):
        self._scroll_job_type_into_view()
        return self.wait_for_element(self.JOB_TYPE_PARENT_CONTAINER)

    def get_job_type_clickable_descendants(self) -> list:
        return self.get_job_type_parent_container().find_elements(
            *self.JOB_TYPE_CLICKABLE_DESCENDANTS
        )

    def get_job_type_clickable_container(self):
        descendants = self.get_job_type_clickable_descendants()
        if len(descendants) == 1:
            return descendants[0]
        if not descendants:
             raise AssertionError("No clickable descendants found inside the Job Type parent row")
        return max(descendants, key=lambda el: el.rect.get("width", 0))

    def get_job_type_value(self) -> str:
        self._scroll_job_type_into_view()
        return (
            self.wait_for_element(self._dropdown_trigger_locator(self.JOB_TYPE_PLACEHOLDER))
                .get_attribute("content-desc") or ""
        ).strip()

    def tap_job_type_dropdown(self):
        self._scroll_job_type_into_view()
        el = self.wait_for_element(self._dropdown_trigger_locator(self.JOB_TYPE_PLACEHOLDER))
        try:
            el.click()
        except Exception:
            rect = el.rect
            self.driver.execute_script("mobile: clickGesture", {
                "x": int(rect["x"] + rect["width"] / 2),
                "y": int(rect["y"] + rect["height"] / 2),
            })

    def select_random_job_type(self) -> str:
        current_value = self.get_job_type_value()
        self.tap_job_type_dropdown()
        self.wait_seconds(1)
        candidates = [v for v in self._get_job_type_option_values() if v != current_value]
        if not candidates:
            raise ValueError(
                f"No alternative Job Type options found "
                f"(current: {current_value!r}, seen: {self._get_job_type_option_values()})"
            )
        chosen = random.choice(candidates)
        self.click(self._dropdown_option_locator(chosen))
        return chosen
    
     # ================================================================== #
    #  LABOR CATEGORY DROPDOWN
    # ================================================================== #

    def _scroll_labor_category_into_view(self):
        try:
            self.scroll_content_to_text(self.LABOR_CATEGORY_PLACEHOLDER)
        except Exception:
            pass

    def _get_labor_category_option_values(self) -> list:
        values, seen = [], set()
        for el in self.find_elements(self.LABOR_CATEGORY_DROPDOWN_OPTIONS):
            v = (el.get_attribute("content-desc") or "").strip()
            if v and v not in seen:
                seen.add(v)
                values.append(v)
        return values

    def get_labor_category_parent_container(self):
        self._scroll_labor_category_into_view()
        return self.wait_for_element(self.LABOR_CATEGORY_PARENT_CONTAINER)

    def get_labor_category_clickable_descendants(self) -> list:
        return self.get_labor_category_parent_container().find_elements(
            *self.LABOR_CATEGORY_CLICKABLE_DESCENDANTS
        )
    
    def get_labor_category_clickable_container(self):
        descendants = self.get_labor_category_clickable_descendants()
        if len(descendants) == 1:
            return descendants[0]
        if not descendants:
            raise AssertionError("No clickable descendants found inside the Labor Category parent row")
        return max(descendants, key=lambda el: el.rect.get("width", 0))

    def get_labor_category_value(self) -> str:
        self._scroll_labor_category_into_view()
        return (
            self.wait_for_element(self._dropdown_trigger_locator(self.LABOR_CATEGORY_PLACEHOLDER))
                .get_attribute("content-desc") or ""
        ).strip()

    def tap_labor_category_dropdown(self):
        self._scroll_labor_category_into_view()
        el = self.wait_for_element(self._dropdown_trigger_locator(self.LABOR_CATEGORY_PLACEHOLDER))
        try:
            el.click()
        except Exception:
            rect = el.rect
            self.driver.execute_script("mobile: clickGesture", {
                "x": int(rect["x"] + rect["width"] / 2),
                "y": int(rect["y"] + rect["height"] / 2),
            })

    def select_random_labor_category(self) -> str:
        current_value = self.get_labor_category_value()
        self.tap_labor_category_dropdown()
        self.wait_seconds(1)
        candidates = [v for v in self._get_labor_category_option_values() if v != current_value]
        if not candidates:
            raise ValueError(
                f"No alternative Labor Category options found "
                f"(current: {current_value!r}, seen: {self._get_labor_category_option_values()})"
            )
        
        chosen = random.choice(candidates)
        self.click(self._dropdown_option_locator(chosen))
        return chosen
    

    def fill_job_info1_fields(self, data: dict):
        """Clear and fill each EditText field present in *data*.

        Scrolls into view before typing so off-screen fields are reached.
        """
        _field_map = {
            "Job Number":              self.JOB_NUMBER_INPUT,
            "Project Number":          self.PROJECT_NUMBER_INPUT,
            "Purchase Order Number":   self.PURCHASE_ORDER_NUMBER_INPUT,
        }

        for field_name, value in data.items():
            locator = _field_map.get(field_name)
            if locator is None:
                continue
            try:
                self.scroll_content_to_text(field_name)
            except Exception:
                pass
            self.send_keys(locator, value)
            try:
                self.driver.hide_keyboard()
            except Exception:
                pass

    def fill_job_info2_fields(self, data: dict):
        """Clear and fill each Job Info 2 EditText field present in *data*.

        Scrolls to the field label first, then interacts via presence-based
        wait (not clickable) to avoid TimeoutException for off-screen rows.
        """
        _field_map = {
            "Invoice Number":        self.INVOICE_NUMBER_INPUT,
            "Purchase Order Amount": self.PURCHASE_ORDER_AMOUNT_INPUT,
            "Budgeted Year":         self.BUDGETED_YEAR_INPUT,
            "Budgeted Amount":       self.BUDGETED_AMOUNT_INPUT,
            "Invoice Comment":       self.INVOICE_COMMENT_INPUT,
            "Year Built":            self.YEAR_BUILT_INPUT,
            "COD":                   self.COD_INPUT,
            "Payment Terms":         self.PAYMENT_TERMS_INPUT,
            "Permit Number":         self.PERMIT_NUMBER_INPUT,
            "Sales Order Number":    self.SALES_ORDER_NUMBER_INPUT,
        }

        for field_name, value in data.items():
            locator = _field_map.get(field_name)
            if locator is None:
                continue
            try:
                self.scroll_content_to_text(field_name)
            except Exception:
                pass
            element = self.wait_for_element(locator, timeout=4)
            element.clear()
            element.send_keys(str(value))
            try:
                self.driver.hide_keyboard()
            except Exception:
                pass

    def fill_job_info3_fields(self, data: dict):
        """Clear and fill each Job Info 3 EditText field present in *data*.

        Scrolls to the field label first, then interacts via presence-based
        wait (not clickable) to avoid TimeoutException for off-screen rows.
        """
        _field_map = {
            "Product Amount":        self.PRODUCT_AMOUNT_INPUT,
            "Labor Amount":          self.LABOR_AMOUNT_INPUT,
            "Sales Tax":             self.SALES_TAX_INPUT,
            "Lows Check Number":     self.LOWS_CHECK_NUMBER_INPUT,
            "Lows PR Number":        self.LOWS_PR_NUMBER_INPUT,
            "Lows Payment Amount":   self.LOWS_PAYMENT_AMOUNT_INPUT,
            "Lows Payment Type":     self.LOWS_PAYMENT_TYPE_INPUT,
            "Additional Labor Amount": self.ADDITIONAL_LABOR_AMOUNT_INPUT,
        }

        for field_name, value in data.items():
            locator = _field_map.get(field_name)
            if locator is None:
                continue
            try:
                self.scroll_content_to_text(field_name)
            except Exception:
                pass
            element = self.wait_for_element(locator, timeout=4)
            element.clear()
            element.send_keys(str(value))
            try:
                self.driver.hide_keyboard()
            except Exception:
                pass
