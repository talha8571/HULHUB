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
from Rts_Automation.rtsproject.pages.service import services

class rts(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Chrome(ChromeDriverManager().install())
        cls.driver.get("http://ranktopseo.hul-hub.com/")
        cls.driver.implicitly_wait(30)
        cls.driver.maximize_window()
        print("current url is ",cls.driver.current_url)
        print("current title is ",cls.driver.title)


    def test_a_service(self):
        driver=self.driver
        a=ActionChains(self.driver)
        m=self.driver.find_element_by_xpath("/html/body/div[1]/header/div/nav/ul/li[1]/a/span")
        a.move_to_element(m).perform()
        time.sleep(3)
        ser=services(driver)
        ser.services()
        self.assertEqual(self.driver.current_url,"http://ranktopseo.hul-hub.com/keyword-research-services")




    @classmethod
    def tearDownClass(cls):
        cls.driver.close()

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="C:/Users/1154-Talha/PycharmProjects/rts\Rts_Automation/rtsproject/reports"))


