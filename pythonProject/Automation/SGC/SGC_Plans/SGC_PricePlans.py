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




############################################## STANDRAD CARDS############################################################

class pricePlans(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(ChromeDriverManager().install())
        # cls.driver=webdriver.
        # Firefox(executable_path="C:/Users/PC 1/PycharmProjects/pythonProject/drivers/geckodriver")
        cls.driver.implicitly_wait(100)
        cls.driver.get("https://qa-sgc-web.azurewebsites.net/")
        cls.driver.maximize_window()
        cls.driver.find_element_by_xpath("/html/body/sgc-web/general-layout/div/div/div[3]/a[2]").click()  # login button
        cls.driver.find_element_by_xpath("/html/body/div/div/div[2]/form/div/div/div/div/div[2]/div[2]/span/div/div/div/div/div/div/div/div/div[2]/div/div[1]/div/input").send_keys("talhah")  # username
        cls.driver.find_element_by_xpath("/html/body/div/div/div[2]/form/div/div/div/div/div[2]/div[2]/span/div/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/input").send_keys("box1234....")  # password
        cls.driver.find_element_by_xpath("/html/body/div/div/div[2]/form/div/div/div/button").click()  # login button of login page
        cls.driver.find_element_by_xpath("/html/body/sgc-web/general-layout/div/app-dashboard/div/div/div/div/div[2]/a").click()  # start new submission
        cls.driver.find_element_by_xpath("/html/body/sgc-web/sgc-modal/div/div/terms-alert/div/label/span").click()  # terms and conditions check box
        cls.driver.find_element_by_xpath("/html/body/sgc-web/general-layout/div/checkout/div/checkout-order/div/div/select-expertise-tier/div/div/div").click()  # start your order
        r = random.choice(string.ascii_letters)
        cls.driver.find_element_by_xpath("/html/body/sgc-web/general-layout/div/checkout/div/checkout-order/div/div/add-items/div/div/div[1]/div/input").send_keys("joran")
        cls.driver.find_element_by_xpath("/html/body/sgc-web/general-layout/div/checkout/div/checkout-order/div/div/add-items/div/div/div[1]/p/a").click()  # click here to add you card

    def test_a_sd_dv_LessThan1500(self):
        declare_value = random.randrange(1, 1499)
        # declare value of card
        self.driver.find_element_by_xpath("/html/body/sgc-web/general-layout/div/checkout/div/checkout-order/div/div/add-items/div/div/div[3]/added-order-item/added-card-item/div/div[3]/input").send_keys(declare_value)
        self.driver.find_element_by_xpath("/html/body/sgc-web/general-layout/div/checkout/div/checkout-order/checkout-bottom-nav/div[2]/button").click()  # next button of step 2
        # self.driver.find_element_by_xpath("/html/body/sgc-web/general-layout/div/checkout/div/checkout-order/div/div/add-items/div/div/h2").click()#random click on step 2 heading to hit ip
        time.sleep(3)
        # 20-25 day plan
        standard = self.driver.find_element_by_xpath("/html/body/sgc-web/general-layout/div/checkout/div/checkout-order/div/div/select-plan/div/div/div[1]/div/h3[1]").text
        # 10 day plan
        express = self.driver.find_element_by_xpath("/html/body/sgc-web/general-layout/div/checkout/div/checkout-order/div/div/select-plan/div/div/div[2]/div/h3[1]").text
        # 5 day plan
        super_express = self.driver.find_element_by_xpath("/html/body/sgc-web/general-layout/div/checkout/div/checkout-order/div/div/select-plan/div/div/div[3]/div/h3[1]").text
        # 1-2 day plan
        immediate = self.driver.find_element_by_xpath("/html/body/sgc-web/general-layout/div/checkout/div/checkout-order/div/div/select-plan/div/div/div[4]/div/h3[1]").text

        print(standard)
        print(express)
        print(super_express)
        print(immediate)

        self.assertEqual(standard,"STANDARD")  # 20-25 day
        self.assertEqual(express,"EXPRESS")  # 10 day
        self.assertEqual(super_express,"SUPER EXPRESS")  # 5 day plan
        self.assertEqual(immediate,"IMMEDIATE")  # 1-2 day plan

        time.sleep(2)



    def test_b_sd_dv_lessthan3500(self):
        self.driver.implicitly_wait(100)
        declare_value = random.randrange(1500, 3499)
        # declare value of card
        self.driver.find_element_by_xpath("/html/body/sgc-web/general-layout/div/checkout/div/checkout-order/div/div/add-items/div/div/div[3]/added-order-item/added-card-item/div/div[3]/input").send_keys(declare_value)
        self.driver.find_element_by_xpath("/html/body/sgc-web/general-layout/div/checkout/div/checkout-order/checkout-bottom-nav/div[2]/button").click()  # next button of step 2
        # self.driver.find_element_by_xpath("/html/body/sgc-web/general-layout/div/checkout/div/checkout-order/div/div/add-items/div/div/h2").click()#random click on step 2 heading to hit ip
        time.sleep(2)
        # 5 day plan
        super_express = self.driver.find_element_by_xpath("/html/body/sgc-web/general-layout/div/checkout/div/checkout-order/div/div/select-plan/div/div/div[1]/div/h3[1]").text
        # 1-2 day plan
        immediate = self.driver.find_element_by_xpath("/html/body/sgc-web/general-layout/div/checkout/div/checkout-order/div/div/select-plan/div/div/div[2]/div/h3[1]").text

        print(super_express)
        print(immediate)

        self.assertEqual(super_express, "SUPER EXPRESS")  # 5 day plan
        self.assertEqual(immediate, "IMMEDIATE")  # 1-2 day plan
        time.sleep(2)

    def test_c_sd_deGreaterThan3500(self):
        self.driver.implicitly_wait(100)
        declare_value = random.randrange(5500, 9999999)
        # declare value of card
        self.driver.find_element_by_xpath("/html/body/sgc-web/general-layout/div/checkout/div/checkout-order/div/div/add-items/div/div/div[3]/added-order-item/added-card-item/div/div[3]/input").send_keys(declare_value)
        self.driver.find_element_by_xpath("/html/body/sgc-web/general-layout/div/checkout/div/checkout-order/checkout-bottom-nav/div[2]/button").click()  # next button of step 2
        # self.driver.find_element_by_xpath("/html/body/sgc-web/general-layout/div/checkout/div/checkout-order/div/div/add-items/div/div/h2").click()#random click on step 2 heading to hit ip
        time.sleep(2)
        # 1-2 day plan
        immediate = self.driver.find_element_by_xpath("/html/body/sgc-web/general-layout/div/checkout/div/checkout-order/div/div/select-plan/div/div/div/div/h3[1]").text

        # print(super_express)
        print(immediate)
        self.assertEqual(immediate, "IMMEDIATE")  # 1-2 day plan
        time.sleep(2)



############################################# oversized cards###########################################################
    def test_d_dv_ovLessThan3500(self):
        self.driver.find_element_by_xpath("/html/body/sgc-web/general-layout/div/checkout/div/checkout-order/div/div/add-items/div/div/div[3]/added-order-item/added-card-item/div/div[4]/label[2]/span").click()  # oversized check box of card
        self.driver.implicitly_wait(100)
        declare_value = random.randrange(1, 3499)
        # declare value of card
        self.driver.find_element_by_xpath("/html/body/sgc-web/general-layout/div/checkout/div/checkout-order/div/div/add-items/div/div/div[3]/added-order-item/added-card-item/div/div[3]/input").send_keys(declare_value)
        self.driver.find_element_by_xpath("/html/body/sgc-web/general-layout/div/checkout/div/checkout-order/checkout-bottom-nav/div[2]/button").click()  # next button of step 2
        # self.driver.find_element_by_xpath("/html/body/sgc-web/general-layout/div/checkout/div/checkout-order/div/div/add-items/div/div/h2").click()#random click on step 2 heading to hit ip
        time.sleep(2)

        # 20-25 day plan
        standard = self.driver.find_element_by_xpath("/html/body/sgc-web/general-layout/div/checkout/div/checkout-order/div/div/select-plan/div/div/div[1]/div/h3[1]").text

        # 5 day plan
        super_express = self.driver.find_element_by_xpath("/html/body/sgc-web/general-layout/div/checkout/div/checkout-order/div/div/select-plan/div/div/div[2]/div/h3[1]").text

        print(super_express)
        print(standard)

        self.assertEqual(standard, "STANDARD")  # 20-25 day
        self.assertEqual(super_express, "SUPER EXPRESS")  # 1-2 day plan
        time.sleep(2)

    def test_e_ov_dv_greaterThan_3499(self):
        self.driver.find_element_by_xpath("/html/body/sgc-web/general-layout/div/checkout/div/checkout-order/div/div/add-items/div/div/div[3]/added-order-item/added-card-item/div/div[4]/label[2]/span").click()  # oversized check box of card
        self.driver.implicitly_wait(100)
        declare_value = random.randrange(3500, 9999999)
        # declare value of card
        self.driver.find_element_by_xpath("/html/body/sgc-web/general-layout/div/checkout/div/checkout-order/div/div/add-items/div/div/div[3]/added-order-item/added-card-item/div/div[3]/input").send_keys(declare_value)
        self.driver.find_element_by_xpath("/html/body/sgc-web/general-layout/div/checkout/div/checkout-order/checkout-bottom-nav/div[2]/button").click()  # next button of step 2
        # self.driver.find_element_by_xpath("/html/body/sgc-web/general-layout/div/checkout/div/checkout-order/div/div/add-items/div/div/h2").click()#random click on step 2 heading to hit ip
        time.sleep(2)

        # 5 day plan
        super_express = self.driver.find_element_by_xpath("/html/body/sgc-web/general-layout/div/checkout/div/checkout-order/div/div/select-plan/div/div/div/div/h3[1]").text

        print(super_express)
        self.assertEqual(super_express, "SUPER EXPRESS")  # 1-2 day plan
        time.sleep(2)


############################################# Reholders ###############################################################################

    def test_f_RE_lessThan_1500(self):

        self.driver.implicitly_wait(100)
        declare_value = random.randrange(1, 1499)
        # declare value of card
        self.driver.find_element_by_xpath("/html/body/sgc-web/general-layout/div/checkout/div/checkout-order/div/div/add-items/div/div/div[3]/added-order-item/added-card-item/div/div[3]/input").send_keys(declare_value)


        RE_Dropdown = self.driver.find_element_by_xpath("/html/body/sgc-web/general-layout/div/checkout/div/checkout-order/div/div/add-items/div/div/div[3]/added-order-item/added-card-item/div/div[5]/div/select") #dropdown
        RE = Select(RE_Dropdown)
        RE.select_by_index(3)

        self.driver.find_element_by_xpath("/html/body/sgc-web/general-layout/div/checkout/div/checkout-order/div/div/add-items/div/div/div[3]/added-order-item/added-card-item/div/div[6]/div[1]/div[2]/input").send_keys("1234567") #ssg certification code

        self.driver.find_element_by_xpath("/html/body/sgc-web/general-layout/div/checkout/div/checkout-order/div/div/add-items/div/div/div[3]/added-order-item/added-card-item/div/h3").click()#heading of card

        self.driver.find_element_by_xpath("/html/body/sgc-web/general-layout/div/checkout/div/checkout-order/checkout-bottom-nav/div[2]/button").click()  # next button of step 2
        # self.driver.find_element_by_xpath("/html/body/sgc-web/general-layout/div/checkout/div/checkout-order/div/div/add-items/div/div/h2").click()#random click on step 2 heading to hit ip
        time.sleep(2)

        # 20-25 day plan
        standard = self.driver.find_element_by_xpath("/html/body/sgc-web/general-layout/div/checkout/div/checkout-order/div/div/select-plan/div/div/div[1]/div/h3[1]").text

        # 5 day plan
        super_express = self.driver.find_element_by_xpath("/html/body/sgc-web/general-layout/div/checkout/div/checkout-order/div/div/select-plan/div/div/div[2]/div/h3[1]").text

        # 1-2 day plan
        immediate = self.driver.find_element_by_xpath("/html/body/sgc-web/general-layout/div/checkout/div/checkout-order/div/div/select-plan/div/div/div[3]/div/h3[1]").text

        print(standard,"\n",super_express,"\n",immediate)

        self.assertEqual(standard,"STANDARD")  # 20-25 day
        self.assertEqual(super_express,"SUPER EXPRESS")  # 5 day plan
        self.assertEqual(immediate,"IMMEDIATE")  # 1-2 day plan
        time.sleep(2)


    def test_g_RE_lessThan_7500(self):

        self.driver.implicitly_wait(100)
        declare_value = random.randrange(1500, 7499)
        # declare value of card
        self.driver.find_element_by_xpath("/html/body/sgc-web/general-layout/div/checkout/div/checkout-order/div/div/add-items/div/div/div[3]/added-order-item/added-card-item/div/div[3]/input").send_keys(declare_value)


        RE_Dropdown = self.driver.find_element_by_xpath("/html/body/sgc-web/general-layout/div/checkout/div/checkout-order/div/div/add-items/div/div/div[3]/added-order-item/added-card-item/div/div[5]/div/select") #dropdown
        RE = Select(RE_Dropdown)
        RE.select_by_index(3)

        self.driver.find_element_by_xpath("/html/body/sgc-web/general-layout/div/checkout/div/checkout-order/div/div/add-items/div/div/div[3]/added-order-item/added-card-item/div/div[6]/div[1]/div[2]/input").send_keys("1234567") #ssg certification code

        self.driver.find_element_by_xpath("/html/body/sgc-web/general-layout/div/checkout/div/checkout-order/div/div/add-items/div/div/div[3]/added-order-item/added-card-item/div/h3").click()#heading of card

        self.driver.find_element_by_xpath("/html/body/sgc-web/general-layout/div/checkout/div/checkout-order/checkout-bottom-nav/div[2]/button").click()  # next button of step 2
        # self.driver.find_element_by_xpath("/html/body/sgc-web/general-layout/div/checkout/div/checkout-order/div/div/add-items/div/div/h2").click()#random click on step 2 heading to hit ip
        time.sleep(2)


        # 5 day plan
        super_express = self.driver.find_element_by_xpath("/html/body/sgc-web/general-layout/div/checkout/div/checkout-order/div/div/select-plan/div/div/div[1]/div/h3[1]").text

        # 1-2 day plan
        immediate = self.driver.find_element_by_xpath("/html/body/sgc-web/general-layout/div/checkout/div/checkout-order/div/div/select-plan/div/div/div[2]/div/h3[1]").text

        print(super_express,"\n",immediate)

        self.assertEqual(super_express,"SUPER EXPRESS")  # 5 day plan
        self.assertEqual(immediate,"IMMEDIATE")  # 1-2 day plan
        time.sleep(2)


    def test_h_RE_greaterThan_7500(self):

        self.driver.implicitly_wait(100)
        declare_value = random.randrange(7500, 9999999)
        # declare value of card
        self.driver.find_element_by_xpath("/html/body/sgc-web/general-layout/div/checkout/div/checkout-order/div/div/add-items/div/div/div[3]/added-order-item/added-card-item/div/div[3]/input").send_keys(declare_value)


        RE_Dropdown = self.driver.find_element_by_xpath("/html/body/sgc-web/general-layout/div/checkout/div/checkout-order/div/div/add-items/div/div/div[3]/added-order-item/added-card-item/div/div[5]/div/select") #dropdown
        RE = Select(RE_Dropdown)
        RE.select_by_index(3)

        self.driver.find_element_by_xpath("/html/body/sgc-web/general-layout/div/checkout/div/checkout-order/div/div/add-items/div/div/div[3]/added-order-item/added-card-item/div/div[6]/div[1]/div[2]/input").send_keys("1234567") #ssg certification code

        self.driver.find_element_by_xpath("/html/body/sgc-web/general-layout/div/checkout/div/checkout-order/div/div/add-items/div/div/div[3]/added-order-item/added-card-item/div/h3").click()#heading of card

        self.driver.find_element_by_xpath("/html/body/sgc-web/general-layout/div/checkout/div/checkout-order/checkout-bottom-nav/div[2]/button").click()  # next button of step 2
        # self.driver.find_element_by_xpath("/html/body/sgc-web/general-layout/div/checkout/div/checkout-order/div/div/add-items/div/div/h2").click()#random click on step 2 heading to hit ip
        time.sleep(2)
        # 1-2 day plan
        immediate = self.driver.find_element_by_xpath("/html/body/sgc-web/general-layout/div/checkout/div/checkout-order/div/div/select-plan/div/div/div/div/h3[1]").text

        print(immediate)

        self.assertEqual(immediate,"IMMEDIATE")  # 1-2 day plan
        time.sleep(2)




    def test_i_OVRE_lessthan_1500(self):

        self.driver.implicitly_wait(100)
        declare_value = random.randrange(1, 1499)
        # declare value of card
        self.driver.find_element_by_xpath("/html/body/sgc-web/general-layout/div/checkout/div/checkout-order/div/div/add-items/div/div/div[3]/added-order-item/added-card-item/div/div[3]/input").send_keys(declare_value)


        RE_Dropdown = self.driver.find_element_by_xpath("/html/body/sgc-web/general-layout/div/checkout/div/checkout-order/div/div/add-items/div/div/div[3]/added-order-item/added-card-item/div/div[5]/div/select") #dropdown
        RE = Select(RE_Dropdown)
        RE.select_by_index(3)

        self.driver.find_element_by_xpath("/html/body/sgc-web/general-layout/div/checkout/div/checkout-order/div/div/add-items/div/div/div[3]/added-order-item/added-card-item/div/div[4]/label[2]/span").click()  # oversized check box of card

        self.driver.find_element_by_xpath("/html/body/sgc-web/general-layout/div/checkout/div/checkout-order/div/div/add-items/div/div/div[3]/added-order-item/added-card-item/div/div[6]/div[1]/div[2]/input").send_keys("1234567") #ssg certification code

        #self.driver.find_element_by_xpath("/html/body/sgc-web/general-layout/div/checkout/div/checkout-order/div/div/add-items/div/div/div[3]/added-order-item/added-card-item/div/h3").click()#heading of card
        time.sleep(1)
        self.driver.find_element_by_xpath("/html/body/sgc-web/general-layout/div/checkout/div/checkout-order/div/div/add-items/div/div/div[3]/added-order-item/added-card-item/div/div[3]/input")

        self.driver.find_element_by_xpath("/html/body/sgc-web/general-layout/div/checkout/div/checkout-order/checkout-bottom-nav/div[2]/button").click()  # next button of step 2
        # self.driver.find_element_by_xpath("/html/body/sgc-web/general-layout/div/checkout/div/checkout-order/div/div/add-items/div/div/h2").click()#random click on step 2 heading to hit ip
        time.sleep(2)

        #20-25 daylan
        standard=self.driver.find_element_by_xpath("/html/body/sgc-web/general-layout/div/checkout/div/checkout-order/div/div/select-plan/div/div/div[1]/div/h3[1]").text

        # 5 day plan
        super_express=self.driver.find_element_by_xpath("/html/body/sgc-web/general-layout/div/checkout/div/checkout-order/div/div/select-plan/div/div/div[2]/div/h3[1]").text

        self.assertEqual(standard, "STANDARD")  # 20-25 day
        self.assertEqual(super_express,"SUPER EXPRESS")  # 5 day plan
        time.sleep(2)


    def test_j_OVRE_greaterhan_1500(self):

        self.driver.implicitly_wait(100)
        declare_value = random.randrange(1500,999999)
        # declare value of card
        self.driver.find_element_by_xpath("/html/body/sgc-web/general-layout/div/checkout/div/checkout-order/div/div/add-items/div/div/div[3]/added-order-item/added-card-item/div/div[3]/input").send_keys(declare_value)


        RE_Dropdown = self.driver.find_element_by_xpath("/html/body/sgc-web/general-layout/div/checkout/div/checkout-order/div/div/add-items/div/div/div[3]/added-order-item/added-card-item/div/div[5]/div/select") #dropdown
        RE = Select(RE_Dropdown)
        RE.select_by_index(3)

        self.driver.find_element_by_xpath("/html/body/sgc-web/general-layout/div/checkout/div/checkout-order/div/div/add-items/div/div/div[3]/added-order-item/added-card-item/div/div[4]/label[2]/span").click()  # oversized check box of card

        self.driver.find_element_by_xpath("/html/body/sgc-web/general-layout/div/checkout/div/checkout-order/div/div/add-items/div/div/div[3]/added-order-item/added-card-item/div/div[6]/div[1]/div[2]/input").send_keys("1234567") #ssg certification code

        self.driver.find_element_by_xpath("/html/body/sgc-web/general-layout/div/checkout/div/checkout-order/div/div/add-items/div/div/div[3]/added-order-item/added-card-item/div/h3").click()#heading of card

        self.driver.find_element_by_xpath("/html/body/sgc-web/general-layout/div/checkout/div/checkout-order/checkout-bottom-nav/div[2]/button").click()  # next button of step 2
        # self.driver.find_element_by_xpath("/html/body/sgc-web/general-layout/div/checkout/div/checkout-order/div/div/add-items/div/div/h2").click()#random click on step 2 heading to hit ip
        time.sleep(2)


        # 5 day plan
        super_express=self.driver.find_element_by_xpath("/html/body/sgc-web/general-layout/div/checkout/div/checkout-order/div/div/select-plan/div/div/div/div/h3[1]").text

        self.assertEqual(super_express,"SUPER EXPRESS")  # 5 day plan
        time.sleep(2)



    def tearDown(self):
        self.driver.find_element_by_xpath("/html/body/sgc-web/general-layout/div/checkout/div/checkout-order/checkout-bottom-nav/button").click()#previous button of step 3
        self.driver.find_element_by_xpath("/html/body/sgc-web/general-layout/div/checkout/div/checkout-order/div/div/add-items/div/div/div[3]/added-order-item/added-card-item/div/div[1]/input").click()#delete button of any card
        r = random.choice(string.ascii_letters)
        self.driver.find_element_by_xpath("/html/body/sgc-web/general-layout/div/checkout/div/checkout-order/div/div/add-items/div/div/div[1]/div/input").send_keys("joran")
        self.driver.find_element_by_xpath("/html/body/sgc-web/general-layout/div/checkout/div/checkout-order/div/div/add-items/div/div/div[1]/p/a").click()  # click here to add you card


if __name__=='__main__':
 unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:/Users/PC 1/PycharmProjects/pythonProject/SGC_Plans/reports'))