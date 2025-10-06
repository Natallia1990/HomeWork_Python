import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture
def driver():
    driver = webdriver.Edge()
    driver.implicitly_wait(5)
    yield driver
    driver.quit()


def test_form_validation(driver):
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    driver.find_element(
        By.CSS_SELECTOR, "input[name='first-name']").send_keys("Иван")
    driver.find_element(
        By.CSS_SELECTOR, "input[name='last-name']").send_keys("Петров")
    driver.find_element(
        By.CSS_SELECTOR, "input[name='address']").send_keys("Ленина, 55-3")
    driver.find_element(
        By.CSS_SELECTOR, "input[name='e-mail']").send_keys("test@skypro.com")
    driver.find_element(
        By.CSS_SELECTOR, "input[name='phone']").send_keys("+7985899998787")
    driver.find_element(
        By.CSS_SELECTOR, "input[name='city']").send_keys("Москва")
    driver.find_element(
        By.CSS_SELECTOR, "input[name='country']").send_keys("Россия")
    driver.find_element(
        By.CSS_SELECTOR, "input[name='job-position']").send_keys("QA")
    driver.find_element(
        By.CSS_SELECTOR, "input[name='company']").send_keys("SkyPro")

    driver.find_element(
        By.CSS_SELECTOR, "button.btn.btn-outline-primary.mt-3").click()

    zip_code = driver.find_element(
        By.CSS_SELECTOR, "#zip-code").value_of_css_property("background-color")
    assert zip_code == "rgba(248, 215, 218, 1)"

    green_fields = [
        "first-name", "last-name", "address", "e-mail",
        "phone", "city", "country", "job-position", "company"
    ]

    for field_id in green_fields:
        field = driver.find_element(By.ID, field_id)
        assert field.value_of_css_property(
            "background-color") == "rgba(209, 231, 221, 1)"

    driver.quit()
