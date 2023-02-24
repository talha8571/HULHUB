import random
import time

from selenium.webdriver.common.keys import Keys


class tag_cloud():
    def __init__(self,driver):
        self.driver=driver

        self.huluhb_icon = "/html/body/app-root/app-layout/div/app-topbar/header/div/div[1]/div/a[2]/span[1]/img"  # hulub icon click to land on dasboard
        self.settings_icon = "/html/body/app-root/app-layout/div/app-topbar/header/div/div[2]/div[5]/button"
        self.ticket_management_tab = "/html/body/app-root/app-layout/div/div/div/app-settings/div/div/div/div[1]/div/ul/li[2]/a/div"
        self.tag_cloud_tag_card="/html/body/app-root/app-layout/div/div/div/app-settings/div/div/div/div[2]/div/div/div/div/div[2]/div[2]/div[2]/div[9]/div/div"
        self.add_tag_field="/html/body/app-root/app-layout/div/div/div/app-tag-cloud/div/div/div[2]/form/div/div/div/div/div/app-input-validations/div/form/ng-select/div/div/div[2]/input"
        self.add_tag_button="/html/body/app-root/app-layout/div/div/div/app-tag-cloud/div/div/div[2]/form/div/div/div/div/div/button"
        self.search_bar_of_tags="/html/body/app-root/app-layout/div/div/div/app-tag-cloud/div/div/div[1]/div/div/div/div[1]/div[1]/div/input"
        self.delete_button_of_searched_tag="/html/body/app-root/app-layout/div/div/div/app-tag-cloud/div/div/div[1]/div/div/div/div[2]/div/div/div[2]/span[2]/i"
        self.ok_button_from_confirmation="/html/body/ngb-modal-window/div/div/app-confirmation/div[3]/button[1]"

    def tag_cloud_method(self):
        self.driver.implicitly_wait(30)
        fe = self.driver.find_element_by_xpath
        fe(self.huluhb_icon).click()
        fe(self.settings_icon).click()
        fe(self.ticket_management_tab).click()
        time.sleep(2)
        fe(self.tag_cloud_tag_card).click()
        time.sleep(2)

        tag_name="#Automation"+str(random.randint(1,100))
        fe(self.add_tag_field).send_keys(tag_name,Keys.ENTER)
        time.sleep(1)
        fe(self.add_tag_button).click()
        print("tag has been created")
        time.sleep(1)
        fe(self.search_bar_of_tags).send_keys(tag_name)
        time.sleep(3)
        fe(self.delete_button_of_searched_tag).click()
        time.sleep(2)
        fe(self.ok_button_from_confirmation).click()
        print("tag has been created")
        time.sleep(3)






