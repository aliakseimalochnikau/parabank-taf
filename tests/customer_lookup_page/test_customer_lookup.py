import random
import allure
import pytest
from src.pages.customer_lookup_page import CustomerLookupPage
from src.pages.home_page import HomePage
from src.pages.register_page import RegisterPage


@allure.feature("Customer Lookup")
class TestCustomerLookup:
    @pytest.mark.smoke
    @allure.title("User can successfully lookup for credentials by providing valid data")
    def test_lookup_with_valid_data(self, driver):
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

        with allure.step("Log out"):
            register_page.log_out_link.click()
            home_page.is_opened()

        with allure.step("Navigate to Customer Lookup page"):
            home_page.forgot_login_link.click()
            customer_lookup_page = CustomerLookupPage(driver)
            customer_lookup_page.is_opened()

        with allure.step("Fill in lookup form"):
            customer_lookup_page.first_name_field.send_text(checked_user.first_name)
            customer_lookup_page.last_name_field.send_text(checked_user.last_name)
            customer_lookup_page.address_field.send_text(checked_user.address)
            customer_lookup_page.city_field.send_text(checked_user.city)
            customer_lookup_page.state_field.send_text(checked_user.state)
            customer_lookup_page.zip_code_field.send_text(checked_user.zip_code)
            customer_lookup_page.ssn_field.send_text(checked_user.ssn)

        with allure.step("Submit the form"):
            customer_lookup_page.find_my_login_info_button.click()

        with allure.step("Check user is logged in"):
            customer_lookup_page.greeting_text.assert_text(f"Welcome {checked_user.first_name} "
                                                           f"{checked_user.last_name}")

    @allure.title("User can't successfully lookup for credentials by submitting an empty form.")
    def test_lookup_with_empty_form(self, driver):
        with allure.step("Navigate to Customer Lookup page"):
            customer_lookup_page = CustomerLookupPage(driver)
            customer_lookup_page.open_page()
            customer_lookup_page.is_opened()

        with allure.step("Submit the form with empty fields"):
            customer_lookup_page.find_my_login_info_button.click()

        with allure.step("Check error message is displayed for each field left empty"):
            customer_lookup_page.errors_list.assert_error_count(7)

    @allure.title("User can't successfully lookup for credentials by leaving one of the fields empty.")
    def test_lookup_with_empty_random_field(self, driver):
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

        with allure.step("Log out"):
            register_page.log_out_link.click()
            home_page.is_opened()

        with allure.step("Navigate to Customer Lookup page"):
            home_page.forgot_login_link.click()
            customer_lookup_page = CustomerLookupPage(driver)
            customer_lookup_page.is_opened()

        with allure.step("Fill in all the required fields but one"):
            form_fields = {
                1: (customer_lookup_page.first_name_field, new_user.first_name),
                2: (customer_lookup_page.last_name_field, new_user.last_name),
                3: (customer_lookup_page.address_field, new_user.address),
                4: (customer_lookup_page.city_field, new_user.city),
                5: (customer_lookup_page.state_field, new_user.state),
                6: (customer_lookup_page.zip_code_field, new_user.zip_code),
                7: (customer_lookup_page.ssn_field, new_user.ssn)
            }
            no_fill_num = random.randint(1, 7)
            for i in range(1, 8):
                if i == no_fill_num:
                    continue
                else:
                    field, value = form_fields[i]
                    field.send_text(value)

        with allure.step("Submit the form with one empty field"):
            customer_lookup_page.find_my_login_info_button.click()

        with allure.step("Check error message is displayed"):
            field_errors = {
                1: (customer_lookup_page.first_name_error, "First name is required."),
                2: (customer_lookup_page.last_name_error, "Last name is required."),
                3: (customer_lookup_page.address_error, "Address is required."),
                4: (customer_lookup_page.city_error, "City is required."),
                5: (customer_lookup_page.state_error, "State is required."),
                6: (customer_lookup_page.zip_code_error, "Zip Code is required."),
                7: (customer_lookup_page.ssn_error, "Social Security Number is required.")
            }

            error_locator, error_text = field_errors[no_fill_num]
            error_locator.assert_text(error_text)

