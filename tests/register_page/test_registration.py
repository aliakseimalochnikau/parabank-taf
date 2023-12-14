import random
import allure
import pytest
from src.utils.generator import generated_data
from src.pages.home_page.home_page import HomePage
from src.pages.home_page.register_page import RegisterPage


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
            assert register_page.PAGE_URL in register_page.get_current_url()

        with allure.step("Fill in the fields"):
            new_user = next(generated_data())
            register_page.first_name_field.send_text(new_user.first_name)
            register_page.last_name_field.send_text(new_user.last_name)
            register_page.address_field.send_text(new_user.address)
            register_page.city_field.send_text(new_user.city)
            register_page.state_field.send_text(new_user.state)
            register_page.zip_code_field.send_text(new_user.zip_code)
            register_page.phone_number_field.send_text(new_user.phone_number)
            register_page.ssn_field.send_text(new_user.ssn)
            register_page.username_field.send_text(new_user.username)
            register_page.password_field.send_text(new_user.password)
            register_page.confirm_password_field.send_text(new_user.password)

        with allure.step("Submit the form"):
            register_page.register_button.click()

        with allure.step("Check registration is successful"):
            expected_message = f"Welcome {new_user.username}"
            current_message = register_page.welcome_username_text.get_text()
            assert expected_message in current_message, (f"Expected '{expected_message}' message, but got "
                                                         f"'{current_message}'.")

    @allure.title("User can't successfully register by submitting an empty form.")
    def test_registration_with_empty_form(self, driver):
        with allure.step("Navigate to Home page"):
            home_page = HomePage(driver)
            home_page.open_page()
            home_page.is_opened()

        with allure.step("Navigate to Register page"):
            home_page.register_link.click()
            register_page = RegisterPage(driver)
            assert register_page.PAGE_URL in register_page.get_current_url()

        with allure.step("Submit the form with empty fields"):
            register_page.register_button.click()

        with allure.step("Check error message is displayed for each field left empty"):
            expected_error_count = 10
            current_error_count = register_page.errors_list.count_elements()
            assert expected_error_count == current_error_count, (f"Expected {expected_error_count} errors, but got "
                                                                 f"{current_error_count}.")

    @allure.title("User can't successfully register by leaving one of the fields empty.")
    def test_registration_with_empty_random_field(self, driver):
        with allure.step("Navigate to Home page"):
            home_page = HomePage(driver)
            home_page.open_page()
            home_page.is_opened()

        with allure.step("Navigate to Register page"):
            home_page.register_link.click()
            register_page = RegisterPage(driver)
            assert register_page.PAGE_URL in register_page.get_current_url()

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
                expected_message = error_text
                current_message = error_locator.get_text()
                assert expected_message in current_message, (f"Expected '{expected_message}' message, but got "
                                                             f"'{current_message}'.")

    @allure.title("User can't successfully register by providing mismatched passwords")
    def test_registration_with_mismatched_passwords(self, driver):
        with allure.step("Navigate to Home page"):
            home_page = HomePage(driver)
            home_page.open_page()
            home_page.is_opened()

        with allure.step("Navigate to Register page"):
            home_page.register_link.click()
            register_page = RegisterPage(driver)
            assert register_page.PAGE_URL in register_page.get_current_url()

        with allure.step("Fill in the fields"):
            new_user = next(generated_data())
            register_page.first_name_field.send_text(new_user.first_name)
            register_page.last_name_field.send_text(new_user.last_name)
            register_page.address_field.send_text(new_user.address)
            register_page.city_field.send_text(new_user.city)
            register_page.state_field.send_text(new_user.state)
            register_page.zip_code_field.send_text(new_user.zip_code)
            register_page.phone_number_field.send_text(new_user.phone_number)
            register_page.ssn_field.send_text(new_user.ssn)
            register_page.username_field.send_text(new_user.username)
            register_page.password_field.send_text(new_user.password)
            register_page.confirm_password_field.send_text("somerandompassword_823!")

        with allure.step("Submit the form with mismatched passwords"):
            register_page.register_button.click()

        with allure.step("Check error message is displayed"):
            expected_message = f"Passwords did not match"
            current_message = register_page.confirm_password_error.get_text()
            assert expected_message in current_message, (f"Expected '{expected_message}' message, but got "
                                                         f"'{current_message}'.")

