import pytest
from selenium import webdriver
from FormPage import FormPage


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(4)
    driver.maximize_window()
    yield driver
    driver.quit()


def test_form_validation(driver):
    form_page = FormPage(driver)
    form_page.open()
    form_page.fill_form()
    form_page.submit_form()


def check_form_submission(self):
    assert self.check_zip_code_error()
    assert self.check_fields_success()
