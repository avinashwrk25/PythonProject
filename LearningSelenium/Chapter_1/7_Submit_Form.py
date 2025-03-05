from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Initialize the Chrome WebDriver
driver = webdriver.Chrome()

# Open the webpage
driver.get('https://example.com/login')

# Locate the username and password fields
username_field = driver.find_element(By.ID, 'username')
password_field = driver.find_element(By.ID, 'password')

# Enter credentials
username_field.send_keys('your_username')
password_field.send_keys('your_password')

# Submit the form by pressing Enter in the password field
password_field.send_keys(Keys.RETURN)

# Alternatively, locate and click the submit button
submit_button = driver.find_element(By.ID, 'submit')
submit_button.click()

# Wait for a few seconds to observe the result
time.sleep(5)

# Close the browser
driver.quit()