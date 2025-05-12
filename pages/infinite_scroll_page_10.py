from selenium.webdriver import Keys
from .base_page import BasePage
from elements.web_element import WebElement
from selenium.webdriver.common.action_chains import ActionChains
import time


class InfiniteScrollPage(BasePage):
    UNIQUE_ELEMENT = "//*[text()='Infinite Scroll']"
    PARAGRAPH = "//*[@class='jscroll-added']"
    BODY = "//body"

    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser
        self.actions = ActionChains(self.browser.driver)
        self.unique_element = WebElement(self.browser, self.UNIQUE_ELEMENT)
        self.paragraph = WebElement(self.browser, self.PARAGRAPH)
        self.body = WebElement(self.browser, self.BODY)

    def scroll_until_number_of_paragraphs(self, age, timeout=20):
        start_time = time.time()
        last_count = 0
        try:
            while time.time() - start_time < timeout:
                current_elements = self.paragraph.wait_for_presence_all_elements()
                current_count = len(current_elements)
                if current_count >= age:
                    break
                if current_count == last_count:
                    self.actions.send_keys(Keys.PAGE_DOWN).perform()
                last_count = current_count
        finally:
            self.actions.key_up(Keys.PAGE_DOWN).perform()

        return len(self.paragraph.wait_for_presence_all_elements())