import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class LoginPage:
    """
    Page Object класс для страницы авторизации интернет-магазина.

    Предоставляет методы для открытия страницы
    и выполнения авторизации пользователя.
    """

    def __init__(self, driver: WebDriver) -> None:
        """
        Инициализация страницы авторизации.

        Args:
            driver: Экземпляр веб-драйвера для взаимодействия с браузером
        """
        self.driver = driver
        self.username_field = (By.ID, "user-name")
        self.password_field = (By.ID, "password")
        self.login_button = (By.ID, "login-button")

    @allure.step("Открыть страницу авторизации")
    def open_driver(self) -> None:
        """
        Открывает страницу авторизации интернет-магазина.

        Returns:
            None
        """
        self.driver.get("https://www.saucedemo.com/")

    @allure.step("Выполнить авторизацию с логином '{username}'")
    def login(self, username: str, password: str) -> None:
        """
        Выполняет авторизацию пользователя в системе.

        Args:
            username: Логин пользователя для авторизации
            password: Пароль пользователя для авторизации

        Returns:
            None
        """
        self.driver.find_element(*self.username_field).send_keys(username)
        self.driver.find_element(*self.password_field).send_keys(password)
        self.driver.find_element(*self.login_button).click()
