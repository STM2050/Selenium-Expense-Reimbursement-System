import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome('./chromedriver.exe')

driver.get("http://127.0.0.1:5500/Front-End-Expense-Reimbursement-System/index.html")
print(driver.title)

username_input = driver.find_element(By.ID, "username")

username_input.send_keys("bipul513")

password_input = driver.find_element(By.ID, "password")

password_input.send_keys("password")

login_button = driver.find_element(By.ID, "login")

login_button.click()

window_after = driver.window_handles[0]
driver.switch_to.window(window_after)
time.sleep(10)
driver.quit()