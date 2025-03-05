#driver.close(): Closes the current active browser window that the WebDriver is controlling. If it's the only open window, it effectively ends the session. However, if multiple windows or tabs are open, only the one in focus is closed, and the WebDriver session continues with the remaining windows.
#driver.quit(): Terminates the entire browser session, closing all open windows or tabs associated with the WebDriver. This method also ends the WebDriver session gracefully, ensuring all resources are released.

from selenium import webdriver
import time

# Initialize the Chrome WebDriver
driver = webdriver.Chrome()

# Open the first website
driver.get('https://www.example.com')
time.sleep(2)  # Wait for 2 seconds

# Open a new tab using JavaScript
driver.execute_script("window.open('https://www.secondexample.com');")
time.sleep(2)  # Wait for 2 seconds

# Switch to the new tab
driver.switch_to.window(driver.window_handles[1])
time.sleep(2)  # Wait for 2 seconds

# Close the current tab (second website)
driver.close()
time.sleep(10)

# Switch back to the first tab
driver.switch_to.window(driver.window_handles[0])
time.sleep(2)  # Wait for 2 seconds

# Quit the browser and end the WebDriver session
driver.quit()