from src.base.base_element import BaseElement
from src.base.base_page import BasePage
from src.config.links import Links


class OpenNewAccountPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

        # Page URL
        self.PAGE_URL = Links.OPEN_NEW_ACCOUNT_PAGE

        # Dropdowns
        self.account_type_dropdown = BaseElement(driver, "//select[@id='type']")
        self.from_account_dropdown = BaseElement(driver, "//select[@id='fromAccountId']")

        # Buttons
        self.open_account_button = BaseElement(driver, "//input[@class='button']")

        # Links
        self.new_account_id_link = BaseElement(driver, "//*[@id='newAccountId']")

        # Texts
        self.account_opened_text = BaseElement(driver, "//*[contains (text(), 'Account Opened!')]")
