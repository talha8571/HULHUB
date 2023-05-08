# -*- coding: utf-8 -*-

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
from globalsqa.Pages.hulhubdropdown import dropdownhulhub
from globalsqa.Pages.new_window import new_window
from colorama import Fore

class SQA(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Chrome(ChromeDriverManager().install())
        cls.driver.get("https://www.globalsqa.com/demo-site/")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()


    def test_a_tabs(self):
        driver=self.driver
        driver.implicitly_wait(30)
        fts=firststep_tabs(driver)
        fts.clicking()

        # a=ActionChains(driver)
        # a.key_down(Keys.CONTROL).send_keys(Keys.END).keys_up(Keys.CONTROL).perform()


    def test_b_slider(self):
        driver=self.driver
        self.driver.get("https://www.globalsqa.com/demo-site/sliders/")
        driver.implicitly_wait(20)
        s=sliders(driver)
        time.sleep(2)
        s.slider_execution_rgb() ##first function

        self.driver.switch_to.default_content()
        #
        s.double_slider_execution()#second method for double slider

    def test_c_tooltip(self):

        driver=self.driver
        self.driver.get("https://www.globalsqa.com/demo-site/tooltip/")
        self.driver.implicitly_wait(20)
        tp=Tooltip(driver)
        tp.tooltip_method()

        time.sleep(2)

    def test_d_drag_and_drop(self):
        driver=self.driver
        self.driver.get("https://www.globalsqa.com/demo-site/draganddrop/")
        driver.implicitly_wait(20)
        dd=dragdrop(driver)
        dd.draganddrop_method()##method one
        time.sleep(2)

        driver.switch_to.default_content()
        time.sleep(1)
        dd.drag_drop_by_ofset()#method 2
    #

    def test_hulhub_dropdown(self):
        driver=self.driver
        self.driver.implicitly_wait(30)
        driver.get("https://www.hulhub.com/products")

        hl=dropdownhulhub(driver)
        dp=self.driver.find_element_by_xpath(hl.dropdown_xpath)
        driver.execute_script("arguments[0].scrollIntoView();", dp)
        hl.xyz()


        list=self.driver.find_element_by_xpath("/html/body/div[1]/main/section[3]/div/div/div[2]/form/div[1]/div[3]/div/div/div/ul/li[1]")

        malaysia=self.driver.find_element_by_xpath("/html/body/div/main/section[3]/div/div/div[2]/form/div[1]/div[3]/div/div/div/ul/li[130]").text
        malaysia1=self.driver.find_element_by_xpath("/html/body/div/main/section[3]/div/div/div[2]/form/div[1]/div[3]/div/div/div/ul/li[130]")




        # Perform an action to bring the list element into view
        actions = ActionChains(driver)
        actions.move_to_element(list)
        actions.perform()

        s=1

        while s<=244:
            country=self.driver.find_element_by_xpath(f'/html/body/div/main/section[3]/div/div/div[2]/form/div[1]/div[3]/div/div/div/ul/li[{s}]').text
            print(country.encode('utf-8').decode('ascii', 'ignore')+ "<br/>")
            # country_str=country_bytes.decode('utf-8')
            # print(country_str)
            if malaysia==country:
                # print(country.encode('utf-8').decode('ascii', 'ignore')+ "<br/>")
                # print("expected country ", country)
                print("expeccetd country = ", country.encode('utf-8').decode('ascii', 'ignore')+ "<br/>")
                #
                print("Desired Country Found!!!!!!!!!!!"+ "<br/>")
                break
            else:
                # Scroll down using the down arrow key
                actions = ActionChains(driver)
                actions.send_keys(Keys.ARROW_DOWN)
                actions.perform()


            s=s+1

        # Scroll down using the down arrow key
        actions = ActionChains(driver)
        actions.send_keys(Keys.END)
        actions.perform()

    def test_newwindow(self):
        driver=self.driver
        self.driver.get("https://www.globalsqa.com/demo-site/frames-and-windows/")
        nw=new_window(driver)
        nw.new_window_method()




    # @classmethod
    # def tearDownClass(cls):
    #     cls.driver.quit()





if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:/Users/1154-Talha/PycharmProjects/rts/globalsqa/Reports'))
