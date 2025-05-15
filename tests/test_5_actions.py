from pages.slider_page_5 import SliderPage
from random import randint

SLIDER_PAGE_URL = "https://the-internet.herokuapp.com/horizontal_slider"
number = randint(-4, 4)
INITIAL_VALUE = 2.5
EXPECTED_VALUE = INITIAL_VALUE + number * 0.5


def test_actions(browser):
    slider_page = SliderPage(browser)

    browser.get(SLIDER_PAGE_URL)
    slider_page.wait_for_open()
    slider_page.move_slider(number)

    assert slider_page.get_slider_value() == EXPECTED_VALUE, \
        (f"Ожидаемое значение слайдера: {EXPECTED_VALUE}"
         f"Фактическое значение слайдера: {slider_page.get_slider_value()}")
