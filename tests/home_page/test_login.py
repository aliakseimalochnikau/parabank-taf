import pytest

from src.pages.accounts_overview_page import AccountsOverviewPage
from src.pages.home_page import HomePage
from src.pages.login_page import LoginPage
from src.config.data import Data


class TestLogin:
    def test_login_valid_credentials(self, driver):
        home_page = HomePage(driver)
        home_page.open_page()
        home_page.is_opened()
        home_page.username_field.send_text(Data.LOGIN)
        home_page.password_field.send_text(Data.PASSWORD)
        home_page.log_in_button.click()
        overview_page = AccountsOverviewPage(driver)

        expected_url = overview_page.PAGE_URL
        current_url = overview_page.get_current_url()
        expected_message = Data.USER_GREETING
        current_message = overview_page.greeting_text.get_text()

        assert current_url in expected_url, f"Expected '{expected_url}', but got '{current_url}'"
        assert current_message in expected_message, f"Expected '{expected_message} message, but got '{current_message}'"

    @pytest.mark.xfail(reason="Known security issue")
    def test_login_valid_username_invalid_password(self, driver):
        home_page = HomePage(driver)
        home_page.open_page()
        home_page.is_opened()
        home_page.username_field.send_text(Data.LOGIN)
        home_page.password_field.send_text("orange533")
        home_page.log_in_button.click()
        login_page = LoginPage(driver)

        expected_error = "An internal error has occurred and has been logged."
        current_error = login_page.internal_error.get_text()

        assert current_error in expected_error, f"Expected '{expected_error} message, but got '{current_error}'"

    @pytest.mark.xfail(reason="Known security issue")
    def test_login_invalid_username_valid_password(self, driver):
        home_page = HomePage(driver)
        home_page.open_page()
        home_page.is_opened()
        home_page.username_field.send_text("orange253")
        home_page.password_field.send_text(Data.PASSWORD)
        home_page.log_in_button.click()
        login_page = LoginPage(driver)

        expected_error = "An internal error has occurred and has been logged."
        current_error = login_page.internal_error.get_text()

        assert current_error in expected_error, f"Expected '{expected_error} message, but got '{current_error}'"

    def test_login_empty_username(self, driver):
        home_page = HomePage(driver)
        home_page.open_page()
        home_page.is_opened()
        home_page.password_field.send_text(Data.PASSWORD)
        home_page.log_in_button.click()
        login_page = LoginPage(driver)

        expected_error = "Please enter a username and password."
        current_error = login_page.empty_field_error.get_text()

        assert current_error in expected_error, f"Expected '{expected_error} message, but got '{current_error}'"

    def test_login_with_empty_password(self, driver):
        home_page = HomePage(driver)
        home_page.open_page()
        home_page.is_opened()
        home_page.username_field.send_text(Data.LOGIN)
        home_page.log_in_button.click()
        login_page = LoginPage(driver)

        expected_error = "Please enter a username and password."
        current_error = login_page.empty_field_error.get_text()

        assert current_error in expected_error, f"Expected '{expected_error} message, but got '{current_error}'"
