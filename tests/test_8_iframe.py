from pages.iframe_page_8 import IFramePage, NestedFramePage

IFRAME_PAGE_LINK = "https://demoqa.com/frames"
PARENT_FRAME_EXP_TEXT = "Parent frame"
CHILD_FRAME_EXP_TEXT = "Child Iframe"


def test_iframes(browser):
    iframe_page = IFramePage(browser)
    nested_frame_page = NestedFramePage(browser)

    browser.get(IFRAME_PAGE_LINK)
    iframe_page.wait_for_open()
    iframe_page.go_to_nested_frames()
    nested_frame_page.wait_for_open()
    parent_text = nested_frame_page.get_parent_frame_text()
    child_text = nested_frame_page.get_child_frame_text()
    assert parent_text == PARENT_FRAME_EXP_TEXT and child_text == CHILD_FRAME_EXP_TEXT, \
        (f"Ожидаемые тексты фреймов: {PARENT_FRAME_EXP_TEXT}, {CHILD_FRAME_EXP_TEXT}"
         f"Фактические тексты фреймов: {parent_text}, {child_text}") \

    nested_frame_page.go_to_frames()
    iframe_page.wait_for_open()
    frame_1_text = iframe_page.get_frame1_text()
    frame_2_text = iframe_page.get_frame2_text()
    assert frame_1_text == frame_2_text, \
        (f"Ожидалось, что тексты фреймов будут совпадать"
         f"Фактически текст фрейма1: {frame_1_text} и фрейма2: {frame_2_text}")
