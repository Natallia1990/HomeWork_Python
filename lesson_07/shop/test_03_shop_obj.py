import pytest
from selenium import webdriver
from LoginPage import LoginPage
from MainPage import MainPage
from CartPage import CartPage
from CheckoutPage import CheckoutPage


@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.implicitly_wait(5)
    yield driver
    driver.quit()


def test_shop_total_price(driver):
    login_page = LoginPage(driver)
    login_page.open_driver()
    login_page.login("standard_user", "secret_sauce")

    main_page = MainPage(driver)
    main_page.add_backpack_to_cart()
    main_page.add_tshirt_to_cart()
    main_page.add_onesie_to_cart()
    main_page.go_to_cart()

    cart_page = CartPage(driver)
    cart_page.click_checkout()

    checkout_page = CheckoutPage(driver)
    checkout_page.fill_customer_info("Наталья", "Клещенко", "220035")

    total_text = checkout_page.get_total_price()

    expected_total = "Total: $58.29"
    assert total_text == expected_total
