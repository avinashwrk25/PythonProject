import time
from selenium import webdriver #importing  selenium  webdriver
from selenium.webdriver.chrome.service import Service #Locate chromedriver to connect with Chrome browser

s = Service('C:/browserdriver/chromedriver.exe')
driver = webdriver.Chrome(service=s) #initiating chrome driver

driver.get("https://www.google.com")
time.sleep(2)
driver.execute_script("window.open('');")
time.sleep(2)
driver.switch_to.window(driver.window_handles[1])
driver.get("https://demo.opencart.com/admin/index.php")
driver.save_screenshot("screenshot_1.png")
time.sleep(2)
driver.close()