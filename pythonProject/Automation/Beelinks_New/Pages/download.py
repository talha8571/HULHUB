class Dnld():
    def __init__(self, driver):
        self.driver=driver

        self.agentstab_xpath="/html/body/app-root/app-layout/div/app-sidebar/div/div/div/div/ul/li[8]/a"
        self.arrowbutton="/html/body/app-root/app-layout/div/div/div/app-agents/div/div/div[1]/div/div[1]/div[1]/div/div/button"
        self.bulk_upload="/html/body/app-root/app-layout/div/div/div/app-agents/div/div/div[1]/div/div[1]/div[1]/div/div[2]/a[1]"
        self.downlaod_button="/html/body/div[2]/div[2]/div/mat-dialog-container/app-update-shift-timing-dialog/div[2]/a/span"


    def file(self):
        t=self.driver.find_element_by_xpath
        self.driver.find_element_by_xpath(self.agentstab_xpath).click()
        self.driver.find_element_by_xpath(self.arrowbutton).click()
        t(self.bulk_upload).click()
        t(self.downlaod_button).click()
