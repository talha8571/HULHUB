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
#from webdriver_manager.chrome import ChromeDriverManager
import HtmlTestRunner
from webdriver_manager.chrome import ChromeDriverManager
import random
import string
from Automation.Beelinks_Old.Pages.login import loginn
import re

class BL(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Chrome(ChromeDriverManager().install())
        cls.driver.get("https://staging.beelinks.solutions/")
        cls.driver.implicitly_wait(30)
        cls.driver.maximize_window()

    def test_a_login(self):
        driver=self.driver
        self.driver.implicitly_wait(20)
        lg=loginn(driver)
        lg.loginpage()

    def test_b_multiple(self):
            x = 0
            while x <= 2:
                a=["xyz@gmail.com","xyz@gmail3443.com","xyz@gmail343434.com" ]
                b=[12451,15113,154641]


                #
                self.driver.find_element_by_xpath("/html/body/app-root/div[2]/app-login/div[1]/div/form/div[1]/input").send_keys(a[x])
                self.driver.find_element_by_xpath("/html/body/app-root/div[2]/app-login/div[1]/div/form/div[2]/input").send_keys(b[x])
                time.sleep(2)
                self.driver.find_element_by_xpath("/html/body/app-root/div[2]/app-login/div[1]/div/form/div[1]/input").clear()
                self.driver.find_element_by_xpath("/html/body/app-root/div[2]/app-login/div[1]/div/form/div[2]/input").clear()


                x += 1




    @classmethod
    def tearDownClass(cls):
        time.sleep(3)
        cls.driver.close()

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="C:/Users/1154-Talha/PycharmProjects/pythonProject/Automation/Beelinks_Old/Report"))
