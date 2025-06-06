import logging
import time
import pyautogui
from logger.logger import Logger


class PyAutogui:
    @staticmethod
    def upload_file_pyatogui(file_path: str) -> None:
        Logger.info("Handle file dialog window for uploading file")
        time.sleep(2)

        logging.debug(f"Write '{file_path}' into search field of dialog window")
        pyautogui.typewrite(file_path)
        logging.debug("Press Enter")
        pyautogui.hotkey('enter')

        time.sleep(2)
