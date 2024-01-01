import allure
from src.pages.about_us_page import AboutUsPage
from src.pages.contact_page import ContactPage
from src.pages.customer_lookup_page import CustomerLookupPage
from src.pages.home_page import HomePage
from src.pages.register_page import RegisterPage


@allure.feature("Register page navigation")
class TestRegisterPageNavigation:

    # Basic navigation
    # =================================================================================
    @allure.title("User can proceed from Register page to Customer Lookup page")
    def test_navigation_register_to_customer_lookup(self, driver):
        with allure.step("Navigate to Register page"):
            register_page = RegisterPage(driver)
            register_page.open_page()
            register_page.is_opened()

        with allure.step("Proceed to Customer Lookup page via link"):
            register_page.forgot_login_link.click()

        with allure.step("Check user is redirected to Customer Lookup page"):
            customer_lookup_page = CustomerLookupPage(driver)
            customer_lookup_page.is_opened()

    @allure.title("User can proceed from Register page to Contact page")
    def test_navigation_register_to_contact(self, driver):
        with allure.step("Navigate to Register page"):
            register_page = RegisterPage(driver)
            register_page.open_page()
            register_page.is_opened()

        with allure.step("Proceed to Contact page via button"):
            register_page.contact_button.click()

        with allure.step("Check user is redirected to Contact page"):
            contact_page = ContactPage(driver)
            contact_page.is_opened()

    @allure.title("User can proceed from Register page to About Us page")
    def test_navigation_register_to_about_us(self, driver):
        with allure.step("Navigate to Register page"):
            register_page = RegisterPage(driver)
            register_page.open_page()
            register_page.is_opened()

        with allure.step("Proceed to About Us page via button"):
            register_page.about_us_button.click()

        with allure.step("Check user is redirected to About Us page"):
            about_us_page = AboutUsPage(driver)
            about_us_page.is_opened()

    @allure.title("User can proceed from Register page to Home page")
    def test_navigation_register_to_home(self, driver):
        with allure.step("Navigate to Register page"):
            register_page = RegisterPage(driver)
            register_page.open_page()
            register_page.is_opened()

        with allure.step("Proceed to Home page via button"):
            register_page.home_button.click()

        with allure.step("Check user is redirected to Home page"):
            home_page = HomePage(driver)
            home_page.is_opened()
