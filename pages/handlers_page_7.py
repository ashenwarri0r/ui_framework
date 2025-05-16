from .base_page import BasePage
from elements.web_element import WebElement


class HandlersPage(BasePage):
    UNIQUE_ELEMENT = "//*[contains(text(), 'new window')]"
    NEW_WINDOW = "//*[contains(text(), 'Click')]"

    def __init__(self, browser):
        super().__init__(browser)
        self.unique_element = WebElement(self.browser, self.UNIQUE_ELEMENT)
        self.new_window = WebElement(self.browser, self.NEW_WINDOW)

    def click_new_window(self):
        self.new_window.click()


class NewWindowPage(BasePage):
    UNIQUE_ELEMENT = "//*[contains(text(), 'New Window')]"

    def __init__(self, browser):
        super().__init__(browser)
        self.unique_element = WebElement(self.browser, self.UNIQUE_ELEMENT)
