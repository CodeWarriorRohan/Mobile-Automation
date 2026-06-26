class TestQAndAPage:

    def test_tc93_tap_q_and_a_tab(self, q_and_a_page):
        """TC-93: Open Q&A tab
        1. Tap on the "Q&A's" tab in the Action Docs section header.
        """
        # Step 1: Tap on the "Q&A's" tab in the Action Docs section header.
        q_and_a_page.click_q_and_a_tab()
        q_and_a_page.wait_seconds(3)

    def test_tc94_open_q_and_a_dropdown(self, q_and_a_page):
        """TC-94: Open Q&A dropdown
        1. Tap on the dropdown.
        2. Select an option from the dropdown.
        """
        # Step 1: Tap on the dropdown.
        category = q_and_a_page.open_first_dropdown()
        print(f'[Step 1] Opened dropdown: "{category}"')
        q_and_a_page.wait_seconds(2)

        # Step 2: Select the first available option from the dropdown.
        chosen = q_and_a_page.select_first_dropdown_option()
        print(f'[Step 2] Selected option: "{chosen}"')
        q_and_a_page.wait_seconds(2)
        q_and_a_page.tap_back_arrow()
        q_and_a_page.wait_seconds(2)