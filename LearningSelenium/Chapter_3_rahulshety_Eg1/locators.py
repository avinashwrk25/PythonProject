import time
import pytest
from selenium import webdriver #importing  selenium  webdriver
from selenium.webdriver.chrome.service import Service #Locate chromedriver to connect with Chrome browser
from selenium.webdriver.common.by import By

s = Service('C:/browserdriver/chromedriver.exe')
driver = webdriver.Chrome(service=s) #initiating chrome driver


driver.get("https://rahulshettyacademy.com/angularpractice/")

# ID, Xpath, CSSSelactor, Classname, name, linkText
driver.find_element(By.CSS_SELECTOR,"div[class='form-group'] input[name='name']").send_keys("Abhi")
driver.find_element(By.NAME,'email').send_keys("xyz@gmail.com")
driver.find_element(By.ID,'exampleInputPassword1').send_keys("123456")
driver.find_element(By.ID,'exampleCheck1').click()
driver.find_element(By.XPATH,"(//input[@type='text'])[3]").send_keys("Hellow again")
time.sleep(2)

driver.find_element(By.XPATH,"//input[@value='Submit']").click()
message = driver.find_element(By.CLASS_NAME, "alert-success").text
print(message)
assert "Success" in message
driver.find_element(By.XPATH,"(//input[@type='text'])[3]").send_keys("Hellow again")
