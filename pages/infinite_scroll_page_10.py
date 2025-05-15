from selenium.webdriver import Keys
from .base_page import BasePage
from elements.web_element import WebElement
from elements.multi_web_element import MultiWebElement
from selenium.webdriver.common.action_chains import ActionChains
from logger.logger import Logger
import time


class InfiniteScrollPage(BasePage):
    UNIQUE_ELEMENT = "//*[text()='Infinite Scroll']"
    PARAGRAPH = "//*[contains(@class,'jscroll-added')][{}]"
    BODY = "//body"

    def __init__(self, browser):
        super().__init__(browser)
        self.actions = ActionChains(self.browser.driver)
        self.unique_element = WebElement(self.browser, self.UNIQUE_ELEMENT)
        self.paragraphs = MultiWebElement(
            self.browser, self.PARAGRAPH, description="Infinite Scroll Page -> same paragraphs")
        self.body = WebElement(self.browser, self.BODY)

    def scroll_until_number_of_paragraphs(self, age, timeout=20):
        start_time = time.time()
        last_count = 0
        try:
            while time.time() - start_time < timeout:
                current_elements = self.paragraphs
                current_count = len(list(current_elements))
                if current_count == age:
                    break
                if current_count == last_count:
                    self.actions.send_keys(Keys.PAGE_DOWN).perform()
                last_count = current_count
        finally:
            self.actions.key_up(Keys.PAGE_DOWN).perform()

        return len(list(current_elements))
