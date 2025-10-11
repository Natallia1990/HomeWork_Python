import pytest
from selenium import webdriver
from CalcPage import CalcPage


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(4)
    yield driver
    driver.quit()


def test_calc_validation(driver):
    calc_page = CalcPage(driver)
    calc_page.open()
    calc_page.set_delay(45)
    calc_page.perform_calculation(7, "+", 8)
    calc_page.wait_for_result(15, timeout=45)

    result = calc_page.get_result()
    assert result == "15"
