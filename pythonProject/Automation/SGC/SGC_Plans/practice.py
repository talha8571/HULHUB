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


class practice(unittest.TestCase):
    @classmethod
    def setUpclass(cls):
        cls.driver=webdriver(ChromeDriverManager.install())
        cls.driver.get("https??:hello.com")
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(20)

    def test_a(self):
        self.driver.find_element_by_xpath("hello")

    @classmethod
    def teardowmClass(cls):
        cls.driver.close()




if __name__=='__main__':
 unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:/Users/PC 1/PycharmProjects/pythonProject/SGC_Plans/reports'))
