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
import re
from globalsqa.Pages.tabs import firststep_tabs
from globalsqa.Pages.slider import sliders
from globalsqa.Pages.tooltip import Tooltip
from globalsqa.Pages.draganddrop import dragdrop

class SQA(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Chrome(ChromeDriverManager().install())
        cls.driver.get("https://www.globalsqa.com/demo-site/")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()


    def test_tabs(self):
        driver=self.driver
        driver.implicitly_wait(30)
        fts=firststep_tabs(driver)
        fts.clicking()

        # a=ActionChains(driver)
        # a.key_down(Keys.CONTROL).send_keys(Keys.END).keys_up(Keys.CONTROL).perform()


    def test_slider(self):
        driver=self.driver
        driver.implicitly_wait(20)
        s=sliders(driver)
        time.sleep(2)
        s.slider_execution_rgb() ##first function

        # self.driver.switch_to_default_content()
        #
        # s.double_slider_execution()#second method for double slider

    def test_tooltip(self):

        driver=self.driver
        self.driver.get("https://www.globalsqa.com/demo-site/tooltip/")
        self.driver.implicitly_wait(20)
        tp=Tooltip(driver)
        tp.tooltip_method()

        time.sleep(2)

    def test_drag_and_drop(self):
        driver=self.driver
        self.driver.get("https://www.globalsqa.com/demo-site/draganddrop/")
        driver.implicitly_wait(20)
        dd=dragdrop(driver)
        # dd.draganddrop_method()##method one

        dd.drag_drop_by_ofset()#method 2
    #
    # @classmethod
    # def tearDownClass(cls):
    #     cls.driver.quit()

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="C:/Users/1154-Talha/PycharmProjects/rts/globalsqa/Reports"))
