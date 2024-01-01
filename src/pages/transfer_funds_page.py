from src.base.base_page import BasePage
from src.config.links import Links


class TransferFundsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

        # Page URL
        self.PAGE_URL = Links.TRANSFER_FUNDS_PAGE
