from pages.slider_page_5 import SliderPage

SLIDER_PAGE_URL = "https://the-internet.herokuapp.com/horizontal_slider"


def test_actions(browser):
    slider_page = SliderPage(browser)

    browser.get(SLIDER_PAGE_URL)
    slider_page.wait_for_open()

    assert slider_page.check_slider_behaviour_is_correct(), \
        "Поведение слайдера некорректно"
