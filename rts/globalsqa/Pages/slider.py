from selenium.webdriver import ActionChains

class sliders():

    def __init__(self,driver):
        self.driver=driver

        self.slider_button_xpath="/html/body/div/div[1]/div/div[2]/div/div/div[2]/div[1]/ul/li[3]/a"
        self.red_slider_icon="/html/body/div[1]/span"



    def slider_execution(self):
        self.driver.implicitly_wait(20)


        self.driver.find_element_by_xpath(self.slider_button_xpath).click()
        self.driver.switch_to_frame(self.driver.find_element_by_xpath("/html/body/div/div[1]/div[2]/div/div/div[2]/div/div/div[1]/p/iframe"))

        redslider=self.driver.find_element_by_xpath(self.red_slider_icon)

        ActionChains(self.driver).drag_and_drop_by_offset(redslider,-20,0).perform()