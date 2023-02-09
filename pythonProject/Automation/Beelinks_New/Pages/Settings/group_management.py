import random
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class group_management_class():
    def __init__(self,driver):
        self.driver=driver

        self.huluhb_icon = "/html/body/app-root/app-layout/div/app-topbar/header/div/div[1]/div/a[2]/span[1]/img"  # hulub icon click to land on dasboard
        self.settings_icon = "/html/body/app-root/app-layout/div/app-topbar/header/div/div[2]/div[5]/button"
        self.general_tab = "/html/body/app-root/app-layout/div/div/div/app-settings/div/div/div/div[1]/div/ul/li[1]/a/div"
        self.group_management_card="/html/body/app-root/app-layout/div/div/div/app-settings/div/div/div/div[2]/div/div/div/div/div[2]/div[2]/div[2]/div[1]/div/div"
        self.add_group_button="/html/body/app-root/app-layout/div/div/div/app-group-management/div/div/div[1]/div/div/div/div[1]/div[1]/button"
        self.group_name="/html/body/app-root/app-layout/div/div/div/app-group-management/div/div/div[1]/div/div/div/div[1]/div[1]/div/form/div/div[1]/div/input"
        self.description="/html/body/app-root/app-layout/div/div/div/app-group-management/div/div/div[1]/div/div/div/div[1]/div[1]/div/form/div/div[2]/div/textarea"
        self.add_Group_button_in_popup="/html/body/app-root/app-layout/div/div/div/app-group-management/div/div/div[1]/div/div/div/div[1]/div[1]/div/form/div/div[3]/button"
        self.search_bar_of_group="/html/body/app-root/app-layout/div/div/div/app-group-management/div/div/div[1]/div/div/div/div[2]/div/div/input"
        self.add_agent_in_group_button="/html/body/app-root/app-layout/div/div/div/app-group-management/div/div/div[2]/div/div/div[1]/div/div/div[2]/div/div[1]/button"
        self.select_agent_search_bar="/html/body/app-root/app-layout/div/div/div/app-group-management/div/div/div[2]/div/div/div[1]/div/div/div[2]/div/div[1]/div/form/div/div/ng-select/div/div/div[2]/input"
        self.assign_agent_button_after_selection="/html/body/app-root/app-layout/div/div/div/app-group-management/div/div/div[2]/div/div/div[1]/div/div/div[2]/div/div[1]/div/form/div/button"
        self.all_check_box="/html/body/app-root/app-layout/div/div/div/app-group-management/div/div/div[2]/div/div/div[3]/div/div/table/thead/tr/td/div/input"
        self.unassigned_agents="/html/body/app-root/app-layout/div/div/div/app-group-management/div/div/div[2]/div/div/div[1]/div/div/div[2]/div/button[1]"
        self.ok_button_of_confirmationbox="/html/body/ngb-modal-window/div/div/app-confirmation/div[3]/button[1]"
        self.no_record_available="/html/body/app-root/app-layout/div/div/div/app-group-management/div/div/div[2]/div/div/div[3]/div/div/div/div/h4"



    def add_group_in_settings(self):
        self.driver.implicitly_wait(20)
        fe = self.driver.find_element_by_xpath

        fe(self.huluhb_icon).click()
        fe(self.settings_icon).click()
        fe(self.general_tab).click()

        fe(self.group_management_card).click()
        fe(self.add_group_button).click()

        rand=random.randint(1,85274196325)
        group_name="Automation Group"+str(rand) #group name
        fe(self.group_name).send_keys(group_name)
        fe(self.description).send_keys("this group is created with automation script")
        fe(self.add_Group_button_in_popup).click()
        time.sleep(3)
        fe(self.search_bar_of_group).send_keys(group_name)
        time.sleep(2)
        fe("/html/body/app-root/app-layout/div/div/div/app-group-management/div/div/div[1]/div/div/div/ul/li[1]/div/a/div[1]").click()##first result after searching

        ##add agent in the group

        fe(self.add_agent_in_group_button).click()

        fe(self.select_agent_search_bar).click()
        fe(self.select_agent_search_bar).send_keys("talhah@mailinator.com")

        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, "/html/body/app-root/app-layout/div/div/div/app-group-management/div/div/div[2]/div/div/div[1]/div/div/div[2]/div/div[1]/div/form/div/div/ng-select/ng-dropdown-panel/div/div[2]/div[1]/span")))
        fe(self.select_agent_search_bar).send_keys(Keys.ENTER)



        # fe(self.select_agent_search_bar).send_keys("talhah@mailinator.com",Keys.ENTER)
        # time.sleep(3)
        # fe(self.select_agent_search_bar).send_keys(Keys.ENTER)
        # email1=fe("/html/body/app-root/app-layout/div/div/div/app-group-management/div/div/div[2]/div/div/div[1]/div/div/div[2]/div/div[1]/div/form/div/div/ng-select/ng-dropdown-panel/div/div[2]/div[1]/span").text
        #
        # if email1=="talhah@mailinator.com":
        #     time.sleep(1)
        #     fe("/html/body/app-root/app-layout/div/div/div/app-group-management/div/div/div[2]/div/div/div[1]/div/div/div[2]/div/div[1]/div/form/div/div/ng-select/ng-dropdown-panel/div/div[2]/div/span").click()
        #
        # else:
        #     time.sleep(5)
        #     fe("/html/body/app-root/app-layout/div/div/div/app-group-management/div/div/div[2]/div/div/div[1]/div/div/div[2]/div/div[1]/div/form/div/div/ng-select/ng-dropdown-panel/div/div[2]/div/span").click()

        # # while True:
        # email2 = fe("/html/body/app-root/app-layout/div/div/div/app-group-management/div/div/div[2]/div/div/div[1]/div/div/div[2]/div/div[1]/div/form/div/div/ng-select/ng-dropdown-panel/div/div[2]/div[1]/span").text
        #     if email1==email2:
        #         time.sleep(2)
        #         fe("/html/body/app-root/app-layout/div/div/div/app-group-management/div/div/div[2]/div/div/div[1]/div/div/div[2]/div/div[1]/div/form/div/div/ng-select/ng-dropdown-panel/div/div[2]/div[1]").click()
        #         break

        # fe("/html/body/app-root/app-layout/div/div/div/app-group-management/div/div/div[2]/div/div/div[1]/div/div/div[2]/div/div[1]/div/form/div/div/ng-select/ng-dropdown-panel/div/div[2]/div/span").click()


        fe(self.assign_agent_button_after_selection).click()
        time.sleep(3)
        print("agent has been added in the group")

        fe("/html/body/app-root/app-layout/div/div/div/app-group-management/div/div/div[2]/div/div/div[1]/div/div/div[2]/div/div[3]/div/input").send_keys("talhah@mailinator.com")#3searching added agent int he group list
        searched_result=fe("/html/body/app-root/app-layout/div/div/div/app-group-management/div/div/div[2]/div/div/div[3]/div/div/table/tbody/tr/td[2]/span").text #after searching capturing the text of the agent
        print(searched_result)

        if searched_result=="talhah@mailinator.com":
            print("agent added and appeared in the list")
            time.sleep(1)
            fe("/html/body/app-root/app-layout/div/div/div/app-group-management/div/div/div[2]/div/div/div[1]/div/div/div[2]/div/div[3]/div/input").clear() #clearing agent in the group list

        time.sleep(1)
        fe(self.all_check_box).click()
        time.sleep(2)
        fe(self.unassigned_agents).click()
        print("agents unassigned")
        time.sleep(1)
        fe(self.ok_button_of_confirmationbox).click()
        time.sleep(5)

        # # while True:
        # #     ncr=fe("/html/body/app-root/app-layout/div/div/div/app-group-management/div/div/div[2]/div/div/div[3]/div/div/div/div/h4").text
        # #     if ncr.is_displayed:
        # #         print("done")
        # #         break
        #
        # self.driver.refresh()
        # fe(self.search_bar_of_group).send_keys(group_name)
        # time.sleep(2)
        # fe("/html/body/app-root/app-layout/div/div/div/app-group-management/div/div/div[1]/div/div/div/ul/li[1]/div/a/div[1]").click()  ##first result after searching






