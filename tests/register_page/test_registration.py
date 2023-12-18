import random
import allure
import pytest
from src.utils.data_generator import generated_data
from src.pages.home_page import HomePage
from src.pages.register_page import RegisterPage


@allure.feature("Registration")
class TestRegistration:
    @pytest.mark.smoke 
    @allure.title("User can successfully register by filling in all the fields.")
    def test_successful_registration(self, driver):
        with allure.step("Navigate to Home page"):
            home_page = HomePage(driver)
            home_page.open_page()
            home_page.is_opened()

        with allure.step("Navigate to Register page"):
            home_page.register_link.click()
            register_page = RegisterPage(driver)
            register_page.is_opened()

        with allure.step("Fill in the fields"):
            new_user = register_page.new_registration()

        with allure.step("Submit the form"):
            register_page.register_button.click()
            # Processing the case of existing username
            checked_user = register_page.re_generate_username(new_user)

        with allure.step("Check registration is successful"):
            register_page.welcome_username_text.assert_text(f"Welcome {checked_user.username}")

    @allure.title("User can't successfully register by submitting an empty form.")
    def test_registration_with_empty_form(self, driver):
        with allure.step("Navigate to Home page"):
            home_page = HomePage(driver)
            home_page.open_page()
            home_page.is_opened()

        with allure.step("Navigate to Register page"):
            home_page.register_link.click()
            register_page = RegisterPage(driver)
            register_page.is_opened()

        with allure.step("Submit the form with empty fields"):
            register_page.register_button.click()

        with allure.step("Check error message is displayed for each field left empty"):
            register_page.errors_list.assert_error_count(10)

    @allure.title("User can't successfully register by leaving one of the fields empty.")
    def test_registration_with_empty_random_field(self, driver):
        with allure.step("Navigate to Home page"):
            home_page = HomePage(driver)
            home_page.open_page()
            home_page.is_opened()

        with allure.step("Navigate to Register page"):
            home_page.register_link.click()
            register_page = RegisterPage(driver)
            register_page.is_opened()

        with allure.step("Fill in all the required fields but one"):
            new_user = next(generated_data())
            form_fields = {
                1: (register_page.first_name_field, new_user.first_name),
                2: (register_page.last_name_field, new_user.last_name),
                3: (register_page.address_field, new_user.address),
                4: (register_page.city_field, new_user.city),
                5: (register_page.state_field, new_user.state),
                6: (register_page.zip_code_field, new_user.zip_code),
                7: (register_page.ssn_field, new_user.ssn),
                8: (register_page.username_field, new_user.username),
                9: (register_page.password_field, new_user.password),
                10: (register_page.confirm_password_field, new_user.password)
            }
            no_fill_num = random.randint(1, 10)
            for i in range(1, 11):
                if i == no_fill_num:
                    continue
                else:
                    field, value = form_fields[i]
                    field.send_text(value)

            with allure.step("Submit the form with one empty field"):
                register_page.register_button.click()

            with allure.step("Check error message is displayed"):
                field_errors = {
                    1: (register_page.first_name_error, "First name is required."),
                    2: (register_page.last_name_error, "Last name is required."),
                    3: (register_page.address_error, "Address is required."),
                    4: (register_page.city_error, "City is required."),
                    5: (register_page.state_error, "State is required."),
                    6: (register_page.zip_code_error, "Zip Code is required."),
                    7: (register_page.ssn_error, "Social Security Number is required."),
                    8: (register_page.username_error, "Username is required."),
                    9: (register_page.password_error, "Password is required."),
                    10: (register_page.confirm_password_error, "Password confirmation is required.")
                }

                error_locator, error_text = field_errors[no_fill_num]
                error_locator.assert_text(error_text)

    @allure.title("User can't successfully register by providing mismatched passwords")
    def test_registration_with_mismatched_passwords(self, driver):
        with allure.step("Navigate to Home page"):
            home_page = HomePage(driver)
            home_page.open_page()
            home_page.is_opened()

        with allure.step("Navigate to Register page"):
            home_page.register_link.click()
            register_page = RegisterPage(driver)
            register_page.is_opened()

        with allure.step("Fill in the fields with mismatched passwords"):
            register_page.missmatch_pass_registration()

        with allure.step("Submit the form"):
            register_page.register_button.click()

        with allure.step("Check error message is displayed"):
            register_page.confirm_password_error.assert_error("Passwords did not match.")

    @allure.title("User can't successfully register with existing username.")
    def test_registration_of_existing_user(self, driver):
        with allure.step("Navigate to Home page"):
            home_page = HomePage(driver)
            home_page.open_page()
            home_page.is_opened()

        with allure.step("Navigate to Register page"):
            home_page.register_link.click()
            register_page = RegisterPage(driver)
            register_page.is_opened()

        with allure.step("Register a new user"):
            new_user = register_page.new_registration()

        with allure.step("Submit the form"):
            register_page.register_button.click()

        with allure.step("Log out"):
            register_page.log_out_link.click()
            home_page.is_opened()

        with allure.step("Navigate to Register page"):
            home_page.register_link.is_visible()
            home_page.register_link.click()
            register_page.is_opened()

        with allure.step("Register a user with the same username"):
            register_page.repeat_registration(new_user)

        with allure.step("Submit the form"):
            register_page.register_button.click()

        with allure.step("Check error message is displayed"):
            register_page.username_error.assert_error("This username already exists.")
