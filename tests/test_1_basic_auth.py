from pages.basic_auth_page_1 import BasicAuthPage

EXPECTED_TEXT = "Congratulations! You must have the proper credentials."
AUTH_PAGE_URL = "the-internet.herokuapp.com/basic_auth"
USERNAME = "admin"
PASSWORD = "admin"


def test_basic_auth(browser):
    auth_page = BasicAuthPage(browser)

    url = f"https://{USERNAME}:{PASSWORD}@{AUTH_PAGE_URL}"

    browser.get(url)
    auth_page.wait_for_open()

    assert auth_page.do_auth() == EXPECTED_TEXT, \
        (f"Ожидаемый текст: {EXPECTED_TEXT}"
         f"Фактический текст: {auth_page.success_message.get_text()}")
