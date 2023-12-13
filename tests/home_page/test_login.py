import allure
import pytest
from src.pages.common_page.overview_page import AccountsOverviewPage
from src.pages.home_page.home_page import HomePage
from src.pages.home_page.login_page import LoginPage
from src.config.data import ActiveUser


@allure.feature("Login")
class TestLogin:
    @pytest.mark.smoke
    @allure.title("User can successfully log in with valid credentials.")
    def test_login_with_valid_credentials(self, driver):
        with allure.step("Navigate to Home page"):
            home_page = HomePage(driver)
            home_page.open_page()
            home_page.is_opened()

        with allure.step("Fill in valid username and password"):
            home_page.username_field.send_text(ActiveUser.LOGIN)
            home_page.password_field.send_text(ActiveUser.PASSWORD)

        with allure.step("Log in"):
            home_page.log_in_button.click()

        with allure.step("Check user is logged in"):
            overview_page = AccountsOverviewPage(driver)
            expected_url = overview_page.PAGE_URL
            current_url = overview_page.get_current_url()
            expected_message = f"Welcome {ActiveUser.FIRST_NAME} {ActiveUser.LAST_NAME}"
            current_message = overview_page.greeting_text.get_text()
            assert expected_url in current_url, f"Expected '{expected_url}', but got '{current_url}'"
            assert expected_message in current_message, (f"Expected '{expected_message}' message, but got "
                                                         f"'{current_message}'.")

    @allure.title("User can't successfully log in with invalid password.")
    def test_login_with_invalid_password(self, driver):
        with allure.step("Navigate to Home page"):
            home_page = HomePage(driver)
            home_page.open_page()
            home_page.is_opened()

        with allure.step("Fill in valid username, but invalid password"):
            home_page.username_field.send_text(ActiveUser.LOGIN)
            home_page.password_field.send_text("orange533")

        with allure.step("Log in"):
            home_page.log_in_button.click()

        with allure.step("Check error message is displayed"):
            login_page = LoginPage(driver)
            expected_error = "The username and password could not be verified."
            server_error = "An internal error has occurred and has been logged."
            current_error = login_page.error_text.get_text()
            if server_error in current_error:
                pytest.xfail(reason="Known server-side issue")
            else:
                assert expected_error in current_error, f"Expected '{expected_error}' error, but got '{current_error}'."

    @allure.title("User can't successfully log in with invalid username.")
    def test_login_with_invalid_username(self, driver):
        with allure.step("Navigate to Home page"):
            home_page = HomePage(driver)
            home_page.open_page()
            home_page.is_opened()

        with allure.step("Fill in valid password, but invalid username"):
            home_page.username_field.send_text("orange533")
            home_page.password_field.send_text(ActiveUser.PASSWORD)

        with allure.step("Log in"):
            home_page.log_in_button.click()
            login_page = LoginPage(driver)

        with allure.step("Check error message is displayed"):
            expected_error = "The username and password could not be verified."
            server_error = "An internal error has occurred and has been logged."
            current_error = login_page.error_text.get_text()
            if server_error in current_error:
                pytest.xfail(reason="Known server-side issue")
            else:
                assert expected_error in current_error, f"Expected '{expected_error}' error, but got '{current_error}'."

    @allure.title("User can't successfully log in with empty username.")
    def test_login_with_empty_username(self, driver):
        with allure.step("Navigate to Home page"):
            home_page = HomePage(driver)
            home_page.open_page()
            home_page.is_opened()

        with allure.step("Fill in a password without specifying a username"):
            home_page.password_field.send_text(ActiveUser.PASSWORD)

        with allure.step("Log in"):
            home_page.log_in_button.click()

        with allure.step("Check error message is displayed"):
            login_page = LoginPage(driver)
            expected_error = "Please enter a username and password."
            current_error = login_page.error_text.get_text()
            assert expected_error in current_error, f"Expected '{expected_error}' error, but got '{current_error}'."

    @allure.title("User can't successfully log in with empty password.")
    def test_login_with_empty_password(self, driver):
        with allure.step("Navigate to Home page"):
            home_page = HomePage(driver)
            home_page.open_page()
            home_page.is_opened()

        with allure.step("Fill in a username without specifying a password"):
            home_page.username_field.send_text(ActiveUser.LOGIN)

        with allure.step("Log in"):
            home_page.log_in_button.click()

        with allure.step("Check error message is displayed"):
            login_page = LoginPage(driver)
            expected_error = "Please enter a username and password."
            current_error = login_page.error_text.get_text()
            assert expected_error in current_error, f"Expected '{expected_error}' error, but got '{current_error}'."
