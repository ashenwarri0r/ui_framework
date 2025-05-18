import pytest
from selenium.webdriver import Chrome
from browser.browser import Browser
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--headless=new")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

@pytest.fixture(scope="function")
def browser():
    driver = Chrome(options=options)
    browser = Browser(driver)
    yield browser
    browser.quit()
