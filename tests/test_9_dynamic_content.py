from pages.dynamic_page_9 import DynamicPage

DYNAMIC_PAGE_URL = "http://the-internet.herokuapp.com/dynamic_content"
MAX_REFRESHES = 100


def test_dynamic_content(browser):
    dynamic_page = DynamicPage(browser)

    browser.get(DYNAMIC_PAGE_URL)
    dynamic_page.wait_for_open()
    dynamic_page.refresh_until_images_match(MAX_REFRESHES)

    assert True, \
        f"За {MAX_REFRESHES} обновлений страницы изображения так и не совпали"
