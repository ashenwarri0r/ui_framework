from pages.hovers_page_6 import HoversPage
import pytest

HOVERS_PAGE_URL = "https://the-internet.herokuapp.com/hovers"
BASE_USER_LINK = "https://the-internet.herokuapp.com/users/"


@pytest.mark.parametrize("user_id", [1, 2, 3])
def test_hovers_page(browser, user_id):
    hovers_page = HoversPage(browser)

    browser.get(HOVERS_PAGE_URL)
    hovers_page.wait_for_open()
    hovers_page.hover_avatar(user_id)
    user_name = hovers_page.get_username(user_id)
    user_link = hovers_page.get_profile_link(user_id)
    assert user_name == f"name: user{user_id}" and user_link == f"{BASE_USER_LINK}{user_id}", \
        (f"Ожидаемое имя пользователя: name: user{user_id}, фактическое: {user_name}\n"
         f"Ожидаемая ссылка пользователя: {BASE_USER_LINK}{user_id}, фактическая: {user_link}")

    hovers_page.go_to_user_profile(user_id)
    assert browser.current_url == f"{BASE_USER_LINK}{user_id}", \
        (f"Ожидаемый адрес страницы: {BASE_USER_LINK}{user_id}\n"
         f"Фактический адрес страницы: {browser.current_url}")

    browser.back()
    hovers_page.wait_for_open()
