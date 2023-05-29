
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

class toolbarClass():
    def __init__(self,driver):
        self.driver=driver
        self.toolbar_frame="/html/body/div[1]/div[1]/div[2]/div/div/div[2]/div/div/div[1]/p/iframe"
        self.internalpage="/html/body/div[1]/pre"


    def frame_scrolling(self):
        self.driver.switch_to.frame(self.driver.find_element_by_xpath(self.toolbar_frame))
        print("frame switched")
        self.driver.find_element_by_xpath(self.internalpage).click()

        self.t=self.driver.find_element_by_xpath(self.internalpage)
        ActionChains(self.driver).move_to_element(self.t)

        c=1
        while c<=200:
            ActionChains(self.driver).send_keys(Keys.ARROW_DOWN).perform()

            c=c+1

        self.driver.execute_script("window.scrollTo(0,300)")
