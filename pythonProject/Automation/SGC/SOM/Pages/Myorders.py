import time


class myorders:
    def __init__(self,driver):
        self.driver=driver


        self.myorders_page_xpath="/html/body/sgc-web/general-layout/div/account-profile/div[1]/div/nav/div/ul/li[2]/a"
        self.my_submission_heading="/html/body/sgc-web/general-layout/div/app-my-submissions/div[2]/div/div[1]/label/h3"
        self.completed_orders_heading="/html/body/sgc-web/general-layout/div/app-my-submissions/div[2]/div/div[2]/label/h3"
        self.draft_orders_heading="/html/body/sgc-web/general-layout/div/app-my-submissions/div[2]/div/div[3]/label/h3"

    def mmorders(self):
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_xpath(self.myorders_page_xpath).click()
        self.driver.execute_script("window.scrollTo(0,400)")
        time.sleep(1)
        self.driver.execute_script("window.scrollTo(400,600)")
        time.sleep(1)
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        time.sleep(1)
        self.driver.execute_script("window.scrollTo(document.body.scrollHeight,0)")

        ######## verifcation of headings #######################
        submission=self.driver.find_element_by_xpath(self.my_submission_heading)
        ss=submission.is_displayed()
        if ss==True:
            print("submitted orders are displayed, ")
        else:
            print("Submitted orders are not displayed")

        completed = self.driver.find_element_by_xpath(self.completed_orders_heading)
        cc = completed.is_displayed()
        if cc == True:
            print("completed orders are displayed")
        else:
            print("completed orders are not displayed")


        draft=self.driver.find_element_by_xpath(self.draft_orders_heading)
        dd=draft.is_displayed()
        if dd == True:
            print("draft orders are displayed")
        else:
            print("draft orders are not displayed")