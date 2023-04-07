from selenium import webdriver
from selenium.webdriver import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
import time



import unittest
from selenium import webdriver
import time
#from webdriver_manager.chrome import ChromeDriverManager
import HtmlTestRunner
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
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


class daraz(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Chrome(ChromeDriverManager().install())
        cls.driver.get("https://www.daraz.pk/")
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(30)


    def test_a_daraz_modal(self):
        groceries = self.driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div/div/div/div/div/div/div/ul/li[1]/a/span")
        Beverage = self.driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div/div/div/div/div/div/div/ul/ul[1]/li[1]/a")
        coffee = self.driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div/div/div/div/div/div/div/ul/ul[1]/li[1]/ul/li[1]/a")

        actions = ActionChains(self.driver)
        actions.move_to_element(groceries).move_to_element(Beverage).move_to_element(coffee).click().perform()
        # actions.move_to_element(admin).move_to_element(vehicle).click
        time.sleep(1)
        # /html/body/div[3]/div/div[3]/div[1]/div/div[1]/div[2]/div[1]/div/div/div[1]/div/a
        self.driver.find_element_by_xpath('//*[@id="root"]/div/div[3]/div[1]/div/div[1]/div[2]/div[1]/div/div/div[1]/div/a').click()
        time.sleep(4)

        self.driver.find_element_by_xpath('//*[@id="module_add_to_cart"]/div/button[1]').click()
        time.sleep(1)

        # self.driver.find_element_by_id("container").click()
        # s = self.driver.find_element_by_id("container").text
        # print(s)
        time.sleep(3)
        self.driver.switch_to.frame(self.driver.find_element_by_xpath("/html/body/div[7]/div/div[2]/div/iframe"))
        time.sleep(2)
        self.driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div/div/div[1]/p/span/a').click()




if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="C:/Users/1154-Talha/PycharmProjects/rts\Rts_Automation/rtsproject/reports"))
