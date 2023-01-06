from selenium import webdriver
class llogin():

    def __init__(self, driver):
        self.driver=driver

        self.profile_dropddown="/html/body/app-root/app-layout/div/app-topbar/header/div/div[2]/div[4]/button"
        self.logout_xpath="/html/body/app-root/app-layout/div/app-topbar/header/div/div[2]/div[4]/div/a[5]"
        self.email_field="/html/body/app-root/app-login/div/div/div/div/div[1]/div[2]/div[2]/form/div[1]/input"
        self.password="/html/body/app-root/app-login/div/div/div/div/div[1]/div[2]/div[2]/form/div[2]/div/input"
        self.login_button="/html/body/app-root/app-login/div/div/div/div/div[1]/div[2]/div[2]/form/div[3]/button"
        self.popup_xpath="/div/snack-bar-container/div/div/app-snackbar-dialog/div/span[2]"
        self.validation_message_for_email="/html/body/app-root/app-login/div/div/div/div/div[1]/div[2]/div[2]/form/div[1]/div/div"




    def invalid_login(self):
        email=[" ","wsdsds","acs@gmaiil.com","qa.bizzchats@gmail.com"]
        password=[" ","12345678","12345678","12345678"]
        ss=self.driver.find_element_by_xpath

        ss(self.profile_dropddown).click()
        ss(self.logout_xpath).click()
        email_array_size=len(email)
        print("the size of array is = ",email_array_size)
        a=0
        while a < email_array_size:
            ss(self.email_field).send_keys(email[a])
            ss(self.password).send_keys(password[a])
            ss(self.login_button).click()
            # element=ss(self.validation_message_for_email)
            # element_lenght = len(element)
            try:
                # t=ss(self.validation_message_for_email).is_displayed()
                self.vm = ss(self.validation_message_for_email).text
                print(self.vm)
            except:
                print("No")

            url=self.driver.current_url
            print(url)
            if url =="https://new.beelinks.solutions/login":
                ss(self.email_field).clear()
                ss(self.password).clear()

            else:
                print("youre logged in")


            a +=1







