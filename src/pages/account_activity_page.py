from src.base.base_element import BaseElement
from src.base.base_page import BasePage
from src.config.links import Links


class AccountActivityPage(BasePage):
    def __init__(self, driver, account_id):
        super().__init__(driver)
        self.account_id = account_id

        # Page URL
        self.PAGE_URL = f"{Links.ACCOUNT_ACTIVITY_PAGE}{account_id}"

        # Texts
        self.account_number_text = BaseElement(driver, "//*[@id='accountId']")
        self.account_type_text = BaseElement(driver, "//*[@id='accountType']")
        self.account_balance_text = BaseElement(driver, "//*[@id='balance']")
        self.account_available_text = BaseElement(driver, "//*[@id='availableBalance']")

        # Add remaining locators

