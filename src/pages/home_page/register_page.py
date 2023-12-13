from src.base.base_element import BaseElement
from src.config.links import Links
from src.pages.home_page.home_page import HomePage


class RegisterPage(HomePage):
    def __init__(self, driver):
        super().__init__(driver)

        # Fields and buttons
        self.first_name_field = BaseElement(driver, "//*[@id='customer.firstName']")
        self.last_name_field = BaseElement(driver, "//*[@id='customer.lastName']")
        self.address_field = BaseElement(driver, "//*[@id='customer.address.street']")
        self.city_field = BaseElement(driver, "//*[@id='customer.address.city']")
        self.state_field = BaseElement(driver, "//*[@id='customer.address.state']")
        self.zip_code_field = BaseElement(driver, "//*[@id='customer.address.zipCode']")
        self.phone_number_field = BaseElement(driver, "//*[@id='customer.phoneNumber']")
        self.ssn_field = BaseElement(driver, "//*[@id='customer.ssn']")
        self.username_field = BaseElement(driver, "//*[@id='customer.username']")
        self.password_field = BaseElement(driver, "//*[@id='customer.password']")
        self.confirm_password_field = BaseElement(driver, "//*[@id='repeatedPassword']")
        self.register_button = BaseElement(driver, "//*[@value='Register']")

        # Texts
        self.welcome_username_text = BaseElement(driver, "//*[@class='title']")

        # Lists
        self.errors_list = BaseElement(driver, "//*[@class='error']")
        self.input_field_list = BaseElement(driver, "//table//*[@class='input']")

        # Errors
        self.first_name_error = BaseElement(driver, "//*[@id='customer.firstName.errors']")
        self.last_name_error = BaseElement(driver, "//*[@id='customer.lastName.errors']")
        self.address_error = BaseElement(driver, "//*[@id='customer.address.street.errors']")
        self.city_error = BaseElement(driver, "//*[@id='customer.address.city.errors']")
        self.state_error = BaseElement(driver, "//*[@id='customer.address.state.errors']")
        self.zip_code_error = BaseElement(driver, "//*[@id='customer.address.zipCode.errors']")
        self.ssn_error = BaseElement(driver, "//*[@id='customer.ssn.errors']")
        self.username_error = BaseElement(driver, "//*[@id='customer.username.errors']")
        self.password_error = BaseElement(driver, "//*[@id='customer.password.errors']")
        self.confirm_password_error = BaseElement(driver, "//*[@id='repeatedPassword.errors']")

    PAGE_URL = Links.REGISTER_PAGE
