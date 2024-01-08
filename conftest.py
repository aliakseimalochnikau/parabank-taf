import allure
import pytest
import requests
from selenium import webdriver
from src.config.links import Links


# Fixture that manages Chrome webdriver lifecycle
@pytest.fixture(scope="function")
@allure.title("Initialize driver")
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")
    prefs = {'autofill.profile_enabled': False}
    options.add_experimental_option('prefs', prefs)
    driver = webdriver.Chrome(options)
    yield driver
    with allure.step("Terminate driver"):
        driver.quit()


# Fixture that does a health check prior to a test run
@pytest.fixture(autouse=True, scope="session")
@allure.title("Health check request")
def health_check():
    url = Links.HOST
    response = requests.get(url)
    if not response.ok:
        pytest.xfail(reason=f"Health check failed with status code {response.status_code}")
