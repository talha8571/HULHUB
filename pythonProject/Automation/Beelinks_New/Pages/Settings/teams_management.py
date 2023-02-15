import random
import time


class Teamsmanagement():
    def __init__(self,driver):
        self.driver=driver

        self.huluhb_icon = "/html/body/app-root/app-layout/div/app-topbar/header/div/div[1]/div/a[2]/span[1]/img"  # hulub icon click to land on dasboard
        self.settings_icon = "/html/body/app-root/app-layout/div/app-topbar/header/div/div[2]/div[5]/button"
        self.general_tab = "/html/body/app-root/app-layout/div/div/div/app-settings/div/div/div/div[1]/div/ul/li[1]/a/div"
        self.teams_management_card="/html/body/app-root/app-layout/div/div/div/app-settings/div/div/div/div[2]/div/div/div/div/div[2]/div[2]/div[2]/div[2]/div/div"
        self.add_team_button="/html/body/app-root/app-layout/div/div/div/app-team-management/div/div/div[1]/div/div/div[1]/button"
        self.team_name_field="/html/body/app-root/app-layout/div/div/div/app-team-management/div/div/div[1]/div/div/div[2]/div/form/div[1]/input"
        self.enter_description="/html/body/app-root/app-layout/div/div/div/app-team-management/div/div/div[1]/div/div/div[2]/div/form/div[2]/textarea"
        self.add_buttonofteamspopup="/html/body/app-root/app-layout/div/div/div/app-team-management/div/div/div[1]/div/div/div[2]/div/form/button"
        self.search_bar_of_teams="/html/body/app-root/app-layout/div/div/div/app-team-management/div/div/div[1]/div/div/div[2]/div/input"
        self.first_result_of_search_ofteam="/html/body/app-root/app-layout/div/div/div/app-team-management/div/div/div[1]/div/div/ul/li/a"
        self.add_agent_button="/html/body/app-root/app-layout/div/div/div/app-team-management/div/div/div[2]/div/div/div[1]/div/div[2]/div/button"
        self.select_agent_searchbar="/html/body/app-root/app-layout/div/div/div/app-team-management/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/ng-select/div/div/div[2]/input"
        self.first_result_of_searchedagent="/html/body/app-root/app-layout/div/div/div/app-team-management/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/ng-select/ng-dropdown-panel/div/div[2]/div"
        self.list_close_drop_down="/html/body/app-root/app-layout/div/div/div/app-team-management/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/ng-select/div/span[2]"
        self.add_button_afteraddigagent="/html/body/app-root/app-layout/div/div/div/app-team-management/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/button"




    def add_teams_management_method(self):
        fe=self.driver.find_element_by_xpath
        fe(self.huluhb_icon).click()
        fe(self.settings_icon).click()
        fe(self.general_tab).click()
        fe(self.teams_management_card).click()
        fe(self.add_team_button).click()
        ran=random.randint(1,4516841565460)
        team_name="Team"+str(ran)
        fe(self.team_name_field).send_keys(team_name)
        fe(self.enter_description).send_keys("Team created with automation script")
        fe(self.add_buttonofteamspopup).click()#clcik on add button afer adding name and description
        print("Team created")
        fe(self.search_bar_of_teams).send_keys(team_name)

        fe(self.first_result_of_search_ofteam).click()
        print("team appeared in the list")
        fe(self.add_agent_button).click()
        fe(self.select_agent_searchbar).send_keys("talhah@mailinator.com")
        time.sleep(5)
        fe(self.first_result_of_searchedagent).click()
        time.sleep(1)
        fe(self.list_close_drop_down).click()
        fe(self.add_button_afteraddigagent).click()
        print("agent added in the list")
        time.sleep(5)

