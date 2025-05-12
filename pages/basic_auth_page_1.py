from .base_page import BasePage
from elements.web_element import WebElement


class BasicAuthPage(BasePage):
    UNIQUE_ELEMENT = "//*[contains(text(), 'Basic Auth')]"
    SUCCESSFUL_AUTH = "//*[contains(text(), 'Congratulations')]"

    def __init__(self, browser):
        super().__init__(browser)
        self.page_name = "Basic Auth"
        self.unique_element = WebElement(self.browser, self.UNIQUE_ELEMENT)
        self.success_message = WebElement(self.browser, self.SUCCESSFUL_AUTH,
                                          description="Basic Auth Page -> Success message")

    def successful_auth(self):
        self.success_message.wait_for_visible()
        return self.success_message.get_text()
