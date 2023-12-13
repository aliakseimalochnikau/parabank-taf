from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BaseElement:
    def __init__(self, driver, xpath):
        self.driver = driver
        self.xpath = xpath

    def assert_element(self, clickable=False, return_many=False):
        wait = WebDriverWait(self.driver, 15, 1)
        wait.until(EC.presence_of_element_located(("xpath", self.xpath)))
        wait.until(EC.visibility_of_element_located(("xpath", self.xpath)))
        if clickable:
            wait.until(EC.element_to_be_clickable(("xpath", self.xpath)))
        if return_many:
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

    def get_text(self) -> None:
        element = self.assert_element()
        return element.text

    def hover_over(self) -> None:
        element = self.assert_element(clickable=True)
        action = ActionChains(self.driver)
        action.move_to_element(element).perform()

    def count_elements(self):
        elements = self.assert_element(return_many=True)
        return len(elements)

