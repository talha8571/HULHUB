
import unittest
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
# from webdriver_manager.chrome import ChromeDriverManager
import HtmlTestRunner
from webdriver_manager.chrome import ChromeDriverManager
import random
import string
from colorama import Fore
from openpyxl import Workbook



class HttpsandHttpLink(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Chrome(ChromeDriverManager().install())
        cls.driver.get("https://inspection.hrms.solutions/backend/login")
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(20)
        cls.driver.find_element_by_xpath("/html/body/div/div/div/form/div[1]/input").send_keys("Webadmin")#email field
        cls.driver.find_element_by_xpath("/html/body/div/div/div/form/div[2]/input").send_keys("!nsp3cti0n123!") #password field
        cls.driver.find_element_by_xpath("/html/body/div/div/div/form/div[3]/div/button").click()#signin button


    def test_findignlinks(self):
        time.sleep(5)
        # Find all <a> tags in the page
        links = self.driver.find_elements_by_tag_name("a")

        print(links)
        # Extract the href attribute from each link, filter out None values
        link_urls = [link.get_attribute("href") for link in links if link.get_attribute("href")]

        # Print the total number of links
        print("Total number of links are =", len(link_urls))

        # Print the URLs with color formatting
        for link_url in link_urls:
            if link_url.startswith("http"):
                print(Fore.RED + link_url + Fore.RESET)
            else:
                print(link_url)

        # Store links in an Excel file
        wb = Workbook()
        ws = wb.active
        ws.append(["Links"])
        for link_url in link_urls:
            ws.append([link_url])

        # Save the Excel file
        wb.save("links.xlsx")


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="output='C:/Users/1154-Talha/PycharmProjects/rts/Practice'"))