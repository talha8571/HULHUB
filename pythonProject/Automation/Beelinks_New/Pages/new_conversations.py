import random
import time
from selenium.webdriver.common.keys import Keys



class nEW_COnversations():

    def __init__(self, driver):
        self.driver=driver
        self.conversation_icon_to_open_option="/html/body/app-root/app-layout/div/div/div/app-agents/div/div/div[1]/div/div[1]/div[2]/div/div[1]/button"
        self.new_conversation_text="/html/body/app-root/app-layout/div/div/div/app-agents/div/div/div[1]/div/div[1]/div[2]/div/div[2]/a[1]"
        self.search_bar_of_agent="/html/body/div[2]/div[2]/div/mat-dialog-container/app-new-conversation-dialog/div/div/div[2]/div/form/div/input"
        self.agent_selection_from_list="/html/body/div[2]/div[2]/div/mat-dialog-container/app-new-conversation-dialog/div/div/div[2]/ul/li[1]/div/div/div[2]"
        self.start_chat_button="/html/body/div[2]/div[2]/div/mat-dialog-container/app-new-conversation-dialog/div/div/div[3]/mat-dialog-actions/button[1]"
        self.email_of_agent_From_Searchbar="/html/body/div[2]/div[2]/div/mat-dialog-container/app-new-conversation-dialog/div/div/div[2]/ul/li[1]/div/div/div[2]/span[1]"
        self.email_of_agent_from_chatwindow="/html/body/app-root/app-layout/div/div/div/app-agents/div/div/div[2]/div/div[1]/app-agents-chat/div/div[1]/div/h5/span"
        self.enter_message_field="/html/body/app-root/app-layout/div/div/div/app-agents/div/div/div[2]/div/div[1]/app-agents-chat/div/div[2]/div/div[2]/div/div[1]/div/input"
        self.email_from_list_ofagents="/html/body/app-root/app-layout/div/div/div/app-agents/div/div/div[1]/div/div[3]/app-agent-conv-list-sidebar/div/div[2]/ul/li[1]/a/div/div/div[2]/div/div[2]/b"



    def conversation_method(self):
        fe=self.driver.find_element_by_xpath

        huluhb_icon=fe("/html/body/app-root/app-layout/div/app-topbar/header/div/div[1]/div/a[2]/span[1]/img").click() #hulub icon click to land on dasboard
        agentstab=fe("/html/body/app-root/app-layout/div/app-sidebar/div/div/div/div/ul/li[8]/a").click() #agents tab from left panel

        fe(self.conversation_icon_to_open_option).click()
        fe(self.new_conversation_text).click()

        ed=random.randint(1,9)
        fe(self.search_bar_of_agent).send_keys("Automation",ed)
        time.sleep(6)
        email1=fe(self.email_of_agent_From_Searchbar).text
        fe(self.agent_selection_from_list).click()
        time.sleep(1)
        fe(self.start_chat_button).click()
        time.sleep(1)
        fe("/html/body/app-root/app-layout/div/div/div/app-agents/div/div/div[1]/div/div[3]/app-agent-conv-list-sidebar/div/div[1]/div/input").send_keys(email1)#3search the selected email
        time.sleep(2)
        fe("/html/body/app-root/app-layout/div/div/div/app-agents/div/div/div[1]/div/div[3]/app-agent-conv-list-sidebar/div/div[2]/ul/li[1]/a/div/div/div[2]/div/div[2]").click()
        time.sleep(2)
        email3=fe(self.email_from_list_ofagents).text
        time.sleep(1)
        email2=fe(self.email_of_agent_from_chatwindow).text

        # visibility_of_email_2=False


        # while visibility_of_email_2 == True:
        #     fe(self.email_from_list_ofagents).click()
        #     visibility_of_email_2 = email2.is_visible()
        #     print("clicked")


        print("email1, agent selected =", email1)
        print("email2. agent in the list =", email2)
        print("email3, agent in the chat window",email3)






        if email1 == email3:
            time.sleep(2)
            fe("/html/body/app-root/app-layout/div/div/div/app-agents/div/div/div[1]/div/div[3]/app-agent-conv-list-sidebar/div/div[2]/ul/li[1]/a/div/div/div[2]/div/div[2]").click() #click on the agent after searching
            self.driver.execute_script("window.scrollTo(0,600)")
            fe(self.enter_message_field).send_keys("this message is from automaion script",Keys.ENTER) ##sending message
            print("new conversation has been created and message has been send")

        elif email1== email2:
            self.driver.execute_script("window.scrollTo(0,600)")
            fe(self.enter_message_field).send_keys("this message is from automaion script",Keys.ENTER)  ##sending message
            print("new conversation has been created and message has been send")



        else:
            print("ERROR emails of selected and agent appeared in the list are different")
