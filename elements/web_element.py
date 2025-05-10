from .base_element import BaseElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class WebElement(BaseElement):

    @property
    def native_element(self):
        return WebDriverWait(self.browser.driver, self.timeout).until(
            EC.presence_of_element_located(self.locator)
        )