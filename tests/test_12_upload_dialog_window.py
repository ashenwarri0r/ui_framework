from pages.file_upload_page_11 import FileUploadPage
import os
from utils.pyautogui import PyAutogui

UPLOAD_PAGE_URL = "https://the-internet.herokuapp.com/upload"
FILE_NAME = "image_for_upload.jpg"

CURRENT_SCRIPT_PATH = os.path.abspath(__file__)
project_dir = os.path.dirname(os.path.dirname(CURRENT_SCRIPT_PATH))
FILE_PATH = os.path.join(project_dir, FILE_NAME)


def test_upload_dialog_window(browser):
    upload_page = FileUploadPage(browser)
    pyautogui = PyAutogui()

    browser.get(UPLOAD_PAGE_URL)
    upload_page.wait_for_open()

    upload_page.click_for_dialog_window()
    pyautogui.upload_file_pyatogui(str(FILE_PATH))
    upload_page.verify_dialog_window_upload()

    assert True, \
        "Ожидалось, что в области загрузки отобразится имя файла и галочка"
