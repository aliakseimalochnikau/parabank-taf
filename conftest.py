import pytest
from selenium import webdriver


# Fixture that manages Chrome webdriver lifecycle
@pytest.fixture(scope="function")
def driver():
    options = webdriver.ChromeOptions()
    # options.add_argument("--headless")
    options.add_argument("--disable-popup-blocking")
    options.add_argument('--disable-save-password-bubble')
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")
    prefs = {'autofill.profile_enabled': False}
    options.add_experimental_option('prefs', prefs)
    with webdriver.Chrome(options) as driver:
        yield driver
