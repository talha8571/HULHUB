import time
class customer_survey():
    def __init__(self, driver):
        self.driver=driver

        self.huluhb_icon = "/html/body/app-root/app-layout/div/app-topbar/header/div/div[1]/div/a[2]/span[1]/img"  # hulub icon click to land on dasboard
        self.settings_icon = "/html/body/app-root/app-layout/div/app-topbar/header/div/div[2]/div[5]/button"
        self.general_tab = "/html/body/app-root/app-layout/div/div/div/app-settings/div/div/div/div[1]/div/ul/li[1]/a/div"
        self.customer_stisfaction_survery="/html/body/app-root/app-layout/div/div/div/app-settings/div/div/div/div[2]/div/div/div/div/div[2]/div[2]/div[2]/div[8]/div/div"



    def customer_survery_method(self):
        fe = self.driver.find_element_by_xpath

        fe(self.huluhb_icon).click()
        fe(self.settings_icon).click()
        fe(self.general_tab).click()
        time.sleep(1)
        self.driver.execute_script("window.scrollTo(0,700)")
        fe(self.customer_stisfaction_survery).click()
        time.sleep(3)