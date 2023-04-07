import time
import unittest

from selenium.webdriver import ActionChains

class services():
    def __init__(self,driver):
        self.driver=driver

        self.keyword_xpath="/html/body/div[1]/header/div/nav/ul/li[1]/ul/li/div/div/div/div[2]/div/div[1]/div/div[2]/a"



    def services(self):
        a = ActionChains(self.driver)
        m = self.driver.find_element_by_xpath("/html/body/div[1]/header/div/nav/ul/li[1]/a/span")
        a.move_to_element(m).perform()
        time.sleep(3)

        self.driver.find_element_by_xpath(self.keyword_xpath).click()


        print(self.driver.current_url)

