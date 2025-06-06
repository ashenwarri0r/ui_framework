from elements.multi_web_element import MultiWebElement
from .base_page import BasePage
from elements.web_element import WebElement


class DynamicPage(BasePage):
    UNIQUE_ELEMENT = "//*[text()='Dynamic Content']"
    IMAGES = "(//*[@class='large-2 columns'])[{}]/img"

    def __init__(self, browser):
        super().__init__(browser)
        self.unique_element = WebElement(self.browser, self.UNIQUE_ELEMENT)
        self.images = MultiWebElement(self.browser, self.IMAGES,
                                      description="Dynamic page -> images for comparison")

    def refresh_until_images_match(self, max_refreshes):
        refresh_count = 0
        while refresh_count <= max_refreshes:
            all_src = [img.get_attribute('src') for img in self.images]
            if len(set(all_src)) == 1:
                return refresh_count
            self.browser.refresh_page()
            refresh_count += 1

        raise AssertionError(f"За {max_refreshes} обновлений страницы изображения не совпали")
