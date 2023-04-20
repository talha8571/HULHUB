from selenium.webdriver.common.action_chains import ActionChains

class Tooltip:
    def __init__(self,driver):
        self.driver=driver
        self.tooltip_button="/html/body/div[1]/div[1]/div/div[2]/div/div/div[2]/div[1]/ul/li[4]/a"
        self.image_xpath="/html/body/div[1]/a/img"
        self.iframe_tooltip="/html/body/div/div[1]/div[2]/div/div/div[2]/div/div/div[1]/p[1]/iframe"


    def tooltip_method(self):
        self.driver.implicitly_wait(20)
        # self.driver.find_element_by_xpath(self.tooltip_button).click()
        self.driver.switch_to.frame(self.driver.find_element_by_xpath(self.iframe_tooltip))

        image=self.driver.find_element_by_xpath(self.image_xpath)

        ActionChains(self.driver).move_to_element(image).perform()

        tooltip=image.get_attribute("alt")


        if tooltip=="St. Stephen's Cathedral":
            print("Tool tip is verified, Current tooltip is", tooltip)