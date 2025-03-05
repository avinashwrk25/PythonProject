import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestExample(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://example.com")

    def test_title(self):
        driver = self.driver
        # Hard Assertion (Is actually Assert, And the test will stop if the step fails)
        self.assertEqual(driver.title, "Example Domain", "Title does not match")

    def test_element_presence(self):
        driver = self.driver
        # Soft Assertion (Is actually Verify, And the test will continue even if the step fails)
        try:
            element = driver.find_element(By.ID,"nonexistent-element")
            self.assertIsNotNone(element, "Element should be present")
        except AssertionError as e:
            print(f"Soft Assertion Failed: {e}")
        except Exception as e:
            print(f"Exception occurred: {e}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()