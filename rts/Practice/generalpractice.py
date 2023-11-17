import time
import unittest
import time

import HtmlTestRunner
from selenium.webdriver.common.keys import Keys

import requests
import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options


option = webdriver.ChromeOptions()
option.add_argument("start-maximized")

        # z=self.driver.find_elements_by_xpath("//*[@id]")
        # w=[id.get_attribute("id")for id in z]
        #
        # for n in w:
        #     print(n)

    #     self.first_image_xpath = "/html/body/div[1]/ul/li[1]/img"
    #     self.trash_xpath = "/html/body/div[1]/div"
    #     self.iframe_drag_drop = "/html/body/div[1]/div[1]/div[2]/div/div/div[2]/div/div/div[1]/p/iframe"
    #     self.driver.implicitly_wait(20)
    #     self.driver.switch_to.frame(self.driver.find_element_by_xpath(self.iframe_drag_drop))
    #     # Identify the source and target elements for the drag and drop operation
    #     source=self.driver.find_element_by_xpath(self.first_image_xpath)
    #     target=self.driver.find_element_by_xpath(self.trash_xpath)
    #
    #     # Perform the drag and drop operation
    #     ActionChains(self.driver).drag_and_drop(source,target).perform()
    #     time.sleep(2)
    #
    #
    #
    # def drag_drop_by_ofset(self):
    #     self.driver.implicitly_wait(20)
    #
    #     # click on the accepted elements
    #     self.driver.find_element_by_xpath("/html/body/div/div[1]/div[2]/div/div/div[2]/div/ul/li[2]").click()
    #
    #     ### switch in to frame
    #     self.driver.switch_to.frame(self.driver.find_element_by_xpath("/html/body/div/div[1]/div[2]/div/div/div[2]/div/div/div[2]/p/iframe"))##second iframe
    #
    #
    #
    #     element=self.driver.find_element_by_xpath("/html/body/div[1]/p")
    #
    #     ActionChains(self.driver).drag_and_drop_by_offset(element,588, 129).perform()##moving the element with help of ofsett


class practice(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Chrome(executable_path="C:/Users/1154-Talha/PycharmProjects/rts/webdriver/chromedriver_win64/chromedriver.exe")
        cls.driver.get("https://www.google.com/")
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(30)


    def test_a_chrome(self):
        print(self.driver.current_url)
        print(self.driver.title)
        self.driver.find_element_by_xpath("/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/textarea").send_keys("selenium automation")
        a=ActionChains(self.driver)
        b=a.send_keys(Keys.ENTER)
        b.perform()



    # @classmethod
    # def tearDownClass(cls):
    # cls.driver.close()


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="C:/Users/1154-Talha/PycharmProjects/rts/Practice"))
#



