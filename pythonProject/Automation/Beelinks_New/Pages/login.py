import time

from selenium import webdriver
class llogin():

    def __init__(self, driver):
        self.driver=driver

        self.profile_dropddown="/html/body/app-root/app-layout/div/app-topbar/header/div/div[2]/div[4]/button"
        self.logout_xpath="/html/body/app-root/app-layout/div/app-topbar/header/div/div[2]/div[4]/div/a[5]"
        self.email_field="/html/body/app-root/app-login/div/div/div/div/div[1]/div[2]/div[2]/form/div[1]/input"
        self.password="/html/body/app-root/app-login/div/div/div/div/div[1]/div[2]/div[2]/form/div[2]/div/input"
        self.login_button="/html/body/app-root/app-login/div/div/div/div/div[1]/div[2]/div[2]/form/div[3]/button"
        self.hideandviewbutton_xpaht="/html/body/app-root/app-login/div/div/div/div/div[1]/div[2]/div[2]/form/div[2]/div/button"
        self.popup_xpath="/div/snack-bar-container/div/div/app-snackbar-dialog/div/span[2]"
        self.validation_message_for_email="/html/body/app-root/app-login/div/div/div/div/div[1]/div[2]/div[2]/form/div[1]/div/div"
        self.forgot_password_link="/html/body/app-root/app-login/div/div/div/div/div[1]/div[2]/div[2]/form/div[5]/a"
        self.emailof_forgot_password="/html/body/app-root/app-forget-password/div/div/div/div/div[1]/div[2]/form/div[1]/input"
        self.validation_message_forgot_password="/html/body/app-root/app-forget-password/div/div/div/div/div[1]/div[2]/form/div[1]/div/div"
        self.submit_button="/html/body/app-root/app-forget-password/div/div/div/div/div[1]/div[2]/form/div[2]/button"

    def logout_fucntion(self):
        ss = self.driver.find_element_by_xpath
        ss(self.profile_dropddown).click()
        ss(self.logout_xpath).click()




    def invalid_login(self):
        email=[" ","wsdsds"," ","acs@gmaiil.com","talhahhulhub@gmail.com"]
        password=[" ","12345678","12345678","12345678","12345678"]
        ss=self.driver.find_element_by_xpath
        self.logout_fucntion() #to logout from the system

        email_array_size=len(email)
        print("the size of array is = ",email_array_size) #checking siz eof array
        a=0
        while a < email_array_size:     # whiel loop for multiple valid and invalid emails
            ss(self.email_field).send_keys(email[a])
            ss(self.password).send_keys(password[a])
            ss(self.hideandviewbutton_xpaht).click()
            time.sleep(1)
            ss(self.hideandviewbutton_xpaht).click()
            time.sleep(1)
            ss(self.login_button).click()
            # element=ss(self.validation_message_for_email)
            # element_lenght = len(element)
            try:
                self.vm = ss(self.validation_message_for_email).text   # this try is to check if message is present then print if not then move to next step
                print(self.vm)
            except:
                print("No")

            url=self.driver.current_url #catching the url
            print(url)
            if url =="https://new.beelinks.solutions/login":  #this means url is not changed and
                ss(self.email_field).clear()
                ss(self.password).clear()

            else:
                print("you're logged in")
                break

            a +=1



    def forgot_passwords(self):
        self.driver.implicitly_wait(10)
        self.logout_fucntion() ## to logout again from the system
        time.sleep(2)
        self.driver.execute_script("window.scrollTo(0,500)")
        time.sleep(2)
        self.driver.find_element_by_xpath(self.forgot_password_link).click()#click on the forgot password link
        email_fotgot=["123456","agfgaf","325afa$#@$","talhahhulhub@gmail.com"]
        size_email=len(email_fotgot)

        f=0
        while f< size_email:
            self.driver.find_element_by_xpath(self.emailof_forgot_password).send_keys(email_fotgot[f]) #entee thg  email if email is invalid then it checks the message  and if message is present  then it will try new email
            try:
                msg = self.driver.find_element_by_xpath(self.validation_message_forgot_password).text
                print(msg)
                self.driver.find_element_by_xpath(self.emailof_forgot_password).clear()
                print("Please try a valid email that has been registered in beelinks")


            except:
                self.driver.find_element_by_xpath(self.submit_button).click()
                print("message sent ")

            f +=1


        print("second function executed")





