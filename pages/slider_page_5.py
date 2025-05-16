from .base_page import BasePage
from elements.web_element import WebElement
from selenium.webdriver import Keys, ActionChains
import random


class SliderPage(BasePage):
    UNIQUE_ELEMENT = "content"
    SLIDER = "//input"
    SLIDER_VALUE = "range"

    def __init__(self, browser):
        super().__init__(browser)
        self.page_name = "HorizontalSlider"
        self.unique_element = WebElement(self.browser, self.UNIQUE_ELEMENT)
        self.slider = WebElement(self.browser, self.SLIDER)
        self.slider_value = WebElement(self.browser, self.SLIDER_VALUE)

    def click_slider(self):
        self.slider.wait_for_clickable()
        self.slider.click()

    def get_slider_value(self):
        self.slider_value.wait_for_visible()
        return float(self.slider_value.get_text())

    def check_slider_behaviour_is_correct(self):
        min_value = float(self.slider.get_attribute("min"))
        max_value = float(self.slider.get_attribute("max"))
        step = float(self.slider.get_attribute("step"))

        self.click_slider()
        initial_value = float(self.get_slider_value())

        if random.random() < 0.5:
            direction = Keys.ARROW_RIGHT
            max_steps = int((max_value - initial_value) / step)
        else:
            direction = Keys.ARROW_LEFT
            max_steps = int((initial_value - min_value) / step)

        steps = random.randint(1, max_steps - 1)

        for _ in range(steps):
            ActionChains(self.browser.driver).key_down(direction).perform()

        step_change = steps * step
        expected_value = initial_value + step_change if direction == Keys.ARROW_RIGHT else initial_value - step_change

        return float(self.get_slider_value()) == round(expected_value, 1)
