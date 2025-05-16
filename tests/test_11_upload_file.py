from pages.file_upload_page_11 import FileUploadPage


UPLOAD_PAGE_URL = "https://the-internet.herokuapp.com/upload"
FILE_NAME = "image_for_upload.jpg"
CONFIRMATION_TEXT = "File Uploaded!"


def test_upload_file(browser):
    upload_page = FileUploadPage(browser)

    browser.get(UPLOAD_PAGE_URL)
    upload_page.wait_for_open()
    upload_page.upload_file(f"{FILE_NAME}")

    result = upload_page.get_file_upload_result()
    text = result['text']
    file_name = result['file_name']

    assert text == f'{CONFIRMATION_TEXT}' and file_name == f'{FILE_NAME}', \
        (f"Ожидаемое сообщение: {CONFIRMATION_TEXT} и имя файла: {FILE_NAME}"
         f"Фактическое сообщение: {text} и имя файла: {file_name}")
