from elements.label import Label
from .base_page import BasePage
from elements.web_element import WebElement
from selenium.webdriver import ActionChains


class HoversPage(BasePage):
    UNIQUE_ELEMENT = "//*[contains(text(), 'Hovers')]"
    USER_NAME_TEMPLATE = "//*[contains(text(), 'name: user{0}')]"
    AVATAR_TEMPLATE = "//div[contains(@class,'figure')][{0}]/img"
    VIEW_PROFILE_TEMPLATE = "//*[contains(text(), 'name: user{0}')]/../a"

    def __init__(self, browser):
        super().__init__(browser)
        self.unique_element = Label(self.browser, self.UNIQUE_ELEMENT)

    def hover_avatar(self, user_id: int) -> None:
        user_avatar_locator = self.AVATAR_TEMPLATE.format(user_id)
        user_avatar = WebElement(self.browser, user_avatar_locator)

        ActionChains(self.driver).move_to_element(user_avatar.wait_for_visible()).perform()

    def get_username(self, user_id: int) -> str:
        user_name_locator = self.USER_NAME_TEMPLATE.format(user_id)
        user_name = Label(self.browser, user_name_locator)
        user_name.wait_for_visible()
        return user_name.get_text()

    def get_profile_link(self, user_id: int) -> str:
        view_profile_locator = self.VIEW_PROFILE_TEMPLATE.format(user_id)
        view_profile = WebElement(self.browser, view_profile_locator)
        view_profile.wait_for_visible()
        return view_profile.get_attribute("href")

    def go_to_user_profile(self, user_id: int) -> None:
        view_profile_locator = self.VIEW_PROFILE_TEMPLATE.format(user_id)
        view_profile = WebElement(self.browser, view_profile_locator)
        view_profile.click()
