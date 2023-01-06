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
from PracticePOM.Pages.LoginPage import login
from PracticePOM.Pages.dashboard import dsh

class exer(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Chrome(ChromeDriverManager.install())
        cls.driver.get()
        cls.driver.implicitly_wait(30)
        cls.driver.maximize_window()


    def test_a_talhah(self):
        driver=self.driver
        a=dsh(driver)
        a.ping("fsf")

#
# if __name__ == '__main__':
#     unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="C:/Users/PC 1/PycharmProjects/pythonProject/PracticePOM/PracticeReports"))
#

























