from src.base.base_element import BaseElement
from src.base.base_page import BasePage
from src.config.links import Links


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

        # Errors
        self.error_text = BaseElement(driver, "//*[@class='error']")

    PAGE_URL = Links.LOGIN_PAGE
