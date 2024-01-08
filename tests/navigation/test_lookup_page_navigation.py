import allure
from src.pages.about_us_page import AboutUsPage
from src.pages.contact_page import ContactPage
from src.pages.customer_lookup_page import CustomerLookupPage
from src.pages.home_page import HomePage
from src.pages.register_page import RegisterPage


@allure.epic("PARA-15240: User registration and authentication")
@allure.feature("PARA-15265: Customer Lookup page navigation")
class TestCustomerLookupPageNavigation:

    # Basic navigation
    # =================================================================================
    @allure.severity("Normal")
    @allure.title("User can proceed from Customer Lookup page to Register page")
    def test_navigation_customer_lookup_to_register(self, driver):
        with allure.step("Open Customer Lookup page"):
            customer_lookup_page = CustomerLookupPage(driver)
            customer_lookup_page.open_page()
            customer_lookup_page.is_opened()

        with allure.step("Navigate to Register page via link"):
            customer_lookup_page.register_link.click()

        with allure.step("Check user is redirected to Register page"):
            register_page = RegisterPage(driver)
            register_page.is_opened()

    @allure.severity("Normal")
    @allure.title("User can proceed from Customer Lookup page to Contact page")
    def test_navigation_customer_lookup_to_contact(self, driver):
        with allure.step("Open Customer Lookup page"):
            customer_lookup_page = CustomerLookupPage(driver)
            customer_lookup_page.open_page()
            customer_lookup_page.is_opened()

        with allure.step("Navigate to Contact page via button"):
            customer_lookup_page.contact_button.click()

        with allure.step("Check user is redirected to Contact page"):
            contact_page = ContactPage(driver)
            contact_page.is_opened()

    @allure.severity("Normal")
    @allure.title("User can proceed from Customer Lookup page to About Us page")
    def test_navigation_customer_lookup_to_about_us(self, driver):
        with allure.step("Open Customer Lookup page"):
            customer_lookup_page = CustomerLookupPage(driver)
            customer_lookup_page.open_page()
            customer_lookup_page.is_opened()

        with allure.step("Navigate to About Us page via button"):
            customer_lookup_page.about_us_button.click()

        with allure.step("Check user is redirected to About Us page"):
            about_us_page = AboutUsPage(driver)
            about_us_page.is_opened()

    @allure.severity("Normal")
    @allure.title("User can proceed from Customer Lookup page to Home page")
    def test_navigation_customer_lookup_to_home(self, driver):
        with allure.step("Open Customer Lookup page"):
            customer_lookup_page = CustomerLookupPage(driver)
            customer_lookup_page.open_page()
            customer_lookup_page.is_opened()

        with allure.step("Proceed to Home page via button"):
            customer_lookup_page.home_button.click()

        with allure.step("Check user is redirected to Home page"):
            home_page = HomePage(driver)
            home_page.is_opened()
