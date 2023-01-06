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
from seleniumwire import webdriver
from Automation.Beelinks_New.Pages.dashboard import dshb
from Automation.Beelinks_New.Pages.login import llogin

from Automation.Beelinks_New.Pages.download import Dnld
from Automation.Beelinks_New.Pages.agenstscroll import scroll
import re
from selenium.webdriver.chrome.service import Service

import Automation.Beelinks_New.Pages.login

class HOV(unittest.TestCase):
    import Automation.Beelinks_New.Pages.login

    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Chrome(ChromeDriverManager().install())
        cls.driver.implicitly_wait(30)
        cls.driver.get("https://new.beelinks.solutions/login")
        # a = cls.driver.find_element_by_xpath
        cls.driver.maximize_window()
        cls.driver.find_element_by_xpath("/html/body/app-root/app-login/div/div/div/div/div[1]/div[2]/div[2]/form/div[1]/input").send_keys("qa.bizzchats@gmail.com")
        cls.driver.find_element_by_xpath("/html/body/app-root/app-login/div/div/div/div/div[1]/div[2]/div[2]/form/div[2]/div/input").send_keys("12345678")
        cls.driver.find_element_by_xpath("/html/body/app-root/app-login/div/div/div/div/div[1]/div[2]/div[2]/form/div[3]/button").click()




    def test_a_login(self):
        driver=self.driver
        self.driver.implicitly_wait(10)
        lg=llogin(driver)
        lg.invalid_login()

        # o=self.assertEqual("Email must be a valid email address",lg.vm)
        # print(o)










    # def test_a_hhh(self):
    #     s=self.driver.find_element_by_xpath("/html/body/app-root/app-login/div/div/div/div/div[1]/div[2]/div[2]/form/div[1]/input")
    #     print(s)
    #     self.driver.implicitly_wait(20)
    #     driver=self.driver
    #     hov1=dshb(driver)
    #     hov1.hovering()
    #     time.sleep(10)

    # def test_b_finl(self):
    #     driver=self.driver
    #     self.driver.implicitly_wait(20)
    #     dd=Dnld(driver)
    #     dd.file()
    #     time.sleep(20)
    #
    # def test_c_scc(self):
    #     self.driver.implicitly_wait(20)
    #     driver=self.driver
    #     sdc=scroll(driver)
    #     sdc.sc()
    #     time.sleep(5)
        
    # @classmethod
    # def tearDownClass(cls):
    #     cls.driver.close()
        
        
        
if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="C:/Users/1154-Talha/PycharmProjects/pythonProject/Automation/Beelinks_New/Report"))