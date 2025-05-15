from .base_page import BasePage
from elements.web_element import WebElement
from selenium.webdriver import Keys, ActionChains


class SliderPage(BasePage):
    UNIQUE_ELEMENT = "range"
    SLIDER = "//input"
    SLIDER_VALUE = "range"

    def __init__(self, browser):
        super().__init__(browser)
        self.page_name = "HorizontalSlider"
        self.unique_element = WebElement(self.browser, self.UNIQUE_ELEMENT)
        self.slider = WebElement(self.browser, self.SLIDER)
        self.slider_value = WebElement(self.browser, self.SLIDER_VALUE)

    def move_slider(self, number: int):
        self.slider.click()

        direction = Keys.ARROW_RIGHT if number > 0 else Keys.ARROW_LEFT

        for _ in range(abs(number)):
            ActionChains(self.browser.driver).key_down(direction).perform()

    def get_slider_value(self):
        self.slider_value.wait_for_visible()
        return float(self.slider_value.get_text())
