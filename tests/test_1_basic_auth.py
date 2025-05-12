from pages.basic_auth_page_1 import BasicAuthPage


EXPECTED_TEXT = "Congratulations! You must have the proper credentials."
AUTH_PAGE_URL = "the-internet.herokuapp.com/basic_auth"


def test_basic_auth(browser):
    auth_page = BasicAuthPage(browser)

    username = "admin"
    password = "admin"
    url = f"https://{username}:{password}@{AUTH_PAGE_URL}"

    browser.get(url)
    auth_page.wait_for_open()

    assert auth_page.successful_auth() == EXPECTED_TEXT,\
        (f"Ожидаемый текст: {EXPECTED_TEXT}"
         f"Фактический текст: {auth_page.success_message.get_text()}")
