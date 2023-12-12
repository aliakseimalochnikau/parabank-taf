from src.base.base_element import BaseElement
from src.config.links import Links
from src.pages.home_page import HomePage


class LoginPage(HomePage):
    def __init__(self, driver):
        super().__init__(driver)

        self.internal_error = BaseElement(
            driver, "//*[contains(text(), 'internal error')]"
        )

        self.empty_field_error = BaseElement(
            driver, "//*[contains(text(), 'Please enter')]"
        )

    PAGE_URL = Links.LOGIN_PAGE
