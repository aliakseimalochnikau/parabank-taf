from src.base.base_element import BaseElement
from src.base.base_page import BasePage
from src.config.links import Links


class CustomerLookupPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

        # Fields and buttons
        self.first_name_field = BaseElement(driver, "//*[@id='firstName']")
        self.last_name_field = BaseElement(driver, "//*[@id='lastName']")
        self.address_field = BaseElement(driver, "//*[@id='address.street']")
        self.city_field = BaseElement(driver, "//*[@id='address.city']")
        self.state_field = BaseElement(driver, "//*[@id='address.state']")
        self.zip_code_field = BaseElement(driver, "//*[@id='address.zipCode']")
        self.ssn_field = BaseElement(driver, "//*[@id='ssn']")
        self.find_my_login_info_button = BaseElement(driver, "//*[@value='Find My Login Info']")

    PAGE_URL = Links.CUSTOMER_LOOKUP_PAGE
