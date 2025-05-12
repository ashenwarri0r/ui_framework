from pages.dynamic_page_9 import DynamicPage

DYNAMIC_PAGE_URL = "http://the-internet.herokuapp.com/dynamic_content"

def test_dynamic_content(browser):
    dynamic_page = DynamicPage(browser)

    browser.get(DYNAMIC_PAGE_URL)

    refreshes_needed = dynamic_page.refresh_until_images_match()
    print(f"Понадобилось обновлений: {refreshes_needed}")

    assert refreshes_needed < 101, \
        "За 100 обновлений страницы изображения так и не совпали"
