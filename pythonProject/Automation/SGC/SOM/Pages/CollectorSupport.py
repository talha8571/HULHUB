import time
from selenium.webdriver.support.select import Select

class collectorSupport():
    def __init__(self,driver):
        self.driver=driver

        self.collector_supportTab_xapth="/html/body/sgc-web/general-layout/div/div/ul/li[4]/a"
        self.typeofinquiry_xpath="/html/body/sgc-web/general-layout/div/static-layout/ng-component/contact-us/div[2]/div[2]/form/ul/li[1]/div/div/select"
        self.name="/html/body/sgc-web/general-layout/div/static-layout/ng-component/contact-us/div[2]/div[2]/form/ul/li[2]/div/input"
        self.email="/html/body/sgc-web/general-layout/div/static-layout/ng-component/contact-us/div[2]/div[2]/form/ul/li[3]/div[1]/input"
        self.message="/html/body/sgc-web/general-layout/div/static-layout/ng-component/contact-us/div[2]/div[2]/form/ul/li[4]/div[1]/textarea"
        self.send_button="/html/body/sgc-web/general-layout/div/static-layout/ng-component/contact-us/div[2]/div[2]/form/ul/li[5]/div/button"
        self.message_after_contatcusform_xpath="/html/body/sgc-web/general-layout/div/static-layout/ng-component/contact-us/div[2]/div[2]/form/ul/li[5]/div/label"


    def collectorsupport(self,name,email,message):
        self.driver.find_element_by_xpath(self.collector_supportTab_xapth).click()

        tp=self.driver.find_element_by_xpath(self.typeofinquiry_xpath) #selection of general inquiries
        typeOfinquiry=Select(tp)
        typeOfinquiry.select_by_visible_text("General Inquiries")


        self.driver.find_element_by_xpath(self.name).send_keys(name)
        time.sleep(1)
        self.driver.find_element_by_xpath(self.email).send_keys(email)
        time.sleep(1)
        self.driver.find_element_by_xpath(self.message).send_keys(message)

        self.driver.find_element_by_xpath(self.send_button).click()
        time.sleep(2)


