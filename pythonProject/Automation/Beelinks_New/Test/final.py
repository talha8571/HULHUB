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
from seleniumwire import webdriver

################### import of classes from different pages #####################################

from Automation.Beelinks_New.Pages.login import llogin
from Automation.Beelinks_New.Pages.createagent import Createagent
from Automation.Beelinks_New.Pages.create_ticket import create_tickets
from Automation.Beelinks_New.Pages.new_conversations import nEW_COnversations
from Automation.Beelinks_New.Pages.new_group import new_group
from Automation.Beelinks_New.Pages.upload_bulk_shift_timings import shift_timings
from Automation.Beelinks_New.Pages.upload_bulk_supervisor import bulk_supervisor
from Automation.Beelinks_New.Pages.visitors import visitors_class

from Automation.Beelinks_New.Pages.marketing import marketing_tab


from Automation.Beelinks_New.Pages.lms import Dashbaord_LMS


###############################################################################################

import re
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

class HOV(unittest.TestCase):


    @classmethod
    def setUpClass(cls):
        cls.option1=Options()
        cls.option1.add_argument("--disable-notifications")
        cls.driver=webdriver.Chrome(ChromeDriverManager().install())
        cls.driver.implicitly_wait(30)
        cls.driver.get("https://new.beelinks.solutions/login")
        # a = cls.driver.find_element_by_xpath
        cls.driver.maximize_window()
        cls.driver.find_element_by_xpath("/html/body/app-root/app-login/div/div/div/div/div[1]/div[2]/div[2]/form/div[1]/input").send_keys("talhahhulhub@gmail.com")
        cls.driver.find_element_by_xpath("/html/body/app-root/app-login/div/div/div/div/div[1]/div[2]/div[2]/form/div[2]/div/input").send_keys("12345678")
        cls.driver.find_element_by_xpath("/html/body/app-root/app-login/div/div/div/div/div[1]/div[2]/div[2]/form/div[3]/button").click()




    def test_a_login(self):
        driver=self.driver
        self.driver.implicitly_wait(10)
        lg=llogin(driver)
        lg.invalid_login() ## first method for login test

        ##s second method for forgot password
        lg.forgot_passwords()
        time.sleep(2)
        self.driver.back()
        self.driver.find_element_by_xpath("/html/body/app-root/app-login/div/div/div/div/div[1]/div[2]/div[2]/form/div[1]/input").send_keys("qa.bizzchats@gmail.com")
        self.driver.find_element_by_xpath("/html/body/app-root/app-login/div/div/div/div/div[1]/div[2]/div[2]/form/div[2]/div/input").send_keys("12345678")
        self.driver.find_element_by_xpath("/html/body/app-root/app-login/div/div/div/div/div[1]/div[2]/div[2]/form/div[3]/button").click()


    def test_b_createagent(self):
        driver=self.driver
        self.driver.implicitly_wait(20)
        cra=Createagent(driver)
        cra.createagent_method() ######### first method

        time.sleep(2)
        # self.driver.refresh()
        cra.ageentstab() ########## second method
        time.sleep(2)

        agentsname = self.driver.find_element_by_xpath("/html/body/app-root/app-layout/div/div/div/app-agents/div/div/div[1]/div/div[3]/app-agent-list-sidebar/div[2]/ul/li/div/div/div[3]/h5").text

        self.assertEqual(agentsname, cra.nickname)
        print("agent has been created and appeared in the list as well")
        time.sleep(2)
        cra.edit_profile() ##third method
        time.sleep(4)

        cra.edit_role()#fourth method


        # print("role from array is" , cra.role_agent)
        # print("role captured from screen is ",cra.role_of_agent_in_tag)
        # self.assertEqual(cra.role_agent, cra.role_of_agent_in_tag)
        print("role has been updated")

        time.sleep(2)
        cra.edit_password() #edit password method
        print("password updated")
        time.sleep(1)


    def test_c_agent_notification(self):
        self.driver.implicitly_wait(20)
        driver=self.driver
        noti=Createagent(driver)##class name
        noti.profile_notifications()

        email_notification_heading=self.driver.find_element_by_xpath("/html/body/app-root/app-layout/div/div/div/app-agents/div/div/div[2]/div/div/div/div/div/div[1]/div/div[1]/h4").text
        window_notification_heading=self.driver.find_element_by_xpath("/html/body/app-root/app-layout/div/div/div/app-agents/div/div/div[2]/div/div/div/div/div/div[1]/div/div[2]/h4").text
        Audio_notification_heading=self.driver.find_element_by_xpath("/html/body/app-root/app-layout/div/div/div/app-agents/div/div/div[2]/div/div/div/div/div/div[1]/div/div[3]/h4").text

        if email_notification_heading == "Email Notifications" and window_notification_heading == "Window Notifications" and Audio_notification_heading =="Audio Notifications":
            print("email, window and audio notifications are displayed")

        else:
            print("notifications are not displayed")



    def test_d_new_conversation(self):
        driver=self.driver
        self.driver.implicitly_wait(20)

        nc=nEW_COnversations(driver)
        nc.conversation_method()
        time.sleep(2)

    def test_e_new_group(self):
        driver = self.driver
        self.driver.implicitly_wait(20)
        ng=new_group(driver)
        ng.create_new_group()

    def test_f_upload_bulkshift(self):

        driver=self.driver
        driver.implicitly_wait(20)
        us=shift_timings(driver)
        us.upload_shift_timings_method()
        time.sleep(10)

    def test_g_upload_supervisor(self):
        driver=self.driver
        self.driver.implicitly_wait(20)
        us=bulk_supervisor(driver)
        us.bulk_supervisor() ###calling mtheod from file
        time.sleep(2)


    def test_g_viistors(self):
        driver=self.driver
        self.driver.implicitly_wait(20)
        vst=visitors_class(driver)
        vst.visitors_method()





    def test_h_marketing(self):
        driver=self.driver
        driver.implicitly_wait(30)
        mk=marketing_tab(driver)
        mk.create_contact_list() ##function of create contact list
        time.sleep(2)
        mk.campaign_creation()#function of campaign creation
        time.sleep(2)
        mk.campaign_execution()









    # def test_d_create_ticket(self):
    #     self.driver.implicitly_wait(30)
    #     driver=self.driver
    #     ct=create_tickets(driver)
    #     ct.create_tickets_manual()
    #     time.sleep(5)








    def test_i_lmscmd(self):
        self.driver.implicitly_wait(30)
        driver=self.driver
        dlms=Dashbaord_LMS(driver)
        dlms.LMS_method()

        self.assertEqual(dlms.lmshead_v, "LIVE MONITORING SYSTEM") #heading verification
        print("Lms Heading verified")
        self.assertEqual(dlms.onlineag_v, "Online Agents")
        print("Online agents heading verified")
        self.assertEqual(dlms.active_v, "Active Agents")
        print("Active agents heading verified")
        self.assertEqual(dlms.agents_on_break_V, "Agents on Break")
        print("Agents on breaks heading verified")
        self.assertEqual(dlms.agent_chatting_V, "Agents Chatting")
        print("agents chatting heading verified")
        self.assertEqual(dlms.agent_not_chatting_V, "Agents Not Chatting")
        print("agents not chatting verified")
        self.assertEqual(dlms.total_chats_V, "Total Chats")
        print("total chats heading verified")
        self.assertEqual(dlms.average_speed_V, "Average Speed of Answer")
        print("average speed of answer heading verified")
        self.assertEqual(dlms.occupancy_v, "Occupancy")
        print("occupancy heading verified")
        self.assertEqual(dlms.visitors_text_v, "Visitors")
        print("Visitors heading verified")
        self.driver.execute_script("window.scrollTo(0,500)")
        self.assertEqual(dlms.agent_list_v, "Agent List", "Agent list verified")

        t=self.driver.current_url
        self.assertEqual(t,"https://new.beelinks.solutions/dashboards/lms","url matched")
        
    # @classmethod
    # def tearDownClass(cls):
    #     cls.driver.close()


        
        
        
if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="C:/Users/1154-Talha/PycharmProjects/pythonProject/Automation/Beelinks_New/Report"))