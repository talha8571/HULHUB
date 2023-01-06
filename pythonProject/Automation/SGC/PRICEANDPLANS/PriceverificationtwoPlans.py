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
        cls.driver.find_element_by_xpath("/html/body/div/div/div[2]/form/div/div/div/div/div[2]/div[2]/span/div/div/div/div/div/div/div/div/div[2]/div/div[1]/div/input").send_keys("customerqa@kinetica.com")  # username
        cls.driver.find_element_by_xpath("/html/body/div/div/div[2]/form/div/div/div/div/div[2]/div[2]/span/div/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/input").send_keys("Box1234....")  # password
        cls.driver.find_element_by_xpath("/html/body/div/div/div[2]/form/div/div/div/button").click()  # login button of login page
        cls.driver.find_element_by_xpath("/html/body/sgc-web/general-layout/div/app-dashboard/div/div/div/div/div[2]/a").click()  # start new submission
        cls.driver.find_element_by_xpath("/html/body/sgc-web/sgc-modal/div/div/terms-alert/div/label/span").click()  # terms and conditions check box
        cls.driver.find_element_by_xpath("/html/body/sgc-web/general-layout/div/checkout/div/checkout-order/div/div/select-expertise-tier/div/div/div").click()  # start your order
        r = random.choice(string.ascii_letters)
        cls.driver.find_element_by_xpath("/html/body/sgc-web/general-layout/div/checkout/div/checkout-order/div/div/add-items/div/div/div[1]/div/input").send_keys("jordan")
        cls.driver.find_element_by_xpath("/html/body/sgc-web/general-layout/div/checkout/div/checkout-order/div/div/add-items/div/div/div[1]/p/a").click()  # click here to add you card

    def test_a1_sd_dv_LessThan1500(self):
        declare_value = random.randrange(1, 1499)
        # declare value of card
        self.driver.find_element_by_xpath("/html/body/sgc-web/general-layout/div/checkout/div/checkout-order/div/div/add-items/div/div/div[3]/added-order-item/added-card-item/div/div[3]/input").send_keys(declare_value)
        self.driver.find_element_by_xpath("/html/body/sgc-web/general-layout/div/checkout/div/checkout-order/checkout-bottom-nav/div[2]/button").click()  # next button of step 2
        # self.driver.find_element_by_xpath("/html/body/sgc-web/general-layout/div/checkout/div/checkout-order/div/div/add-items/div/div/h2").click()#random click on step 2 heading to hit ip
        time.sleep(3)
        # 20-25 day plan
        standard_day = self.driver.find_element_by_xpath("/html/body/sgc-web/general-layout/div/checkout/div/checkout-order/div/div/select-plan/div/div/div[1]/div/h3[1]").text
        # 1-2 day plan
        immediate_day = self.driver.find_element_by_xpath("/html/body/sgc-web/general-layout/div/checkout/div/checkout-order/div/div/select-plan/div/div/div[2]/div/h3[1]").text

        #standard price
        standard_price=self.driver.find_element_by_xpath("/html/body/sgc-web/general-layout/div/checkout/div/checkout-order/div/div/select-plan/div/div/div[1]/div/h3[3]").text

        #immediate price
        immediate_price=self.driver.find_element_by_xpath("/html/body/sgc-web/general-layout/div/checkout/div/checkout-order/div/div/select-plan/div/div/div[2]/div/h3[3]").text

        print(standard_day)
        print(immediate_day)

        #assertion of plan
        self.assertEqual(standard_day,"STANDARD")  # 20-25 day
        self.assertEqual(immediate_day,"IMMEDIATE")  # 1-2 day plan

        print(standard_price)
        print(immediate_price)

        #assertion of price
        self.assertEqual(standard_price, "$30")  # 10 day
        self.assertEqual(immediate_price, "$125")  # 5 day plan

        time.sleep(2)



    def test_a2_sd_dv_lessthan3500(self):
        self.driver.implicitly_wait(100)
        declare_value = random.randrange(1500, 3499)
        # declare value of card
        self.driver.find_element_by_xpath("/html/body/sgc-web/general-layout/div/checkout/div/checkout-order/div/div/add-items/div/div/div[3]/added-order-item/added-card-item/div/div[3]/input").send_keys(declare_value)
        self.driver.find_element_by_xpath("/html/body/sgc-web/general-layout/div/checkout/div/checkout-order/checkout-bottom-nav/div[2]/button").click()  # next button of step 2
        # self.driver.find_element_by_xpath("/html/body/sgc-web/general-layout/div/checkout/div/checkout-order/div/div/add-items/div/div/h2").click()#random click on step 2 heading to hit ip
        time.sleep(2)
        # standard day
        standard_day = self.driver.find_element_by_xpath("/html/body/sgc-web/general-layout/div/checkout/div/checkout-order/div/div/select-plan/div/div/div[1]/div/h3[1]").text
        # immedaite day
        immediate_day = self.driver.find_element_by_xpath("/html/body/sgc-web/general-layout/div/checkout/div/checkout-order/div/div/select-plan/div/div/div[2]/div/h3[1]").text

        #standard price
        standard_price=self.driver.find_element_by_xpath("/html/body/sgc-web/general-layout/div/checkout/div/checkout-order/div/div/select-plan/div/div/div[1]/div/h3[3]").text

        #immediate price
        immediate_price=self.driver.find_element_by_xpath("/html/body/sgc-web/general-layout/div/checkout/div/checkout-order/div/div/select-plan/div/div/div[2]/div/h3[3]").text
        print(standard_day)
        print(immediate_day)

        self.assertEqual(standard_day, "STANDARD")  # 20-25 day plan
        self.assertEqual(immediate_day, "IMMEDIATE")  # 1-2 day plan

        print(standard_price)
        print(immediate_price)
        self.assertEqual(standard_price, "$85")  # 20-25 day plan
        self.assertEqual(immediate_price, "$125")  # 1-2 day plan

        time.sleep(2)

    def test_a3_sd_delessThan7500(self):
        self.driver.implicitly_wait(100)
        declare_value = random.randrange(3500, 7499)
        # declare value of card
        self.driver.find_element_by_xpath("/html/body/sgc-web/general-layout/div/checkout/div/checkout-order/div/div/add-items/div/div/div[3]/added-order-item/added-card-item/div/div[3]/input").send_keys(declare_value)
        self.driver.find_element_by_xpath("/html/body/sgc-web/general-layout/div/checkout/div/checkout-order/checkout-bottom-nav/div[2]/button").click()  # next button of step 2
        # self.driver.find_element_by_xpath("/html/body/sgc-web/general-layout/div/checkout/div/checkout-order/div/div/add-items/div/div/h2").click()#random click on step 2 heading to hit ip
        time.sleep(2)
        # 1-2 day plan
        immediate_day = self.driver.find_element_by_xpath("/html/body/sgc-web/general-layout/div/checkout/div/checkout-order/div/div/select-plan/div/div/div/div/h3[1]").text

        # print(super_express)
        print(immediate_day)
        self.assertEqual(immediate_day, "IMMEDIATE")  # 1-2 day plan
        time.sleep(2)
        immediate_price=self.driver.find_element_by_xpath("/html/body/sgc-web/general-layout/div/checkout/div/checkout-order/div/div/select-plan/div/div/div/div/h3[3]").text
        print("immediate price is",immediate_price)
        self.assertEqual(immediate_price, "$250")  # 1-2 day plan

    def test_a4_sd_delessThan20000(self):
        self.driver.implicitly_wait(100)
        declare_value = random.randrange(7500, 19999)
        # declare value of card
        self.driver.find_element_by_xpath("/html/body/sgc-web/general-layout/div/checkout/div/checkout-order/div/div/add-items/div/div/div[3]/added-order-item/added-card-item/div/div[3]/input").send_keys(declare_value)
        self.driver.find_element_by_xpath("/html/body/sgc-web/general-layout/div/checkout/div/checkout-order/checkout-bottom-nav/div[2]/button").click()  # next button of step 2
        # self.driver.find_element_by_xpath("/html/body/sgc-web/general-layout/div/checkout/div/checkout-order/div/div/add-items/div/div/h2").click()#random click on step 2 heading to hit ip
        time.sleep(2)
        # 1-2 day plan
        immediate_day = self.driver.find_element_by_xpath("/html/body/sgc-web/general-layout/div/checkout/div/checkout-order/div/div/select-plan/div/div/div/div/h3[1]").text

        # print(super_express)
        print(immediate_day)
        self.assertEqual(immediate_day, "IMMEDIATE")  # 1-2 day plan
        time.sleep(2)
        immediate_price=self.driver.find_element_by_xpath("/html/body/sgc-web/general-layout/div/checkout/div/checkout-order/div/div/select-plan/div/div/div/div/h3[3]").text
        print("immediate price is",immediate_price)
        self.assertEqual(immediate_price, "$500")  # 1-2 day plan


    def test_a5_sd_delessThan50000(self):
        self.driver.implicitly_wait(100)
        declare_value = random.randrange(20000, 49999)
        # declare value of card
        self.driver.find_element_by_xpath("/html/body/sgc-web/general-layout/div/checkout/div/checkout-order/div/div/add-items/div/div/div[3]/added-order-item/added-card-item/div/div[3]/input").send_keys(declare_value)
        self.driver.find_element_by_xpath("/html/body/sgc-web/general-layout/div/checkout/div/checkout-order/checkout-bottom-nav/div[2]/button").click()  # next button of step 2
        # self.driver.find_element_by_xpath("/html/body/sgc-web/general-layout/div/checkout/div/checkout-order/div/div/add-items/div/div/h2").click()#random click on step 2 heading to hit ip
        time.sleep(2)
        # 1-2 day plan
        immediate_day = self.driver.find_element_by_xpath("/html/body/sgc-web/general-layout/div/checkout/div/checkout-order/div/div/select-plan/div/div/div/div/h3[1]").text

        # print(super_express)
        print(immediate_day)
        self.assertEqual(immediate_day, "IMMEDIATE")  # 1-2 day plan
        time.sleep(2)
        immediate_price=self.driver.find_element_by_xpath("/html/body/sgc-web/general-layout/div/checkout/div/checkout-order/div/div/select-plan/div/div/div/div/h3[3]").text
        print("immediate price is",immediate_price)
        self.assertEqual(immediate_price, "$1,000")  # 1-2 day plan

    def test_a6_sd_delessThan100000(self):
        self.driver.implicitly_wait(100)
        declare_value = random.randrange(50000, 99999)
        # declare value of card
        self.driver.find_element_by_xpath("/html/body/sgc-web/general-layout/div/checkout/div/checkout-order/div/div/add-items/div/div/div[3]/added-order-item/added-card-item/div/div[3]/input").send_keys(declare_value)
        self.driver.find_element_by_xpath("/html/body/sgc-web/general-layout/div/checkout/div/checkout-order/checkout-bottom-nav/div[2]/button").click()  # next button of step 2
        # self.driver.find_element_by_xpath("/html/body/sgc-web/general-layout/div/checkout/div/checkout-order/div/div/add-items/div/div/h2").click()#random click on step 2 heading to hit ip
        time.sleep(2)
        # 1-2 day plan
        immediate_day = self.driver.find_element_by_xpath("/html/body/sgc-web/general-layout/div/checkout/div/checkout-order/div/div/select-plan/div/div/div/div/h3[1]").text

        # print(super_express)
        print(immediate_day)
        self.assertEqual(immediate_day, "IMMEDIATE")  # 1-2 day plan
        time.sleep(2)
        immediate_price=self.driver.find_element_by_xpath("/html/body/sgc-web/general-layout/div/checkout/div/checkout-order/div/div/select-plan/div/div/div/div/h3[3]").text
        print("immediate price is",immediate_price)
        self.assertEqual(immediate_price, "$2,000")  # 1-2 day plan


    def test_a7_sd_de100000(self):
        self.driver.implicitly_wait(100)
        declare_value = 100000
        # declare value of card
        self.driver.find_element_by_xpath("/html/body/sgc-web/general-layout/div/checkout/div/checkout-order/div/div/add-items/div/div/div[3]/added-order-item/added-card-item/div/div[3]/input").send_keys(declare_value)
        self.driver.find_element_by_xpath("/html/body/sgc-web/general-layout/div/checkout/div/checkout-order/checkout-bottom-nav/div[2]/button").click()  # next button of step 2
        # self.driver.find_element_by_xpath("/html/body/sgc-web/general-layout/div/checkout/div/checkout-order/div/div/add-items/div/div/h2").click()#random click on step 2 heading to hit ip
        time.sleep(2)
        # 1-2 day plan
        immediate_day = self.driver.find_element_by_xpath("/html/body/sgc-web/general-layout/div/checkout/div/checkout-order/div/div/select-plan/div/div/div/div/h3[1]").text

        # print(super_express)
        print(immediate_day)
        self.assertEqual(immediate_day, "IMMEDIATE")  # 1-2 day plan
        time.sleep(2)
        immediate_price=self.driver.find_element_by_xpath("/html/body/sgc-web/general-layout/div/checkout/div/checkout-order/div/div/select-plan/div/div/div/div/h3[3]").text
        print("immediate price is",immediate_price)
        self.assertEqual(immediate_price, "$3,750")  # 1-2 day plan




############################################ oversized cards###########################################################

    def test_b1_dv_ovLessThan3500(self):
        self.driver.find_element_by_xpath("/html/body/sgc-web/general-layout/div/checkout/div/checkout-order/div/div/add-items/div/div/div[3]/added-order-item/added-card-item/div/div[4]/label[2]/span").click()  # oversized check box of card
        self.driver.implicitly_wait(100)
        declare_value = random.randrange(1, 3499)
        # declare value of card
        self.driver.find_element_by_xpath("/html/body/sgc-web/general-layout/div/checkout/div/checkout-order/div/div/add-items/div/div/div[3]/added-order-item/added-card-item/div/div[3]/input").send_keys(declare_value)
        self.driver.find_element_by_xpath("/html/body/sgc-web/general-layout/div/checkout/div/checkout-order/checkout-bottom-nav/div[2]/button").click()  # next button of step 2
        # self.driver.find_element_by_xpath("/html/body/sgc-web/general-layout/div/checkout/div/checkout-order/div/div/add-items/div/div/h2").click()#random click on step 2 heading to hit ip
        time.sleep(2)

        # 20-25 day plan
        standard_day = self.driver.find_element_by_xpath("/html/body/sgc-web/general-layout/div/checkout/div/checkout-order/div/div/select-plan/div/div/div[1]/div/h3[1]").text
        # standard price
        standard_price = self.driver.find_element_by_xpath("/html/body/sgc-web/general-layout/div/checkout/div/checkout-order/div/div/select-plan/div/div/div/div/h3[3]").text

        print(standard_day)
        print(standard_price)

        #standard day
        self.assertEqual(standard_day, "STANDARD")  # 20-25 day
        #standard price
        self.assertEqual(standard_price, "$100")  # 1-2 day plan
        time.sleep(2)


    def test_b2_dv_ovLessThan7500(self):
        self.driver.find_element_by_xpath("/html/body/sgc-web/general-layout/div/checkout/div/checkout-order/div/div/add-items/div/div/div[3]/added-order-item/added-card-item/div/div[4]/label[2]/span").click()  # oversized check box of card
        self.driver.implicitly_wait(100)
        declare_value = random.randrange(3500, 7499)
        # declare value of card
        self.driver.find_element_by_xpath("/html/body/sgc-web/general-layout/div/checkout/div/checkout-order/div/div/add-items/div/div/div[3]/added-order-item/added-card-item/div/div[3]/input").send_keys(declare_value)
        self.driver.find_element_by_xpath("/html/body/sgc-web/general-layout/div/checkout/div/checkout-order/checkout-bottom-nav/div[2]/button").click()  # next button of step 2
        # self.driver.find_element_by_xpath("/html/body/sgc-web/general-layout/div/checkout/div/checkout-order/div/div/add-items/div/div/h2").click()#random click on step 2 heading to hit ip
        time.sleep(2)

        # 20-25 day plan
        standard_day = self.driver.find_element_by_xpath("/html/body/sgc-web/general-layout/div/checkout/div/checkout-order/div/div/select-plan/div/div/div[1]/div/h3[1]").text
        # standard price
        standard_price = self.driver.find_element_by_xpath("/html/body/sgc-web/general-layout/div/checkout/div/checkout-order/div/div/select-plan/div/div/div/div/h3[3]").text

        print(standard_day)
        print(standard_price)

        #standard day
        self.assertEqual(standard_day, "STANDARD")  # 20-25 day
        #standard price
        self.assertEqual(standard_price, "$250")  # 1-2 day plan
        time.sleep(2)


    def test_b3_dv_ovLessThan20000(self):
        self.driver.find_element_by_xpath("/html/body/sgc-web/general-layout/div/checkout/div/checkout-order/div/div/add-items/div/div/div[3]/added-order-item/added-card-item/div/div[4]/label[2]/span").click()  # oversized check box of card
        self.driver.implicitly_wait(100)
        declare_value = random.randrange(7500, 19999)
        # declare value of card
        self.driver.find_element_by_xpath("/html/body/sgc-web/general-layout/div/checkout/div/checkout-order/div/div/add-items/div/div/div[3]/added-order-item/added-card-item/div/div[3]/input").send_keys(declare_value)
        self.driver.find_element_by_xpath("/html/body/sgc-web/general-layout/div/checkout/div/checkout-order/checkout-bottom-nav/div[2]/button").click()  # next button of step 2
        # self.driver.find_element_by_xpath("/html/body/sgc-web/general-layout/div/checkout/div/checkout-order/div/div/add-items/div/div/h2").click()#random click on step 2 heading to hit ip
        time.sleep(2)

        # 20-25 day plan
        standard_day = self.driver.find_element_by_xpath("/html/body/sgc-web/general-layout/div/checkout/div/checkout-order/div/div/select-plan/div/div/div[1]/div/h3[1]").text
        # standard price
        standard_price = self.driver.find_element_by_xpath("/html/body/sgc-web/general-layout/div/checkout/div/checkout-order/div/div/select-plan/div/div/div/div/h3[3]").text

        print(standard_day)
        print(standard_price)

        #standard day
        self.assertEqual(standard_day, "STANDARD")  # 20-25 day
        #standard price
        self.assertEqual(standard_price, "$500")  # 1-2 day plan
        time.sleep(2)

    def test_b4_dv_ovLessThan50000(self):
        self.driver.find_element_by_xpath("/html/body/sgc-web/general-layout/div/checkout/div/checkout-order/div/div/add-items/div/div/div[3]/added-order-item/added-card-item/div/div[4]/label[2]/span").click()  # oversized check box of card
        self.driver.implicitly_wait(100)
        declare_value = random.randrange(20000, 49999)
        # declare value of card
        self.driver.find_element_by_xpath("/html/body/sgc-web/general-layout/div/checkout/div/checkout-order/div/div/add-items/div/div/div[3]/added-order-item/added-card-item/div/div[3]/input").send_keys(declare_value)
        self.driver.find_element_by_xpath("/html/body/sgc-web/general-layout/div/checkout/div/checkout-order/checkout-bottom-nav/div[2]/button").click()  # next button of step 2
        # self.driver.find_element_by_xpath("/html/body/sgc-web/general-layout/div/checkout/div/checkout-order/div/div/add-items/div/div/h2").click()#random click on step 2 heading to hit ip
        time.sleep(2)

        # 20-25 day plan
        standard_day = self.driver.find_element_by_xpath("/html/body/sgc-web/general-layout/div/checkout/div/checkout-order/div/div/select-plan/div/div/div[1]/div/h3[1]").text
        # standard price
        standard_price = self.driver.find_element_by_xpath("/html/body/sgc-web/general-layout/div/checkout/div/checkout-order/div/div/select-plan/div/div/div/div/h3[3]").text

        print(standard_day)
        print(standard_price)

        #standard day
        self.assertEqual(standard_day, "STANDARD")  # 20-25 day
        #standard price
        self.assertEqual(standard_price, "$1,000")  # 1-2 day plan
        time.sleep(2)

    def test_b5_dv_ovLessThan100000(self):
        self.driver.find_element_by_xpath("/html/body/sgc-web/general-layout/div/checkout/div/checkout-order/div/div/add-items/div/div/div[3]/added-order-item/added-card-item/div/div[4]/label[2]/span").click()  # oversized check box of card
        self.driver.implicitly_wait(100)
        declare_value = random.randrange(50000, 99999)
        # declare value of card
        self.driver.find_element_by_xpath("/html/body/sgc-web/general-layout/div/checkout/div/checkout-order/div/div/add-items/div/div/div[3]/added-order-item/added-card-item/div/div[3]/input").send_keys(declare_value)
        self.driver.find_element_by_xpath("/html/body/sgc-web/general-layout/div/checkout/div/checkout-order/checkout-bottom-nav/div[2]/button").click()  # next button of step 2
        # self.driver.find_element_by_xpath("/html/body/sgc-web/general-layout/div/checkout/div/checkout-order/div/div/add-items/div/div/h2").click()#random click on step 2 heading to hit ip
        time.sleep(2)

        # 20-25 day plan
        standard_day = self.driver.find_element_by_xpath("/html/body/sgc-web/general-layout/div/checkout/div/checkout-order/div/div/select-plan/div/div/div[1]/div/h3[1]").text
        # standard price
        standard_price = self.driver.find_element_by_xpath("/html/body/sgc-web/general-layout/div/checkout/div/checkout-order/div/div/select-plan/div/div/div/div/h3[3]").text

        print(standard_day)
        print(standard_price)

        #standard day
        self.assertEqual(standard_day, "STANDARD")  # 20-25 day
        #standard price
        self.assertEqual(standard_price, "$2,000")  # 1-2 day plan
        time.sleep(2)


    def test_b6_dv_100000(self):
        self.driver.find_element_by_xpath("/html/body/sgc-web/general-layout/div/checkout/div/checkout-order/div/div/add-items/div/div/div[3]/added-order-item/added-card-item/div/div[4]/label[2]/span").click()  # oversized check box of card
        self.driver.implicitly_wait(100)
        declare_value = 100000
        # declare value of card
        self.driver.find_element_by_xpath("/html/body/sgc-web/general-layout/div/checkout/div/checkout-order/div/div/add-items/div/div/div[3]/added-order-item/added-card-item/div/div[3]/input").send_keys(declare_value)
        self.driver.find_element_by_xpath("/html/body/sgc-web/general-layout/div/checkout/div/checkout-order/checkout-bottom-nav/div[2]/button").click()  # next button of step 2
        # self.driver.find_element_by_xpath("/html/body/sgc-web/general-layout/div/checkout/div/checkout-order/div/div/add-items/div/div/h2").click()#random click on step 2 heading to hit ip
        time.sleep(2)

        # 20-25 day plan
        standard_day = self.driver.find_element_by_xpath("/html/body/sgc-web/general-layout/div/checkout/div/checkout-order/div/div/select-plan/div/div/div[1]/div/h3[1]").text
        # standard price
        standard_price = self.driver.find_element_by_xpath("/html/body/sgc-web/general-layout/div/checkout/div/checkout-order/div/div/select-plan/div/div/div/div/h3[3]").text

        print(standard_day)
        print(standard_price)

        #standard day
        self.assertEqual(standard_day, "STANDARD")  # 20-25 day
        #standard price
        self.assertEqual(standard_price, "$3,750")  # 1-2 day plan
        time.sleep(2)









# ############################################# Reholders ###############################################################################
#
    def test_c1_RE_lessThan_1500(self):

        self.driver.implicitly_wait(10)
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
        standard_day = self.driver.find_element_by_xpath("/html/body/sgc-web/general-layout/div/checkout/div/checkout-order/div/div/select-plan/div/div/div[1]/div/h3[1]").text

        # 1-2 day plan
        immediate_day = self.driver.find_element_by_xpath("/html/body/sgc-web/general-layout/div/checkout/div/checkout-order/div/div/select-plan/div/div/div[2]/div/h3[1]").text

        print(standard_day,"\n",immediate_day)

        standard_price=self.driver.find_element_by_xpath("/html/body/sgc-web/general-layout/div/checkout/div/checkout-order/div/div/select-plan/div/div/div[1]/div/h3[3]").text
        immediate_price=self.driver.find_element_by_xpath("/html/body/sgc-web/general-layout/div/checkout/div/checkout-order/div/div/select-plan/div/div/div[2]/div/h3[3]").text

        self.assertEqual(standard_day,"STANDARD")  # 20-25 day
        self.assertEqual(immediate_day,"IMMEDIATE")  # 1-2 day plan

        self.assertEqual(standard_price,"$30")
        self.assertEqual(immediate_price,"$125")
        time.sleep(2)

#

    def test_c2_RE_lessThan_7500(self):

        self.driver.implicitly_wait(10)
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

        # 20-25 day plan
        standard_day = self.driver.find_element_by_xpath("/html/body/sgc-web/general-layout/div/checkout/div/checkout-order/div/div/select-plan/div/div/div[1]/div/h3[1]").text

        # 1-2 day plan
        immediate_day = self.driver.find_element_by_xpath("/html/body/sgc-web/general-layout/div/checkout/div/checkout-order/div/div/select-plan/div/div/div[2]/div/h3[1]").text

        print(standard_day,"\n",immediate_day)

        standard_price = self.driver.find_element_by_xpath("/html/body/sgc-web/general-layout/div/checkout/div/checkout-order/div/div/select-plan/div/div/div[1]/div/h3[3]").text
        immediate_price = self.driver.find_element_by_xpath("/html/body/sgc-web/general-layout/div/checkout/div/checkout-order/div/div/select-plan/div/div/div[2]/div/h3[3]").text

        self.assertEqual(standard_day,"STANDARD")  # 20-25 day
        self.assertEqual(immediate_day,"IMMEDIATE")  # 1-2 day plan

        self.assertEqual(standard_price,"$75")
        self.assertEqual(immediate_price,"$125")
        time.sleep(2)

    def test_c3_RE_greaterThan_7500(self):

        self.driver.implicitly_wait(10)
        declare_value = random.randrange(1, 14990000)
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
        immediate_day = self.driver.find_element_by_xpath("/html/body/sgc-web/general-layout/div/checkout/div/checkout-order/div/div/select-plan/div/div/div/div/h3[1]").text

        print(immediate_day)

        immediate_price = self.driver.find_element_by_xpath("/html/body/sgc-web/general-layout/div/checkout/div/checkout-order/div/div/select-plan/div/div/div/div/h3[3]").text

        self.assertEqual(immediate_day,"IMMEDIATE")  # 1-2 day plan

        self.assertEqual(immediate_price,"$125")
        time.sleep(2)





##########################   oversized reholders    ###################################################################################
    def test_d1_OVRE_lessthan_1500(self):

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
        standard_day=self.driver.find_element_by_xpath("/html/body/sgc-web/general-layout/div/checkout/div/checkout-order/div/div/select-plan/div/div/div[1]/div/h3[1]").text

        #standard price
        standard_price=self.driver.find_element_by_xpath("/html/body/sgc-web/general-layout/div/checkout/div/checkout-order/div/div/select-plan/div/div/div/div/h3[3]").text

        self.assertEqual(standard_day, "STANDARD")  # 20-25 day
        time.sleep(2)
        self.assertEqual(standard_price,"$100")


    def test_d2_OVRE_greaterhan_1500(self):

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

        # 20-25 daylan
        standard_day = self.driver.find_element_by_xpath("/html/body/sgc-web/general-layout/div/checkout/div/checkout-order/div/div/select-plan/div/div/div[1]/div/h3[1]").text

        # standard price
        standard_price = self.driver.find_element_by_xpath("/html/body/sgc-web/general-layout/div/checkout/div/checkout-order/div/div/select-plan/div/div/div/div/h3[3]").text

        self.assertEqual(standard_day, "STANDARD")  # 20-25 day
        time.sleep(2)
        self.assertEqual(standard_price, "$250")





########################################  Pre GRADING ####################################################################

    def test_e1_dvlessthan_1500(self):
        declare_value=random.randrange(1,1499)
        # declare value of card
        self.driver.find_element_by_xpath("/html/body/sgc-web/general-layout/div/checkout/div/checkout-order/div/div/add-items/div/div/div[3]/added-order-item/added-card-item/div/div[3]/input").send_keys(declare_value)

        pregrade=self.driver.find_element_by_xpath("/html/body/sgc-web/general-layout/div/checkout/div/checkout-order/div/div/add-items/div/div/div[3]/added-order-item/added-card-item/div/div[5]/div/select")
        pregrade_dropdown=Select(pregrade)
        pregrade_dropdown.select_by_value("Pre-Grade Encapsulation")


        sgc_pregrade_grade=self.driver.find_element_by_xpath("/html/body/sgc-web/general-layout/div/checkout/div/checkout-order/div/div/add-items/div/div/div[3]/added-order-item/added-card-item/div/div[6]/div[1]/div[2]/input[1]").send_keys("9MT")
        sgc_pregrade_grade_certcode=self.driver.find_element_by_xpath("/html/body/sgc-web/general-layout/div/checkout/div/checkout-order/div/div/add-items/div/div/div[3]/added-order-item/added-card-item/div/div[6]/div[1]/div[2]/input[2]").send_keys("123456")
        self.driver.find_element_by_xpath("/html/body/sgc-web/general-layout/div/checkout/div/checkout-order/checkout-bottom-nav/div[2]/button").click()  # next button of step 2
        # self.driver.find_element_by_xpath("/html/body/sgc-web/general-layout/div/checkout/div/checkout-order/div/div/add-items/div/div/h2").click()#random click on step 2 heading to hit ip
        time.sleep(3)
        # 20-25 day plan
        standard_day = self.driver.find_element_by_xpath("/html/body/sgc-web/general-layout/div/checkout/div/checkout-order/div/div/select-plan/div/div/div[1]/div/h3[1]").text
         # 1-2 day plan
        immediate_day = self.driver.find_element_by_xpath("/html/body/sgc-web/general-layout/div/checkout/div/checkout-order/div/div/select-plan/div/div/div[2]/div/h3[1]").text

        #standard price
        standard_price=self.driver.find_element_by_xpath("/html/body/sgc-web/general-layout/div/checkout/div/checkout-order/div/div/select-plan/div/div/div[1]/div/h3[3]").text

        #immediate price
        immediate_price=self.driver.find_element_by_xpath("/html/body/sgc-web/general-layout/div/checkout/div/checkout-order/div/div/select-plan/div/div/div[2]/div/h3[3]").text

        print(standard_day)
        print(immediate_day)

        #assertion of plan
        self.assertEqual(standard_day,"STANDARD")  # 20-25 day
        self.assertEqual(immediate_day,"IMMEDIATE")  # 1-2 day plan

        print(standard_price)
        print(immediate_price)

        #assertion of price
        self.assertEqual(standard_price, "$18")  # 10 day
        self.assertEqual(immediate_price, "$75")  # 5 day plan
        time.sleep(2)

    def test_e2_dvlessthan_3500(self):
        declare_value=random.randrange(1500,3499)
        # declare value of card
        self.driver.find_element_by_xpath("/html/body/sgc-web/general-layout/div/checkout/div/checkout-order/div/div/add-items/div/div/div[3]/added-order-item/added-card-item/div/div[3]/input").send_keys(declare_value)

        pregrade=self.driver.find_element_by_xpath("/html/body/sgc-web/general-layout/div/checkout/div/checkout-order/div/div/add-items/div/div/div[3]/added-order-item/added-card-item/div/div[5]/div/select")
        pregrade_dropdown=Select(pregrade)
        pregrade_dropdown.select_by_value("Pre-Grade Encapsulation")


        sgc_pregrade_grade=self.driver.find_element_by_xpath("/html/body/sgc-web/general-layout/div/checkout/div/checkout-order/div/div/add-items/div/div/div[3]/added-order-item/added-card-item/div/div[6]/div[1]/div[2]/input[1]").send_keys("9MT")
        sgc_pregrade_grade_certcode=self.driver.find_element_by_xpath("/html/body/sgc-web/general-layout/div/checkout/div/checkout-order/div/div/add-items/div/div/div[3]/added-order-item/added-card-item/div/div[6]/div[1]/div[2]/input[2]").send_keys("123456")
        self.driver.find_element_by_xpath("/html/body/sgc-web/general-layout/div/checkout/div/checkout-order/checkout-bottom-nav/div[2]/button").click()  # next button of step 2
        # self.driver.find_element_by_xpath("/html/body/sgc-web/general-layout/div/checkout/div/checkout-order/div/div/add-items/div/div/h2").click()#random click on step 2 heading to hit ip
        time.sleep(3)
        # 20-25 day plan
        standard_day = self.driver.find_element_by_xpath("/html/body/sgc-web/general-layout/div/checkout/div/checkout-order/div/div/select-plan/div/div/div[1]/div/h3[1]").text
         # 1-2 day plan
        immediate_day = self.driver.find_element_by_xpath("/html/body/sgc-web/general-layout/div/checkout/div/checkout-order/div/div/select-plan/div/div/div[2]/div/h3[1]").text

        #standard price
        standard_price=self.driver.find_element_by_xpath("/html/body/sgc-web/general-layout/div/checkout/div/checkout-order/div/div/select-plan/div/div/div[1]/div/h3[3]").text

        #immediate price
        immediate_price=self.driver.find_element_by_xpath("/html/body/sgc-web/general-layout/div/checkout/div/checkout-order/div/div/select-plan/div/div/div[2]/div/h3[3]").text

        print(standard_day)
        print(immediate_day)

        #assertion of plan
        self.assertEqual(standard_day,"STANDARD")  # 20-25 day
        self.assertEqual(immediate_day,"IMMEDIATE")  # 1-2 day plan

        print(standard_price)
        print(immediate_price)

        #assertion of price
        self.assertEqual(standard_price, "$51")  # 10 day
        self.assertEqual(immediate_price, "$75")  # 5 day plan
        time.sleep(2)



    def tearDown(self):
        self.driver.find_element_by_xpath("/html/body/sgc-web/general-layout/div/checkout/div/checkout-order/checkout-bottom-nav/button").click()#previous button of step 3
        self.driver.find_element_by_xpath("/html/body/sgc-web/general-layout/div/checkout/div/checkout-order/div/div/add-items/div/div/div[3]/added-order-item/added-card-item/div/div[1]/input").click()#delete button of any card
        r = random.choice(string.ascii_letters)
        self.driver.find_element_by_xpath("/html/body/sgc-web/general-layout/div/checkout/div/checkout-order/div/div/add-items/div/div/div[1]/div/input").send_keys("joran")
        self.driver.find_element_by_xpath("/html/body/sgc-web/general-layout/div/checkout/div/checkout-order/div/div/add-items/div/div/div[1]/p/a").click()  # click here to add you card


if __name__=='__main__':
 unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:/Users/PC 1/PycharmProjects/pythonProject/PRICEANDPLANS/reports'))

