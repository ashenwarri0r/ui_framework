from .base_page import BasePage
from elements.web_element import WebElement


class DynamicPage(BasePage):
    UNIQUE_ELEMENT = "//*[text()='Dynamic Content']"
    IMAGE_1 = "(//*[@class='large-2 columns'])[1]/img"
    IMAGE_2 = "(//*[@class='large-2 columns'])[2]/img"
    IMAGE_3 = "(//*[@class='large-2 columns'])[3]/img"

    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser
        self.unique_element = WebElement(self.browser, self.UNIQUE_ELEMENT)
        self.image_1 = WebElement(self.browser, self.IMAGE_1)
        self.image_2 = WebElement(self.browser, self.IMAGE_2)
        self.image_3 = WebElement(self.browser, self.IMAGE_3)

    def refresh_until_images_match(self):
        refresh_count = 0
        while True:
            img_1 = self.image_1.wait_for_visible().get_attribute('src')
            img_2 = self.image_2.wait_for_visible().get_attribute('src')
            img_3 = self.image_3.wait_for_visible().get_attribute('src')
            if img_1 == img_2 or img_1 == img_3 or img_2 == img_3:
                break
            self.browser.refresh_page()
            refresh_count += 1
        return refresh_count
