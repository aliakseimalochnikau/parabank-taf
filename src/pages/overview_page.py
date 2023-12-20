from src.base.base_page import BasePage
from src.config.links import Links


class AccountsOverviewPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    PAGE_URL = Links.ACCOUNTS_OVERVIEW_PAGE
