from src.base.base_element import BaseElement
from src.base.base_page import BasePage
from src.config.links import Links


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

        self.username_field = BaseElement(
            driver, "//*[@name='username']"
        )

        self.password_field = BaseElement(
            driver, "//*[@name='password']"
        )

        self.log_in_button = BaseElement(
            driver, "//*[@type='submit']"
        )

    PAGE_URL = Links.HOME_PAGE



