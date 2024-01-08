import pytest
from selenium.common import NoSuchElementException


def block_checker(driver):
    try:
        if driver.find_element("xpath", "//*[text()='Sorry, you have been blocked']"):
            pytest.xfail(reason="Execution blocked by Cloudflare")
    except NoSuchElementException:
        pass
