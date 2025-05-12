from enum import StrEnum
from selenium import webdriver
from logger.logger import Logger
from selenium.webdriver.remote.webdriver import WebDriver

class AvailableDriverNames(StrEnum):
    CHROME = "chrome"

class BrowserFactory:
    @staticmethod
    def get_driver(
            driver_name: AvailableDriverNames = AvailableDriverNames.CHROME,
            options: list[str] = None
    ) -> WebDriver:
        if options is None:
            options = []

        Logger.info(f"Start webdriver '{driver_name}' with options '{options}'")
        if driver_name == AvailableDriverNames.CHROME:
            chrome_options = webdriver.ChromeOptions()

            for option in options:
                chrome_options.add_argument(option)

                driver = webdriver.Chrome(options=chrome_options)
        else:
            raise NotImplementedError(f"'{driver_name}' is not implemented")
        return driver