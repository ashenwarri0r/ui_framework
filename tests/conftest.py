import pytest
from selenium.webdriver import Chrome
from browser.browser import Browser
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--headless=new")

@pytest.fixture(scope="function")
def browser():
    driver = Chrome(options=options)
    browser = Browser(driver)
    yield browser
    browser.quit()
