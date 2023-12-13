from src.base.base_element import BaseElement
from src.config.links import Links
from src.pages.home_page.home_page import HomePage


class LoginPage(HomePage):
    def __init__(self, driver):
        super().__init__(driver)

        # Errors
        self.error_text = BaseElement(driver, "//*[@class='error']")

    PAGE_URL = Links.LOGIN_PAGE
