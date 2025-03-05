from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
# Step 1) Open Firefox
browser = webdriver.Firefox()
# Step 2) Navigate to Facebook
browser.get("https://www.facebook.com")
# Step 3) Search & Enter the Email or Phone field & Enter Password
username = browser.find_element(By.ID,"email")
password = browser.find_element(By.ID,"pass")
submit   = browser.find_element(By.ID,"login button")
username.send_keys("PARLOURMAID")
password.send_keys("YOUR PASSWORD")
# Step 4) Click Login
submit.click()
wait = WebDriverWait( browser, 5 )
page_title = browser.title
assert page_title == "Facebook"