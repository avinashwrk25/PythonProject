from selenium import webdriver
import pickle

# Initialize the WebDriver
driver = webdriver.Chrome()

# Navigate to the target website
driver.get('https://example.com')

# Add a cookie
driver.add_cookie({'name': 'session_id', 'value': '12345'})

# Retrieve and print all cookies
print(driver.get_cookies())

# Save cookies to a file
with open('cookies.pkl', 'wb') as file:
    pickle.dump(driver.get_cookies(), file)

# Delete all cookies
driver.delete_all_cookies()

# Load cookies from the file
with open('cookies.pkl', 'rb') as file:
    cookies = pickle.load(file)
    for cookie in cookies:
        driver.add_cookie(cookie)

# Verify the loaded cookies
print(driver.get_cookies())

# Close the WebDriver
driver.quit()