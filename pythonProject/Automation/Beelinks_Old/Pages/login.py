# from Automation.testing import variables
import Automation.testing

# email = Automation.testing.email
class loginn():

    def __init__(self, driver):
        self.driver = driver

        self.email_xpath="/html/body/app-root/div[2]/app-login/div[1]/div/form/div[1]/input"
        self.password_xpath="/html/body/app-root/div[2]/app-login/div[1]/div/form/div[2]/input"
        self.login_button_xpath="/html/body/app-root/div[2]/app-login/div[1]/div/form/button"

    def loginpage(self):
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_xpath(self.email_xpath).send_keys(Automation.testing.email)
        self.driver.find_element_by_xpath(self.password_xpath).send_keys("12345678")
        self.driver.find_element_by_xpath(self.login_button_xpath).click()

