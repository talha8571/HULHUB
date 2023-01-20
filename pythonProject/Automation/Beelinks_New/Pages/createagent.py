import random
import time

from selenium.webdriver.common.keys import Keys

class Createagent():
    def __init__(self, driver):
        self.driver=driver

        self.plussign_xpath="/html/body/app-root/app-layout/div/app-topbar/header/div/div[2]/div[1]/button"
        self.createagent_xpaht="/html/body/app-root/app-layout/div/app-topbar/header/div/div[2]/div[1]/div/div/div[1]/div[2]/a"
        self.firstname_Xpath="/html/body/div[2]/div[2]/div/mat-dialog-container/app-add-agent-dialog/div/form/div[1]/div[1]/input"
        self.last_name_xpath="/html/body/div[2]/div[2]/div/mat-dialog-container/app-add-agent-dialog/div/form/div[1]/div[2]/input"
        self.nick_name="/html/body/div[2]/div[2]/div/mat-dialog-container/app-add-agent-dialog/div/form/div[2]/input"
        self.phone_no_xpath="/html/body/div[2]/div[2]/div/mat-dialog-container/app-add-agent-dialog/div/form/div[3]/input"
        self.extension="/html/body/div[2]/div[2]/div/mat-dialog-container/app-add-agent-dialog/div/form/div[4]/input"
        self.email="/html/body/div[2]/div[2]/div/mat-dialog-container/app-add-agent-dialog/div/form/div[5]/div[1]/input"
        self.password="/html/body/div[2]/div[2]/div/mat-dialog-container/app-add-agent-dialog/div/form/div[5]/div[2]/input"
        self.role="/html/body/div[2]/div[2]/div/mat-dialog-container/app-add-agent-dialog/div/form/div[7]/ng-select/div/div/div[2]/input"
        self.group="/html/body/div[2]/div[2]/div/mat-dialog-container/app-add-agent-dialog/div/form/div[8]/ng-select/div/div/div[2]/input"
        self.Simultaneous_Chats="/html/body/div[2]/div[2]/div/mat-dialog-container/app-add-agent-dialog/div/form/div[9]/input"
        self.submit_button="/html/body/div[2]/div[2]/div/mat-dialog-container/app-add-agent-dialog/div/form/div[12]/button"

    def createagent_method(self):
        self.driver.implicitly_wait(30)
        random_number=random.randint(0,99999)
        fe=self.driver.find_element_by_xpath #stroing driver.find element in variable to use next time
        fe(self.plussign_xpath).click()
        fe(self.createagent_xpaht).click()
        fe(self.firstname_Xpath).send_keys("test") #name
        nickname="nick"+str(random_number)

        fe(self.last_name_xpath).send_keys(nickname) #last name
        fe(self.nick_name).send_keys("nickname",random_number) #nickname

        phone_number_number = random.randint(0, 99999999999)
        fe(self.phone_no_xpath).send_keys(phone_number_number) #phone number

        fe(self.extension).send_keys(random_number) #extension
        fe(self.email).send_keys("bingo",random_number,"@test.com")#email
        fe(self.password).send_keys("12345678")
        time.sleep(2)

        fe(self.role).send_keys("admin",Keys.RETURN)
        fe(self.group).send_keys("qa testing",Keys.RETURN)
        fe(self.Simultaneous_Chats).send_keys("3")
        time.sleep(2)
        fe(self.submit_button).click()

        time.sleep(10)


