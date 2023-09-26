import time
from selenium.webdriver import ActionChains

class homepage():

    def __init__(self, driver):

        self.driver=driver
        self.slider_right_button_xpath="/html/body/main/div/div[1]/div[1]/div[1]/div/div/div/div/div[3]/i"
        self.slider_left_button_xpath="/html/body/main/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/i"
        self.navbar_xpath="/html/body/div[1]/div[1]/div/div[2]/div[2]/div/div/a"
        self.below_slider="/html/body/main/div/div[1]/div[1]/div[2]/div/div/div[1]/div/div/a"
        self.continental_biscuits_heading="/html/body/main/div/div[1]/div[2]/div/div[2]/div/h2"
        self.our_brands_heading="/html/body/main/div/div[1]/div[4]/div/div/div/h2"
        self.ourbrands_rightarrow="/html/body/main/div/div[1]/div[5]/div/div/div/div/div[3]/i"
        self.ourbrands_leftarrow="/html/body/main/div/div[1]/div[5]/div/div/div/div/div[2]/i"

    def home_execution(self):
        x=self.driver.find_element_by_xpath

        #hover on the nav bar icon to see nav bar
        b=ActionChains(self.driver)
        h=x(self.navbar_xpath)
        b.move_to_element(h).perform()


        #clcik on the right arrow
        for i in range(1,5):
            x(self.slider_right_button_xpath).click()
            time.sleep(0.5)

        # clcik on the left arrow
        for i in range(1, 5):
            x(self.slider_left_button_xpath).click()
            time.sleep(0.5)

        x(self.below_slider).click()#clcik on the below slider
        a=x(self.continental_biscuits_heading).text
        print(a)
        if a=="CONTINENTAL BISCUITS LIMITED":
            print("heading verified")

        else:
            print("heading not verified")

    def ourbrands_heading(self):
        x = self.driver.find_element_by_xpath

        for i in range(1,12):
            x(self.ourbrands_rightarrow).click()
            time.sleep(0.5)
        time.sleep(1)

        for i in range(1,12):
            x(self.ourbrands_leftarrow).click()
            time.sleep(0.5)



