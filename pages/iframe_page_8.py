from .base_page import BasePage
from elements.web_element import WebElement
from elements.button import Button


class IFramePage(BasePage):
    UNIQUE_ELEMENT = "//*[contains(@class, 'center') and text()='Frames']"
    NESTED_FRAMES = "//*[text()='Nested Frames']/.."
    FRAMES_TEXT = "//*[@id='sampleHeading']"
    FRAME_1 = "frame1"
    FRAME_2 = "frame2"

    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser
        self.unique_element = WebElement(self.browser, self.UNIQUE_ELEMENT)
        self.nested_frames_link = Button(self.browser, self.NESTED_FRAMES)
        self.frames_text = WebElement(self.browser, self.FRAMES_TEXT)
        self.frame1 = WebElement(self.browser, self.FRAME_1)
        self.frame2 = WebElement(self.browser, self.FRAME_2)


    def go_to_nested_frames(self):
        self.nested_frames_link.wait_for_presence()
        self.nested_frames_link.js_click()

    def get_frames_text(self) -> tuple:
        self.browser.switch_to_frame(self.frame1)
        frame_1_text = self.frames_text.wait_for_presence().text
        self.browser.switch_to_default_content()
        self.browser.switch_to_frame(self.frame2)
        frame_2_text = self.frames_text.wait_for_presence().text
        self.browser.switch_to_default_content()
        return frame_1_text, frame_2_text

class NestedFramePage(BasePage):
    UNIQUE_ELEMENT = "//*[contains(@class, 'center') and text()='Nested Frames']"
    FRAMES = "//*[text()='Frames']/.."
    PARENT_FRAME = "frame1"
    PARENT_TEXT = "//body"
    CHILD_FRAME = "//*[contains(@srcdoc, 'Child Iframe')]"
    CHILD_TEXT = "//p"

    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser
        self.unique_element = WebElement(self.browser, self.UNIQUE_ELEMENT)
        self.frames_link = Button(self.browser, self.FRAMES)
        self.parent_frame = WebElement(self.browser, self.PARENT_FRAME)
        self.child_frame = WebElement(self.browser, self.CHILD_FRAME)
        self.parent_text = WebElement(self.browser, self.PARENT_TEXT)
        self.child_text = WebElement(self.browser, self.CHILD_TEXT)

    def go_to_frames(self):
        self.frames_link.wait_for_presence()
        self.frames_link.js_click()

    def check_frame_text(self) -> tuple:
        self.browser.switch_to_frame(self.parent_frame)
        parent_text = self.parent_text.wait_for_presence().text
        self.browser.switch_to_frame(self.child_frame)
        child_text = self.child_text.wait_for_presence().text
        self.browser.switch_to_default_content()
        return parent_text, child_text