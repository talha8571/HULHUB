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
from Automation.SGC.SOM.Pages.CardGradingPage import cardgrading
from Automation.SGC.SOM.Pages.PopReportPage import popreport
from Automation.SGC.SOM.Pages.CertVerification import certverification
from Automation.SGC.SOM.Pages.CollectorSupport import collectorSupport
from Automation.SGC.SOM.Pages.Ordersubmission import ordersubmission
from Automation.SGC.SOM.Pages.Profile import profile
from Automation.SGC.SOM.Pages.SellerReady import sellerReady
from Automation.SGC.SOM.Pages.Myorders import myorders
from Automation.SGC.SOM.Pages.PayPallPayments import PaypallPayments
from Automation.SGC.SOM.Pages.needhelp import needhelp
import re


class plans(unittest.TestCase):

################# FOR DEV ##############################
    # @classmethod
    # def setUpClass(cls):
    #     cls.driver=webdriver.Chrome(ChromeDriverManager().install())
    #     cls.driver.implicitly_wait(30)
    #     cls.driver.get("https://dev-sgc-web.azurewebsites.net/")#for dev
    #     cls.driver.maximize_window()
    #     cls.driver.find_element_by_xpath("/html/body/sgc-web/general-layout/div/div/div[3]/a[2]").click()  # login button
    #     cls.driver.find_element_by_xpath("/html/body/div/div/div[2]/form/div/div/div[3]/span/div/div/div/div/div/div/div/div/div[2]/div[1]/div/input").send_keys("customerdev@kinetica.com")  # username for dev
    #     cls.driver.find_element_by_xpath("/html/body/div/div/div[2]/form/div/div/div[3]/span/div/div/div/div/div/div/div/div/div[2]/div[2]/div[1]/div/input").send_keys("box1234...")  # password for dev
    #     cls.driver.find_element_by_xpath("/html/body/div/div/div[2]/form/div/div/button").click() #for dev login button

#################### FOR QA ###########################
    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Chrome(ChromeDriverManager().install())
        cls.driver.implicitly_wait(30)
        cls.driver.get("https://qa-sgc-web.azurewebsites.net/")
        cls.driver.maximize_window()
        cls.driver.find_element_by_xpath("/html/body/sgc-web/general-layout/div/div/div[3]/a[2]").click()  # login button
        cls.driver.find_element_by_xpath("/html/body/div/div/div[2]/form/div/div/div/div/div[2]/div[2]/span/div/div/div/div/div/div/div/div/div[2]/div/div[1]/div/input").send_keys("customerqa@kinetica.com")  # username
        cls.driver.find_element_by_xpath("/html/body/div/div/div[2]/form/div/div/div/div/div[2]/div[2]/span/div/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/input").send_keys("Box1234....")  # password
        cls.driver.find_element_by_xpath("/html/body/div/div/div[2]/form/div/div/div/button").click()  # login button of login page QA



if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="C:/Users/PC 1/PycharmProjects/pythonProject/SOM/Reports"))
