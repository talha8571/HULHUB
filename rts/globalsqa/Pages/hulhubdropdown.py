import time


class dropdownhulhub:

    def __init__(self,driver):
        self.driver=driver

        self.dropdown_xpath="/html/body/div[1]/main/section[3]/div/div/div[2]/form/div[1]/div[3]/div/div/div"
        self.countries="/html/body/div[1]/main/section[3]/div/div/div[2]/form/div[1]/div[3]/div/div/div/ul"





    def xyz(self):

        self.driver.find_element_by_xpath(self.dropdown_xpath).click()






