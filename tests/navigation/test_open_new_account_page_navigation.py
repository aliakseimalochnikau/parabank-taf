import allure
from src.config.data import ActiveUser
from src.pages.about_us_page import AboutUsPage
from src.pages.accounts_overview_page import AccountsOverviewPage
from src.pages.bill_pay_page import BillPayPage
from src.pages.contact_page import ContactPage
from src.pages.find_transactions_page import FindTransactionsPage
from src.pages.home_page import HomePage
from src.pages.open_new_account_page import OpenNewAccountPage
from src.pages.request_loan_page import RequestLoanPage
from src.pages.transfer_funds_page import TransferFundsPage
from src.pages.update_profile_page import UpdateProfilePage


@allure.epic("PARA-15241: Account operations")
@allure.feature("PARA-15254: Open New Account page navigation")
class TestOpenNewAccountPageNavigation:

    # Basic navigation
    # =================================================================================
    @allure.severity("Normal")
    @allure.title("User can proceed from Open New Account page to Contact page")
    def test_navigation_open_new_account_to_contact(self, driver):
        with allure.step("Navigate to Home page"):
            home_page = HomePage(driver)
            home_page.open_page()
            home_page.is_opened()

        with allure.step("Fill in valid username and password"):
            home_page.username_field.send_text(ActiveUser.LOGIN)
            home_page.password_field.send_text(ActiveUser.PASSWORD)

        with allure.step("Log in"):
            home_page.log_in_button.click()
            accounts_overview_page = AccountsOverviewPage(driver)
            accounts_overview_page.is_opened()

        with allure.step("Navigate to Open New Account page"):
            accounts_overview_page.open_new_account_link.click()
            open_new_account_page = OpenNewAccountPage(driver)
            open_new_account_page.is_opened()

        with allure.step("Navigate to Contact page via button"):
            open_new_account_page.contact_button.click()

        with allure.step("Check user is redirected to Contact page"):
            contact_page = ContactPage(driver)
            contact_page.is_opened()

    @allure.severity("Normal")
    @allure.title("User can proceed from Open New Account page to About Us page")
    def test_navigation_open_new_account_to_about_us(self, driver):
        with allure.step("Navigate to Home page"):
            home_page = HomePage(driver)
            home_page.open_page()
            home_page.is_opened()

        with allure.step("Fill in valid username and password"):
            home_page.username_field.send_text(ActiveUser.LOGIN)
            home_page.password_field.send_text(ActiveUser.PASSWORD)

        with allure.step("Log in"):
            home_page.log_in_button.click()
            accounts_overview_page = AccountsOverviewPage(driver)
            accounts_overview_page.is_opened()

        with allure.step("Navigate to Open New Account page"):
            accounts_overview_page.open_new_account_link.click()
            open_new_account_page = OpenNewAccountPage(driver)
            open_new_account_page.is_opened()

        with allure.step("Navigate to About Us page via button"):
            open_new_account_page.about_us_button.click()

        with allure.step("Check user is redirected to About Us page"):
            about_us_page = AboutUsPage(driver)
            about_us_page.is_opened()

    @allure.severity("Normal")
    @allure.title("User can proceed from Open New Account page to Home page")
    def test_navigation_open_new_account_to_home(self, driver):
        with allure.step("Navigate to Home page"):
            home_page = HomePage(driver)
            home_page.open_page()
            home_page.is_opened()

        with allure.step("Fill in valid username and password"):
            home_page.username_field.send_text(ActiveUser.LOGIN)
            home_page.password_field.send_text(ActiveUser.PASSWORD)

        with allure.step("Log in"):
            home_page.log_in_button.click()
            accounts_overview_page = AccountsOverviewPage(driver)
            accounts_overview_page.is_opened()

        with allure.step("Navigate to Open New Account page"):
            accounts_overview_page.open_new_account_link.click()
            open_new_account_page = OpenNewAccountPage(driver)
            open_new_account_page.is_opened()

        with allure.step("Proceed to Home page via button"):
            open_new_account_page.home_button.click()

        with allure.step("Check user is redirected to Home page"):
            home_page.is_opened()

    # Account Services navigation
    # =================================================================================
    @allure.severity("Normal")
    @allure.title("User can proceed from Open New Account page to Accounts Overview page")
    def test_navigation_open_new_account_to_accounts_overview(self, driver):
        with allure.step("Navigate to Home page"):
            home_page = HomePage(driver)
            home_page.open_page()
            home_page.is_opened()

        with allure.step("Fill in valid username and password"):
            home_page.username_field.send_text(ActiveUser.LOGIN)
            home_page.password_field.send_text(ActiveUser.PASSWORD)

        with allure.step("Log in"):
            home_page.log_in_button.click()
            accounts_overview_page = AccountsOverviewPage(driver)
            accounts_overview_page.is_opened()

        with allure.step("Navigate to Open New Account page"):
            accounts_overview_page.open_new_account_link.click()
            open_new_account_page = OpenNewAccountPage(driver)
            open_new_account_page.is_opened()

        with allure.step("Proceed to Accounts Overview page via link"):
            open_new_account_page.accounts_overview_link.click()

        with allure.step("Check user is redirected to Accounts Overview page"):
            accounts_overview_page = AccountsOverviewPage(driver)
            accounts_overview_page.is_opened()

    @allure.severity("Normal")
    @allure.title("User can proceed from Open New Account page to Transfer Funds page")
    def test_navigation_open_new_account_to_transfer_funds(self, driver):
        with allure.step("Navigate to Home page"):
            home_page = HomePage(driver)
            home_page.open_page()
            home_page.is_opened()

        with allure.step("Fill in valid username and password"):
            home_page.username_field.send_text(ActiveUser.LOGIN)
            home_page.password_field.send_text(ActiveUser.PASSWORD)

        with allure.step("Log in"):
            home_page.log_in_button.click()
            accounts_overview_page = AccountsOverviewPage(driver)
            accounts_overview_page.is_opened()

        with allure.step("Navigate to Open New Account page"):
            accounts_overview_page.open_new_account_link.click()
            open_new_account_page = OpenNewAccountPage(driver)
            open_new_account_page.is_opened()

        with allure.step("Proceed to Transfer Funds page via link"):
            open_new_account_page.transfer_funds_link.click()

        with allure.step("Check user is redirected to Transfer Funds page"):
            transfer_funds_page = TransferFundsPage(driver)
            transfer_funds_page.is_opened()

    @allure.severity("Normal")
    @allure.title("User can proceed from Open New Account page to Bill Pay page")
    def test_navigation_open_new_account_to_bill_pay(self, driver):
        with allure.step("Navigate to Home page"):
            home_page = HomePage(driver)
            home_page.open_page()
            home_page.is_opened()

        with allure.step("Fill in valid username and password"):
            home_page.username_field.send_text(ActiveUser.LOGIN)
            home_page.password_field.send_text(ActiveUser.PASSWORD)

        with allure.step("Log in"):
            home_page.log_in_button.click()
            accounts_overview_page = AccountsOverviewPage(driver)
            accounts_overview_page.is_opened()

        with allure.step("Navigate to Open New Account page"):
            accounts_overview_page.open_new_account_link.click()
            open_new_account_page = OpenNewAccountPage(driver)
            open_new_account_page.is_opened()

        with allure.step("Proceed to Bill Pay page via link"):
            open_new_account_page.bill_pay_link.click()

        with allure.step("Check user is redirected to Bill Pay page"):
            bill_pay_page = BillPayPage(driver)
            bill_pay_page.is_opened()

    @allure.severity("Normal")
    @allure.title("User can proceed from Open New Account page to Find Transactions page")
    def test_navigation_open_new_account_to_find_transactions(self, driver):
        with allure.step("Navigate to Home page"):
            home_page = HomePage(driver)
            home_page.open_page()
            home_page.is_opened()

        with allure.step("Fill in valid username and password"):
            home_page.username_field.send_text(ActiveUser.LOGIN)
            home_page.password_field.send_text(ActiveUser.PASSWORD)

        with allure.step("Log in"):
            home_page.log_in_button.click()
            accounts_overview_page = AccountsOverviewPage(driver)
            accounts_overview_page.is_opened()

        with allure.step("Navigate to Open New Account page"):
            accounts_overview_page.open_new_account_link.click()
            open_new_account_page = OpenNewAccountPage(driver)
            open_new_account_page.is_opened()

        with allure.step("Proceed to Find Transactions page via link"):
            open_new_account_page.find_transactions_link.click()

        with allure.step("Check user is redirected to Find Transactions page"):
            find_transactions_page = FindTransactionsPage(driver)
            find_transactions_page.is_opened()

    @allure.severity("Normal")
    @allure.title("User can proceed from Open New Account page to Update Profile page")
    def test_navigation_open_new_account_to_update_profile(self, driver):
        with allure.step("Navigate to Home page"):
            home_page = HomePage(driver)
            home_page.open_page()
            home_page.is_opened()

        with allure.step("Fill in valid username and password"):
            home_page.username_field.send_text(ActiveUser.LOGIN)
            home_page.password_field.send_text(ActiveUser.PASSWORD)

        with allure.step("Log in"):
            home_page.log_in_button.click()
            accounts_overview_page = AccountsOverviewPage(driver)
            accounts_overview_page.is_opened()

        with allure.step("Navigate to Open New Account page"):
            accounts_overview_page.open_new_account_link.click()
            open_new_account_page = OpenNewAccountPage(driver)
            open_new_account_page.is_opened()

        with allure.step("Proceed to Update Profile page via link"):
            open_new_account_page.update_contact_info_link.click()

        with allure.step("Check user is redirected to Update Profile page"):
            update_profile_page = UpdateProfilePage(driver)
            update_profile_page.is_opened()

    @allure.severity("Normal")
    @allure.title("User can proceed from Open New Account page to Request Loan page")
    def test_navigation_open_new_account_to_request_loan(self, driver):
        with allure.step("Navigate to Home page"):
            home_page = HomePage(driver)
            home_page.open_page()
            home_page.is_opened()

        with allure.step("Fill in valid username and password"):
            home_page.username_field.send_text(ActiveUser.LOGIN)
            home_page.password_field.send_text(ActiveUser.PASSWORD)

        with allure.step("Log in"):
            home_page.log_in_button.click()
            accounts_overview_page = AccountsOverviewPage(driver)
            accounts_overview_page.is_opened()

        with allure.step("Navigate to Open New Account page"):
            accounts_overview_page.open_new_account_link.click()
            open_new_account_page = OpenNewAccountPage(driver)
            open_new_account_page.is_opened()

        with allure.step("Proceed to Request Loan page via link"):
            open_new_account_page.request_loan_link.click()

        with allure.step("Check user is redirected to Request Loan page"):
            request_loan_page = RequestLoanPage(driver)
            request_loan_page.is_opened()

    @allure.severity("Normal")
    @allure.title("User can log out from Open New Account page")
    def test_logout_from_open_new_account(self, driver):
        with allure.step("Navigate to Home page"):
            home_page = HomePage(driver)
            home_page.open_page()
            home_page.is_opened()

        with allure.step("Fill in valid username and password"):
            home_page.username_field.send_text(ActiveUser.LOGIN)
            home_page.password_field.send_text(ActiveUser.PASSWORD)

        with allure.step("Log in"):
            home_page.log_in_button.click()
            accounts_overview_page = AccountsOverviewPage(driver)
            accounts_overview_page.is_opened()

        with allure.step("Navigate to Open New Account page"):
            accounts_overview_page.open_new_account_link.click()
            open_new_account_page = OpenNewAccountPage(driver)
            open_new_account_page.is_opened()

        with allure.step("Log out"):
            open_new_account_page.log_out_link.click()

        with allure.step("Check user is redirected to Home page"):
            home_page.is_opened()
            home_page.log_in_button.is_visible()
