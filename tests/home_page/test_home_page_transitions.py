import allure
from src.pages.about_us_page import AboutUsPage
from src.pages.customer_care_page import CustomerCarePage
from src.pages.customer_lookup_page import CustomerLookupPage
from src.pages.home_page import HomePage
from src.pages.register_page import RegisterPage


@allure.feature("Home page transitions")
class TestHomePageTransitions:
    @allure.title("User can proceed from Home page to Customer Lookup page")
    def test_transition_home_to_customer_lookup(self, driver):
        with allure.step("Navigate to Home page"):
            home_page = HomePage(driver)
            home_page.open_page()
            home_page.is_opened()

        with allure.step("Proceed to Customer Lookup page via link"):
            home_page.forgot_login_link.click()

        with allure.step("Check user is redirected to Customer Lookup page"):
            customer_lookup_page = CustomerLookupPage(driver)
            customer_lookup_page.is_opened()

    @allure.title("User can proceed from Home page to Register page")
    def test_transition_home_to_register(self, driver):
        with allure.step("Navigate to Home page"):
            home_page = HomePage(driver)
            home_page.open_page()
            home_page.is_opened()

        with allure.step("Proceed to Register page via link"):
            home_page.register_link.click()

        with allure.step("Check user is redirected to Register page"):
            register_page = RegisterPage(driver)
            register_page.is_opened()

    @allure.title("User can proceed from Home page to Customer Care page")
    def test_transition_home_to_customer_care(self, driver):
        with allure.step("Navigate to Home page"):
            home_page = HomePage(driver)
            home_page.open_page()
            home_page.is_opened()

        with allure.step("Proceed to Customer Care page via button"):
            home_page.contact_button.click()

        with allure.step("Check user is redirected to Customer Care page"):
            customer_care_page = CustomerCarePage(driver)
            customer_care_page.is_opened()

    @allure.title("User can proceed from Home page to About Us page")
    def test_transition_home_to_about_us(self, driver):
        with allure.step("Navigate to Home page"):
            home_page = HomePage(driver)
            home_page.open_page()
            home_page.is_opened()

        with allure.step("Proceed to About Us page via button"):
            home_page.about_us_button.click()

        with allure.step("Check user is redirected to About Us page"):
            about_us_page = AboutUsPage(driver)
            about_us_page.is_opened()

