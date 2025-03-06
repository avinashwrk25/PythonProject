import pytest
from selenium import webdriver

@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_google_search(browser):
    browser.get("https://www.google.com")
    assert "Google" in browser.title