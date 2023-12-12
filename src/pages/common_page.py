from src.base.base_element import BaseElement
from src.base.base_page import BasePage


class CommonPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

        self.open_new_account_link = BaseElement(
            driver, "//*[@id='leftPanel']//a[text()='Open New Account']"
        )

        self.accounts_overview_link = BaseElement(
            driver, "//*[@id='leftPanel']//a[text()='Accounts Overview']"
        )

        self.transfer_funds_link = BaseElement(
            driver, "//*[@id='leftPanel']//a[text()='Transfer Funds']"
        )

        self.bill_pay_link = BaseElement(
            driver, "//*[@id='leftPanel']//a[text()='Bill Pay']"
        )

        self.find_transactions_link = BaseElement(
            driver, "//*[@id='leftPanel']//a[text()='Find Transactions']"
        )

        self.update_contact_info_link = BaseElement(
            driver, "//*[@id='leftPanel']//a[text()='Update Contact Info']"
        )

        self.request_loan_link = BaseElement(
            driver, "//*[@id='leftPanel']//a[text()='Request Loan']"
        )

        self.log_out_link = BaseElement(
            driver, "//*[@id='leftPanel']//a[text()='Log Out']"
        )

        self.home_button = BaseElement(
            driver, "//*[contains(text(), 'home')]"
        )



