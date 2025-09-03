import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

APP_URL = os.getenv("APP_URL", "http://localhost:5173")
username = "monica"
password = "123456"


@pytest.fixture(scope="function")
def driver():
    opts = Options()

    opts.add_argument("--window-size=1280,800")
    opts.set_capability("unhandledPromptBehavior", "dismiss and notify")
    d = webdriver.Chrome(options=opts)
    try:
        yield d
    finally:
        d.quit()


def test_login_with_username_and_password(driver):
    driver.get(APP_URL)

    username = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, 'input[placeholder="Username"]')
        )
    )
    password = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, 'input[type="password"][placeholder="Password"]')
        )
    )
    login_btn = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button.button-primary"))
    )

    username.clear()
    username.send_keys("monica")
    password.clear()
    password.send_keys("123456")
    login_btn.click()

    add_product = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            (By.XPATH, "//input[@placeholder= 'Product Name']")
        )
    )
    create_button = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            (By.XPATH, "//button[contains(text(), 'Create Product')]")
        )
    )

    add_product.send_keys("Apple")
    create_button.click()

    WebDriverWait(driver, 10).until(EC.url_contains("/dashboard"))
