import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class CartPage:
    """
    Page Object класс для страницы корзины покупок.

    Предоставляет методы для взаимодействия
    с элементами корзины и перехода к оформлению заказа.
    """

    def __init__(self, driver: WebDriver) -> None:
        """
        Инициализация страницы корзины покупок.

        Args:
            driver: Экземпляр веб-драйвера для взаимодействия с браузером
        """
        self.driver = driver
        self.checkout_button = (By.ID, "checkout")

    @allure.step("Нажать кнопку оформления заказа")
    def click_checkout(self) -> None:
        """
        Нажимает кнопку для перехода к процессу оформления заказа.

        Returns:
            None
        """
        self.driver.find_element(*self.checkout_button).click()
