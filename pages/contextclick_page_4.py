from .base_page import BasePage
from elements.web_element import WebElement
from selenium.webdriver import ActionChains


class ContextClickPage(BasePage):
    UNIQUE_ELEMENT = "hot-spot"
    CONTEXT_CLICK_AREA = "hot-spot"

    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser
        self.page_name = "Context Click"
        self.unique_element = WebElement(self.browser, self.UNIQUE_ELEMENT)
        self.context_click_area = WebElement(self.browser, self.CONTEXT_CLICK_AREA)


    def right_click_area(self):
        ActionChains(self.browser.driver).context_click(self.context_click_area.wait_for_presence()).perform()