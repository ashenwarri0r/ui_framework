from pages.file_upload_page_11 import FileUploadPage


UPLOAD_PAGE_URL = "https://the-internet.herokuapp.com/upload"
FILE_NAME = "image_for_upload.jpg"
FILE_PATH = fr"C:\Users\ASHEN\PycharmProjects\UI Framework\{FILE_NAME}"

def test_upload_dialog_window(browser):
    upload_page = FileUploadPage(browser)

    browser.get(UPLOAD_PAGE_URL)
    upload_page.wait_for_open()

    upload_page.dialog_window_upload(FILE_PATH)

    assert upload_page.dialog_window_verify_upload(), \
    "Ожидалось, что в области загрузки отобразится имя файла и галочка"