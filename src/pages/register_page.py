from src.base.base_element import BaseElement
from src.base.base_page import BasePage
from src.config.links import Links
from src.utils.data_generator import generated_data


class RegisterPage(BasePage):
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
        self.welcome_username_text = BaseElement(driver, "//h1[contains(text(), 'Welcome')]")

        # Lists
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

    def new_registration(self):
        new_user = next(generated_data())
        self.first_name_field.send_text(new_user.first_name)
        self.last_name_field.send_text(new_user.last_name)
        self.address_field.send_text(new_user.address)
        self.city_field.send_text(new_user.city)
        self.state_field.send_text(new_user.state)
        self.zip_code_field.send_text(new_user.zip_code)
        self.phone_number_field.send_text(new_user.phone_number)
        self.ssn_field.send_text(new_user.ssn)
        self.username_field.send_text(new_user.username)
        self.password_field.send_text(new_user.password)
        self.confirm_password_field.send_text(new_user.password)
        return new_user

    def repeat_registration(self, user):
        self.first_name_field.send_text(user.first_name)
        self.last_name_field.send_text(user.last_name)
        self.address_field.send_text(user.address)
        self.city_field.send_text(user.city)
        self.state_field.send_text(user.state)
        self.zip_code_field.send_text(user.zip_code)
        self.phone_number_field.send_text(user.phone_number)
        self.ssn_field.send_text(user.ssn)
        self.username_field.send_text(user.username)
        self.password_field.send_text(user.password)
        self.confirm_password_field.send_text(user.password)

    def missmatch_pass_registration(self):
        new_user = next(generated_data())
        self.first_name_field.send_text(new_user.first_name)
        self.last_name_field.send_text(new_user.last_name)
        self.address_field.send_text(new_user.address)
        self.city_field.send_text(new_user.city)
        self.state_field.send_text(new_user.state)
        self.zip_code_field.send_text(new_user.zip_code)
        self.phone_number_field.send_text(new_user.phone_number)
        self.ssn_field.send_text(new_user.ssn)
        self.username_field.send_text(new_user.username)
        self.password_field.send_text(new_user.password)
        self.confirm_password_field.send_text("somerandompassword_823!")
        return new_user

    def clear_fields(self):
        self.first_name_field.clear_contents()
        self.last_name_field.clear_contents()
        self.address_field.clear_contents()
        self.city_field.clear_contents()
        self.state_field.clear_contents()
        self.zip_code_field.clear_contents()
        self.phone_number_field.clear_contents()
        self.ssn_field.clear_contents()
        self.username_field.clear_contents()

    def re_generate_username(self, user):
        # Processing the case of existing username
        while True:
            if self.username_error.is_invisible():
                break
            else:
                self.clear_fields()
                user = self.new_registration()
                self.register_button.click()
        return user


