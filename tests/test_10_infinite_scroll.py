from pages.infinite_scroll_page_10 import InfiniteScrollPage

INFINITE_SCROLL_PAGE_URL = "https://the-internet.herokuapp.com/infinite_scroll"
AGE_OF_THE_ENGINEER = 24

def test_infinite_scroll(browser):
    infinite_scroll_page = InfiniteScrollPage(browser)

    browser.get(INFINITE_SCROLL_PAGE_URL)
    infinite_scroll_page.wait_for_open()
    paragraphs_number = infinite_scroll_page.scroll_until_number_of_paragraphs(AGE_OF_THE_ENGINEER)
    assert paragraphs_number == AGE_OF_THE_ENGINEER, \
        (f"Ожидалось, что кол-во абзацев будет равно возрасту инженера: {AGE_OF_THE_ENGINEER}"
         f"Фактическое количество абзацев после прокрутки: {paragraphs_number}")
