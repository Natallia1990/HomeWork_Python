from selenium.webdriver.common.by import By


class MainPage:
    def __init__(self, driver):
        self.driver = driver
        self.cart_link = (By.CLASS_NAME, "shopping_cart_link")

    def add_backpack_to_cart(self):
        backpack_button = (By.ID, "add-to-cart-sauce-labs-backpack")
        self.driver.find_element(*backpack_button).click()

    def add_tshirt_to_cart(self):
        tshirt_button = (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
        self.driver.find_element(*tshirt_button).click()

    def add_onesie_to_cart(self):
        onesie_button = (By.ID, "add-to-cart-sauce-labs-onesie")
        self.driver.find_element(*onesie_button).click()

    def go_to_cart(self):
        self.driver.find_element(*self.cart_link).click()
