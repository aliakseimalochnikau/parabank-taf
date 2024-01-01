from src.base.base_element import BaseElement
from src.base.base_page import BasePage
from src.config.links import Links


class ContactPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

        # Page URL
        self.PAGE_URL = Links.CONTACT_PAGE

        # Fields and buttons
        self.name_field = BaseElement(driver, "//*[@id='name']")
        self.email_field = BaseElement(driver, "//*[@id='email']")
        self.phone_field = BaseElement(driver, "//*[@id='phone']")
        self.message_field = BaseElement(driver, "//*[@id='message']")
        self.send_to_customer_care_button = BaseElement(driver, "//*[@value='Send to Customer Care']")

        # Texts
        self.thank_you_text = BaseElement(driver, "//*[@id='rightPanel']//p[contains (text(), 'Thank you')]")

        # Errors
        self.name_error = BaseElement(driver, "//*[@id='name.errors']")
        self.email_error = BaseElement(driver, "//*[@id='email.errors']")
        self.phone_error = BaseElement(driver, "//*[@id='phone.errors']")
        self.message_error = BaseElement(driver, "//*[@id='message.errors']")


