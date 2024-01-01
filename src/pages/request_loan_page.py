from src.base.base_page import BasePage
from src.config.links import Links


class RequestLoanPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

        # Page URL
        self.PAGE_URL = Links.REQUEST_LOAN_PAGE