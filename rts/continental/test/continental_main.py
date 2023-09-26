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

from continental.pages.home import homepage

class Continental_site(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # cls.driver=webdriver.Chrome(ChromeDriverManager().install())
        cls.driver = webdriver.Chrome(executable_path='C:/Users/1154-Talha/PycharmProjects/rts/webdriver/chromedriver_win64/chromedriver.exe')
        cls.driver.get("https://continentalbiscuits.hul-hub.com/")
        cls.driver.implicitly_wait(30)
        cls.driver.maximize_window()


    def test_home_page(self):
        driver=self.driver
        hp=homepage(driver)
        hp.home_execution()##callign the function
        time.sleep(2)

        #scroll till the our brands heading
        ob = self.driver.find_element_by_xpath("/html/body/main/div/div[1]/div[4]/div/div/div/h2")#finding the our brands heading
        self.driver.execute_script("arguments[0].scrollIntoView(true);", ob);

        hp.ourbrands_heading() ##second method calling


        self.driver.execute_script("window.scrollTo(0,500)")




if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="C:/Users/1154-Talha/PycharmProjects/rts/continental/reports"))