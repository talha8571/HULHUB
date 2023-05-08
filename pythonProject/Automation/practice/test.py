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
import re



driver=webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(30)
driver.get("https://demo.automationtesting.in/Windows.html")
driver.implicitly_wait(30)
driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div[2]/div[1]/a/button").click()


print(driver.current_window_handle)  # parent window
handles = driver.window_handles  # return all the handle value of windows
print(handles)
for handle in handles:
    driver.switch_to.window(handle)
    print(driver.title)

s = driver.current_window_handle
print(s)
driver.close()



handles = driver.window_handles  # return all the handle value of windows
print(handles)
for handle in handles:
    driver.switch_to.window(handle)
    print(driver.title)
print(driver.current_url)

