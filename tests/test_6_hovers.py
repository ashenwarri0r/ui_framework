from selenium import webdriver
from browser.browser import Browser
from pages.hovers_page_6 import HoversPage
import pytest

HOVERS_PAGE_URL = "https://the-internet.herokuapp.com/hovers"
BASE_USER_LINK = "https://the-internet.herokuapp.com/users/"

@pytest.mark.parametrize("user_id", [1, 2, 3])
def test_hovers_page(user_id):
    browser = Browser(driver=webdriver.Chrome())
    hovers_page = HoversPage(browser)

    browser.get(HOVERS_PAGE_URL)
    hovers_page.wait_for_open()
    user_name, user_link = hovers_page.hover_avatar(1)
    assert user_name == "name: user1" and user_link == f"{BASE_USER_LINK}1", \
        (f"Ожидаемое имя пользователя: {"name: user1"}, фактическое: {user_name}"
         f"Ожидаемая ссылка пользователя: {BASE_USER_LINK}1, фактическая: {user_link}")

    hovers_page.go_to_user_profile()
    assert browser.driver.current_url == f"{BASE_USER_LINK}1", \
        (f"Ожидаемый адрес страницы: {BASE_USER_LINK}1"
         f"Фактический адрес страницы: {browser.driver.current_url}")

    browser.driver.back()
    hovers_page.wait_for_open()

    browser.driver.quit()