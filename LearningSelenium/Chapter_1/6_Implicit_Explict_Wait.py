
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize the Chrome WebDriver
driver = webdriver.Chrome()

# Set an implicit wait of 10 seconds
driver.implicitly_wait(10)

# Open a webpage
driver.get('https://example.com')

# Attempt to locate an element
element = driver.find_element(By.ID,'example-id')
# Continue with further actions
# ...

driver.get('https://example.com')

try:
    # Set an explicit wait of up to 10 seconds for a specific condition
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'example-id'))
    )
    # Perform actions with the element
    # ...
finally:
    # Close the browser
    driver.quit()