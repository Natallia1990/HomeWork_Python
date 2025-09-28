from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("http://the-internet.herokuapp.com/login")

input_field = driver.find_element(By.ID, "username")
input_field.send_keys("tomsmith")
sleep(1)
input_field = driver.find_element(By.ID, "password")
input_field.send_keys("SuperSecretPassword!")

login_button = driver.find_element(By.CLASS_NAME, "radius")
login_button.click()
sleep(1)

success_message = driver.find_element(By.CLASS_NAME, "flash.success")
message_text = success_message.text.strip()

print(message_text)

driver.quit()
sleep(10)
