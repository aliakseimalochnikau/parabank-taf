import allure

from src.pages.home_page.about_us_page import AboutUsPage
from src.pages.home_page.customer_care_page import CustomerCarePage
from src.pages.home_page.customer_lookup_page import CustomerLookupPage
from src.pages.home_page.home_page import HomePage
from src.pages.home_page.register_page import RegisterPage


@allure.feature("Register page transitions")
class TestRegisterPageTransitions:
    @allure.title("User can proceed from Register page to Customer Lookup page")
    def test_transition_register_to_customer_lookup(self, driver):
        with allure.step("Navigate to Register page"):
            register_page = RegisterPage(driver)
            register_page.open_page()
            register_page.is_opened()

        with allure.step("Proceed to Customer Lookup page via link"):
            register_page.forgot_login_link.click()

        with allure.step("Check user is redirected to Customer Lookup page"):
            customer_lookup_page = CustomerLookupPage(driver)
            expected_url = customer_lookup_page.PAGE_URL
            current_url = customer_lookup_page.get_current_url()
            assert expected_url in current_url, f"Expected '{expected_url}' URL, but got '{current_url}'."

    @allure.title("User can proceed from Register page to Customer Care page")
    def test_transition_register_to_customer_care(self, driver):
        with allure.step("Navigate to Register page"):
            register_page = RegisterPage(driver)
            register_page.open_page()
            register_page.is_opened()

        with allure.step("Proceed to Customer Care page via button"):
            register_page.contact_button.click()

        with allure.step("Check user is redirected to Customer Care page"):
            customer_care_page = CustomerCarePage(driver)
            expected_url = customer_care_page.PAGE_URL
            current_url = customer_care_page.get_current_url()
            assert expected_url in current_url, f"Expected '{expected_url}' URL, but got '{current_url}'."

    @allure.title("User can proceed from Register page to About Us page")
    def test_transition_register_to_about_us(self, driver):
        with allure.step("Navigate to Register page"):
            register_page = RegisterPage(driver)
            register_page.open_page()
            register_page.is_opened()

        with allure.step("Proceed to About Us page via button"):
            register_page.about_us_button.click()

        with allure.step("Check user is redirected to About Us page"):
            about_us_page = AboutUsPage(driver)
            expected_url = about_us_page.PAGE_URL
            current_url = about_us_page.get_current_url()
            assert expected_url in current_url, f"Expected '{expected_url}' URL, but got '{current_url}'."

    @allure.title("User can proceed from Register page to Home page")
    def test_transition_register_to_home(self, driver):
        with allure.step("Navigate to Register page"):
            register_page = RegisterPage(driver)
            register_page.open_page()
            register_page.is_opened()

        with allure.step("Proceed to Home page via button"):
            register_page.home_button.click()

        with allure.step("Check user is redirected to Home page"):
            home_page = HomePage(driver)
            expected_url = home_page.PAGE_URL
            current_url = home_page.get_current_url()
            assert expected_url in current_url, f"Expected '{expected_url}' URL, but got '{current_url}'."
