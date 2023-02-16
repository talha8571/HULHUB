import random
import string
import time

from selenium.webdriver.common.keys import Keys


class incomingEmail():
    def __init__(self, driver):
        self.driver=driver

        self.huluhb_icon = "/html/body/app-root/app-layout/div/app-topbar/header/div/div[1]/div/a[2]/span[1]/img"  # hulub icon click to land on dasboard
        self.settings_icon = "/html/body/app-root/app-layout/div/app-topbar/header/div/div[2]/div[5]/button"
        self.general_tab = "/html/body/app-root/app-layout/div/div/div/app-settings/div/div/div/div[1]/div/ul/li[1]/a/div"
        self.incoming_email_card="/html/body/app-root/app-layout/div/div/div/app-settings/div/div/div/div[2]/div/div/div/div/div[2]/div[2]/div[2]/div[5]/div/div"
        self.enter_name_field="/html/body/app-root/app-layout/div/div/div/app-incoming-email/div/div/div[2]/div/div/form/div/div[1]/div/input"
        self.add_external_email="/html/body/app-root/app-layout/div/div/div/app-incoming-email/div/div/div[2]/div/div/form/div/div[2]/div/input"
        self.assign_to_group="/html/body/app-root/app-layout/div/div/div/app-incoming-email/div/div/div[2]/div/div/form/div/div[3]/div/ng-select/div/div/div[2]/input"
        self.save_button="/html/body/app-root/app-layout/div/div/div/app-incoming-email/div/div/div[2]/div/div/form/button[1]"
        self.search_bar_of_incoming_email="/html/body/app-root/app-layout/div/div/div/app-incoming-email/div/div/div[1]/div[1]/div/div/input"
        self.delete_icon_of_forwarder="/html/body/app-root/app-layout/div/div/div/app-incoming-email/div/div/div[1]/div[2]/div[1]/div/div/div[2]/div[1]/div[2]/span[2]/i"
        self.ok_button_from_confirmation_popup="/html/body/ngb-modal-window/div/div/app-confirmation/div[3]/button[1]"


    def email_forwarder(self):
        fe = self.driver.find_element_by_xpath
        fe(self.huluhb_icon).click()
        fe(self.settings_icon).click()
        fe(self.general_tab).click()
        self.driver.execute_script("window.scrollTo(0,600)")
        fe(self.incoming_email_card).click()
        rand=random.randint(1,879454152)
        name="Automation"+str(rand)
        fe(self.enter_name_field).send_keys(rand)
        lettrr = random.choice(string.ascii_lowercase)
        email="Automated"+str(rand)+lettrr+"@gmail.com"
        fe(self.add_external_email).send_keys(email)
        fe(self.assign_to_group).click()
        fe(self.assign_to_group).send_keys("QA Testing",Keys.ENTER)
        time.sleep(1)
        fe(self.save_button).click()
        print("New Email Forwarder Created")
        time.sleep(4)

        fe(self.search_bar_of_incoming_email).send_keys(email)
        time.sleep(2)
        fe(self.delete_icon_of_forwarder).click()
        fe(self.ok_button_from_confirmation_popup).click()

        time.sleep(5)
        print("Email has been deleted")
        fe(self.search_bar_of_incoming_email).clear()

        nodata=fe("/html/body/app-root/app-layout/div/div/div/app-incoming-email/div/div/div[1]/div[2]/div/span[2]").is_displayed()
        print(nodata)



