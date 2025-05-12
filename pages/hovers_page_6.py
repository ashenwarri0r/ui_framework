from elements.label import Label
from .base_page import BasePage
from elements.web_element import WebElement
from selenium.webdriver import ActionChains


class HoversPage(BasePage):
    UNIQUE_ELEMENT = "//*[contains(text(), 'Hovers')]"
    USER_NAME = "//*[contains(text(), 'name:')]"
    AVATAR_TEMPLATE = "//div[@class='figure'][{0}]/img"

    def __init__(self, browser):
        super().__init__(browser)
        self.unique_element = Label(self.browser, self.UNIQUE_ELEMENT)

    def hover_avatar(self, user_id: int) -> None:
        user_avatar_locator = self.AVATAR_TEMPLATE.format(user_id)
        user_avatar = WebElement(self.browser, user_avatar_locator)

        ActionChains(self.driver).move_to_element(user_avatar.wait_for_visible()).perform()

    def get_username(self, user_id: int) -> str:
        user_name_locator = f"//*[contains(text(), 'name: user{user_id}')]"
        user_name = Label(self.browser, user_name_locator)
        user_name.wait_for_visible()
        return user_name.get_text()

    def get_profile_link(self, user_id: int) -> str:
        view_profile_locator = f"//*[contains(text(), 'name: user{user_id}')]/../a"
        view_profile = WebElement(self.browser, view_profile_locator)
        view_profile.wait_for_visible()
        return view_profile.get_attribute("href")

    def go_to_user_profile(self, user_id: int) -> None:
        view_profile_locator = f"//*[contains(text(), 'name: user{user_id}')]/../a"
        view_profile = WebElement(self.browser, view_profile_locator)
        view_profile.wait_for_clickable()
        view_profile.click()