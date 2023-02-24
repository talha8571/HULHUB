import random

from selenium.webdriver.common.keys import Keys
import time



class ticketruleset():
    def __init__(self, driver):
        self.driver = driver

        self.huluhb_icon = "/html/body/app-root/app-layout/div/app-topbar/header/div/div[1]/div/a[2]/span[1]/img"  # hulub icon click to land on dasboard
        self.settings_icon = "/html/body/app-root/app-layout/div/app-topbar/header/div/div[2]/div[5]/button"
        self.general_tab = "/html/body/app-root/app-layout/div/div/div/app-settings/div/div/div/div[1]/div/ul/li[1]/a/div"
        self.ruleset_settings_card="/html/body/app-root/app-layout/div/div/div/app-settings/div/div/div/div[2]/div/div/div/div/div[2]/div[2]/div[2]/div[3]/div/div"
        self.first_heading="/html/body/app-root/app-layout/div/div/div/app-ruleset-management/div/div/div[1]/div/app-ruleset-list/div[2]/div[1]/div/div/div/div[1]/h5"
        self.Ruleset_name="/html/body/app-root/app-layout/div/div/div/app-ruleset-management/div/div/div[2]/div/app-ruleset-add-new/div/div/div/div/div/div/div[2]/form/div[1]/input"
        self.if_fieldname="/html/body/app-root/app-layout/div/div/div/app-ruleset-management/div/div/div[2]/div/app-ruleset-add-new/div/div/div/div/div/div/div[2]/form/div[3]/div[1]/div[2]/div/div/div[2]/div[1]/div/ng-select/div/div/div[3]"
        self.subject_option_fromdropdown="/html/body/app-root/app-layout/div/div/div/app-ruleset-management/div/div/div[2]/div/app-ruleset-add-new/div/div/div/div/div/div/div[2]/form/div[3]/div[1]/div[2]/div/div/div[2]/div[1]/div/ng-select/ng-dropdown-panel/div/div[2]/div[2]"
        self.matching_criteria_Dropdown="/html/body/app-root/app-layout/div/div/div/app-ruleset-management/div/div/div[2]/div/app-ruleset-add-new/div/div/div/div/div/div/div[2]/form/div[3]/div[1]/div[2]/div/div/div[2]/div[2]/div/div/div/ng-select/div/div/div[3]"
        self.contains_option="/html/body/app-root/app-layout/div/div/div/app-ruleset-management/div/div/div[2]/div/app-ruleset-add-new/div/div/div/div/div/div/div[2]/form/div[3]/div[1]/div[2]/div/div/div[2]/div[2]/div/div/div/ng-select/ng-dropdown-panel/div/div[2]/div[2]"
        self.keyword_field="/html/body/app-root/app-layout/div/div/div/app-ruleset-management/div/div/div[2]/div/app-ruleset-add-new/div/div/div/div/div/div/div[2]/form/div[3]/div[1]/div[2]/div/div/div[2]/div[3]/div/ng-select/div/div/div[2]/input"
        self.selectaction_dropdown="/html/body/app-root/app-layout/div/div/div/app-ruleset-management/div/div/div[2]/div/app-ruleset-add-new/div/div/div/div/div/div/div[2]/form/div[3]/div[2]/div[2]/div/div/div[2]/div[1]/ng-select/div/div/div[3]"
        self.addnote_option="/html/body/app-root/app-layout/div/div/div/app-ruleset-management/div/div/div[2]/div/app-ruleset-add-new/div/div/div/div/div/div/div[2]/form/div[3]/div[2]/div[2]/div/div/div[2]/div[1]/ng-select/ng-dropdown-panel/div/div[2]/div[5]"
        self.text_area_of_note="/html/body/app-root/app-layout/div/div/div/app-ruleset-management/div/div/div[2]/div/app-ruleset-add-new/div/div/div/div/div/div/div[2]/form/div[3]/div[2]/div[2]/div/div/div[2]/div[2]/div/div/ckeditor/div[2]/p"
        self.add_ruleset_button="/html/body/app-root/app-layout/div/div/div/app-ruleset-management/div/div/div[2]/div/app-ruleset-add-new/div/div/div/div/div/div/div[2]/button"


    def ticket_ruleset(self): #### navigation
        self.driver.implicitly_wait(20)
        fe=self.driver.find_element_by_xpath
        fe(self.huluhb_icon).click()
        fe(self.settings_icon).click()
        fe(self.general_tab).click()
        fe(self.ruleset_settings_card).click()
        fe(self.first_heading).click()
        time.sleep(2)
        body = self.driver.find_element_by_css_selector('body')
        body.send_keys(Keys.END)
        time.sleep(2)


    def ticketruleset_Creation(self):##creation fo rule set
        self.driver.implicitly_wait(20)
        fe = self.driver.find_element_by_xpath
        ran=random.randint(0,79845612478)
        ruleset_name="Automation_Rule_set"+str(ran)
        fe(self.Ruleset_name).send_keys(ruleset_name)
        fe(self.if_fieldname).click()
        fe(self.subject_option_fromdropdown).click()##clickign the subject option from dropdwon
        fe(self.matching_criteria_Dropdown).click()
        fe(self.contains_option).click()
        fe(self.keyword_field).send_keys("test",Keys.ENTER)

        fe(self.selectaction_dropdown).click()
        fe(self.addnote_option).click()
        self.driver.execute_script("window.scrollTo(0,800)")
        fe(self.text_area_of_note).send_keys("This rule set is created with automation script")
        time.sleep(2)
        fe(self.add_ruleset_button).click()
        time.sleep(6)
        fe("/html/body/app-root/app-layout/div/div/div/app-ruleset-management/div/div/div[1]/div/app-ruleset-list/div[1]/div/input").send_keys(ruleset_name)###ruleset name searching
        print("Ticket Rule Set created")
        time.sleep(2)
        searched_result=fe("/html/body/app-root/app-layout/div/div/div/app-ruleset-management/div/div/div[1]/div/app-ruleset-list/div[2]/div/div/div/div/div[1]/h5").text ##searcehd result from search bar
        if searched_result==ruleset_name:
            print("Ruleset Appeared in the List")
            fe("/html/body/app-root/app-layout/div/div/div/app-ruleset-management/div/div/div[1]/div/app-ruleset-list/div[2]/div/div/div/div/div[1]/div/div/span[2]").click()##delete button of searched ruleset

            time.sleep(1)
            fe("/html/body/ngb-modal-window/div/div/app-confirmation/div[3]/button[1]").click()#ok button from confiramtion message
            time.sleep(1)
            fe("/html/body/app-root/app-layout/div/div/div/app-ruleset-management/div/div/div[1]/div/app-ruleset-list/div[1]/div/input").clear()##clearing eh searched field
            time.sleep(5)


        else:
            print(" Searched Result Is Different")
