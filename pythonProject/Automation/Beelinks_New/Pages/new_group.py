import random
import time
from selenium.webdriver.common.keys import Keys
import colorama
from colorama import Fore

 ########################  This will create new group for agents chats ############
class new_group():

    def __init__(self, driver):
        self.driver=driver
        self.huluhb_icon ="/html/body/app-root/app-layout/div/app-topbar/header/div/div[1]/div/a[2]/span[1]/img" # hulub icon click to land on dasboard
        self.agentstab ="/html/body/app-root/app-layout/div/app-sidebar/div/div/div/div/ul/li[8]/a" # agents tab from left panel
        self.conversation_icon_to_open_option = "/html/body/app-root/app-layout/div/div/div/app-agents/div/div/div[1]/div/div[1]/div[2]/div/div[1]/button"
        self.create_new_group_text="/html/body/app-root/app-layout/div/div/div/app-agents/div/div/div[1]/div/div[1]/div[2]/div/div[2]/a[2]"
        self.group_name_field="/html/body/div[2]/div[2]/div/mat-dialog-container/app-new-conversation-dialog/div/div/div[2]/div/input"
        self.next_button="/html/body/div[2]/div[2]/div/mat-dialog-container/app-new-conversation-dialog/div/div/div[3]/mat-dialog-actions/button[1]"
        self.search_agents_field="/html/body/div[2]/div[2]/div/mat-dialog-container/app-new-conversation-dialog/div/div/div[2]/div/form/div/input"
        self.start_chat_button="/html/body/div[2]/div[2]/div/mat-dialog-container/app-new-conversation-dialog/div/div/div[3]/mat-dialog-actions/button[2]"
        self.search_result="/html/body/div[2]/div[2]/div/mat-dialog-container/app-new-conversation-dialog/div/div/div[2]/ul/li[1]/div/div/div[2]"
        self.group_name_in_list_chats="/html/body/app-root/app-layout/div/div/div/app-agents/div/div/div[1]/div/div[3]/app-agent-conv-list-sidebar/div/div[2]/ul/li[1]/a/div/div/div[2]/div/div[2]"
        self.enter_message_field = "/html/body/app-root/app-layout/div/div/div/app-agents/div/div/div[2]/div/div[1]/app-agents-chat/div/div[2]/div/div[2]/div/div[1]/div/input" #message field of chats


    def create_new_group(self):
        fe=self.driver.find_element_by_xpath
        time.sleep(2)
        fe(self.huluhb_icon).click()
        fe(self.agentstab).click()
        fe("/html/body/app-root/app-layout/div/div/div/app-agents/div/div/div[1]/div/div[3]/ul/li[1]/a").click()#click on agents tab from panel
        fe(self.conversation_icon_to_open_option).click()
        fe(self.create_new_group_text).click()

        rad=random.randint(0,3147896523684)
        group_name="Automation"+str(rad)
        fe(self.group_name_field).send_keys(group_name)
        fe(self.next_button).click()

        fe(self.search_agents_field).send_keys("Automation")##SEARCHING AGENTS
        time.sleep(4)
        fe(self.search_result).click() #firsst search result
        fe("/html/body/div[2]/div[2]/div/mat-dialog-container/app-new-conversation-dialog/div/div/div[2]/ul/li[2]/div/div/div[2]").click() ##second result after searching
        time.sleep(3)
        fe(self.search_agents_field).clear()
        time.sleep(2)
        fe(self.start_chat_button).click()
        time.sleep(1)

        group_name_from_list=fe("/html/body/app-root/app-layout/div/div/div/app-agents/div/div/div[1]/div/div[3]/app-agent-conv-list-sidebar/div/div[2]/ul/li[1]/a/div/div/div[2]/div/div[2]/b").text

        print(Fore.YELLOW+"group created =", group_name)
        print(Fore.YELLOW+"group appeared in the list =",group_name_from_list)


        if group_name==group_name_from_list:
            fe(self.group_name_in_list_chats).click()
            print("group created")
            time.sleep(2)
            self.driver.execute_script("window.scrollTo(0,600)")
            time.sleep(5)
            # fe("/html/body/app-root/app-layout/div/div/div/app-agents/div/div/div[2]/div/div[1]/app-agents-chat/div/div[2]/div/div[2]/div/div[1]/div/input").click()
            time.sleep(1)
            fe("/html/body/app-root/app-layout/div/div/div/app-agents/div/div/div[2]/div/div[1]/app-agents-chat/div/div[2]/div/div[2]/div/div[1]/div/input").send_keys("this message is from automation script in the group")  ##sending message

            time.sleep(2)
            fe("/html/body/app-root/app-layout/div/div/div/app-agents/div/div/div[2]/div/div[1]/app-agents-chat/div/div[2]/div/div[2]/div/div[2]/button").click()
            print("MESSAGE SENT")

            time.sleep(5)





        else:
            print(Fore.RED+"ERROR!!!! ")





