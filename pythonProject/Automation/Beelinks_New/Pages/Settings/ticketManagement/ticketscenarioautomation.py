import random
import time

from selenium.webdriver.common.keys import Keys


class ticketSCenario():

    def __init__(self, driver):
        self.driver=driver

        self.huluhb_icon = "/html/body/app-root/app-layout/div/app-topbar/header/div/div[1]/div/a[2]/span[1]/img"  # hulub icon click to land on dasboard
        self.settings_icon = "/html/body/app-root/app-layout/div/app-topbar/header/div/div[2]/div[5]/button"
        self.general_tab = "/html/body/app-root/app-layout/div/div/div/app-settings/div/div/div/div[1]/div/ul/li[1]/a/div"
        self.ticketscenarioautomationcard="/html/body/app-root/app-layout/div/div/div/app-settings/div/div/div/div[2]/div/div/div/div/div[2]/div[2]/div[2]/div[6]/div/div"
        self.scenarioname="/html/body/app-root/app-layout/div/div/div/app-scenario-automation/div/div/div[2]/div/div/form/div[1]/div[1]/div/input"
        self.scenario_description="/html/body/app-root/app-layout/div/div/div/app-scenario-automation/div/div/div[2]/div/div/form/div[1]/div[2]/div/textarea"
        self.addactiondropdown="/html/body/app-root/app-layout/div/div/div/app-scenario-automation/div/div/div[2]/div/div/form/div[1]/div[3]/div/div/div[2]/div[1]/div/ng-select/div/div/div[2]/input"
        self.paragraph_area="/html/body/app-root/app-layout/div/div/div/app-scenario-automation/div/div/div[2]/div/div/form/div[1]/div[3]/div/div/div[2]/div[4]/div/ckeditor/div[2]/p"
        self.save_button="/html/body/app-root/app-layout/div/div/div/app-scenario-automation/div/div/div[2]/div/div/form/div[2]/button[1]"
        self.first_heading_of_creted_scenario="/html/body/app-root/app-layout/div/div/div/app-scenario-automation/div/div/div[1]/div/div[1]/div/div[1]/h5"
        self.delete_icon="/html/body/app-root/app-layout/div/div/div/app-scenario-automation/div/div/div[1]/div/div[1]/div/div[1]/div/div/span[2]/i"
        self.ok_button_of_confirmation_message="/html/body/ngb-modal-window/div/div/app-confirmation/div[3]/button[1]"


    def ticketscenariomethod(self):
        fe = self.driver.find_element_by_xpath
        fe(self.huluhb_icon).click()
        fe(self.settings_icon).click()
        fe(self.general_tab).click()
        self.driver.execute_script("window.scrollTo(0,600)")
        fe(self.ticketscenarioautomationcard).click()
        scenarioname="Automated"+str(random.randint(1,852369715))
        fe(self.scenarioname).send_keys(scenarioname)
        fe(self.scenario_description).send_keys("Automated description")
        fe(self.addactiondropdown).click()
        fe(self.addactiondropdown).send_keys("Add Note",Keys.ENTER)
        self.driver.execute_script("window.scrollTo(0,600)")
        fe(self.paragraph_area).send_keys("Testing decription")
        fe(self.save_button).click()
        print("ticket scenario has been created with the name",scenarioname,"\n")
        time.sleep(4)
        first_text=fe(self.first_heading_of_creted_scenario).text
        if first_text==scenarioname:
            fe("/html/body/app-root/app-layout/div/div/div/app-scenario-automation/div/div/div[1]/div").click()
            body = self.driver.find_element_by_css_selector('body')
            body.send_keys(Keys.HOME)
            time.sleep(1)
            fe(self.delete_icon).click()
            fe(self.ok_button_of_confirmation_message).click()
            print("Ticket Scenario",scenarioname, "has been DELETED!!!!\n")
            time.sleep(3)


