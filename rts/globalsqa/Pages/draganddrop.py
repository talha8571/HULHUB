import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
class dragdrop:


    def __init__(self,driver):
        self.driver=driver
        self.first_image_xpath="/html/body/div[1]/ul/li[1]/img"
        self.trash_xpath="/html/body/div[1]/div"
        self.iframe_drag_drop="/html/body/div[1]/div[1]/div[2]/div/div/div[2]/div/div/div[1]/p/iframe"



    def draganddrop_method(self):
        self.driver.implicitly_wait(20)
        self.driver.switch_to.frame(self.driver.find_element_by_xpath(self.iframe_drag_drop))
        # Identify the source and target elements for the drag and drop operation
        source=self.driver.find_element_by_xpath(self.first_image_xpath)
        target=self.driver.find_element_by_xpath(self.trash_xpath)

        # Perform the drag and drop operation
        ActionChains(self.driver).drag_and_drop(source,target).perform()
        time.sleep(2)



    def drag_drop_by_ofset(self):
        self.driver.implicitly_wait(20)
        # click on the accepted elements
        self.driver.find_element_by_xpath("/html/body/div/div[1]/div[2]/div/div/div[2]/div/ul/li[2]").click()

        ### switch in to frame
        self.driver.switch_to.frame(self.driver.find_element_by_xpath("/html/body/div/div[1]/div[2]/div/div/div[2]/div/div/div[2]/p/iframe"))##second iframe



        element=self.driver.find_element_by_xpath("/html/body/div[1]/p")

        ActionChains(self.driver).drag_and_drop_by_offset(element,588, 129).perform()##moving the element with help of ofsett





