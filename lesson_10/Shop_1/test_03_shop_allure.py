import pytest
import allure
from selenium import webdriver
from LoginPageAllure import LoginPage
from MainPageAllure import MainPage
from CartPageAllure import CartPage
from CheckoutPageAllure import CheckoutPage


@pytest.fixture
def driver():
    """
    Фикстура для инициализации и закрытия браузера.

    Returns:
        webdriver.Firefox: Экземпляр драйвера Firefox
    """
    driver = webdriver.Firefox()
    driver.implicitly_wait(5)
    yield driver
    driver.quit()


@allure.title("Проверка общей стоимости товаров в корзине")
@allure.description("Тест проверяет расчет общей стоимости трех товаров:"
                    "рюкзака, футболки и комбинезона")
@allure.feature("Корзина покупок")
@allure.severity(allure.severity_level.CRITICAL)
def test_shop_total_price(driver):
    """
    Тест проверяет корректность расчета общей стоимости товаров в корзине.

    Args:
        driver: Фикстура с экземпляром веб-драйвера
    """
    with allure.step("Открыть страницу логина и авторизоваться"):
        login_page = LoginPage(driver)
        login_page.open_driver()
        login_page.login("standard_user", "secret_sauce")

    with allure.step("Добавить товары в корзину"):
        main_page = MainPage(driver)
        main_page.add_backpack_to_cart()
        main_page.add_tshirt_to_cart()
        main_page.add_onesie_to_cart()
        main_page.go_to_cart()

    with allure.step("Перейти к оформлению заказа"):
        cart_page = CartPage(driver)
        cart_page.click_checkout()

    with allure.step("Заполнить информацию о покупателе"):
        checkout_page = CheckoutPage(driver)
        checkout_page.fill_customer_info("Наталья", "Клещенко", "220035")

    with allure.step("Проверить общую стоимость"):
        total_text = checkout_page.get_total_price()
        expected_total = "Total: $58.29"

        with allure.step(f"Проверить что общая стоимость'{total_text}'"
                         f"равна ожидаемой '{expected_total}'"):
            assert total_text == expected_total, (
                f"Ожидалось: {expected_total},"
                f"Получено: {total_text}")
