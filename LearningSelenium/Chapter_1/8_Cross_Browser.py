import unittest
from selenium import webdriver

class CrossBrowserTest(unittest.TestCase):

    def setUp(self):
        # Define the browsers to test
        self.browsers = ['chrome', 'firefox', 'edge']
        self.drivers = []

        for browser in self.browsers:
            if browser == 'chrome':
                driver = webdriver.Chrome()
            elif browser == 'firefox':
                driver = webdriver.Firefox()
            elif browser == 'edge':
                driver = webdriver.Edge()
            else:
                raise ValueError(f'Browser "{browser}" is not supported.')
            self.drivers.append(driver)

    def test_example(self):
        for driver in self.drivers:
            driver.get('https://google.com')
            self.assertIn('google', driver.title)

    def tearDown(self):
        for driver in self.drivers:
            driver.quit()

if __name__ == '__main__':
    unittest.main()