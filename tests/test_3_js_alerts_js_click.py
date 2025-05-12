from pages.js_alerts_page_2 import JavascriptAlertsPage
from faker import Faker
fake = Faker()


JS_PAGE_URL = "https://the-internet.herokuapp.com/javascript_alerts"
ALERT_EXPECTED_TEXT = "You successfully clicked an alert"
CONFIRM_EXPECTED_TEXT = "You clicked: Ok"
PROMPT_INPUT = fake.text(15)
PROMPT_EXPECTED_TEXT = f"You entered: {PROMPT_INPUT}"

def test_js_alerts_js_click(browser):
    js_alerts_page = JavascriptAlertsPage(browser)

    browser.get(JS_PAGE_URL)
    js_alerts_page.wait_for_open()
    js_alerts_page.click_js_alert(js=True)
    browser.wait_alert_present()
    browser.accept_alert()
    assert js_alerts_page.get_result_text() == ALERT_EXPECTED_TEXT,\
        (f"Ожидаемый текст: {ALERT_EXPECTED_TEXT}"
         f"Фактический текст: {js_alerts_page.get_result_text()}")

    js_alerts_page.click_js_confirm(js=True)
    browser.wait_alert_present()
    browser.accept_alert()
    assert js_alerts_page.get_result_text() == CONFIRM_EXPECTED_TEXT, \
        (f"Ожидаемый текст: {CONFIRM_EXPECTED_TEXT}"
         f"Фактический текст: {js_alerts_page.get_result_text()}")

    js_alerts_page.click_js_prompt(js=True)
    browser.wait_alert_present()
    browser.send_keys_alert(PROMPT_INPUT)
    browser.accept_alert()
    assert js_alerts_page.get_result_text() == PROMPT_EXPECTED_TEXT, \
        (f"Ожидаемый текст: {PROMPT_EXPECTED_TEXT}"
         f"Фактический текст: {js_alerts_page.get_result_text()}")
