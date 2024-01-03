import time
import allure
import pytest
from src.config.data import ActiveUser
from src.pages.account_activity_page import AccountActivityPage
from src.pages.accounts_overview_page import AccountsOverviewPage
from src.pages.home_page import HomePage


class TestAccountDataConsistency:
    @pytest.mark.smoke
    @allure.title("Sum of accounts' balances match total")
    def test_accounts_balances_sum_matches_total(self, driver):
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

        with allure.step("Sum balances across opened accounts"):
            time.sleep(.5)
            balances = accounts_overview_page.get_balances()
            total = balances.pop(-1)
            balances_sum = round(sum(balances), 2)

        with allure.step("Check sum of balances matches total"):
            assert balances_sum == total, f"{balances_sum} != {total}"

    @allure.title("Balance and amount are consistent across Accounts Overview and Account Details pages")
    def test_balance_and_amount_consistency_across_pages(self, driver):
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

        with allure.step("Get balance and amount on Accounts Overview page"):
            time.sleep(.5)
            account_num = accounts_overview_page.account_id.get_text()
            overview_balance = accounts_overview_page.balance.get_text()
            overview_available_amount = accounts_overview_page.available_amount.get_text()

        with allure.step("Proceed to Account Activity page"):
            accounts_overview_page.account_id_link.click()
            account_activity_page = AccountActivityPage(driver, account_num)
            account_activity_page.is_opened()

        with allure.step("Get balance and amount on Account Activity page"):
            time.sleep(.5)
            activity_balance = account_activity_page.account_balance_text.get_text()
            activity_available_amount = account_activity_page.account_available_text.get_text()

        with allure.step("Check balance and amount are consistent across pages"):
            assert overview_balance == activity_balance, f"{overview_balance} doesn't match {activity_balance}"
            assert overview_available_amount == activity_available_amount, (f"{overview_available_amount} "
                                                                            f"doesn't match {activity_available_amount}")
