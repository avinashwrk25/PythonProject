import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--headless") #to run script in headless mode
driver = webdriver.Chrome(options=options)

driver.get("https://www.google.com")
element = driver.find_element("xpath", "//*[@id='APjFqb']")
driver.save_screenshot("screenshot_2.png")
time.sleep(6)
driver.close()