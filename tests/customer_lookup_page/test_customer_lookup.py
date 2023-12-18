import allure
import pytest
from src.pages.customer_lookup_page import CustomerLookupPage
from src.pages.home_page import HomePage
from src.pages.register_page import RegisterPage


@allure.feature("Customer Lookup")
class TestCustomerLookup:
    @pytest.mark.smoke
    @allure.title("User can successfully lookup for his credentials providing valid data")
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

        with (allure.step("Submit the form")):
            register_page.register_button.click()
            # Processing the case of existing username
            checked_user = register_page.re_generate_username(new_user)

        with allure.step("Check registration is successful"):
            register_page.welcome_username_text.assert_text(f"Welcome {checked_user.username}")

        with (allure.step("Log out")):
            register_page.log_out_link.click()
            home_page.is_opened()

        with (allure.step("Navigate to Customer Lookup page")):
            home_page.forgot_login_link.click()
            customer_lookup_page = CustomerLookupPage(driver)
            customer_lookup_page.is_opened()

        with (allure.step("Fill in lookup form")):
            customer_lookup_page.first_name_field.send_text(checked_user.first_name)
            customer_lookup_page.last_name_field.send_text(checked_user.last_name)
            customer_lookup_page.address_field.send_text(checked_user.address)
            customer_lookup_page.city_field.send_text(checked_user.city)
            customer_lookup_page.state_field.send_text(checked_user.state)
            customer_lookup_page.zip_code_field.send_text(checked_user.zip_code)
            customer_lookup_page.ssn_field.send_text(checked_user.ssn)

        with (allure.step("Submit the form")):
            customer_lookup_page.find_my_login_info_button.click()

        with allure.step("Check user is logged in"):
            customer_lookup_page.greeting_text.assert_text(f"Welcome {checked_user.first_name} "
                                                           f"{checked_user.last_name}")
