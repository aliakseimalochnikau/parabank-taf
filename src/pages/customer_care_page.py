from src.base.base_element import BaseElement
from src.base.base_page import BasePage
from src.config.links import Links


class CustomerCarePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

        # Fields and buttons
        self.name_field = BaseElement(driver, "//*[@id='name']")
        self.email_field = BaseElement(driver, "//*[@id='email']")
        self.phone_field = BaseElement(driver, "//*[@id='phone']")
        self.message_field = BaseElement(driver, "//*[@id='message']")
        self.send_to_customer_care_button = BaseElement(driver, "//*[@value='Send to Customer Care']")

    PAGE_URL = Links.CUSTOMER_CARE_PAGE
