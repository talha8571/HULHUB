import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import HtmlTestRunner

class LoginPage:
    USERNAME_INPUT = (By.XPATH, "/html/body/app-root/app-login/div/div/div/div/div[1]/div[2]/div[2]/form/div[2]/div/input")
    PASSWORD_INPUT = (By.XPATH, "/html/body/app-root/app-login/div/div/div/div/div[1]/div[2]/div[2]/form/div[3]/button")
    LOGIN_BUTTON = (By.XPATH, "/html/body/app-root/app-login/div/div/div/div/div[1]/div[2]/div[2]/form/div[3]/button")

    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        username_input = self.driver.find_element(*LoginPage.USERNAME_INPUT)
        password_input = self.driver.find_element(*LoginPage.PASSWORD_INPUT)
        login_button = self.driver.find_element(*LoginPage.LOGIN_BUTTON)

        username_input.clear()
        username_input.send_keys(username)

        password_input.clear()
        password_input.send_keys(password)

        login_button.click()

class BeelinksTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        options = Options()
        options.add_argument("--start-maximized")
        cls.driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
        cls.driver.get("https://new.beelinks.solutions/login")
        cls.driver.implicitly_wait(10)

    def test_successful_login(self):
        login_page = LoginPage(self.driver)
        login_page.login("testuser", "testpassword")
        # Add assertions here to verify the expected behavior
        self.assertEqual(self.driver.title, "Dashboard - Beelinks")

    def test_failed_login(self):
        login_page = LoginPage(self.driver)
        login_page.login("invaliduser", "invalidpassword")
        # Add assertions here to verify the expected behavior
        error_message = self.driver.find_element(By.XPATH, "/html/body/app-root/app-login/div/div/div/div/div[1]/div[2]/div[2]/form/div[1]").text
        self.assertEqual(error_message, "Invalid email or password")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="C:/Users/1154-Talha/PycharmProjects/pythonProject/Automation/Beelinks_New/Report"))
