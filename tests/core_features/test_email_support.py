import allure
from src.config.data import ActiveUser
from src.pages.contact_page import ContactPage
from src.utils.empty_field_picker import fill_form_with_empty_random_field


@allure.epic("PARA-15243: User support")
@allure.feature("PARA-15280: Email support request")
class TestEmailSupportRequest:
    @allure.severity("Normal")
    @allure.title("User can successfully send email support request.")
    def test_successful_email_support_request(self, driver):
        with allure.step("Navigate to Customer Care page"):
            contact_page = ContactPage(driver)
            contact_page.open_page()
            contact_page.is_opened()

        with allure.step("Fill in request form"):
            contact_page.name_field.send_text(f"{ActiveUser.FIRST_NAME} {ActiveUser.LAST_NAME}")
            contact_page.email_field.send_text(ActiveUser.EMAIL)
            contact_page.phone_field.send_text(ActiveUser.PHONE_NUMBER)
            contact_page.message_field.send_text("Please, reach out to me asap.")

        with allure.step("Submit the form"):
            contact_page.send_to_customer_care_button.click()

        with allure.step("Check confirmation message is displayed"):
            contact_page.thank_you_text.assert_text(f"Thank you {ActiveUser.FIRST_NAME}")

    @allure.severity("Minor")
    @allure.title("User can't successfully send email support request by submitting an empty form.")
    def test_email_support_request_with_empty_form(self, driver):
        with allure.step("Navigate to Customer Care page"):
            contact_page = ContactPage(driver)
            contact_page.open_page()
            contact_page.is_opened()

        with allure.step("Submit the form with empty fields"):
            contact_page.send_to_customer_care_button.click()

        with allure.step("Check error message is displayed for each field left empty"):
            contact_page.errors_list.assert_error_count(4)

    @allure.severity("Minor")
    @allure.title("User can't successfully send email support request by leaving one of the fields empty.")
    def test_email_support_request_with_empty_random_field(self, driver):
        with allure.step("Navigate to Customer Care page"):
            contact_page = ContactPage(driver)
            contact_page.open_page()
            contact_page.is_opened()

        with allure.step("Fill in all the required fields but one"):
            form_fields = {
                1: (contact_page.name_field, ActiveUser.FIRST_NAME),
                2: (contact_page.email_field, ActiveUser.EMAIL),
                3: (contact_page.phone_field, ActiveUser.PHONE_NUMBER),
                4: (contact_page.message_field, "Please, reach out to me asap."),
            }
            no_fill_num = fill_form_with_empty_random_field(form_fields, number_of_fields=4)

        with allure.step("Submit the form with one empty field"):
            contact_page.send_to_customer_care_button.click()

        with allure.step("Check error message is displayed"):
            field_errors = {
                1: (contact_page.name_error, "Name is required."),
                2: (contact_page.email_error, "Email is required."),
                3: (contact_page.phone_error, "Phone is required."),
                4: (contact_page.message_error, "Message is required."),
            }
            error_locator, error_text = field_errors[no_fill_num]
            error_locator.assert_error(error_text)
