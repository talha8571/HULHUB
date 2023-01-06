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

    def test_a_card_grading(self):
        driver=self.driver
        self.driver.implicitly_wait(20)
        Card=cardgrading(driver)
        Card.clickcardgrading()

        text="55/45 or better centering, sharp focus, four sharp corners*, free of stains, no breaks in surface gloss, no print or refractor lines, and no visible wear. A slight print spot visible under close scrutiny is allowable if it does not detract from the aesthetics of the card."
        text2="55/45 or better centering, sharp focus, four sharp corners*, free of stains, no breaks in surface gloss, no print or refractor lines, and no visible wear. A slight print spot visible under close scrutiny is allowable if it does not detract from the aesthetics of the card."

        self.assertEqual(text,text2)

    def test_b_popreport(self):
        driver=self.driver
        self.driver.implicitly_wait(20)
        pop=popreport(driver)
        pop.search_pop("topps","t205","t206")#first method



    def test_c_certverification(self):
        driver=self.driver
        self.driver.implicitly_wait(30)
        Certv=certverification(driver)
        Certv.cert_verification("0453446")
        time.sleep(2)

        print("Cert code has been searched properly and user is able to click front and back images")

    def test_d_collectorSupport(self):
        driver=self.driver
        self.driver.implicitly_wait(20)
        cc=collectorSupport(driver)
        cc.collectorsupport("talhah", "talha858@gmail.com","this message is only for testing purpose")

        message_after_contatcusform_xpath=self.driver.find_element_by_xpath("/html/body/sgc-web/general-layout/div/static-layout/ng-component/contact-us/div[2]/div[2]/form/ul/li[5]/div/label").text
        expected_text="Message sent successfully."

        self.assertEqual(message_after_contatcusform_xpath,expected_text)

    def test_e_orderubmission(self):
        driver=self.driver
        self.driver.implicitly_wait(30)
        ordersub=ordersubmission(driver)
        ordersub.sdLessthan1500("jordan")
        ordersub.afteplan("ForQa") ##after assertion


    def test_f_profile(self):
        self.driver.implicitly_wait(20)
        driver=self.driver
        pro=profile(driver)
        pro.profile()
        time.sleep(2)
        pro.add_address("14879547542")
        time.sleep(2)


        # odp=self.driver.find_element_by_xpath("/html/body/sgc-web/general-layout/div/account-profile/div[2]/div[1]/div[4]/div[1]/h3")
        # # print("order preferences is displayed ",odp.is_displayed())
        # o=odp.is_displayed()
        # if o==True:
        #     print("my order preferencs is displayed")
        # else:
        #     print("my order preferencs is NOT displayed")
        #
        # communication_preferences=self.driver.find_element_by_xpath("/html/body/sgc-web/general-layout/div/account-profile/div[2]/div[2]/div/div[1]/h3")
        # ccc=communication_preferences.is_displayed()
        # if ccc==True:
        #     print("communication preferencs is displayed")
        # else:
        #     print("communication is NOT displayed")
        #
        #
        # reuqest_your_personal_data=self.driver.find_element_by_xpath("/html/body/sgc-web/general-layout/div/account-profile/div[2]/div[3]/div/div[1]/h3")
        # rr=reuqest_your_personal_data.is_displayed()
        # if rr==True:
        #     print("reuqest_your_personal_data is displayed")
        # else:
        #     print("reuqest_your_personal_data is NOT displayed")
        #
        #
        # cancel_request=self.driver.find_element_by_xpath("/html/body/sgc-web/general-layout/div/account-profile/div[2]/div[4]/div/div[1]/h3")
        # c_r=cancel_request.is_displayed()
        # if c_r==True:
        #     print("cancel_request is displayed")
        # else:
        #     print("cancel_request is NOT displayed")
        # time.sleep(5)
        # self.driver.execute_script("window.scrollTo(0,300)")
        # time.sleep(1)
        # self.driver.execute_script("window.scrollTo(300,600)")
        # time.sleep(1)
        # self.driver.execute_script("window.scrollTo(600,900)")
        # time.sleep(1)
        # self.driver.execute_script("window.scrollTo(900,0)")
        # time.sleep(3)

    def test_g_myorders(self):
        driver=self.driver
        self.driver.implicitly_wait(20)
        my=myorders(driver)
        my.mmorders()


    def test_h_paypallpayments(self):
        self.driver.implicitly_wait(30)
        driver=self.driver
        paypall_variable=PaypallPayments(driver)
        paypall_variable.paypall_method()

    def test_i_i_needhelp(self):
        driver=self.driver
        self.driver.implicitly_wait(20)
        nh=needhelp(driver)
        nh.needhelp("Talhha","talhah@kineticasysy.com","this message is only for testing")

    def test_j_SellerReady(self):
        self.driver.implicitly_wait(30)
        driver=self.driver
        sell=sellerReady(driver)
        sell.sellerReadypage()

        print(driver.current_window_handle)  # parent window
        handles = driver.window_handles  # return all the handle value of windows
        print(handles)
        for handle in handles:
            driver.switch_to.window(handle)
            print(driver.title)

        s = driver.current_window_handle
        print(s)
        time.sleep(3)
        self.driver.close()

# @classmethod
    # def tearDownClass(cls):
    #     cls.driver.close()

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="C:/Users/PC 1/PycharmProjects/pythonProject/SOM/Reports"))
