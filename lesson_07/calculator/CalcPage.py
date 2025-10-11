from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class CalcPage:
    def __init__(self, driver):
        self.driver = driver
        self.delay_input = (By.CSS_SELECTOR, "#delay")
        self.screen = (By.CSS_SELECTOR, ".screen")
        self.button_template = "//span[text()='{}']"

    def open(self):
        self.driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/"
            "slow-calculator.html"
        )

    def set_delay(self, delay):
        delay_element = self.driver.find_element(*self.delay_input)
        delay_element.clear()
        delay_element.send_keys(str(delay))

    def click_button(self, button_text):
        button_locator = (By.XPATH, self.button_template.format(button_text))
        self.driver.find_element(*button_locator).click()

    def perform_calculation(self, num1, operator, num2):
        self.click_button(str(num1))
        self.click_button(operator)
        self.click_button(str(num2))
        self.click_button("=")

    def wait_for_result(self, expected_result, timeout=45):
        wait = WebDriverWait(self.driver, timeout)
        wait.until(
            ec.text_to_be_present_in_element(self.screen, str(expected_result))
        )

    def get_result(self):
        return self.driver.find_element(*self.screen).text
