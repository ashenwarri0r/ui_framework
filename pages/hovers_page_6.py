from .base_page import BasePage
from elements.web_element import WebElement
from selenium.webdriver import ActionChains


class HoversPage(BasePage):
    UNIQUE_ELEMENT = "//*[contains(text(), 'Hovers')]"
    USER_1_AVATAR = "(//div[@class='figure']/img)[1]"
    USER_2_AVATAR = "(//div[@class='figure']/img)[2]"
    USER_3_AVATAR = "(//div[@class='figure']/img)[3]"
    VIEW_PROFILE = "//a[contains(text(), 'View profile')]"
    USER_NAME = "//*[contains(text(), 'name:')]"

    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser
        self.driver = browser.driver
        self.unique_element = WebElement(self.browser, self.UNIQUE_ELEMENT)
        self.user_1_avatar = WebElement(self.browser, self.USER_1_AVATAR)
        self.user_2_avatar = WebElement(self.browser, self.USER_2_AVATAR)
        self.user_3_avatar = WebElement(self.browser, self.USER_3_AVATAR)
        self.view_profile = WebElement(self.browser, self.VIEW_PROFILE)
        self.user_name = WebElement(self.browser, self.USER_NAME)

    def hover_avatar(self, user: int) -> tuple[str, str]:
        if user == 1:
            self.user_1_avatar.wait_for_visible()
            ActionChains(self.driver).move_to_element(self.user_1_avatar.native_element).perform()
        elif user == 2:
            self.user_2_avatar.wait_for_visible()
            ActionChains(self.driver).move_to_element(self.user_2_avatar.native_element).perform()
        elif user == 3:
            self.user_3_avatar.wait_for_visible()
            ActionChains(self.driver).move_to_element(self.user_3_avatar.native_element).perform()
        else:
            raise ValueError("Неверный user, доступны значения от 1 до 3")
        self.view_profile.wait_for_presence()
        self.user_name.wait_for_visible()
        return self.user_name.get_text(), self.view_profile.get_attribute('href')

    def go_to_user_profile(self):
        self.view_profile.wait_for_clickable()
        self.view_profile.click()