from .base_page import BasePage
from elements.web_element import WebElement
from elements.button import Button


class JavascriptAlertsPage(BasePage):
    UNIQUE_ELEMENT = "result"
    RESULT_FIELD = "result"
    JS_ALERT = "//*[@onclick='jsAlert()']"
    JS_CONFIRM = "//*[@onclick='jsConfirm()']"
    JS_PROMPT = "//*[@onclick='jsPrompt()']"

    def __init__(self, browser):
        super().__init__(browser)
        self.page_name = "JS Alerts"
        self.unique_element = WebElement(self.browser, self.UNIQUE_ELEMENT)
        self.result_field = WebElement(self.browser, self.RESULT_FIELD)
        self.js_alert_button = Button(self.browser, self.JS_ALERT)
        self.js_confirm_button = Button(self.browser, self.JS_CONFIRM)
        self.js_prompt_button = Button(self.browser, self.JS_PROMPT)

    # Опциональный параметр js позволяет вызвать JavaScript-click вместо обычного
    def click_js_alert(self, js=False):
        if js:
            self.js_alert_button.js_click()
        else:
            self.js_alert_button.click()

    def click_js_confirm(self, js=False):
        if not js:
            self.js_confirm_button.click()
        else:
            self.js_confirm_button.js_click()

    def click_js_prompt(self, js=False):
        if not js:
            self.js_prompt_button.click()
        else:
            self.js_prompt_button.js_click()

    def get_result_text(self):
        self.result_field.wait_for_visible()
        return self.result_field.get_text()
