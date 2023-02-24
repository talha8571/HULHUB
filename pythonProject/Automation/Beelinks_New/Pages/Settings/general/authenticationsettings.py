import time


class auth_setting():
    def __init__(self,driver):
        self.driver=driver

        self.huluhb_icon = "/html/body/app-root/app-layout/div/app-topbar/header/div/div[1]/div/a[2]/span[1]/img"  # hulub icon click to land on dasboard
        self.settings_icon = "/html/body/app-root/app-layout/div/app-topbar/header/div/div[2]/div[5]/button"
        self.general_tab = "/html/body/app-root/app-layout/div/div/div/app-settings/div/div/div/div[1]/div/ul/li[1]/a/div"
        self.teams_management_card = "/html/body/app-root/app-layout/div/div/div/app-settings/div/div/div/div[2]/div/div/div/div/div[2]/div[2]/div[2]/div[2]/div/div"
        self.authentication_settings="/html/body/app-root/app-layout/div/div/div/app-settings/div/div/div/div[2]/div/div/div/div/div[2]/div[1]/div[2]/div[5]/div/div"
        self.all_agents_tab="/html/body/app-root/app-layout/div/div/div/app-authentication/div/div/div[1]/div/div[1]/div/div/div/ul/li[1]"
        self.admin_tab="/html/body/app-root/app-layout/div/div/div/app-authentication/div/div/div[1]/div/div[1]/div/div/div/ul/li[2]"
        self.supervisor_tab="/html/body/app-root/app-layout/div/div/div/app-authentication/div/div/div[1]/div/div[1]/div/div/div/ul/li[3]"
        self.agent_tab="/html/body/app-root/app-layout/div/div/div/app-authentication/div/div/div[1]/div/div[1]/div/div/div/ul/li[4]"
        self.sales_person_tab="/html/body/app-root/app-layout/div/div/div/app-authentication/div/div/div[1]/div/div[1]/div/div/div/ul/li[5]"
        self.whatsaap_agent="/html/body/app-root/app-layout/div/div/div/app-authentication/div/div/div[1]/div/div[1]/div/div/div/ul/li[6]"



    def authentication_setting_method(self):
        self.driver.implicitly_wait(30)
        fe=self.driver.find_element_by_xpath
        fe(self.huluhb_icon).click()
        fe(self.settings_icon).click()
        fe(self.general_tab).click()
        fe(self.authentication_settings).click()
        time.sleep(3)

         ## clicking on multiple tabs
        fe(self.admin_tab).click()
        time.sleep(2)
        fe(self.supervisor_tab).click()
        time.sleep(2)
        fe(self.agent_tab).click()
        time.sleep(2)
        fe(self.sales_person_tab).click()
        time.sleep(2)
        fe(self.whatsaap_agent).click()
        time.sleep(2)
        fe(self.all_agents_tab).click()
        time.sleep(2)



