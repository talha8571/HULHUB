import time
import requests
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import requests
import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

class vinfax(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(ChromeDriverManager().install())
        # Open the desired URL
        url = "https://vinfax-api.designitic.com/api/check-balance"
        cls.driver.get(url)

    def test_vinfax_url(self):
        # Get the current URL from the driver
        current_url = self.driver.current_url

        # Send a GET request to the URL using requests library
        response = requests.get(current_url)

        # Get the response content
        response_content = response.json()

        # Print the response content
        print(response_content)


if __name__ == '__main__':
    unittest.main()