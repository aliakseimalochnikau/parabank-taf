import time
import allure
import pytest
from src.config.data import ActiveUser
from src.pages.accounts_overview_page import AccountsOverviewPage
from src.pages.home_page import HomePage
from src.pages.open_new_account_page import OpenNewAccountPage
from src.pages.register_page import RegisterPage
from src.utils.block_checker import block_checker


@allure.epic("PARA-15241: Account operations")
@allure.feature("PARA-15251: Account display in Accounts Overview table")
class TestAccountDisplay:
    @pytest.mark.smoke
    @allure.severity("Critical")
    @allure.title("Default account is displayed in the table for a new user")
    def test_default_account_display(self, driver):
        with allure.step("Navigate to Register page"):
            register_page = RegisterPage(driver)
            register_page.open_page()
            register_page.is_opened()

        with allure.step("Fill in the fields"):
            new_user = register_page.new_registration()

        with allure.step("Submit the form"):
            register_page.register_button.click()
            block_checker(driver)
            # Processing the case of existing username
            checked_user = register_page.re_generate_username(new_user)
            block_checker(driver)

        with allure.step("Check registration is successful"):
            register_page.welcome_username_text.assert_text(f"Welcome {checked_user.username}")

        with allure.step("Proceed to Accounts Overview page"):
            register_page.accounts_overview_link.click()
            accounts_overview_page = AccountsOverviewPage(driver)
            accounts_overview_page.is_opened()

        with allure.step("Check one default account is displayed in the table"):
            time.sleep(.5)
            expected_account_count = 1
            accounts_overview_page.account_id.assert_element_count(expected_account_count, correction=1)

    @allure.severity("Critical")
    @allure.title("Newly created account is displayed in the table")
    def test_new_account_display(self, driver):
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

        with allure.step("Check number of accounts displayed in the table"):
            time.sleep(.5)
            initial_account_count = accounts_overview_page.account_id.count_elements(correction=1)

        with allure.step("Navigate to Open New Account page"):
            accounts_overview_page.open_new_account_link.click()
            open_new_account_page = OpenNewAccountPage(driver)
            open_new_account_page.is_opened()

        with allure.step("Open new account"):
            open_new_account_page.account_type_dropdown.select_by_index(1)
            open_new_account_page.from_account_dropdown.select_by_index(0)
            time.sleep(.5)
            open_new_account_page.open_account_button.click()

        with allure.step("Navigate to Accounts Overview page"):
            open_new_account_page.accounts_overview_link.click()
            accounts_overview_page.is_opened()

        with (allure.step("Check newly created account is displayed in the table")):
            expected_account_count = initial_account_count + 1
            time.sleep(.5)
            accounts_overview_page.account_id.assert_element_count(expected_account_count, correction=1)
