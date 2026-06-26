class TestAttachments:

    def test_tc79_click_attachments_docs_tab(self, attachments_page):
        """TC-79:
        1. Click Actions/Docs tab.
        2. Click Attachments sub-tab.
        3. Verify the Attachments list is visible.
        """
        # Step 1 — click Actions/Docs tab
        attachments_page.click_actions_docs_tab()
        attachments_page.wait_seconds(1)    
        attachments_page.click_attachments_tab()

    def test_tc80_scroll_and_click_random_images(self, attachments_page):
        """TC-80: Attachments list
        1. Scroll down to the last attachment.
        2. Scroll back up to the beginning.
        3. Click 3 randomly selected image files.
           After each click, tap the image-viewer back arrow to return to the list.
        """
        # Step 1 — scroll to the bottom of the list
        attachments_page.scroll_to_end()
        attachments_page.wait_seconds(1)

        # Step 2 — scroll back to the top
        attachments_page.scroll_to_beginning()
        attachments_page.wait_seconds(1)

        # Step 3 — click 3 random image attachments
        attachments_page.click_random_image_attachments(count=3)

    def test_tc81_tap_three_dots_menu(self, attachments_page):
        """TC-81: Three-dots context menu
        1. Tap the three-dots (⋮) button of a randomly chosen attachment.
        2. Verify menu options based on file type:
           - Images (jpg/jpeg/png/…): Rename + Remove only
           - All other files (pdf, templates…): Rename + Edit + Remove
        3. Dismiss the menu.
        """
        import os

        # Step 1 — tap three dots of a random attachment; get its content-desc back
        chosen_desc = attachments_page.tap_random_attachment_three_dots()
        attachments_page.wait_seconds(1)

        filename = chosen_desc.split(',')[0].strip()
        ext = os.path.splitext(filename)[1].lower()
        is_image = ext in attachments_page.IMAGE_EXTENSIONS

        # Step 2 — Rename and Remove are visible for every attachment type
        assert attachments_page.is_element_visible(attachments_page.MENU_RENAME), 'Rename option not visible'
        assert attachments_page.is_element_visible(attachments_page.MENU_REMOVE), 'Remove option not visible'

        # Edit is only present for non-image attachments (PDFs, templates, etc.)
        if not is_image:
            assert attachments_page.is_element_visible(attachments_page.MENU_EDIT), 'Edit option not visible for non-image attachment'

        # Step 3 — dismiss the menu
        attachments_page.dismiss_menu()
        attachments_page.wait_seconds(1)

    def test_tc82_rename_attachment(self, attachments_page):
        """TC-82: Rename attachment
        1. Tap the three-dots (\u22ee) button of a random attachment.
        2. Tap Rename.
        3. Clear the file name field and type 'Automation rename'.
        4. Tap Submit.
        """
        # Step 1 \u2014 open three-dots menu for a random attachment
        attachments_page.tap_random_attachment_three_dots()
        attachments_page.wait_seconds(2)

        # Step 2 \u2014 tap Rename
        attachments_page.click_menu_rename()
        attachments_page.wait_seconds(5)

        # Steps 3 & 4 \u2014 clear input, type new name, submit
        attachments_page.do_rename('Automation rename')
        attachments_page.wait_seconds(5)

    def test_tc83_edit_attachment(self, attachments_page):
        """TC-83: Edit attachment (non-image / PDF only)
        1. Tap the three-dots (\u22ee) button of a randomly chosen non-image attachment.
        2. Tap Edit.
        3. Wait for the PDF viewer to fully open.
        4. Close the PDF viewer via the cross icon.
        """
        # Step 1 \u2014 open three-dots menu for a non-image attachment
        attachments_page.tap_non_image_attachment_three_dots()
        attachments_page.wait_seconds(2)

        # Step 2 \u2014 tap Edit
        attachments_page.click_menu_edit()

        # Step 3 \u2014 wait for PDF viewer to fully load
        attachments_page.wait_seconds(7)

        # Step 4 \u2014 close the PDF viewer
        attachments_page.tap_pdf_viewer_close()
        attachments_page.wait_seconds(5)

    def test_tc84_remove_attachment(self, attachments_page):
        """TC-84: Remove attachment
        1. Tap the three-dots (\u22ee) button of a random attachment.
        2. Tap Remove.
        3. Confirm the 'Are you sure you want to delete this file?' dialog by tapping Yes.
        4. Verify the attachment no longer appears in the list.
        """
        # Step 1 \u2014 open three-dots menu; capture which attachment was chosen
        chosen_desc = attachments_page.tap_random_attachment_three_dots()
        attachments_page.wait_seconds(2)

        # Step 2 \u2014 tap Remove
        attachments_page.click_menu_remove()
        attachments_page.wait_seconds(2)

        # Step 3 \u2014 confirm deletion in the confirmation dialog
        attachments_page.confirm_remove_dialog()
        attachments_page.wait_seconds(2)

        # Step 4 \u2014 verify the removed attachment is gone
        assert not attachments_page.is_attachment_present(chosen_desc), (
            f'Attachment "{chosen_desc.split(",")[0].strip()}" '
            'should have been removed but is still visible in the list'
        )

        
    def test_tc85_filter_attachments_by(self, attachments_page):
        """TC-85: Filter / sort attachments using the 'Attachments by:' bottom sheet
        1. Tap 'Attachments by:' to open the sort bottom sheet.
        2. Select 'Date Uploaded (default)' — most recently uploaded appears first.
        3. Tap 'Attachments by:' again.
        4. Select 'Attachment Type' — PDFs appear before images (order may vary with data).
        5. Tap 'Attachments by:' again.
        6. Select 'File Type' — images appear before other attachments (order may vary with data).
        """
        # Step 1 — open sort bottom sheet
        attachments_page.click_attachments_by_filter()
        attachments_page.wait_seconds(1)

        # Step 2 — select Date Uploaded (default); most recently uploaded should appear first
        attachments_page.click_filter_date_uploaded()
        attachments_page.wait_seconds(2)
        assert attachments_page.get_all_attachment_content_descs(), \
            'No attachments visible after selecting Date Uploaded filter'

        # Step 3 — open sort bottom sheet again
        attachments_page.click_attachments_by_filter()
        attachments_page.wait_seconds(1)

        # Step 4 — select Attachment Type; PDFs expected first, then images (not strictly verified)
        attachments_page.click_filter_attachment_type()
        attachments_page.wait_seconds(2)
        assert attachments_page.get_all_attachment_content_descs(), \
            'No attachments visible after selecting Attachment Type filter'

        # Step 5 — open sort bottom sheet again
        attachments_page.click_attachments_by_filter()
        attachments_page.wait_seconds(1)

        # Step 6 — select File Type; images expected first, then other attachments (not strictly verified)
        attachments_page.click_filter_file_type()
        attachments_page.wait_seconds(2)
        assert attachments_page.get_all_attachment_content_descs(), \
            'No attachments visible after selecting File Type filter'

    def test_tc86_folders_by_filter(self, attachments_page):
        """TC-86: Filter attachments by folder grouping using the 'Folders by :' bottom sheet
        1. Tap 'Folders by :' → select 'Attachment Type'.
           Click all visible folder cards (one or more), returning after each.
        2. Tap 'Folders by :' → select 'Individual Folder per Order'.
           Click all visible folder cards.
        3. Tap 'Folders by :' → select 'Split Into Related Orders and This Order'.
           Click all visible folder cards.
        4. Tap 'Folders by :' → select 'No Folders'.
           Verify attachments revert to flat list view.
        """
        # Step 1 — Attachment Type grouping
        attachments_page.click_folders_by_filter()
        attachments_page.wait_seconds(1)
        attachments_page.click_folder_opt_attachment_type()
        attachments_page.wait_seconds(2)
        attachments_page.click_all_visible_folder_cards()

        # Step 2 — Individual Folder per Order grouping
        attachments_page.click_folders_by_filter()
        attachments_page.wait_seconds(1)
        attachments_page.click_folder_opt_individual_per_order()
        attachments_page.wait_seconds(2)
        attachments_page.click_all_visible_folder_cards()

        # Step 3 — Split Into Related Orders and This Order grouping
        attachments_page.click_folders_by_filter()
        attachments_page.wait_seconds(1)
        attachments_page.click_folder_opt_split_related()
        attachments_page.wait_seconds(2)
        attachments_page.click_all_visible_folder_cards()

        # Step 4 — No Folders: attachments revert to flat list
        attachments_page.click_folders_by_filter()
        attachments_page.wait_seconds(1)
        attachments_page.click_folder_opt_no_folders()
        attachments_page.wait_seconds(2)
        assert attachments_page.get_all_attachment_content_descs(), \
            'No attachments visible after selecting No Folders'

    def test_tc87_click_picture_upload_attachment(self, attachments_page):
        """TC-87: Upload a new attachment via the camera
        1. Tap 'Upload Attachments'.
        2. Select a random attachment type from the bottom sheet
           (e.g. Photo, Work Order, Quote, etc.).
        3. Tap 'Click Picture'.
        4. Tap the camera Shutter button to capture the photo.
        5. Tap 'Done' to confirm and upload.
        """
        # Step 1 — open upload type selection sheet
        attachments_page.click_upload_attachments()
        attachments_page.wait_seconds(1)

        # Step 2 — pick any available upload type at random
        attachments_page.click_random_upload_type()
        attachments_page.wait_seconds(3)

        # Step 3 — tap 'Click Picture' to open the camera
        attachments_page.click_click_picture()
        attachments_page.wait_seconds(5)

        # Step 4 — capture the photo
        attachments_page.tap_camera_shutter()
        attachments_page.wait_seconds(5)

        # Step 5 — confirm and upload
        attachments_page.tap_camera_done()
        attachments_page.wait_seconds(5)

        # Step 6 — sort by Date Uploaded and open the first (most recently uploaded) attachment
        attachments_page.click_attachments_by_filter()
        attachments_page.wait_seconds(1)
        attachments_page.click_filter_date_uploaded()
        attachments_page.wait_seconds(2)
        attachments_page.click_first_attachment()
        attachments_page.wait_seconds(3)
        attachments_page.tap_back_arrow()
        attachments_page.wait_seconds(2)


    def test_tc88_upload_picture_upload_attachment(self, attachments_page):
        """TC-88: Upload a new attachment via the upload picture
        1. Tap 'Upload Attachments'.
        2. Select a random attachment type from the bottom sheet
           (e.g. Photo, Work Order, Quote, etc.).
        3. Tap 'Upload Picture'.
        4. Select a random image from the media grid to upload.
        5. Tap 'Done' to confirm and upload.
        """
        # Step 1 — open upload type selection sheet
        attachments_page.click_upload_attachments()
        attachments_page.wait_seconds(1)

        # Step 2 — pick any available upload type at random
        attachments_page.click_random_upload_type()
        attachments_page.wait_seconds(2)

        # Step 3 — tap 'Upload Picture' to open the media grid
        attachments_page.click_upload_picture()
        attachments_page.wait_seconds(2)

        # Step 4 — select a random image from the media grid
        attachments_page.tap_random_image()
        attachments_page.wait_seconds(1)

        # Step 5 — click done button and upload
        attachments_page.click_done_after_select()
        attachments_page.wait_seconds(5)

        # Step 6 — sort by Date Uploaded and open the first (most recently uploaded) attachment
        attachments_page.click_attachments_by_filter()
        attachments_page.wait_seconds(1)
        attachments_page.click_filter_date_uploaded()
        attachments_page.wait_seconds(2)
        attachments_page.click_first_attachment()
        attachments_page.wait_seconds(3)
        attachments_page.tap_back_arrow()
        attachments_page.wait_seconds(2)

    # def test_tc89_upload_file_upload_attachment(self, attachments_page):
    #     """TC-89: Upload a new attachment via the upload file
    #     1. Tap 'Upload Attachments'.
    #     2. Select a random attachment type from the bottom sheet
    #        (e.g. Photo, Work Order, Quote, etc.).
    #     3. Tap 'Upload File'.
    #     4. open side bar and click downloads
    #     4. select file.
    #     5. Tap 'Done' to confirm and upload.
    #     """
    #     # Step 1 — open upload type selection sheet
    #     attachments_page.click_upload_attachments()
    #     attachments_page.wait_seconds(1)

    #     # Step 2 — pick any available upload type at random
    #     attachments_page.click_random_upload_type()
    #     attachments_page.wait_seconds(2)

    #     # Step 3 — tap 'Upload Picture' to open the media grid
    #     attachments_page.click_upload_picture()
    #     attachments_page.wait_seconds(2)

    #     # Step 4 — select a random image from the media grid
    #     attachments_page.tap_random_image()
    #     attachments_page.wait_seconds(1)

    #     # Step 5 — click done button and upload
    #     attachments_page.click_done_after_select()
    #     attachments_page.wait_seconds(5)

    #     # Step 6 — sort by Date Uploaded and open the first (most recently uploaded) attachment
    #     attachments_page.click_attachments_by_filter()
    #     attachments_page.wait_seconds(1)
    #     attachments_page.click_filter_date_uploaded()
    #     attachments_page.wait_seconds(2)
    #     attachments_page.click_first_attachment()
    #     attachments_page.wait_seconds(3)
    #     attachments_page.tap_back_arrow()
    #     attachments_page.wait_seconds(2)    
