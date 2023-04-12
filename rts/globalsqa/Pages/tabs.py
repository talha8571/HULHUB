import time


class firststep_tabs():

    def __init__(self,driver):
        self.driver=driver


        self.tabs_xpath="/html/body/div/div[1]/div/div[2]/div/div/div[2]/div[1]/ul/li[2]/a"
        self.section1_xpath= 'ui-id-1'
        self.section2_xpath= "ui-id-3"
        self.section3_xpath = "/html/body/div[1]/h3[3]"
        # self.section4_xpath = "/html/body/div[1]/h3[4]"
        self.paragraph_sction2="/html/body/div[1]/div[2]/p"



    def clicking(self):
        dfx=self.driver.find_element_by_id
        self.driver.find_element_by_xpath(self.tabs_xpath).click()
        time.sleep(2)
        self.driver.switch_to.frame(self.driver.find_element_by_xpath("/html/body/div/div[1]/div[2]/div/div/div[2]/div/div/div[1]/p/iframe"))
        time.sleep(2)
        dfx(self.section1_xpath).click()
        dfx(self.section2_xpath).click()
        time.sleep(3)
        parah2=self.driver.find_element_by_xpath(self.paragraph_sction2)


        ##checking if paragraph is displayed or not
        if parah2.is_displayed():
            print("!!!!!!!!!!!!!!!Paragraph is displayed of section 2!!!!!!!!!!!!!!!")
        else:
            print("NOT DISPLAYED")


        self.driver.find_element_by_xpath(self.section3_xpath).click()
        list=self.driver.find_elements_by_xpath("/html/body/div[1]/div[3]/ul")



        if list:
            print("list is visible in section 3")

        else:
            print("LIST IS NOT VISIBLE!!!!!!!!")


        # dfx(self.section3_xpath)
        # dfx(self.section4_xpath)

