from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.get("http://uitestingplayground.com/textinput")

input_field = driver.find_element(By.CSS_SELECTOR, "#newButtonName")
input_field.send_keys("SkyPro")

driver.find_element(By.CSS_SELECTOR, "#updatingButton").click()

WebDriverWait(driver, 10).until(
    EC.text_to_be_present_in_element((By.ID, "updatingButton"), "SkyPro")
)

updated_button = driver.find_element(By.CSS_SELECTOR, "#updatingButton")
txt = updated_button.text
print(txt)

driver.quit()
