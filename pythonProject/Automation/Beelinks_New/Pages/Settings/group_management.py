import random
import time
from selenium.webdriver.common.keys import Keys


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
        fe(self.select_agent_search_bar).send_keys("talhah@mailinator.com", Keys.ENTER, "akhan9424@sbtjapan.com",Keys.ENTER)


