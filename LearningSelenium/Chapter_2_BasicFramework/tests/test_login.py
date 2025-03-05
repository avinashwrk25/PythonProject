import time
import os
import pytest
from selenium import webdriver
from pages.login_page import LoginPage
from utils.data_reader import read_test_data

@pytest.mark.parametrize("username,password",  read_test_data(os.path.join(os.path.dirname(__file__), '../data/test_data.csv')))
def test_login(username, password):
    driver = webdriver.Chrome()
    driver.get('https://demo.opencart.com/admin/index.php')
    time.sleep(60)
    login_page = LoginPage(driver)
    login_page.enter_username(username)
    login_page.enter_password(password)
    login_page.click_login()
    # Add assertions to verify successful login
    driver.quit()
