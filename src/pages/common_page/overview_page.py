from src.base.base_element import BaseElement
from src.config.links import Links
from src.pages.common_page.common_page import CommonPage


class AccountsOverviewPage(CommonPage):
    def __init__(self, driver):
        super().__init__(driver)

        self.greeting_text = BaseElement(
            driver, "//div[@id='leftPanel']/p"
        )

    PAGE_URL = Links.ACCOUNTS_OVERVIEW_PAGE
