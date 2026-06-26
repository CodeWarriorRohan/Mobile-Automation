from appium.webdriver.common.appiumby import AppiumBy

class TestJobInfo:

    def test_tc73_click_job_info_tab_verify_fields_visible(self, job_info_page):
        """TC-73:
        1. Click Job Info tab.
        2. Verify Job Info1, Job Info2, and Job Info3 are visible.
        """
        # Step 1 — click Job sched tab to ensure we're on the right tab
        job_info_page.click_job_sched_tab() 

        # Step 2 — click Job Info tab
        job_info_page.click_job_info_tab()
        job_info_page.wait_seconds(2)

    def test_tc74_click_job_info_1_tab(self, job_info_page):
        """TC-74:
        1. Click Job Information 1 sub-tab.
        2. Select a random Job Status from the dropdown.
        3. Select a random Labor Category from the dropdown.
        4. Select a random Job Type from the dropdown.
        """
        # Step 1 — click Job Information 1 sub-tab
        job_info_page.click_job_info_1_tab()
        job_info_page.wait_seconds(1)

        # Step 2 — Job Status dropdown
        job_info_page._scroll_job_status_into_view()
        job_info_page.wait_seconds(1)
        chosen_status = job_info_page.select_random_job_status()
        job_info_page.wait_seconds(1)

        assert chosen_status, "A Job Status option should have been selected"
        assert job_info_page.get_job_status_value() == chosen_status, \
            f"Job Status should now show '{chosen_status}'"

        # Step 3 — Labor Category dropdown
        job_info_page._scroll_labor_category_into_view()
        job_info_page.wait_seconds(1)
        chosen_labor = job_info_page.select_random_labor_category()
        job_info_page.wait_seconds(1)

        assert chosen_labor, "A Labor Category option should have been selected"
        assert job_info_page.get_labor_category_value() == chosen_labor, \
            f"Labor Category should now show '{chosen_labor}'"

        # Step 4 — Job Type dropdown
        job_info_page._scroll_job_type_into_view()
        job_info_page.wait_seconds(1)
        chosen_type = job_info_page.select_random_job_type()
        job_info_page.wait_seconds(1)

        assert chosen_type, "A Job Type option should have been selected"
        assert job_info_page.get_job_type_value() == chosen_type, \
            f"Job Type should now show '{chosen_type}'"

    def test_tc75_edit_job_info_1_fields(self, job_info_page):
        """TC-75: Navigate to Job Information 1, clear and fill text fields, verify values."""
        
        new_data = {
            "Job Number":            "3948594",
            "Project Number":        "9874657",
            "Purchase Order Number": "555-0100",
        }

        # Step 1 — clear and fill each field
        job_info_page.fill_job_info1_fields(new_data)
        job_info_page.wait_seconds(1)
        # Step 3 — verify each field shows the new value
        for field_hint, expected_value in new_data.items():
            try:
                job_info_page.scroll_content_to_text(field_hint)
            except Exception:
                pass
            locator = (AppiumBy.XPATH, f'//android.widget.EditText[@hint="{field_hint}"]')
            actual = job_info_page.wait_for_element(locator).text
            assert actual == expected_value, \
                f"{field_hint}: expected '{expected_value}', got '{actual}'"

    def test_tc76_click_job_info_2_tab_and_edit_fields(self, job_info_page):
        """TC-76: Navigate to Job Information 2, clear and fill text fields, verify values."""

        # Step 1 — scroll content back to top so the sub-tab bar is visible,
        # then navigate to Job Info 2 sub-tab
        job_info_page.click_job_info_2_tab()
        job_info_page.wait_seconds(2)

        new_data = {
            "Invoice Number":        "INV-1001",
            "Purchase Order Amount": "2500.00",
            "Budgeted Year":         "2026",
            "Budgeted Amount":       "15000.00",
            "Invoice Comment":       "Test invoice comment",
            "Year Built":            "1998",
            "COD":                   "COD-001",
            "Payment Terms":         "Net 30",
            "Permit Number":         "PRM-5678",
            "Sales Order Number":    "SO-9900",
        }

        # Step 2 — clear and fill each field
        job_info_page.fill_job_info2_fields(new_data)
        job_info_page.wait_seconds(1)

        # Step 3 — verify each field shows the new value
        for field_label, expected_value in new_data.items():
            try:
                job_info_page.scroll_content_to_text(field_label)
            except Exception:
                pass
            locator = (
                AppiumBy.XPATH,
                f'//android.widget.TextView[@text="{field_label}"]'
                f'/following-sibling::android.widget.EditText'
            )
            actual = job_info_page.wait_for_element(locator).text
            assert actual == expected_value, \
                f"{field_label}: expected '{expected_value}', got '{actual}'"


    def test_tc77_click_job_info_3_tab_and_edit_fields(self, job_info_page):
        """TC-77: Navigate to Job Information 3, clear and fill text fields, verify values."""

        # Step 1 — scroll content back to top so the sub-tab bar is visible,
        # then navigate to Job Info 3 sub-tab
        job_info_page.click_job_info_3_tab()
        job_info_page.wait_seconds(2)

        new_data = {
            "Product Amount":          "1200.00",
            "Labor Amount":            "800.00",
            "Sales Tax":               "150.00",
            "Lows Check Number":       "CHK-4321",
            "Lows PR Number":          "PR-7890",
            "Lows Payment Amount":     "500.00",
            "Lows Payment Type":       "Credit",
            "Additional Labor Amount": "250.00",
        }

        # Step 2 — clear and fill each field
        job_info_page.fill_job_info3_fields(new_data)
        job_info_page.wait_seconds(1)

        # Step 3 — verify each field shows the new value
        for field_label, expected_value in new_data.items():
            try:
                job_info_page.scroll_content_to_text(field_label)
            except Exception:
                pass
            locator = (
                AppiumBy.XPATH,
                f'(//android.widget.TextView[@text="{field_label}"]'
                f'/parent::android.view.ViewGroup//android.widget.EditText)[1]'
            )
            actual = job_info_page.wait_for_element(locator).text
            assert actual == expected_value, \
                f"{field_label}: expected '{expected_value}', got '{actual}'"


    def test_tc78_click_on_tabs_of_job_sched_section(self, job_info_page):
        """TC-78: Click on each tab of Job Sched section and verify content changes."""
        
        # Click SOW tab
        job_info_page.click_sow_tab()
        job_info_page.wait_seconds(1)

        # Click DIV tab
        job_info_page.click_div_tab()
        job_info_page.wait_seconds(1)

        # Click CREW PAY tab
        job_info_page.click_crew_pay_tab()
        job_info_page.wait_seconds(1)

        # Click Extended tab
        job_info_page.click_extended_tab()  
        job_info_page.wait_seconds(1)      