from pages.contextclick_page_4 import ContextClickPage


CONTEXT_CLICK_PAGE_URL = "https://the-internet.herokuapp.com/context_menu"
EXPECTED_ALERT_TEXT = "You selected a context menu"

def test_context_click(browser):
    context_click_page = ContextClickPage(browser)

    browser.get(CONTEXT_CLICK_PAGE_URL)
    context_click_page.wait_for_open()
    context_click_page.right_click_area()

    assert browser.get_alert_text() == EXPECTED_ALERT_TEXT,\
        (f"Ожидаемый текст: {EXPECTED_ALERT_TEXT}"
         f"Фактический текст: {browser.get_alert_text()}")

    browser.accept_alert()
    assert browser.wait_alert_closed(), "Ожидалось, что Alert закроется, но он не закрылся ¯\_(ツ)_/¯"
