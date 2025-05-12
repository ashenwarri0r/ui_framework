from pages.handlers_page_7 import HandlersPage, NewWindowPage


HANDLERS_PAGE_LINK = "http://the-internet.herokuapp.com/windows"
WINDOW_NAME = "New Window"

def test_handlers(browser):
    handlers_page = HandlersPage(browser)
    new_window_page = NewWindowPage(browser)

    browser.get(HANDLERS_PAGE_LINK)
    for _ in range(2):
        handlers_page.wait_for_open()

        handlers_page.click_new_window()
        browser.switch_to_last_window()
        new_window_page.wait_for_open()

        assert browser.window_title == WINDOW_NAME, \
            (f"Ожидаемое название вкладки: {WINDOW_NAME}"
             f"Фактическое название вкладки: {browser.window_title}")

        browser.switch_to_window("The Internet")

    handlers_page.wait_for_open()
    for _ in range(2):
        browser.switch_to_last_window()
        browser.close()

    number_of_windows = browser.get_windows_number()
    assert number_of_windows == 1, \
        (f"Ожидалось, что открытые ранее вкладки закроются"
         f"Фактически осталось вкладок: {number_of_windows}")
