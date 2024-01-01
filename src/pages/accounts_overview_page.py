from src.base.base_element import BaseElement
from src.base.base_page import BasePage
from src.config.links import Links


class AccountsOverviewPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

        # Page URL
        self.PAGE_URL = Links.ACCOUNTS_OVERVIEW_PAGE

        # Table columns
        self.account_id = BaseElement(driver, "//tbody/tr/td[1]")
        self.balance = BaseElement(driver, "//tbody/tr/td[2]")
        self.available_amount = BaseElement(driver, "//tbody/tr/td[3]")

        # Links
        self.account_id_link = BaseElement(driver, "//a[contains (@href, 'activity.htm')]")
