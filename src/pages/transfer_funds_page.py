from src.base.base_element import BaseElement
from src.base.base_page import BasePage
from src.config.links import Links


class TransferFundsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

        # Page URL
        self.PAGE_URL = Links.TRANSFER_FUNDS_PAGE

        # Fields
        self.amount_field = BaseElement(driver, "//*[@id='amount']")
        self.from_account_dropdown = BaseElement(driver, "//*[@id='fromAccountId']")
        self.to_account_dropdown = BaseElement(driver, "//*[@id='toAccountId']")

        # Buttons
        self.transfer_button = BaseElement(driver, "//*[@type='submit']")

        # Texts
        self.transfer_complete_text = BaseElement(driver, "//*[contains(text(), 'Transfer Complete!')]")

        # Errors
        self.amount_error = BaseElement(driver, "//*[@id='amount.errors']")
