
import time
from selenium.webdriver.support.select import Select
import random


class profile:
    def __init__(self,driver):
        self.driver=driver

        self.profile_logo_xpath="/html/body/sgc-web/general-layout/div/div/div[3]"
        self.myprofile_xpath="/html/body/sgc-web/general-layout/div/div/div[3]/ul/li[2]/a"
        self.edit_name_xpath="/html/body/sgc-web/general-layout/div/account-profile/div[2]/div/div[1]/div[2]/div/div/div[2]/a"
        self.phonenumbereditbutton_xpath="/html/body/sgc-web/general-layout/div/account-profile/div[2]/div/div[1]/div[4]/div/div/div[2]/a/img"
        self.name_textfield_xpath="/html/body/sgc-web/sgc-modal/div/div/edit-profile/div[1]/div/input"
        self.phonetextfield_xpath="/html/body/sgc-web/sgc-modal/div/div/edit-profile/div[1]/div/input"
        self.savebuttonofname="/html/body/sgc-web/sgc-modal/div/div/edit-profile/div[2]/button[2]"
        self.savebuttonofphonenumberxpath="/html/body/sgc-web/sgc-modal/div/div/edit-profile/div[2]/button[2]"
        self.add_address_xpath="/html/body/sgc-web/general-layout/div/account-profile/div[2]/div[1]/div[2]/button"
        self.alertcross_xpath="/html/body/sgc-web/sgc-modal/div/div/app-alert-add-address/img"
        self.street_xpath=("/html/body/sgc-web/sgc-modal/div/div/address-editor/div[1]/div/input[1]")
        self.appartment_xpath=("/html/body/sgc-web/sgc-modal/div/div/address-editor/div[1]/div/input[2]")
        self.city_xpath=("/html/body/sgc-web/sgc-modal/div/div/address-editor/div[1]/div/input[3]")
        self.state_xpath=("/html/body/sgc-web/sgc-modal/div/div/address-editor/div[1]/div/div[2]/select")
        self.zipcode=("/html/body/sgc-web/sgc-modal/div/div/address-editor/div[1]/div/input[4]")
        self.phonenumberofaddress=("/html/body/sgc-web/sgc-modal/div/div/address-editor/div[1]/div/input[5]")
        self.savebuttonofaddressform=("/html/body/sgc-web/sgc-modal/div/div/address-editor/div[2]/button")
    def profile(self):
        self.driver.implicitly_wait(30)
        phonenmber = (random.randint(0, 160000000000))
        self.driver.find_element_by_xpath(self.profile_logo_xpath).click()
        self.driver.find_element_by_xpath(self.myprofile_xpath).click()

        # nameBeforeEdit = self.driver.find_element_by_xpath("/html/body/sgc-web/general-layout/div/account-profile/div[2]/div/div[1]/div[2]/div/div/div[1]/p").text
        # print("name before edit=", nameBeforeEdit)

        #edit name
        self.driver.find_element_by_xpath(self.edit_name_xpath).click()
        self.driver.find_element_by_xpath(self.name_textfield_xpath).clear()
        self.driver.find_element_by_xpath(self.name_textfield_xpath).send_keys("QA Talhah",phonenmber)
        self.driver.find_element_by_xpath(self.savebuttonofname).click()
        time.sleep(2)
        print("name edited")


        # nameafteredit=self.driver.find_element_by_xpath("/html/body/sgc-web/general-layout/div/account-profile/div[2]/div/div[1]/div[2]/div/div/div[1]/p").text
        # print("name after edit=",nameafteredit)

        #edit number
        self.driver.find_element_by_xpath(self.phonenumbereditbutton_xpath).click()
        self.driver.find_element_by_xpath(self.phonetextfield_xpath).clear()
        self.driver.find_element_by_xpath(self.phonetextfield_xpath).send_keys(phonenmber)
        self.driver.find_element_by_xpath(self.savebuttonofphonenumberxpath).click()
        print("number edited")


    #add adddress
    def add_address(self,ph):
        self.driver.find_element_by_xpath(self.add_address_xpath).click()
        self.driver.find_element_by_xpath(self.alertcross_xpath).click()
        self.driver.find_element_by_xpath(self.street_xpath).send_keys("Main Street united states")
        self.driver.find_element_by_xpath(self.appartment_xpath).send_keys("Appartment 76 main street usa")
        self.driver.find_element_by_xpath(self.city_xpath).send_keys("Los Angeles")
        stateAndProvience=self.driver.find_element_by_xpath(self.state_xpath)
        st=Select(stateAndProvience)
        st.select_by_index(3)

        self.driver.find_element_by_xpath(self.zipcode).send_keys("7896541")
        self.driver.find_element_by_xpath(self.phonenumberofaddress).send_keys(ph)
        self.driver.find_element_by_xpath(self.savebuttonofaddressform).click()
        print("Address added")
        time.sleep(5)

        odp = self.driver.find_element_by_xpath(
            "/html/body/sgc-web/general-layout/div/account-profile/div[2]/div[1]/div[4]/div[1]/h3")
        # print("order preferences is displayed ",odp.is_displayed())
        o = odp.is_displayed()
        if o == True:
            print("my order preferencs is displayed")
        else:
            print("my order preferencs is NOT displayed")

        communication_preferences = self.driver.find_element_by_xpath("/html/body/sgc-web/general-layout/div/account-profile/div[2]/div[2]/div/div[1]/h3")
        ccc = communication_preferences.is_displayed()
        if ccc == True:
            print("communication preferencs is displayed")
        else:
            print("communication is NOT displayed")

        reuqest_your_personal_data = self.driver.find_element_by_xpath("/html/body/sgc-web/general-layout/div/account-profile/div[2]/div[3]/div/div[1]/h3")
        rr = reuqest_your_personal_data.is_displayed()
        if rr == True:
            print("reuqest_your_personal_data is displayed")
        else:
            print("reuqest_your_personal_data is NOT displayed")

        cancel_request = self.driver.find_element_by_xpath("/html/body/sgc-web/general-layout/div/account-profile/div[2]/div[4]/div/div[1]/h3")
        c_r = cancel_request.is_displayed()
        if c_r == True:
            print("cancel_request is displayed")
        else:
            print("cancel_request is NOT displayed")
        time.sleep(5)
        self.driver.execute_script("window.scrollTo(0,300)")
        time.sleep(1)
        self.driver.execute_script("window.scrollTo(300,600)")
        time.sleep(1)
        self.driver.execute_script("window.scrollTo(600,900)")
        time.sleep(1)
        self.driver.execute_script("window.scrollTo(900,0)")
        time.sleep(3)

