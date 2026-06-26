import os
import re
import random

from appium.webdriver.common.appiumby import AppiumBy

from src.pages.base_page import BasePage


class AttachmentsPage(BasePage):

    # ------------------------------------------------------------------ #
    #  SECTION HEADER
    # ------------------------------------------------------------------ #

    ACTIONS_DOCS_TAB = (
        AppiumBy.XPATH, '//android.widget.TextView[@text="Actions/Docs"]'
    )

    ATTACHMENTS_TAB = (
        AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="Attachments"]'
    )

    # Every attachment row has content-desc ending with "by Cilio Service"
    ATTACHMENT_ITEM = (
        AppiumBy.XPATH,
        '//android.view.ViewGroup[contains(@content-desc, " by Cilio Service")]'
    )

    # File extensions considered as images
    IMAGE_EXTENSIONS = {'.jpg', '.jpeg', '.png', '.gif', '.bmp', '.webp', '.tiff', '.tif'}

    # Three-dot context menu items
    MENU_RENAME = (AppiumBy.XPATH, '//android.view.View[@content-desc="Rename"]')
    MENU_EDIT   = (AppiumBy.XPATH, '//android.view.View[@content-desc="Edit"]')
    MENU_REMOVE = (AppiumBy.XPATH, '//android.view.View[@content-desc="Remove"]')

    # Rename modal
    RENAME_MODAL_TITLE = (AppiumBy.XPATH, '//android.widget.TextView[@text="Rename"]')
    RENAME_INPUT       = (AppiumBy.XPATH, '//android.view.ViewGroup[@resource-id="AnimatedView"]//android.widget.EditText')
    RENAME_SUBMIT      = (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="Submit"]')

    # Remove confirmation dialog
    REMOVE_CONFIRM_TEXT = (AppiumBy.XPATH, '//android.widget.TextView[@text="Are you sure you want to delete this file?"]')
    REMOVE_CONFIRM_YES  = (AppiumBy.XPATH, '//android.widget.TextView[@text="Yes"]')

    # Filter / sort bottom sheet
    FILTER_ATTACHMENTS_BY   = (AppiumBy.XPATH, '//android.widget.TextView[@text="Attachments by:"]')
    FILTER_DATE_UPLOADED    = (AppiumBy.XPATH, '//android.widget.TextView[@text="Date Uploaded (default)"]')
    FILTER_ATTACHMENT_TYPE  = (AppiumBy.XPATH, '//android.widget.TextView[@text="Attachment Type"]')
    FILTER_FILE_TYPE        = (AppiumBy.XPATH, '//android.widget.TextView[@text="File Type"]')

    # Folders-by bottom sheet
    FILTER_FOLDERS_BY               = (AppiumBy.XPATH, '//android.widget.TextView[@text="Folders by :"]')
    FOLDER_OPT_ATTACHMENT_TYPE      = (AppiumBy.XPATH, '//android.widget.TextView[@text="Attachment Type"]')
    FOLDER_OPT_INDIVIDUAL_PER_ORDER = (AppiumBy.XPATH, '//android.widget.TextView[@text="Individual Folder per Order"]')
    FOLDER_OPT_SPLIT_RELATED        = (AppiumBy.XPATH, '//android.widget.TextView[@text="Split Into Related Orders and This Order"]')
    FOLDER_OPT_NO_FOLDERS           = (AppiumBy.XPATH, '//android.widget.TextView[@text="No Folders"]')

    # Folder card items (variable count — matched by partial content-desc pattern)
    FOLDER_CARD = (AppiumBy.XPATH, '//android.view.ViewGroup[contains(@content-desc, "(")]')

    # Upload attachments
    UPLOAD_ATTACHMENTS_BTN = (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="Upload Attachments"]')
    UPLOAD_TYPE_ITEM       = (AppiumBy.XPATH, '//android.widget.ScrollView//android.view.ViewGroup[@content-desc]')

    # Upload Attachment By Click Picture
    UPLOAD_CLICK_PICTURE   = (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="Click Picture"]')
    CAMERA_SHUTTER         = (AppiumBy.XPATH, '//android.widget.ImageView[@content-desc="Shutter"]')
    CAMERA_DONE            = (AppiumBy.XPATH, '//android.widget.ImageButton[@content-desc="Done"]')

    # Upload Attachment By Upload Picture
    UPLOAD_UPLOAD_PICTURE   = (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="Upload Picture"]')

    MEDIA_GRID_IMAGES = (
    AppiumBy.XPATH,
    '//android.view.View[@content-desc="Media grid"]'
    '/android.view.View/android.view.View[2]/android.view.View[2]/android.view.View'
    )

    UPLOAD_DONE_BTN = (
        AppiumBy.XPATH, '//androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[5]/android.view.View/android.view.View[3]/android.widget.Button'    
    )

    # Upload Attachment By Upload File
    UPLOAD_UPLOAD_FILE   = (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="Upload File"]')

    

    # PDF viewer close button (com.horcrux.svg.SvgView, clickable=false)
    # Bounds [988,105][1054,171] → center (1021, 138)
    PDF_VIEWER_CLOSE_X = 1021
    PDF_VIEWER_CLOSE_Y = 138

    # ------------------------------------------------------------------ #
    #  NAVIGATION HELPERS
    # ------------------------------------------------------------------ #

    def click_actions_docs_tab(self):
        self.click(self.ACTIONS_DOCS_TAB)

    def click_attachments_tab(self):
        self.click(self.ATTACHMENTS_TAB)

    @staticmethod
    def _bounds_center(bounds: str):
        """Parse Appium bounds string '[x1,y1][x2,y2]' into center (x, y)."""
        m = re.match(r'\[(\d+),(\d+)\]\[(\d+),(\d+)\]', bounds)
        x1, y1, x2, y2 = int(m.group(1)), int(m.group(2)), int(m.group(3)), int(m.group(4))
        return (x1 + x2) // 2, (y1 + y2) // 2

    # ------------------------------------------------------------------ #
    #  SCROLL HELPERS
    # ------------------------------------------------------------------ #

    def scroll_to_end(self):
        """Scroll the attachment list down to the very last item."""
        self.driver.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            f'new UiScrollable(new UiSelector().scrollable(true).instance(1))'
            f'.scrollToEnd(10)'
        )

    def scroll_to_beginning(self):
        """Scroll the attachment list back up to the very first item."""
        self.driver.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiScrollable(new UiSelector().scrollable(true).instance(1))'
            '.scrollToBeginning(10)'
        )

    # ------------------------------------------------------------------ #
    #  ATTACHMENT ITEM HELPERS
    # ------------------------------------------------------------------ #

    def get_all_attachment_content_descs(self) -> list:
        """Return content-desc strings for every attachment row visible in the DOM."""
        elements = self.find_elements(self.ATTACHMENT_ITEM)
        return [
            el.get_attribute('content-desc') or ''
            for el in elements
            if el.get_attribute('content-desc')
        ]

    def get_image_attachment_content_descs(self) -> list:
        """Return content-desc strings for all image-type attachment items.

        Filename is the part before the first comma in content-desc.
        Only items whose filename extension is in IMAGE_EXTENSIONS are included.
        """
        elements = self.find_elements(self.ATTACHMENT_ITEM)
        image_descs = []
        for el in elements:
            content_desc = el.get_attribute('content-desc') or ''
            filename = content_desc.split(',')[0].strip()
            ext = os.path.splitext(filename)[1].lower()
            if ext in self.IMAGE_EXTENSIONS:
                image_descs.append(content_desc)
        return image_descs

    def tap_three_dots_for(self, content_desc: str):
        """Tap the three-dots (⋮) button for a specific attachment row.

        The child ViewGroup is clickable=false, so its center is read from the
        bounds attribute and tapped via a coordinate gesture.
        """
        escaped = content_desc.replace('"', '\\"')
        el = self.driver.find_element(
            AppiumBy.XPATH,
            f'//android.view.ViewGroup[@content-desc="{escaped}"]/android.view.ViewGroup'
        )
        x, y = self._bounds_center(el.get_attribute('bounds'))
        self.driver.execute_script('mobile: clickGesture', {'x': x, 'y': y})

    def tap_random_attachment_three_dots(self) -> str:
        """Tap the three-dots button of a randomly chosen attachment.

        Returns the content-desc of the chosen attachment.
        """
        descs = self.get_all_attachment_content_descs()
        assert descs, 'No attachments found in the list'
        chosen = random.choice(descs)
        self.tap_three_dots_for(chosen)
        return chosen

    # ------------------------------------------------------------------ #
    #  CONTEXT MENU ACTIONS
    # ------------------------------------------------------------------ #

    def is_menu_visible(self) -> bool:
        return self.is_element_visible(self.MENU_RENAME)

    def click_menu_rename(self):
        self.click(self.MENU_RENAME)

    def click_menu_edit(self):
        self.click(self.MENU_EDIT)

    def click_menu_remove(self):
        self.click(self.MENU_REMOVE)

    def dismiss_menu(self):
        """Close the context menu by pressing the Android back key."""
        self.driver.back()

    # ------------------------------------------------------------------ #
    #  RENAME MODAL
    # ------------------------------------------------------------------ #

    def do_rename(self, new_name: str):
        """Wait for the Rename modal, clear the input and type new_name, then submit."""
        self.wait_for_element(self.RENAME_MODAL_TITLE)
        input_el = self.wait_for_clickable(self.RENAME_INPUT)
        input_el.clear()
        input_el.send_keys(new_name)
        self.click(self.RENAME_SUBMIT)

    # ------------------------------------------------------------------ #
    #  PDF VIEWER
    # ------------------------------------------------------------------ #

    def tap_pdf_viewer_close(self):
        """Close the PDF viewer via coordinate tap (SvgView has clickable=false).

        Bounds [988,105][1054,171] → center (1021, 138).
        """
        self.driver.execute_script(
            'mobile: clickGesture',
            {'x': self.PDF_VIEWER_CLOSE_X, 'y': self.PDF_VIEWER_CLOSE_Y}
        )

    # ------------------------------------------------------------------ #
    #  REMOVE VALIDATION
    # ------------------------------------------------------------------ #

    def confirm_remove_dialog(self):
        """Wait for the remove confirmation dialog and tap Yes."""
        self.wait_for_element(self.REMOVE_CONFIRM_TEXT)
        self.click(self.REMOVE_CONFIRM_YES)

    # ------------------------------------------------------------------ #
    #  FILTER / SORT BOTTOM SHEET
    # ------------------------------------------------------------------ #

    def click_attachments_by_filter(self):
        """Open the 'Attachments by:' sort bottom sheet."""
        self.click(self.FILTER_ATTACHMENTS_BY)

    def click_filter_date_uploaded(self):
        """Select 'Date Uploaded (default)' from the sort bottom sheet."""
        self.click(self.FILTER_DATE_UPLOADED)

    def click_filter_attachment_type(self):
        """Select 'Attachment Type' from the sort bottom sheet."""
        self.click(self.FILTER_ATTACHMENT_TYPE)

    def click_filter_file_type(self):
        """Select 'File Type' from the sort bottom sheet."""
        self.click(self.FILTER_FILE_TYPE)

    def click_folders_by_filter(self):
        """Open the 'Folders by :' sort bottom sheet."""
        self.click(self.FILTER_FOLDERS_BY)

    def click_folder_opt_attachment_type(self):
        self.click(self.FOLDER_OPT_ATTACHMENT_TYPE)

    def click_folder_opt_individual_per_order(self):
        self.click(self.FOLDER_OPT_INDIVIDUAL_PER_ORDER)

    def click_folder_opt_split_related(self):
        self.click(self.FOLDER_OPT_SPLIT_RELATED)

    def click_folder_opt_no_folders(self):
        self.click(self.FOLDER_OPT_NO_FOLDERS)

    # ------------------------------------------------------------------ #
    #  UPLOAD ATTACHMENT
    # ------------------------------------------------------------------ #

    def click_upload_attachments(self):
        """Tap the 'Upload Attachments' button to open the type-selection sheet."""
        self.click(self.UPLOAD_ATTACHMENTS_BTN)

    def click_random_upload_type(self):
        """Select a random attachment type from the upload bottom sheet.

        Any ViewGroup with a content-desc inside the ScrollView is a valid option
        (e.g. Photo, Work Order, Quote, Drawings, etc.).
        """
        items = self.find_elements(self.UPLOAD_TYPE_ITEM)
        assert items, 'No upload type options found in the bottom sheet'
        random.choice(items).click()

    def click_click_picture(self):
        self.click(self.UPLOAD_CLICK_PICTURE)

    def tap_camera_shutter(self):
        self.click(self.CAMERA_SHUTTER)

    def tap_camera_done(self):
        self.click(self.CAMERA_DONE)

    def click_upload_picture(self):
        self.click(self.UPLOAD_UPLOAD_PICTURE)    

    def tap_random_image(self):
        images = self.find_elements(self.MEDIA_GRID_IMAGES)
        assert images, 'No images found in media grid'
        chosen = random.choice(images)
        chosen.click()

    def click_done_after_select(self):
        self.click(self.UPLOAD_DONE_BTN)

    def click_upload_file(self):
        self.click(self.UPLOAD_UPLOAD_FILE)    

    def click_all_visible_folder_cards(self):
        """Find every visible folder card, expand then collapse it, then move to the next.

        A folder card is any ViewGroup whose content-desc contains '(' —
        e.g. 'Photo, (9)' or 'Other, (1)'.  Each card is clicked once to open/expand it,
        then clicked again to close it before proceeding to the next card.
        """
        cards = self.find_elements(self.FOLDER_CARD)
        assert cards, 'No folder cards found after applying the sort option'
        for card in cards:
            card.click()
            self.wait_seconds(2)
            card.click()
            self.wait_seconds(1)

    def click_first_attachment(self):
        """Click the first attachment in the list to open it."""
        items = self.find_elements(self.ATTACHMENT_ITEM)
        assert items, 'No attachments found in the list'
        items[0].click()

    def is_attachment_present(self, content_desc: str) -> bool:
        """Return True if an attachment with the given content-desc is still in the DOM."""
        escaped = content_desc.replace('"', '\\"')
        locator = (
            AppiumBy.XPATH,
            f'//android.view.ViewGroup[@content-desc="{escaped}"]'
        )
        return self.is_element_present(locator, timeout=5)

    # ------------------------------------------------------------------ #
    #  NON-IMAGE ATTACHMENT HELPERS
    # ------------------------------------------------------------------ #

    def get_non_image_attachment_content_descs(self) -> list:
        """Return content-desc strings for non-image attachments (PDFs, templates, etc.)."""
        elements = self.find_elements(self.ATTACHMENT_ITEM)
        descs = []
        for el in elements:
            content_desc = el.get_attribute('content-desc') or ''
            filename = content_desc.split(',')[0].strip()
            ext = os.path.splitext(filename)[1].lower()
            if ext not in self.IMAGE_EXTENSIONS:
                descs.append(content_desc)
        return descs

    def tap_non_image_attachment_three_dots(self) -> str:
        """Tap the three-dots button of a randomly chosen non-image attachment.

        Returns the content-desc of the chosen attachment.
        """
        descs = self.get_non_image_attachment_content_descs()
        assert descs, 'No non-image attachments found in the list'
        chosen = random.choice(descs)
        self.tap_three_dots_for(chosen)
        return chosen

    def scroll_to_and_click_attachment(self, content_desc: str):
        """Find and click an attachment row by its exact content-desc.

        Items are already in the DOM after scroll_to_beginning(), so a direct
        XPATH lookup is used — no UiScrollable scrollIntoView needed.
        """
        escaped = content_desc.replace('"', '\\"')
        locator = (
            AppiumBy.XPATH,
            f'//android.view.ViewGroup[@content-desc="{escaped}"]'
        )
        self.wait_for_clickable(locator).click()

    # ------------------------------------------------------------------ #
    #  MAIN WORKFLOW
    # ------------------------------------------------------------------ #

    def click_random_image_attachments(self, count: int = 3):
        """Scroll to the beginning, collect all image attachments, click *count* random ones.

        After each click the image-viewer back arrow is tapped to return to the attachments list.
        """
        self.scroll_to_beginning()
        self.wait_seconds(1)

        image_descs = self.get_image_attachment_content_descs()
        assert image_descs, 'No image attachments found in the attachments list'

        chosen = random.sample(image_descs, min(count, len(image_descs)))

        for content_desc in chosen:
            self.scroll_to_and_click_attachment(content_desc)
            self.wait_seconds(10)  # Wait for the image viewer to fully load
            self.tap_back_arrow()
            self.wait_seconds(5)