import time
import allure
import pytest
from src.pages.accounts_overview_page import AccountsOverviewPage
from src.pages.open_new_account_page import OpenNewAccountPage
from src.pages.register_page import RegisterPage
from src.pages.transfer_funds_page import TransferFundsPage
from src.utils.block_checker import block_checker


@allure.epic("PARA-15242: Funds operations")
@allure.feature("PARA-15270: Funds transfer")
class TestFundsTransfer:
    @pytest.mark.smoke
    @allure.severity("Critical")
    @allure.title("User can transfer funds between accounts")
    def test_successful_funds_transfer(self, driver):
        with allure.step("Navigate to Register page"):
            register_page = RegisterPage(driver)
            register_page.open_page()
            register_page.is_opened()

        with allure.step("Register a new user"):
            new_user = register_page.new_registration()
            register_page.register_button.click()
            block_checker(driver)
            # Processing the case of existing username
            checked_user = register_page.re_generate_username(new_user)
            block_checker(driver)

        with allure.step("Check registration is successful"):
            register_page.welcome_username_text.assert_text(f"Welcome {checked_user.username}")

        with allure.step("Proceed to Open New Account page"):
            register_page.open_new_account_link.click()
            open_new_account_page = OpenNewAccountPage(driver)
            open_new_account_page.is_opened()

        with allure.step("Open new account"):
            # time.sleep(.5)
            open_new_account_page.account_type_dropdown.select_by_index(0)
            open_new_account_page.from_account_dropdown.select_by_index(0)
            time.sleep(.5)
            open_new_account_page.open_account_button.click()
            open_new_account_page.account_opened_text.assert_text("Account Opened!")

        with allure.step("Proceed to Accounts Overview page"):
            open_new_account_page.accounts_overview_link.click()
            accounts_overview_page = AccountsOverviewPage(driver)
            accounts_overview_page.is_opened()

        with allure.step("Get initial accounts' balances"):
            # time.sleep(.5)
            balances = accounts_overview_page.get_balances()
            balances.pop(-1)
            from_account_init_balance = balances[0]
            to_account_init_balance = balances[1]

        with allure.step("Proceed to Transfer Funds page"):
            accounts_overview_page.transfer_funds_link.click()
            transfer_funds_page = TransferFundsPage(driver)
            transfer_funds_page.is_opened()

        with allure.step("Transfer Funds between accounts"):
            amount = 50
            time.sleep(1)
            transfer_funds_page.amount_field.send_text(amount)
            transfer_funds_page.from_account_dropdown.select_by_index(0)
            transfer_funds_page.to_account_dropdown.select_by_index(1)
            transfer_funds_page.transfer_button.click()
            transfer_funds_page.transfer_complete_text.assert_text("Transfer Complete!")

        with allure.step("Proceed to Accounts Overview page"):
            transfer_funds_page.accounts_overview_link.click()
            accounts_overview_page.is_opened()

        with allure.step("Get final accounts' balances"):
            # time.sleep(.5)
            balances = accounts_overview_page.get_balances()
            balances.pop(-1)
            from_account_final_balance = balances[0]
            to_account_final_balance = balances[1]

        with allure.step("Check funds were transferred correctly"):
            from_account_expected_balance = from_account_init_balance - amount
            to_account_expected_balance = to_account_init_balance + amount

            assert from_account_expected_balance == from_account_final_balance, (f"Expected "
                                                                                 f"{from_account_expected_balance}, "
                                                                                 f"but got {from_account_final_balance}"
                                                                                 )
            assert to_account_expected_balance == to_account_final_balance, (f"Expected {to_account_expected_balance}, "
                                                                             f"but got {to_account_final_balance}")

    @allure.severity("Minor")
    @allure.title("User can't transfer funds leaving amount field empty")
    def test_funds_transfer_with_empty_amount(self, driver):
        with allure.step("Navigate to Register page"):
            register_page = RegisterPage(driver)
            register_page.open_page()
            register_page.is_opened()

        with allure.step("Register a new user"):
            new_user = register_page.new_registration()
            register_page.register_button.click()
            block_checker(driver)
            # Processing the case of existing username
            checked_user = register_page.re_generate_username(new_user)
            block_checker(driver)

        with allure.step("Check registration is successful"):
            register_page.welcome_username_text.assert_text(f"Welcome {checked_user.username}")

        with allure.step("Proceed to Open New Account page"):
            register_page.open_new_account_link.click()
            open_new_account_page = OpenNewAccountPage(driver)
            open_new_account_page.is_opened()

        with allure.step("Open new account"):
            # time.sleep(.5)
            open_new_account_page.account_type_dropdown.select_by_index(0)
            open_new_account_page.from_account_dropdown.select_by_index(0)
            time.sleep(.5)
            open_new_account_page.open_account_button.click()
            open_new_account_page.account_opened_text.assert_text("Account Opened!")

        with allure.step("Proceed to Transfer Funds page"):
            open_new_account_page.transfer_funds_link.click()
            transfer_funds_page = TransferFundsPage(driver)
            transfer_funds_page.is_opened()

        with allure.step("Try transfer funds leaving 'Amount' field empty"):
            time.sleep(1)
            transfer_funds_page.from_account_dropdown.select_by_index(0)
            transfer_funds_page.to_account_dropdown.select_by_index(1)
            transfer_funds_page.transfer_button.click()
            transfer_funds_page.amount_error.assert_error("The amount cannot be empty.")
