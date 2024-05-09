from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Initialize WebDriver
driver = webdriver.Chrome()

# Open the website
driver.get("https://www.saucedemo.com/")

# Display cookies before login
print("Cookies before login:")
for cookie in driver.get_cookies():
    print(cookie)

# Login
username_input = driver.find_element(By.ID, "user-name")
password_input = driver.find_element(By.ID, "password")
login_button = driver.find_element(By.ID, "login-button")

username_input.send_keys("standard_user")
password_input.send_keys("secret_sauce")
login_button.click()

# Wait for login to complete
WebDriverWait(driver, 10).until(EC.url_contains("inventory.html"))

# Display cookies after login
print("\nCookies after login:")
for cookie in driver.get_cookies():
    print(cookie)

# Logout
menu_button = driver.find_element(By.CLASS_NAME, "bm-burger-button")
menu_button.click()

logout_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "logout_sidebar_link")))
logout_button.click()

# Wait for logout to complete
WebDriverWait(driver, 10).until(EC.url_contains("index.html"))

# Verify logout
assert "https://www.saucedemo.com/" in driver.current_url

# Close the browser
driver.quit()

