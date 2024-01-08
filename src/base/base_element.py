import time
import pytest
from selenium.common import TimeoutException
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BaseElement:
    def __init__(self, driver, xpath):
        self.driver = driver
        self.xpath = xpath
        self.wait = WebDriverWait(self.driver, 15)

    def assert_element(self, clickable=False, return_many=False):
        self.wait.until(EC.presence_of_element_located(("xpath", self.xpath)))
        self.wait.until(EC.visibility_of_element_located(("xpath", self.xpath)))
        if clickable:
            self.wait.until(EC.element_to_be_clickable(("xpath", self.xpath)))
        if return_many:
            self.wait.until(EC.visibility_of_all_elements_located(("xpath", self.xpath)))
            result = self.driver.find_elements("xpath", self.xpath)
        else:
            result = self.driver.find_element("xpath", self.xpath)
        return result

    def click(self) -> None:
        element = self.assert_element(clickable=True)
        element.click()

    def send_text(self, value: str) -> None:
        element = self.assert_element(clickable=True)
        element.send_keys(value)

    def get_text(self) -> str:
        element = self.assert_element()
        return element.text

    def get_text_of_elements(self) -> list:
        elements = self.assert_element(return_many=True)
        return [element.text for element in elements]

    def select_by_index(self, index):
        select = Select(self.driver.find_element("xpath", self.xpath))
        select.select_by_index(index)

    def count_elements(self, correction=0) -> int:
        elements = self.assert_element(return_many=True)
        return len(elements) - correction

    def is_invisible(self):
        try:
            return self.wait.until(EC.invisibility_of_element_located(("xpath", self.xpath)))
        except TimeoutException:
            return None

    def is_visible(self):
        try:
            return self.wait.until(EC.visibility_of_element_located(("xpath", self.xpath)))
        except TimeoutException:
            return None

    def clear_contents(self):
        self.driver.find_element("xpath", self.xpath).clear()

    def assert_error(self, expected_error: str):
        server_error = "An internal error has occurred and has been logged."
        current_error = self.get_text()
        if server_error in current_error:
            pytest.xfail(reason="Known server-side issue")
        else:
            assert expected_error in current_error, f"Expected '{expected_error}' error, but got '{current_error}'."

    def assert_text(self, expected_text: str):
        current_text = None
        for _ in range(10):
            current_text = self.get_text()
            if current_text != '':
                break
            time.sleep(0.5)
        assert expected_text in current_text, (f"Expected '{expected_text}' message, but got "
                                               f"'{current_text}'.")

    def assert_error_count(self, expected_error_count: int):
        current_error_count = self.count_elements()
        assert expected_error_count == current_error_count, (f"Expected {expected_error_count} errors, but got "
                                                             f"{current_error_count}.")

    def assert_element_count(self, expected_element_count: int, correction=0):
        current_element_count = self.count_elements(correction)
        assert expected_element_count == current_element_count, (f"Expected {expected_element_count} elements, but got "
                                                                 f"{current_element_count}.")
