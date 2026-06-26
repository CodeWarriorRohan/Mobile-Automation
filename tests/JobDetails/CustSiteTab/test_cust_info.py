"""
Customer Contact Info Test Cases
---------------------------------
TC-67  Scroll through the Customer Contact Info form, capture all field labels
       and values, and log them to the terminal and report.
TC-68  Tap Edit Info icon → verify Save Changes and Cancel buttons are visible.
"""
import logging
import pytest


class TestCustomer:

    # ================================================================== #
    #  TC-67 — Scroll all the Customer Info fields
    # ================================================================== #

    def test_tc67_scroll_customer_info_page(self, customer_page):
        """TC-67: Scroll down through the Customer Contact Info form then
        scroll back up to the beginning."""
        customer_page.scroll_content_to_text("Customer Contact Info")
        customer_page.wait_seconds(1)
        customer_page.scroll_content_to_beginning()
        customer_page.wait_seconds(1)

    # ================================================================== #
    #  TC-68 — Edit Info flow: tap Edit → verify buttons → Cancel → tap Edit
    # ================================================================== #

    def test_tc68_edit_customer_info(self, customer_page):
        """TC-68:
        1. Tap the Edit Info icon.
        2. Verify Save Changes button is visible.
        3. Verify Cancel button is visible.
        4. Tap Cancel.
        5. Tap Edit Info icon again.
        """
        # Step 1 — tap Edit Info icon
        customer_page.tap_edit_info_icon()
        customer_page.wait_seconds(1)

        customer_page.scroll_content_to_text("Customer Contact Info")
        customer_page.wait_seconds(1)
        customer_page.scroll_content_to_beginning()
        customer_page.wait_seconds(1)

        # Save Changes button must be visible
        assert customer_page.is_save_changes_visible(), \
            "Save Changes button should be visible after tapping Edit Info"

        # Cancel button must be visible
        assert customer_page.is_cancel_visible(), \
            "Cancel button should be visible after tapping Edit Info"

        # Step 4 — tap Cancel
        customer_page.tap_cancel()
        customer_page.wait_seconds(1)

        # Step 5 — tap Edit Info icon again
        customer_page.tap_edit_info_icon()
        customer_page.wait_seconds(1)

    # ================================================================== #
    #  TC-69 — Fill all editable fields and save
    # ================================================================== #

    def test_tc69_update_and_save_customer_info(self, customer_page):
        """TC-69:
        1. Enter edit mode if needed.
        2. Update the country dropdown through its parent-scoped clickable child.
        3. Clear and fill every EditText field with new values.
        4. Tap Save Changes and verify the selected country remains visible.
        """

        # Step 1 — fill all fields
        customer_page.scroll_content_to_beginning()
        customer_page.wait_seconds(1)

        if not customer_page.is_element_visible(customer_page.SAVE_CHANGES_BTN, timeout=1):
            customer_page.tap_edit_info_icon()
            customer_page.wait_seconds(1)

        customer_page.scroll_content_to_text(customer_page.COUNTRY_PLACEHOLDER)
        customer_page.wait_seconds(1)

        country_parent = customer_page.get_country_parent_container()
        clickable_descendants = customer_page.get_country_clickable_descendants()
        country_container = customer_page.get_country_clickable_container()
        current_country = customer_page.get_country_value()

        assert country_parent.is_displayed(), \
            "Country field parent ViewGroup should be visible in edit mode"
        assert clickable_descendants, \
            "Country field parent should contain at least one clickable descendant with content-desc"
        assert any(descendant.id == country_container.id for descendant in clickable_descendants), \
            "Country dropdown should tap a clickable child inside the resolved parent ViewGroup"
        assert customer_page.get_country_hint_element().text == customer_page.COUNTRY_PLACEHOLDER, \
            "Country parent row should contain the Select Country hint text"

        chosen_country = customer_page.select_first_available_country(exclude_current=True)
        customer_page.wait_seconds(1)

        assert chosen_country != customer_page.COUNTRY_PLACEHOLDER, \
            "Country selection should choose a real option instead of the placeholder"
        if current_country != customer_page.COUNTRY_PLACEHOLDER:
            assert chosen_country != current_country, \
                "Country selection should change the currently selected value"
        assert customer_page.get_country_value() == chosen_country, \
            "Country clickable child should expose the chosen option in content-desc"
        assert not customer_page.is_country_empty(), \
            "Country field should not remain empty after selecting an option"
        assert customer_page.get_country_hint_element().text == customer_page.COUNTRY_PLACEHOLDER, \
            "Select Country hint should still be available inside the same parent row after selection"

        new_data = {
            "First Name":    "John",
            "Last Name":     "Doe",
            "Phone":         "555-0100",
            "Alt Phone":     "555-0101",
            "Address":       "123 Main St",
            "Address Two":   "Suite 200",
            "City":          "Chicago",
            "ZIP":           "60601",
            "Email Address": "john.doe@example.com",
            "Customer Email Address": "customer@example.com",
            "Customer Contact Info": "Preferred contact time: afternoons"
        }
        customer_page.fill_customer_fields(new_data)
        customer_page.wait_seconds(1)

        # Step 2 — scroll to Save Changes and tap

        # customer_page.scroll_content_to_text("CUSTOMER CONTACT INFO")
        # customer_page.wait_seconds(1)
        customer_page.tap_save_changes()
        customer_page.wait_seconds(2)
        assert customer_page.get_country_value() == chosen_country, \
            "Selected country should remain visible after saving customer info"

 
