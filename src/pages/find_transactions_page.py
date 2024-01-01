from src.base.base_page import BasePage
from src.config.links import Links


class FindTransactionsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

        # Page URL
        self.PAGE_URL = Links.FIND_TRANSACTIONS_PAGE