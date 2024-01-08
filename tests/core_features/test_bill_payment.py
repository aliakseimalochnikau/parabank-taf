import allure
import pytest
from src.config.data import ActiveUser
from src.pages.accounts_overview_page import AccountsOverviewPage
from src.pages.bill_pay_page import BillPayPage
from src.pages.home_page import HomePage
from src.pages.register_page import RegisterPage
from src.utils.block_checker import block_checker
from src.utils.data_generator import generated_data
from src.utils.empty_field_picker import fill_form_with_empty_random_field


@allure.epic("PARA-15244: Payment operations")
@allure.feature("PARA-15290: Bill payment")
class TestBillPayment:
    @pytest.mark.smoke
    @allure.severity("Critical")
    @allure.title("User can make payment to a certain payee")
    def test_successful_bill_payment(self, driver):
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

        with allure.step("Navigate to Accounts Overview page"):
            register_page.accounts_overview_link.click()
            accounts_overview_page = AccountsOverviewPage(driver)
            accounts_overview_page.is_opened()

        with allure.step("Get account initial balance"):
            balances = accounts_overview_page.get_balances()
            initial_balance = balances[0]

        with allure.step("Navigate to Bill Pay page"):
            accounts_overview_page.bill_pay_link.click()
            bill_pay_page = BillPayPage(driver)
            bill_pay_page.is_opened()

        with allure.step("Enter payee information and payment amount"):
            bill_pay_page.enter_payee_info()
            payment_amount = "50"
            bill_pay_page.amount_field.send_text(payment_amount)

        with allure.step("Send payment"):
            bill_pay_page.send_payment_button.click()

        with allure.step("Check payment is complete"):
            bill_pay_page.payment_complete_text.assert_text("Bill Payment Complete")

        with allure.step("Return to Accounts Overview page"):
            bill_pay_page.accounts_overview_link.click()
            accounts_overview_page.is_opened()

        with allure.step("Check payment amount was deducted from the account"):
            balances = accounts_overview_page.get_balances()
            final_balance = balances[0]
            assert final_balance == initial_balance - float(payment_amount), (f"{final_balance} doesn't match "
                                                                              f"{initial_balance} - {payment_amount}")

    @allure.severity("Minor")
    @allure.title("User can't make a payment by submitting an empty payee info form")
    def test_bill_payment_with_empty_payee_info(self, driver):
        with allure.step("Navigate to Home page"):
            home_page = HomePage(driver)
            home_page.open_page()
            home_page.is_opened()

        with allure.step("Fill in valid username and password"):
            home_page.username_field.send_text(ActiveUser.LOGIN)
            home_page.password_field.send_text(ActiveUser.PASSWORD)

        with allure.step("Login"):
            home_page.log_in_button.click()
            accounts_overview_page = AccountsOverviewPage(driver)
            accounts_overview_page.is_opened()

        with allure.step("Navigate to Bill Pay page"):
            accounts_overview_page.bill_pay_link.click()
            bill_pay_page = BillPayPage(driver)
            bill_pay_page.is_opened()

        with allure.step("Send payment with empty payee information"):
            bill_pay_page.amount_field.send_text("50")
            bill_pay_page.send_payment_button.click()

        with allure.step("Check error message is displayed for each field left empty"):
            bill_pay_page.errors_list.assert_error_count(8)

    @allure.severity("Minor")
    @allure.title("User can't make a payment by leaving one of the payee info fields empty")
    def test_bill_payment_with_empty_random_payee_info_field(self, driver):
        with allure.step("Navigate to Home page"):
            home_page = HomePage(driver)
            home_page.open_page()
            home_page.is_opened()

        with allure.step("Fill in valid username and password"):
            home_page.username_field.send_text(ActiveUser.LOGIN)
            home_page.password_field.send_text(ActiveUser.PASSWORD)

        with allure.step("Login"):
            home_page.log_in_button.click()
            accounts_overview_page = AccountsOverviewPage(driver)
            accounts_overview_page.is_opened()

        with allure.step("Navigate to Bill Pay page"):
            accounts_overview_page.bill_pay_link.click()
            bill_pay_page = BillPayPage(driver)
            bill_pay_page.is_opened()

        with allure.step("Fill in all the required fields but one"):
            new_user = next(generated_data())
            form_fields = {
                1: (bill_pay_page.payee_name_field, f"{new_user.first_name} {new_user.last_name}"),
                2: (bill_pay_page.address_field, new_user.address),
                3: (bill_pay_page.city_field, new_user.city),
                4: (bill_pay_page.state_field, new_user.state),
                5: (bill_pay_page.zip_code_field, new_user.zip_code),
                6: (bill_pay_page.phone_field, new_user.phone_number),
                7: (bill_pay_page.account_field, "50240"),
                8: (bill_pay_page.verify_account_field, "50240")
            }
            no_fill_num = fill_form_with_empty_random_field(form_fields, number_of_fields=8)

        with allure.step("Enter amount and send payment"):
            bill_pay_page.amount_field.send_text("50")
            bill_pay_page.send_payment_button.click()

        with allure.step("Check error message is displayed"):
            field_errors = {
                1: (bill_pay_page.payee_name_error, "Payee name is required."),
                2: (bill_pay_page.address_error, "Address is required."),
                3: (bill_pay_page.city_error, "City is required."),
                4: (bill_pay_page.state_error, "State is required."),
                5: (bill_pay_page.zip_code_error, "Zip Code is required."),
                6: (bill_pay_page.phone_error, "Phone number is required."),
                7: (bill_pay_page.account_error, "Account number is required."),
                8: (bill_pay_page.verify_account_error, "Account number is required.")
            }

            error_locator, error_text = field_errors[no_fill_num]
            error_locator.assert_error(error_text)

    @allure.severity("Minor")
    @allure.title("User can't make a payment by providing mismatched accounts")
    def test_bill_payment_with_mismatched_accounts(self, driver):
        with allure.step("Navigate to Home page"):
            home_page = HomePage(driver)
            home_page.open_page()
            home_page.is_opened()

        with allure.step("Fill in valid username and password"):
            home_page.username_field.send_text(ActiveUser.LOGIN)
            home_page.password_field.send_text(ActiveUser.PASSWORD)

        with allure.step("Login"):
            home_page.log_in_button.click()
            accounts_overview_page = AccountsOverviewPage(driver)
            accounts_overview_page.is_opened()

        with allure.step("Navigate to Bill Pay page"):
            accounts_overview_page.bill_pay_link.click()
            bill_pay_page = BillPayPage(driver)
            bill_pay_page.is_opened()

        with allure.step("Enter payee information with mismatched accounts"):
            bill_pay_page.missmatch_account_payee()

        with allure.step("Enter amount and send payment"):
            bill_pay_page.amount_field.send_text("50")
            bill_pay_page.send_payment_button.click()

        with allure.step("Check error message is displayed"):
            bill_pay_page.account_mismatch_error.assert_error("The account numbers do not match.")

    @allure.severity("Minor")
    @allure.title("User can't make a payment with empty amount")
    def test_bill_payment_with_empty_amount(self, driver):
        with allure.step("Navigate to Home page"):
            home_page = HomePage(driver)
            home_page.open_page()
            home_page.is_opened()

        with allure.step("Fill in valid username and password"):
            home_page.username_field.send_text(ActiveUser.LOGIN)
            home_page.password_field.send_text(ActiveUser.PASSWORD)

        with allure.step("Login"):
            home_page.log_in_button.click()
            accounts_overview_page = AccountsOverviewPage(driver)
            accounts_overview_page.is_opened()

        with allure.step("Navigate to Bill Pay page"):
            accounts_overview_page.bill_pay_link.click()
            bill_pay_page = BillPayPage(driver)
            bill_pay_page.is_opened()

        with allure.step("Enter payee information"):
            bill_pay_page.enter_payee_info()

        with allure.step("Send payment with empty amount"):
            bill_pay_page.send_payment_button.click()

        with allure.step("Check error message is displayed"):
            bill_pay_page.amount_error.assert_error("The amount cannot be empty.")
