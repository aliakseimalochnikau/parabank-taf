import allure
import pytest
from src.config.data import ActiveUser
from src.pages.account_activity_page import AccountActivityPage
from src.pages.accounts_overview_page import AccountsOverviewPage
from src.pages.home_page import HomePage
from src.pages.open_new_account_page import OpenNewAccountPage


@allure.feature("New account opening")
class TestNewAccountOpening:
    @pytest.mark.smoke
    @allure.title("User can successfully open a new account of 'Checking' type.")
    def test_new_checking_account_opening(self, driver):
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

        with allure.step("Select account of 'Checking' type"):
            open_new_account_page.account_type_dropdown.select_element_by_index(0)

        with allure.step("Select source account"):
            open_new_account_page.from_account_dropdown.select_element_by_index(0)

        with allure.step("Open new account"):
            open_new_account_page.open_account_button.click()
            new_account_id = open_new_account_page.new_account_id_link.get_text()
            open_new_account_page.new_account_id_link.click()

        with allure.step("Check user is redirected to Account Activity page"):
            account_activity_page = AccountActivityPage(driver, new_account_id)
            account_activity_page.is_opened()

        with allure.step("Check valid account information is displayed"):
            account_activity_page.account_number_text.assert_text(new_account_id)
            account_activity_page.account_type_text.assert_text("CHECKING")

    @pytest.mark.smoke
    @allure.title("User can successfully open a new account of 'Savings' type.")
    def test_new_savings_account_opening(self, driver):
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

        with allure.step("Select account of 'Savings' type"):
            open_new_account_page.account_type_dropdown.select_element_by_index(1)

        with allure.step("Select source account"):
            open_new_account_page.from_account_dropdown.select_element_by_index(0)

        with allure.step("Open new account"):
            open_new_account_page.open_account_button.click()
            new_account_id = open_new_account_page.new_account_id_link.get_text()
            open_new_account_page.new_account_id_link.click()

        with allure.step("Check user is redirected to Account Activity page"):
            account_activity_page = AccountActivityPage(driver, new_account_id)
            account_activity_page.is_opened()

        with allure.step("Check valid account information is displayed"):
            account_activity_page.account_number_text.assert_text(new_account_id)
            account_activity_page.account_type_text.assert_text("SAVINGS")
