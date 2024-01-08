from src.base.base_element import BaseElement
from src.base.base_page import BasePage
from src.config.links import Links
from src.utils.data_generator import generated_data


class BillPayPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

        # Page URL
        self.PAGE_URL = Links.BILL_PAY_PAGE

        # Fields
        self.payee_name_field = BaseElement(driver, "//*[@name='payee.name']")
        self.address_field = BaseElement(driver, "//*[@name='payee.address.street']")
        self.city_field = BaseElement(driver, "//*[@name='payee.address.city']")
        self.state_field = BaseElement(driver, "//*[@name='payee.address.state']")
        self.zip_code_field = BaseElement(driver, "//*[@name='payee.address.zipCode']")
        self.phone_field = BaseElement(driver, "//*[@name='payee.phoneNumber']")
        self.account_field = BaseElement(driver, "//*[@name='payee.accountNumber']")
        self.verify_account_field = BaseElement(driver, "//*[@name='verifyAccount']")
        self.amount_field = BaseElement(driver, "//*[@name='amount']")

        # Dropdowns
        self.from_account_dropdown = BaseElement(driver, "//*[@name='fromAccountId']")

        # Buttons
        self.send_payment_button = BaseElement(driver, "//*[@value='Send Payment']")

        # Texts
        self.payment_complete_text = BaseElement(driver, "//*[text()='Bill Payment Complete']")

        # Errors
        self.errors_list = BaseElement(driver, "//*[contains(text(), 'is required')]")

        self.payee_name_error = BaseElement(driver, "//*[text()='Payee name is required.']")
        self.address_error = BaseElement(driver, "//*[text()='Address is required.']")
        self.city_error = BaseElement(driver, "//*[text()='City is required.']")
        self.state_error = BaseElement(driver, "//*[text()='State is required.']")
        self.zip_code_error = BaseElement(driver, "//*[text()='Zip Code is required.']")
        self.phone_error = BaseElement(driver, "//*[text()='Phone number is required.']")
        self.account_error = BaseElement(driver, "(//*[text()='Account number is required.'])[1]")
        self.verify_account_error = BaseElement(driver, "(//*[text()='Account number is required.'])[2]")
        self.amount_error = BaseElement(driver, "//*[contains(text(), 'The amount cannot be empty.')]")
        self.account_mismatch_error = BaseElement(driver, "//*[text()='The account numbers do not match.']")

    def _fill_payee_fields(self, user, mismatch_account=None):
        self.payee_name_field.send_text(f"{user.first_name} {user.last_name}")
        self.address_field.send_text(user.address)
        self.city_field.send_text(user.city)
        self.state_field.send_text(user.state)
        self.zip_code_field.send_text(user.zip_code)
        self.phone_field.send_text(user.phone_number)

        self.account_field.send_text("50240")
        if mismatch_account:
            self.verify_account_field.send_text(mismatch_account)
        else:
            self.verify_account_field.send_text("50240")

    def enter_payee_info(self):
        new_user = next(generated_data())
        self._fill_payee_fields(new_user)
        return new_user

    def missmatch_account_payee(self):
        new_user = next(generated_data())
        self._fill_payee_fields(new_user, mismatch_account="25991")
        return new_user
