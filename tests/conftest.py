import pytest
from selenium.webdriver import Chrome
from browser.browser import Browser


@pytest.fixture(scope="function")
def browser():
    driver = Chrome()
    browser = Browser(driver)
    yield browser
    browser.quit()
