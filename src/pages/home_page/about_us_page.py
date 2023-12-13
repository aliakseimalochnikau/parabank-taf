from src.config.links import Links
from src.pages.home_page.home_page import HomePage


class AboutUsPage(HomePage):
    def __init__(self, driver):
        super().__init__(driver)

    PAGE_URL = Links.ABOUT_US_PAGE
