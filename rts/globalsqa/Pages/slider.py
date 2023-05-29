import time
from selenium import webdriver

from selenium.webdriver import ActionChains

class sliders():

    def __init__(self,driver):
        self.driver=driver

        ########  function slider_execution_rgb xpaths ###############

        self.slider_button_xpath="/html/body/div/div[1]/div/div[2]/div/div/div[2]/div[1]/ul/li[3]/a"
        self.red_slider_icon='//*[@id="red"]/span'
        self.green_slider_icon='//*[@id="green"]/span'
        self.blue_slider_icon='//*[@id="blue"]/span'


        ########### double slider execution ######################
        self.rangetab_id="Range"
        self.iframe_of_slider="/html/body/div/div[1]/div[2]/div/div/div[2]/div/div/div[2]/p/iframe"
        self.lefthand_slider_icon='/html[1]/body[1]/div[1]/span[1]'
        self.right_hand_slider_cion='/html[1]/body[1]/div[1]/span[2]'


    def slider_execution_rgb(self):
        self.driver.implicitly_wait(20)


        # self.driver.find_element_by_xpath(self.slider_button_xpath).click()
        self.driver.switch_to.frame(self.driver.find_element_by_xpath("/html/body/div/div[1]/div[2]/div/div/div[2]/div/div/div[1]/p/iframe"))
        time.sleep(2)
        redslider=self.driver.find_element_by_xpath(self.red_slider_icon)
        greenslider=self.driver.find_element_by_xpath(self.green_slider_icon)
        blueslider=self.driver.find_element_by_xpath(self.blue_slider_icon)



        # left moving using pixels
        ActionChains(self.driver).drag_and_drop_by_offset(redslider,-100,0).perform()##moving red slider in start position
        time.sleep(1)
        ActionChains(self.driver).drag_and_drop_by_offset(greenslider,-100,0).perform()#3moving green slider in start position
        time.sleep(1)
        ActionChains(self.driver).drag_and_drop_by_offset(blueslider,-100,0).perform()##this will move slider in start position
        time.sleep(1)

        ##center

        ActionChains(self.driver).drag_and_drop_by_offset(redslider, 40,0).perform()  ##moving red slider in start position
        time.sleep(1)
        ActionChains(self.driver).drag_and_drop_by_offset(greenslider, 45,0).perform()  # 3moving green slider in start position
        time.sleep(1)
        ActionChains(self.driver).drag_and_drop_by_offset(blueslider, 50,0).perform()  ##this will move slider in start position

        ##right

        ActionChains(self.driver).drag_and_drop_by_offset(redslider, 100,0).perform()  ##moving red slider in start position
        time.sleep(1)
        ActionChains(self.driver).drag_and_drop_by_offset(greenslider, 100,0).perform()  # 3moving green slider in start position
        time.sleep(1)
        ActionChains(self.driver).drag_and_drop_by_offset(blueslider, 100,0).perform()  ##this will move slider in start position






        ##practice mmethod for moving the sldier
        #
        # #m0ving the slider using the percentage, first calculate teh width of complete slider
        # fullslidr=self.driver.find_element_by_xpath("/html/body/div[2]")
        # # calculate the percentage offset based on the slider width
        # slider_width = fullslidr.size['width']
        # print(slider_width)
        # percent_offset = 75  # move 25% to the left
        # pixel_offset = int(slider_width * percent_offset / 100)
        # print(pixel_offset)
        # # perform the drag-and-drop action using the pixel offset
        # ActionChains(self.driver).drag_and_drop_by_offset(greenslider, pixel_offset, 0).perform()

        #
        # style_attribute = greenslider.get_attribute("style")
        # print("current style", style_attribute)
        # self.driver.execute_script("arguments[0].style.left = '75%'", greenslider)

        # Get the width of the slider element
        #
        # fullslidergreen = self.driver.find_element_by_xpath("/html/body/div[2]")
        #
        # slider_width = self.driver.execute_script("return arguments[0].offsetWidth", fullslidergreen)
        # print("sldier width",slider_width)
        # # Calculate the horizontal offset for the drag and drop action
        # drag_offset = int(slider_width * 0.45)
        # print("drag ofset is",drag_offset)
        # style_attribute = greenslider.get_attribute("style")
        # print("berfore moving current style", style_attribute)
        # ActionChains(self.driver).drag_and_drop_by_offset(greenslider,-drag_offset,0).perform()
        # style_attribute = greenslider.get_attribute("style")
        # print("after moving current style", style_attribute)

    def double_slider_execution(self):

        self.driver.implicitly_wait(20)
        # self.driver.find_element_by_xpath(self.slider_button_xpath).click()

        self.driver.find_element_by_id(self.rangetab_id).click()
        self.driver.switch_to.frame(self.driver.find_element_by_xpath(self.iframe_of_slider))
        print("frame has been switched")
        time.sleep(2)
        lhs=self.driver.find_element_by_xpath(self.lefthand_slider_icon)
        rhs=self.driver.find_element_by_xpath(self.right_hand_slider_cion)


        ActionChains(self.driver).drag_and_drop_by_offset(lhs,45,0).perform()
        time.sleep(2)
        ActionChains(self.driver).drag_and_drop_by_offset(rhs,45,0).perform()



