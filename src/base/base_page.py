from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from src.base.base_element import BaseElement


class BasePage:
    def __init__(self, driver):
        self.driver = driver

        # Links
        self.open_new_account_link = BaseElement(driver, "//*[@id='leftPanel']//a[text()='Open New Account']")
        self.accounts_overview_link = BaseElement(driver, "//*[@id='leftPanel']//a[text()='Accounts Overview']")
        self.transfer_funds_link = BaseElement(driver, "//*[@id='leftPanel']//a[text()='Transfer Funds']")
        self.bill_pay_link = BaseElement(driver, "//*[@id='leftPanel']//a[text()='Bill Pay']")
        self.find_transactions_link = BaseElement(driver, "//*[@id='leftPanel']//a[text()='Find Transactions']")
        self.update_contact_info_link = BaseElement(driver,
                                                    "//*[@id='leftPanel']//a[text()='Update Contact Info']")
        self.request_loan_link = BaseElement(driver, "//*[@id='leftPanel']//a[text()='Request Loan']")
        self.log_out_link = BaseElement(driver, "//*[@id='leftPanel']//a[text()='Log Out']")
        self.contact_button = BaseElement(driver, "//*[@class='contact']")
        self.about_us_button = BaseElement(driver, "//*[@class='aboutus']")
        self.home_button = BaseElement(driver, "//*[@class='home']")
        self.register_link = BaseElement(driver, "//*[@id='loginPanel']//*[contains (@href, 'register')]")
        self.forgot_login_link = BaseElement(driver, "//*[@id='loginPanel']//*[contains (@href, 'lookup')]")

        # Texts
        self.greeting_text = BaseElement(driver, "//div[@id='leftPanel']/p")

    def open_page(self) -> None:
        self.driver.get(self.PAGE_URL)

    def get_current_url(self) -> str:
        return self.driver.current_url

    def is_opened(self) -> None:
        expected_url = self.PAGE_URL
        current_url = self.driver.current_url
        assert expected_url in current_url, (f"Expected '{expected_url}' URL, but got "
                                             f"'{current_url}'.")
