from src.base.base_element import BaseElement
from src.base.base_page import BasePage
from src.config.links import Links


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

        # Fields and buttons
        self.username_field = BaseElement(driver, "//*[@name='username']")
        self.password_field = BaseElement(driver, "//*[@name='password']")
        self.log_in_button = BaseElement(driver, "//*[@type='submit']")
        self.contact_button = BaseElement(driver, "//*[@class='contact']")
        self.about_us_button = BaseElement(driver, "//*[@class='aboutus']")
        self.home_button = BaseElement(driver, "//*[@class='home']")

        # Links
        self.register_link = BaseElement(driver, "//*[contains(text(), 'Register')]")
        self.forgot_login_link = BaseElement(driver, "//*[contains(text(), 'Forgot login')]")

    PAGE_URL = Links.HOME_PAGE
