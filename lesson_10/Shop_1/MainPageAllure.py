import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class MainPage:
    """
    Page Object класс для главной страницы интернет-магазина.

    Предоставляет методы для взаимодействия
    с товарами и корзиной на главной странице.
    """

    def __init__(self, driver: WebDriver) -> None:
        """
        Инициализация главной страницы.

        Args:
            driver: Экземпляр веб-драйвера для взаимодействия с браузером
        """
        self.driver = driver
        self.cart_link = (By.CLASS_NAME, "shopping_cart_link")

    @allure.step("Добавить рюкзак 'Sauce Labs Backpack' в корзину")
    def add_backpack_to_cart(self) -> None:
        """
        Добавляет товар 'Sauce Labs Backpack' в корзину покупок.

        Returns:
            None
        """
        backpack_button = (By.ID, "add-to-cart-sauce-labs-backpack")
        self.driver.find_element(*backpack_button).click()

    @allure.step("Добавить футболку 'Sauce Labs Bolt T-Shirt' в корзину")
    def add_tshirt_to_cart(self) -> None:
        """
        Добавляет товар 'Sauce Labs Bolt T-Shirt' в корзину покупок.

        Returns:
            None
        """
        tshirt_button = (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
        self.driver.find_element(*tshirt_button).click()

    @allure.step("Добавить комбинезон 'Sauce Labs Onesie' в корзину")
    def add_onesie_to_cart(self) -> None:
        """
        Добавляет товар 'Sauce Labs Onesie' в корзину покупок.

        Returns:
            None
        """
        onesie_button = (By.ID, "add-to-cart-sauce-labs-onesie")
        self.driver.find_element(*onesie_button).click()

    @allure.step("Перейти в корзину покупок")
    def go_to_cart(self) -> None:
        """
        Переходит на страницу корзины покупок.

        Returns:
            None
        """
        self.driver.find_element(*self.cart_link).click()
