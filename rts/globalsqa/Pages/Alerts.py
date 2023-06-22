from selenium.webdriver.common.alert import Alert

import time


class alerts():

    def __init__(self,driver):
        self.driver=driver

        self.alertwithokpage="/html/body/div[1]/div/div/div/div[1]/ul/li[1]/a"
        self.display_button_alert_Box="/html/body/div[1]/div/div/div/div[2]/div[1]/button"
        self.alert_okcnacel_page="/html/body/div[1]/div/div/div/div[1]/ul/li[2]/a"
        self.confirm_box_button="/html/body/div[1]/div/div/div/div[2]/div[2]/button"
        self.alert_withtext_page="/html/body/div[1]/div/div/div/div[1]/ul/li[3]/a"
        self.prompt_box="/html/body/div[1]/div/div/div/div[2]/div[3]/button"



    # ALERT ONLY WITH OK BUTTON
    def alertwithok(self):
        self.driver.get("https://demo.automationtesting.in/Alerts.html")
        self.driver.find_element_by_xpath(self.alertwithokpage).click()
        self.driver.find_element_by_xpath(self.display_button_alert_Box).click()
        time.sleep(2)
        Alert(self.driver).accept()


    #ALERT WITH OK AND CANCEL BUTTON
    def alertWithOkAndCancel(self):
        self.driver.find_element_by_xpath(self.alert_okcnacel_page).click()
        self.driver.find_element_by_xpath(self.confirm_box_button).click()
        # Switch to the alert
        confirmation_alert = Alert(self.driver)

        # Get the text of the confirmation message
        confirmation_text = confirmation_alert.text
        print("Confirmation Message:", confirmation_text)

        # Accept the confirmation box (click OK)
        confirmation_alert.accept()

        # Dismiss the confirmation box (click Cancel)
        # confirmation_alert.dismiss()


    #ALERT WITH TEXT, OK AND CANCEL BUTTON
    def text_alertbox(self):
        self.driver.get("https://demo.automationtesting.in/Alerts.html")

        self.driver.find_element_by_xpath(self.alert_withtext_page).click()
        self.driver.find_element_by_xpath(self.prompt_box).click()

        # Switch to the alert
        prompt_alert = Alert(self.driver)

        # Enter text in the prompt
        prompt_alert.send_keys("Hello, Selenium!")

        # Accept the prompt
        prompt_alert.accept()



