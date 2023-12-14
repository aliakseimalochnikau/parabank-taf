from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15, 1)

    def open_page(self) -> None:
        self.driver.get(self.PAGE_URL)

    def get_current_url(self) -> str:
        return self.driver.current_url

    def is_opened(self) -> None:
        self.wait.until(EC.url_to_be(self.PAGE_URL))




