import logging
log = logging.getLogger(__name__)
class TestNotesAndEmail:

    def test_tc88_click_notes_and_email_tab(self, notes_and_email_page):
        """TC-88:
        1. Click Actions/Docs tab.
        2. Click Notes & Email sub-tab.
        3. Verify the Notes & Email list is visible.
        """
        # Step 1 — click Actions/Docs tab   
        notes_and_email_page.click_notes_and_email_tab()

    def test_tc89_scroll_notes_and_email_list(self, notes_and_email_page):
        """TC-89: Verify that the user can scroll through the Notes and Email list in the Job Details screen.
        1. Scroll to the end of the Notes and Email list.
        2. Scroll back to the beginning of the Notes and Email list.
        """
        # Step 1: Scroll to the end of the Notes and Email list.
        notes_and_email_page.scroll_to_end()

        # Step 2: Scroll back to the beginning of the Notes and Email list.
        notes_and_email_page.scroll_to_beginning()  


    def test_tc90_click_add_notes_and_email_button(self, notes_and_email_page):

        """TC-90: Verify that the user click on the "Add Notes and Email" button in the "Notes and Email" section of the Job Details screen.
        1. Click on the "Add Notes and Email" button.
        2. Enter text in the "Note" field.
        3. Click on the "Add Note" button.
        """

        # Step 1: Click on the "Add Notes and Email" button.
        notes_and_email_page.click_add_notes_button()

        # Step 2: Enter text in the "Note" field.
        note_text = "test note."
        notes_and_email_page.enter_note_text(note_text)

        # Step 3: Click on the "Add Note" button.
        notes_and_email_page.click_add_note_button()
        notes_and_email_page.wait_seconds(2)

    def test_tc91_tap_filter_icon(self, notes_and_email_page):
        """TC-91: Filter Notes and Email list
        1. Tap filter icon in Notes and Email section header.
        2. Select the 'Show Standard Note' filter option.
        3. Click on the "Apply Filters" button.
        4. Verify filter badge notification count is 1.
        """    
        # Step 1: Tap filter icon in Notes and Email section header.
        notes_and_email_page.click_filter_icon()
        notes_and_email_page.wait_seconds(1)

        # Step 2: Select the 'Show Standard Note' filter option.
        chosen_desc, expected_count = notes_and_email_page.click_standard_note_filter()
        notes_and_email_page.wait_seconds(1)
        print(f'[Step 2] Selected filter: "{chosen_desc}" (expected count: {expected_count})')

        # Step 3: Click on the "Apply Filters" button.
        notes_and_email_page.click_apply_filters()
        notes_and_email_page.wait_seconds(2)

        # Step 4: Verify filter badge notification count is 1.
        assert notes_and_email_page.is_filter_badge_one(), (
            f'Filter badge should show 1 after applying filter "{chosen_desc}"'
        )

        notes_and_email_page.scroll_to_end()
        notes_and_email_page.scroll_to_beginning()


    def test_tc92_clear_filters(self, notes_and_email_page):
        """TC-92: Clear Notes and Email filters
        1. Tap filter icon in Notes and Email section header.
        2. Click on the "Clear All" button.
        3. Verify filter badge is no longer visible.
        """    
        # Step 1: Tap filter icon in Notes and Email section header.
        notes_and_email_page.click_filter_icon()
        notes_and_email_page.wait_seconds(1)

        # Step 2: Click on the "Clear All" button.
        notes_and_email_page.click_clear_all()
        notes_and_email_page.wait_seconds(1)

        # Step 3: Verify filter badge is no longer visible.
        assert not notes_and_email_page.is_filter_badge_one(), 'Filter badge should not be visible after clearing filters' 

        notes_and_email_page.scroll_to_end()
        notes_and_email_page.scroll_to_beginning()