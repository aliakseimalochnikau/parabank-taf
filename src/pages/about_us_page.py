from src.base.base_page import BasePage
from src.config.links import Links


class AboutUsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    PAGE_URL = Links.ABOUT_US_PAGE
