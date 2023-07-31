import unittest
from selenium import webdriver
from selenium import webdriver
import time
import string
import unittest
from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.select import Select
from selenium.webdriver import ActionChains
# from webdriver_manager.chrome import ChromeDriverManager
import HtmlTestRunner
from webdriver_manager.chrome import ChromeDriverManager
import random
import string
from colorama import Fore

import re

######## This code finds all the links present in the application

class broken(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(ChromeDriverManager().install())
        cls.driver.get("https://staging.beelinks.solutions/home")
        cls.driver.find_element_by_xpath("/html/body/app-root/div[2]/app-login/div[1]/div/form/div[1]/input").send_keys("talhahhulhub@gmail.com")
        cls.driver.find_element_by_xpath("/html/body/app-root/div[2]/app-login/div[1]/div/form/div[2]/input").send_keys("12345678")
        cls.driver.find_element_by_xpath("/html/body/app-root/div[2]/app-login/div[1]/div/form/button").click()
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(20)

    def test_a_brokenlinks(self):
        time.sleep(5)
        # Find all <a> tags in the page
        links = self.driver.find_elements_by_tag_name("a")
        # Extract the href attribute from each link
        link_urls = [link.get_attribute("href") for link in links]

        # Print the URLs
        for link_url in link_urls:
            print(link_url)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:/Users/1154-Talha/PycharmProjects/rts/Practice'))
