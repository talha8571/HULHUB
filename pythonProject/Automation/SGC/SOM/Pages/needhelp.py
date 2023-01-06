import time
from selenium.webdriver.support.select import Select

class needhelp():
    def __init__(self,driver):
        self.driver=driver

        self.i_need_help_xapth = "/html/body/sgc-web/general-layout/div/app-pay-pal-payment/div[1]/div/nav/div/ul/li[5]/a"
        self.typeofinquiry_xpath = "/html/body/sgc-web/general-layout/div/app-need-help/div[2]/div/div[1]/form/ul/li[1]/div/div/select"
        self.name = "/html/body/sgc-web/general-layout/div/app-need-help/div[2]/div/div[1]/form/ul/li[2]/div/input"
        self.email = "/html/body/sgc-web/general-layout/div/app-need-help/div[2]/div/div[1]/form/ul/li[3]/div/input"
        self.message = "/html/body/sgc-web/general-layout/div/app-need-help/div[2]/div/div[1]/form/ul/li[4]/div/textarea"
        self.send_button = "/html/body/sgc-web/general-layout/div/app-need-help/div[2]/div/div[1]/form/ul/li[5]/div/button"
        self.message_after_contatcusform_xpath = "/html/body/sgc-web/general-layout/div/app-need-help/div[2]/div/div[1]/form/ul/li[5]/div/label"
        self.recently_deleted_orders_xpath="/html/body/sgc-web/general-layout/div/app-need-help/div[2]/div/div[2]/h4"

    def needhelp(self, name, email, message):
        self.driver.find_element_by_xpath(self.i_need_help_xapth).click()

        tp = self.driver.find_element_by_xpath(self.typeofinquiry_xpath)  # selection of general inquiries
        typeOfinquiry = Select(tp)
        typeOfinquiry.select_by_visible_text("General Inquiries")

        self.driver.find_element_by_xpath(self.name).send_keys(name)
        self.driver.find_element_by_xpath(self.email).send_keys(email)
        self.driver.find_element_by_xpath(self.message).send_keys(message)

        self.driver.find_element_by_xpath(self.send_button).click()
        time.sleep(2)

        # Recently Deleted Orders
        rdo=self.driver.find_element_by_xpath("/html/body/sgc-web/general-layout/div/app-need-help/div[2]/div/div[2]/h4")
        rd=rdo.is_displayed()
        if rd==True:
            print("Recently Deleted Orders is Displayed")
        else:
            print("Recently Deleted Orders is NOT Displayed")


