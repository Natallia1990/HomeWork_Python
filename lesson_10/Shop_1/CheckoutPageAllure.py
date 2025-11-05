import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage:
    """
    Page Object класс для страницы оформления заказа.

    Предоставляет методы для заполнения информации
    о покупателе и получения общей стоимости заказа.
    """

    def __init__(self, driver: WebDriver) -> None:
        """
        Инициализация страницы оформления заказа.

        Args:
            driver: Экземпляр веб-драйвера для взаимодействия с браузером
        """
        self.driver = driver
        self.first_name_field = (By.ID, "first-name")
        self.last_name_field = (By.ID, "last-name")
        self.postal_code_field = (By.ID, "postal-code")
        self.continue_button = (By.ID, "continue")
        self.total_label = (By.CLASS_NAME, "summary_total_label")

    @allure.step("Заполнить информацию о покупателе:"
                 "имя '{first_name}',"
                 "фамилия '{last_name}',"
                 "индекс '{postal_code}'")
    def fill_customer_info(
            self, first_name: str, last_name: str, postal_code: str) -> None:
        """
        Заполняет форму с информацией о покупателе для оформления заказа.

        Args:
            first_name: Имя покупателя
            last_name: Фамилия покупателя
            postal_code: Почтовый индекс покупателя

        Returns:
            None
        """
        self.driver.find_element(
            *self.first_name_field).send_keys(first_name)
        self.driver.find_element(
            *self.last_name_field).send_keys(last_name)
        self.driver.find_element(
            *self.postal_code_field).send_keys(postal_code)
        self.driver.find_element(
            *self.continue_button).click()

    @allure.step("Получить общую стоимость заказа")
    def get_total_price(self) -> str:
        """
        Получает текст с общей стоимостью заказа после заполнения информации.

        Returns:
            str: Текст общей стоимости заказа (например, "Total: $58.29")
        """
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.total_label)
        )
        total_element = self.driver.find_element(*self.total_label)
        return total_element.text
