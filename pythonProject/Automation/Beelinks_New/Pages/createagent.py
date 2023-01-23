import random
import time

from selenium.webdriver.common.keys import Keys

class Createagent():
    def __init__(self, driver):
        self.driver=driver

        self.plussign_xpath="/html/body/app-root/app-layout/div/app-topbar/header/div/div[2]/div[1]/button"
        self.createagent_xpaht="/html/body/app-root/app-layout/div/app-topbar/header/div/div[2]/div[1]/div/div/div[1]/div[2]/a"
        self.firstname_Xpath="/html/body/div[2]/div[2]/div/mat-dialog-container/app-add-agent-dialog/div/form/div[1]/div[1]/input"
        self.last_name_xpath="/html/body/div[2]/div[2]/div/mat-dialog-container/app-add-agent-dialog/div/form/div[1]/div[2]/input"
        self.nick_name="/html/body/div[2]/div[2]/div/mat-dialog-container/app-add-agent-dialog/div/form/div[2]/input"
        self.phone_no_xpath="/html/body/div[2]/div[2]/div/mat-dialog-container/app-add-agent-dialog/div/form/div[3]/input"
        self.extension="/html/body/div[2]/div[2]/div/mat-dialog-container/app-add-agent-dialog/div/form/div[4]/input"
        self.email="/html/body/div[2]/div[2]/div/mat-dialog-container/app-add-agent-dialog/div/form/div[5]/div[1]/input"
        self.password="/html/body/div[2]/div[2]/div/mat-dialog-container/app-add-agent-dialog/div/form/div[5]/div[2]/input"
        self.role="/html/body/div[2]/div[2]/div/mat-dialog-container/app-add-agent-dialog/div/form/div[7]/ng-select/div/div/div[2]/input"
        self.group="/html/body/div[2]/div[2]/div/mat-dialog-container/app-add-agent-dialog/div/form/div[8]/ng-select/div/div/div[2]/input"
        self.Simultaneous_Chats="/html/body/div[2]/div[2]/div/mat-dialog-container/app-add-agent-dialog/div/form/div[9]/input"
        self.submit_button="/html/body/div[2]/div[2]/div/mat-dialog-container/app-add-agent-dialog/div/form/div[12]/button"

        ###############################################################################

        ########################   AGENTS TAB X PATH    ###############################

        ###############################################################################


        self.agentstab_leftpanel="/html/body/app-root/app-layout/div/app-sidebar/div/div/div/div/ul/li[8]/a"
        self.online_agents_xpath="/html/body/app-root/app-layout/div/div/div/app-agents/div/div/div[1]/div/div[2]/div/button[2]"
        self.offline_xpath="/html/body/app-root/app-layout/div/div/div/app-agents/div/div/div[1]/div/div[2]/div/button[3]"
        self.allagents="/html/body/app-root/app-layout/div/div/div/app-agents/div/div/div[1]/div/div[2]/div/button[1]"
        self.allagents_Searchbar="/html/body/app-root/app-layout/div/div/div/app-agents/div/div/div[1]/div/div[3]/app-agent-list-sidebar/div[1]/div/input"



        ###############################################################################

        ########################   Edit profile X PATH    ###############################

        ###############################################################################

        self.agentsname_fromsearch="/html/body/app-root/app-layout/div/div/div/app-agents/div/div/div[1]/div/div[3]/app-agent-list-sidebar/div[2]/ul/li/div/div/div[3]/h5"
        self.edit_profile_icon="/html/body/app-root/app-layout/div/div/div/app-agents/div/div/div[2]/div/div/div/div/div/div[1]/div/div/div/div[2]/div/div[1]/ul/li[1]"
        self.firstname_editprofile="/html/body/div[2]/div[2]/div/mat-dialog-container/app-edit-profile-dialog/div/form/div[1]/div[1]/div[1]/input"
        self.nickname_editprofile="/html/body/div[2]/div[2]/div/mat-dialog-container/app-edit-profile-dialog/div/form/div[1]/div[2]/div[1]/input"
        self.manager_editprofiel="/html/body/div[2]/div[2]/div/mat-dialog-container/app-edit-profile-dialog/div/form/div[1]/div[4]/div[1]/ng-select/div/div/div[2]/input"
        self.last_name_editprofile="/html/body/div[2]/div[2]/div/mat-dialog-container/app-edit-profile-dialog/div/form/div[1]/div[1]/div[2]/input"
        self.phonenumber_editprofile="/html/body/div[2]/div[2]/div/mat-dialog-container/app-edit-profile-dialog/div/form/div[1]/div[2]/div[2]/input"
        self.extension_editprofile="/html/body/div[2]/div[2]/div/mat-dialog-container/app-edit-profile-dialog/div/form/div[1]/div[3]/div[2]/input"
        self.simultaneous_chats_editprofile="/html/body/div[2]/div[2]/div/mat-dialog-container/app-edit-profile-dialog/div/form/div[1]/div[4]/div[2]/input"
        self.save_button_Edit_profile="/html/body/div[2]/div[2]/div/mat-dialog-container/app-edit-profile-dialog/div/form/div[2]/button"

    ###############################################################################

    ########################   Edit ROle X PATH    ###############################

    ###############################################################################


        self.edit_role_icon="/html/body/app-root/app-layout/div/div/div/app-agents/div/div/div[2]/div/div/div/div/div/div[1]/div/div/div/div[2]/div/div[1]/ul/li[2]"
        self.assignrole_edit_role="/html/body/div[2]/div[2]/div/mat-dialog-container/app-edit-role-dialog/div/div/div[1]/div/ng-select/div/div/div[3]/input"
        self.asign_role_save_button="/html/body/div[2]/div[2]/div/mat-dialog-container/app-edit-role-dialog/div/div/div[2]/mat-dialog-actions/button[1]"










    def createagent_method(self):
        self.driver.implicitly_wait(30)
        random_number=random.randint(0,99999)
        fe=self.driver.find_element_by_xpath #stroing driver.find element in variable to use next time
        fe(self.plussign_xpath).click()
        fe(self.createagent_xpaht).click()
        fe(self.firstname_Xpath).send_keys("test") #name

        self.nickname="Automation"+str(random_number)



        fe(self.last_name_xpath).send_keys(self.nickname) #last name
        fe(self.nick_name).send_keys(self.nickname) #nickname

        phone_number_number = random.randint(0, 99999999999)
        fe(self.phone_no_xpath).send_keys(phone_number_number) #phone number

        fe(self.extension).send_keys(random_number) #extension
        fe(self.email).send_keys("bingo",random_number,"@test.com")#email
        fe(self.password).send_keys("12345678")
        time.sleep(2)

        fe(self.role).send_keys("admin",Keys.RETURN)
        fe(self.group).send_keys("qa testing",Keys.RETURN)
        fe(self.Simultaneous_Chats).send_keys("3")
        time.sleep(2)
        fe(self.submit_button).click()

        time.sleep(10)

    def ageentstab(self):

        #####click on agents tab and visit all, online and offline agent and search the name of created agent

        self.driver.implicitly_wait(20)
        fe=self.driver.find_element_by_xpath

        fe(self.agentstab_leftpanel).click()
        fe(self.online_agents_xpath).click()
        time.sleep(1)
        fe(self.offline_xpath).click()
        time.sleep(1)
        fe(self.allagents).click()



    def edit_profile(self):
        self.driver.implicitly_wait(20)
        fe=self.driver.find_element_by_xpath
        fe(self.allagents_Searchbar).send_keys(self.nickname) #search the name of the created agent
        time.sleep(1)
        fe(self.agentsname_fromsearch).click()
        fe(self.edit_profile_icon).click()
        fe(self.firstname_editprofile).send_keys("_updated")
        fe(self.nickname_editprofile).send_keys("_updated")
        fe(self.manager_editprofiel).send_keys("qa.bizzchats@gmail.com",Keys.ENTER)
        managername=fe("/html/body/div[2]/div[2]/div/mat-dialog-container/app-edit-profile-dialog/div/form/div[1]/div[4]/div[1]/ng-select/ng-dropdown-panel/div/div[2]/div/span").text

        if managername == "qa.bizzchats@gmail.com":
            fe("/html/body/div[2]/div[2]/div/mat-dialog-container/app-edit-profile-dialog/div/form/div[1]/div[4]/div[1]/ng-select/ng-dropdown-panel/div/div[2]/div/span").click()

        else:
            print("nam not found")



        fe(self.last_name_editprofile).send_keys("_updated")
        time.sleep(1)


        fe(self.phonenumber_editprofile).clear()
        time.sleep(1)
        fe(self.phonenumber_editprofile).send_keys("9234785412374")
        time.sleep(1)



        fe(self.extension_editprofile).clear()
        time.sleep(1)
        fe(self.extension_editprofile).send_keys("112233")



        fe(self.simultaneous_chats_editprofile).clear()
        time.sleep(1)
        fe(self.simultaneous_chats_editprofile).send_keys("4")


        fe(self.save_button_Edit_profile).click()

        print("agent updated successfully")



    def edit_role(self):

        self.driver.find_element_by_xpath













