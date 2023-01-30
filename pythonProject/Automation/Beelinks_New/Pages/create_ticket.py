import random
import time

from selenium.webdriver.common.keys import Keys

class create_tickets():
    def __init__(self, driver):
        self.driver=driver

        self.plussign_xpath="/html/body/app-root/app-layout/div/app-topbar/header/div/div[2]/div[1]/button"
        self.create_Ticket_xpath="/html/body/app-root/app-layout/div/app-topbar/header/div/div[2]/div[1]/div/div/div[1]/div[1]/a"
        self.subject_field="/html/body/app-root/app-layout/div/div/div/app-kycapplication/div/div/div/div[2]/div/div/div/div/div/div/div/form/div[1]/div[1]/div/input"
        self.state="/html/body/app-root/app-layout/div/div/div/app-kycapplication/div/div/div/div[2]/div/div/div/div/div/div/div/form/div[1]/div[2]/div/ng-select/div/div/div[2]/input"
        self.priority="/html/body/app-root/app-layout/div/div/div/app-kycapplication/div/div/div/div[2]/div/div/div/div/div/div/div/form/div[2]/div[1]/div/ng-select/div/div/div[2]/input"
        self.group="/html/body/app-root/app-layout/div/div/div/app-kycapplication/div/div/div/div[2]/div/div/div/div/div/div/div/form/div[2]/div[2]/div/ng-select/div/div/div[2]/input"
        self.agent="/html/body/app-root/app-layout/div/div/div/app-kycapplication/div/div/div/div[2]/div/div/div/div/div/div/div/form/div[3]/div[1]/div/ng-select/div/div/div[2]/input"
        self.watchers="/html/body/app-root/app-layout/div/div/div/app-kycapplication/div/div/div/div[2]/div/div/div/div/div/div/div/form/div[3]/div[2]/div/ng-select/div/div/div[2]/input"
        self.visitors_name="/html/body/app-root/app-layout/div/div/div/app-kycapplication/div/div/div/div[2]/div/div/div/div/div/div/div/form/div[4]/div[1]/div/input"
        self.visiors_email="/html/body/app-root/app-layout/div/div/div/app-kycapplication/div/div/div/div[2]/div/div/div/div/div/div/div/form/div[4]/div[2]/div/input"
        self.tags="/html/body/app-root/app-layout/div/div/div/app-kycapplication/div/div/div/div[2]/div/div/div/div/div/div/div/form/div[5]/div/div/app-input-validations/div/form/ng-select/div/div/div[2]/input"
        self.message="/html/body/app-root/app-layout/div/div/div/app-kycapplication/div/div/div/div[2]/div/div/div/div/div/div/div/form/div[6]/div/ckeditor/div[2]/p"
        self.submit_button="/html/body/app-root/app-layout/div/div/div/app-kycapplication/div/div/div/div[2]/div/div/div/div/div/div/div/form/div[7]/div[1]/button"


    def create_tickets_manual(self):
        self.driver.implicitly_wait(30)

        random_number = random.randint(0, 99999)

        fe=self.driver.find_element_by_xpath
        fe(self.plussign_xpath).click() ##plus sign of maneu
        fe(self.create_Ticket_xpath).click()#create tciket from menu
        fe(self.subject_field).send_keys("FROM AUTOMATION TESTING", random_number) #subject
        fe(self.state).send_keys("OPEN",Keys.ENTER) #selecting state
        fe(self.priority).send_keys("Medium", Keys.ENTER)  # selecting priority
        time.sleep(1)
        fe(self.group).send_keys("QA Testing", Keys.ENTER)  # selecting group


        time.sleep(2)
        fe(self.agent).send_keys("qa.bizzchats@gmail.com",Keys.ENTER)
        time.sleep(1)
        fe(self.watchers).send_keys("talhahhulhub@gmail.com",Keys.ENTER)#selection watchers
        time.sleep(1)
        fe(self.visitors_name).send_keys("Automation")#visiitors name
        fe(self.visiors_email).send_keys("Automation",str(random_number)+"@gmail.com") #visitors email
        fe(self.tags).send_keys("#Automation",Keys.ENTER,"#Testing",Keys.ENTER)# tags
        time.sleep(2)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
        fe(self.message).click() #click on message field
        fe(self.message).send_keys(Keys.CONTROL, 'a')
        fe(self.message).send_keys(Keys.DELETE)
        fe(self.message).send_keys("This message is from automation script ")
        fe(self.submit_button).click()