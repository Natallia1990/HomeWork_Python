import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.implicitly_wait(5)
    yield driver
    driver.quit()


def test_shop_total(driver):
    driver.get(
        "https://www.saucedemo.com/")

    driver.find_element(
        By.CSS_SELECTOR, "#user-name").send_keys("standard_user")
    driver.find_element(
        By.CSS_SELECTOR, "#password").send_keys("secret_sauce")
    driver.find_element(
        By.CSS_SELECTOR, "#login-button").click()

    driver.find_element(
        By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack").click()
    driver.find_element(
        By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt").click()
    driver.find_element(
        By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie").click()
    driver.find_element(
        By.CSS_SELECTOR, "a.shopping_cart_link").click()
    driver.find_element(
        By.CSS_SELECTOR, "#checkout").click()

    driver.find_element(
        By.CSS_SELECTOR, "#first-name").send_keys("Наталья")
    driver.find_element(
        By.CSS_SELECTOR, "#last-name").send_keys("Клещенко")
    driver.find_element(
        By.CSS_SELECTOR, "#postal-code").send_keys("220035")
    driver.find_element(
        By.CSS_SELECTOR, "#continue").click()

    WebDriverWait(driver, 10).until(
        ec.presence_of_element_located(
            (By.CSS_SELECTOR, ".summary_total_label"))
    )

    total_element = driver.find_element(
        By.CSS_SELECTOR, ".summary_total_label")
    total_text = total_element.text

    driver.quit()

    expected_total = "Total: $58.29"
    assert total_text == expected_total

    driver.quit()
