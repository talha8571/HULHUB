import unittest
from selenium import webdriver
import time
#from webdriver_manager.chrome import ChromeDriverManager
import HtmlTestRunner
from webdriver_manager.chrome import ChromeDriverManager
from seleniumwire import webdriver
from selenium.webdriver.chrome.options import Options

class beelinks(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Chrome(ChromeDriverManager().install())
        cls.driver.get("https://new.beelinks.solutions/login")
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(20)

    def test_a_login(self):
        self.driver.find_element_by_xpath("/html/body/app-root/app-login/div/div/div/div/div[1]/div[2]/div[2]/form/div[2]/div/input").send_keys("hello")
        self.driver.find_element_by_xpath("/html/body/app-root/app-login/div/div/div/div/div[1]/div[2]/div[2]/form/div[3]/button").click()

    def test_b_login(self):
        self.driver.find_element_by_xpath("/html/body/app-root/app-login/div/div/div/div/div[1]/div[2]/div[2]/form/div[2]/div/input").clear()
        self.driver.find_element_by_xpath("/html/body/app-root/app-login/div/div/div/div/div[1]/div[2]/div[2]/form/div[2]/div/input").send_keys("hello")
        self.driver.find_element_by_xpath("/html/body/app-root/app-login/div/div/div/div/div[1]/div[2]/div[2]/form/div[3]/button").click()



    @classmethod
    def tearDownClass(cls):
        cls.driver.close()

class bingoo(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Chrome(ChromeDriverManager().install())
        cls.driver.get("https://new.beelinks.solutions/login")
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(20)

    def test_a_login(self):
        self.driver.find_element_by_xpath("/html/body/app-root/app-login/div/div/div/div/div[1]/div[2]/div[2]/form/div[2]/div/input").send_keys("hello")
        self.driver.find_element_by_xpath("/html/body/app-root/app-login/div/div/div/div/div[1]/div[2]/div[2]/form/div[3]/button").click()

    def test_b_login(self):
        self.driver.find_element_by_xpath("/html/body/app-root/app-login/div/div/div/div/div[1]/div[2]/div[2]/form/div[2]/div/input").clear()
        self.driver.find_element_by_xpath("/html/body/app-root/app-login/div/div/div/div/div[1]/div[2]/div[2]/form/div[2]/div/input").send_keys("hello")
        self.driver.find_element_by_xpath("/html/body/app-root/app-login/div/div/div/div/div[1]/div[2]/div[2]/form/div[3]/button").click()



# if __name__ == '__main__':
#     unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="C:/Users/1154-Talha/PycharmProjects/pythonProject/Automation/Beelinks_New/Report"))

if __name__ == "__main__":
    # Create a test suite that includes both test classes
    suite = unittest.TestSuite()
    suite.addTest(beelinks('test_a_login'))
    suite.addTest(beelinks('test_b_login'))
    suite.addTest(bingoo('test_a_login'))
    suite.addTest(bingoo('test_b_login'))

    # Use HtmlTestRunner to generate an HTML report
    runner = HtmlTestRunner.HTMLTestRunner(output='C:/Users/1154-Talha/PycharmProjects/pythonProject/Automation/Beelinks_New/Report')
    runner.run(suite)