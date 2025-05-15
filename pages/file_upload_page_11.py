from .base_page import BasePage
from elements.web_element import WebElement
from elements.button import Button
from elements.input import Input
from collections import namedtuple


class FileUploadPage(BasePage):
    UNIQUE_ELEMENT = "file-upload"
    FILE_UPLOAD = "file-upload"
    UPLOAD_BUTTON = "file-submit"
    FILE_NAME_FIELD = "uploaded-files"
    CONFIRMATION_TEXT = "//h3"
    DRAG_DROP_AREA = "drag-drop-upload"
    DRAG_DROP_HIDDEN_INPUT = "//*[@multiple]"
    DRAG_DROP_SUCCESS_MARK = "//*[@id='drag-drop-upload']//*[text()='✔']"
    DRAG_DROP_FILENAME = "//*[@id='drag-drop-upload']//*[contains(@class,'dz-filename')]"

    def __init__(self, browser):
        super().__init__(browser)
        self.unique_element = Input(self.browser, self.UNIQUE_ELEMENT)
        self.file_upload = Input(self.browser, self.FILE_UPLOAD)
        self.upload_button = Button(self.browser, self.UPLOAD_BUTTON)
        self.file_name_field = WebElement(self.browser, self.FILE_NAME_FIELD)
        self.confirmation_text = WebElement(self.browser, self.CONFIRMATION_TEXT)
        self.drag_drop_area = WebElement(self.browser, self.DRAG_DROP_AREA)
        self.hidden_input = Input(self.browser, self.DRAG_DROP_HIDDEN_INPUT)
        self.success_mark = WebElement(self.browser, self.DRAG_DROP_SUCCESS_MARK)
        self.drag_drop_filename = WebElement(self.browser, self.DRAG_DROP_FILENAME)

    def upload_file(self, file_path):
        self.file_upload.wait_for_visible()
        self.file_upload.send_keys(file_path)
        self.upload_button.click()

    def get_file_upload_result(self):
        result = {'text': '', 'file_name': ''}
        self.file_upload.wait_for_absence()
        self.confirmation_text.wait_for_visible()
        result['text'] = self.confirmation_text.get_text()
        self.file_name_field.wait_for_visible()
        result['file_name'] = self.file_name_field.get_text()
        return result

    def upload_dialog_window(self, file_path):
        self.drag_drop_area.wait_for_visible()
        self.drag_drop_area.click()
        self.hidden_input.wait_for_presence()
        self.hidden_input.send_keys(file_path, clear=False, visible=False)

    def verify_dialog_window_upload(self):
        self.success_mark.wait_for_presence()
        self.drag_drop_filename.wait_for_presence()
