import random
import time
import string
from selenium.webdriver.common.keys import Keys




#########  THIS FILE EXITS THE CREATION FO AGENT, SEARCH AGENT IN THE LIST OF AGENT THEN UPDATE THE PROFILE, EDIT ROLE AND  UPDATE PASSWORD AND VERIFY THE ERROR MESSAGES

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
        self.firstname_editprofile="edit-agent-firstname"
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
        self.assignrole_textfield_edit_role="/html/body/div[2]/div[2]/div/mat-dialog-container/app-edit-role-dialog/div/div/div[1]/div/ng-select/div/div/div[3]/input"
        self.asign_role_save_button="/html/body/div[2]/div[2]/div/mat-dialog-container/app-edit-role-dialog/div/div/div[2]/mat-dialog-actions/button[1]"
        self.confirmation_ok="/html/body/ngb-modal-window/div/div/app-confirmation/div[3]/button[1]"



        ###############################################################################

        ########################   Edit password X PATH    ############################

        ###############################################################################

        self.edit_password_agent_profile="/html/body/app-root/app-layout/div/div/div/app-agents/div/div/div[2]/div/div/div/div/div/div[1]/div/div/div/div[2]/div/div[1]/ul/li[3]"
        self.newpassword_textfield="changePassword-newPass" ##id of new pasword tect
        self.view_iconof_new_password="/html/body/div[2]/div[2]/div/mat-dialog-container/app-change-password-dialog/div[2]/form/div[1]/span/div/i"
        self.confirm_password_textfield="changePassword-confirmNewPass" #3id of confirm password
        self.view_icon_of_confirmpassword="/html/body/div[2]/div[2]/div/mat-dialog-container/app-change-password-dialog/div[2]/form/div[1]/span/div/i"
        self.submit_button_of_password_popup="changePassword-submit" ##id of submit button password popup
        self.error_message_of_same_password="/html/body/div[2]/div[2]/div/mat-dialog-container/app-change-password-dialog/div[2]/form/div[4]/small"
        self.error_message_of_first_field="/html/body/div[2]/div[2]/div/mat-dialog-container/app-change-password-dialog/div/div[2]/form/div[2]/small"
        self.error_message_of_second_field="/html/body/div[2]/div[2]/div/mat-dialog-container/app-change-password-dialog/div/div[2]/form/div[4]/small"
        self.ok_button_of_confirmation="/html/body/ngb-modal-window/div/div/app-confirmation/div[3]/button[1]" #ok button after changing password



        ########################################################################

        ############################ NOTIFICATIONS ############################

        ######################################################################


        self.firstsearchresult="/html/body/app-root/app-layout/div/div/div/app-agents/div/div/div[1]/div/div[3]/app-agent-list-sidebar/div[2]/ul/li[1]/div/div/div[3]/h5"
        self.notifications_tab="/html/body/app-root/app-layout/div/div/div/app-agents/div/div/div[2]/div/div/div/div/div/ul/li[2]/a/span"

        ######## Email notification ###########
        self.new_ticket_created="/html/body/app-root/app-layout/div/div/div/app-agents/div/div/div[2]/div/div/div/div/div/div[1]/div/div[1]/form/div[1]/div/div/div/input"









    def createagent_method(self):
        self.driver.implicitly_wait(10)
        random_number=random.randint(0,999999999)
        fe=self.driver.find_element_by_xpath #storing driver.find element in variable to use next time
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
        time.sleep(3)
        lettrr = random.choice(string.ascii_lowercase)

        while True:
            try:
                error_message_of_email=fe("/html/body/div[2]/div[2]/div/mat-dialog-container/app-add-agent-dialog/div/form/div[5]/div[1]/div/small").text

                if error_message_of_email=="This email has been registered already":
                    fe(self.email).clear()
                    rd=random.randint(0, 99999999999)
                    fe(self.email).send_keys("bingo",lettrr,rd,"@test.com")#email

            except:
                print("email is not registered before")
                break



        fe(self.password).send_keys("12345678")
        time.sleep(1)

        fe(self.role).send_keys("admin",Keys.RETURN)
        fe(self.group).send_keys("qa testing",Keys.RETURN)
        fe(self.Simultaneous_Chats).send_keys("3")
        time.sleep(2)
        fe(self.submit_button).click()

        time.sleep(10)
        print("new agent registered  with the name",self.nickname)
        #agent created

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
        time.sleep(2)
        fe(self.allagents_Searchbar).send_keys(self.nickname)  # search the name of the created agent



    def edit_profile(self):
        self.driver.implicitly_wait(20)
        fe=self.driver.find_element_by_xpath
        time.sleep(1)
        fe(self.agentsname_fromsearch).click() #click ont he agents name
        fe(self.edit_profile_icon).click() #click on edit profile

        ##edit the form of agent
        self.driver.find_element_by_id(self.firstname_editprofile).send_keys("_updated")
        fe(self.nickname_editprofile).send_keys("_updated")
        fe(self.manager_editprofiel).send_keys("qa.bizzchats@gmail.com",Keys.ENTER)
        time.sleep(3)
        managername=fe("/html/body/div[2]/div[2]/div/mat-dialog-container/app-edit-profile-dialog/div/form/div[1]/div[4]/div[1]/ng-select/ng-dropdown-panel/div/div[2]/div/span").text

        if managername == "qa.bizzchats@gmail.com":
            fe("/html/body/div[2]/div[2]/div/mat-dialog-container/app-edit-profile-dialog/div/form/div[1]/div[4]/div[1]/ng-select/ng-dropdown-panel/div/div[2]/div/span").click()

        else:
            print("name of  manager  not found")



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

        fe=self.driver.find_element_by_xpath
        fe(self.edit_role_icon).click()

        role=["supervisor","agent","Whatsapp agent", "Sales Person"]

        rd=random.randint(0,3)

        self.role_agent=role[rd]
        fe(self.assignrole_textfield_edit_role).send_keys(self.role_agent, Keys.ENTER)#select role
        fe(self.asign_role_save_button).click()
        fe(self.confirmation_ok).click()

        # self.role_of_agent_in_tag=fe("/html/body/app-root/app-layout/div/div/div/app-agents/div/div/div[2]/div/div/div/div/div/div[1]/div/div/div/div[1]/ul/li[2]/p").text
        print("role updated")
        time.sleep(2)


    def edit_password(self):

        fe=self.driver.find_element_by_xpath
        fe(self.edit_password_agent_profile).click()
        self.driver.find_element_by_id(self.newpassword_textfield).send_keys("1234")
        self.driver.find_element_by_id(self.confirm_password_textfield).send_keys("1234")

        first_field_password_length_message=fe(self.error_message_of_first_field).text #capturing the error messgae of first field
        print("You have entered the wrong password ",first_field_password_length_message)

        second_field_error_message=fe(self.error_message_of_second_field).text
        print("You have entered the wrong password ",second_field_error_message)

        #condition of erroe messages

        if first_field_password_length_message == "New Password cannot be less than 8 characters" and second_field_error_message == "Confirm Password cannot be less than 8 characters":
            self.driver.find_element_by_id(self.newpassword_textfield).send_keys("5678")
            self.driver.find_element_by_id(self.confirm_password_textfield).send_keys("7896")

            #capturing messgae of
            second_field_error_message = fe(self.error_message_of_second_field).text
            print(second_field_error_message)


            if second_field_error_message == "New Password & Confirm Password must be same":
                self.driver.find_element_by_id(self.newpassword_textfield).clear()
                self.driver.find_element_by_id(self.newpassword_textfield).send_keys("12345678")
                self.driver.find_element_by_id(self.confirm_password_textfield).clear()
                self.driver.find_element_by_id(self.confirm_password_textfield).send_keys("12345678")

            else:
                print("thanks")


        else:
            print("both messages are different")


        self.driver.find_element_by_id(self.submit_button_of_password_popup).click() #submit button of popup window
        time.sleep(2)
        fe(self.ok_button_of_confirmation).click() #ok button of popup window



    def profile_notifications(self):
        no=random.randint(0,9)
        self.driver.implicitly_wait(20)
        fe=self.driver.find_element_by_xpath
        time.sleep(2)
        fe(self.agentstab_leftpanel).click() #click agent tab from left panel
        time.sleep(2)
        fe(self.allagents_Searchbar).clear()#3clear the search bar
        fe(self.allagents_Searchbar).send_keys("Automation",no)  # search the name of the created agent
        time.sleep(2)
        fe(self.firstsearchresult).click()
        time.sleep(2)
        fe(self.notifications_tab).click()
        time.sleep(2)
        t=fe(self.new_ticket_created).is_selected()
        p=print(t)











