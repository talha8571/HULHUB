import time


class cardgrading():
    def __init__(self,driver):
        self.driver=driver

        self.cardgrading_xpath="/html/body/sgc-web/general-layout/div/div/ul/li[1]/a"
        self.moreinfo_xpath="/html/body/sgc-web/general-layout/div/static-layout/ng-component/services-pricing/ul/li[2]/a"
        self.tengm_xpath="/html/body/sgc-web/general-layout/div/static-layout/ng-component/how-it-works/div[2]/section/div/ul/li[2]"
        self.reholder_xpath="/html/body/sgc-web/general-layout/div/static-layout/ng-component/services-pricing/div[2]/ejs-tab/div[1]/div/div[3]/div/div/div"
        self.oversized_xpath="/html/body/sgc-web/general-layout/div/static-layout/ng-component/services-pricing/div[2]/ejs-tab/div[1]/div/div[4]/div/div/div"
        self.ov_reholderxpath="/html/body/sgc-web/general-layout/div/static-layout/ng-component/services-pricing/div[2]/ejs-tab/div[1]/div/div[5]/div/div/div"

    def clickcardgrading(self):
        self.driver.find_element_by_xpath(self.cardgrading_xpath).click()
        self.driver.execute_script("window.scrollTo(0,400)")
        time.sleep(1)
        self.driver.execute_script("window.scrollTo(400,800)")
        time.sleep(1)
        self.driver.execute_script("window.scrollTo(800,0)")
        time.sleep(3)

        self.driver.find_element_by_xpath(self.reholder_xpath).click()

        time.sleep(1)
        self.driver.find_element_by_xpath(self.oversized_xpath).click()

        time.sleep(1)
        self.driver.find_element_by_xpath(self.ov_reholderxpath).click()

        time.sleep(1)

        self.driver.find_element_by_xpath(self.moreinfo_xpath).click()
        self.driver.find_element_by_xpath(self.tengm_xpath).click()
        time.sleep(1)


