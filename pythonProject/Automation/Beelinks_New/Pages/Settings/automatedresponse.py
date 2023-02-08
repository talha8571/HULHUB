import random
import time
from selenium.webdriver.common.keys import Keys


class automaticresponse():
    def __init__(self,driver):
        self.driver=driver
        self.huluhb_icon = "/html/body/app-root/app-layout/div/app-topbar/header/div/div[1]/div/a[2]/span[1]/img"  # hulub icon click to land on dasboard
        self.settings_icon="/html/body/app-root/app-layout/div/app-topbar/header/div/div[2]/div[5]/button"
        self.general_tab="/html/body/app-root/app-layout/div/div/div/app-settings/div/div/div/div[1]/div/ul/li[1]/a/div"
        self.automated_response_card="/html/body/app-root/app-layout/div/div/div/app-settings/div/div/div/div[2]/div/div/div/div/div[2]/div[1]/div[2]/div[1]/div/div"
        self.response_text_area="/html/body/app-root/app-layout/div/div/div/app-automated-response/div/div/div[2]/div/div/form/div[1]/div[1]/div/textarea"
        self.shortcut="/html/body/app-root/app-layout/div/div/div/app-automated-response/div/div/div[2]/div/div/form/div[1]/div[2]/div/input"
        self.sharing_all_checkbox="/html/body/app-root/app-layout/div/div/div/app-automated-response/div/div/div[2]/div/div/form/div[1]/div[3]/div[1]/input"
        self.add_responses_button="/html/body/app-root/app-layout/div/div/div/app-automated-response/div/div/div[2]/div/div/form/div[2]/button[1]"
        self.heading_of_first_message="/html/body/app-root/app-layout/div/div/div/app-automated-response/div/div/div[1]/div/div/div/div/div[1]/div/div/div[1]/h5"




    def response_method(self):
        fe=self.driver.find_element_by_xpath

        fe(self.huluhb_icon).click()
        fe(self.settings_icon).click()
        fe(self.general_tab).click()
        fe(self.automated_response_card).click()
        rd=random.randint(1,853210323)
        response="this is from automation script"+str(rd)
        fe(self.response_text_area).send_keys(response)

        shortcut="#Auto"+str(rd)
        fe(self.shortcut).send_keys(shortcut)

        fe(self.sharing_all_checkbox).click()
        fe(self.add_responses_button).click()#click on add response
        time.sleep(5)

        print("tag created with name ",shortcut )

        fe(self.heading_of_first_message).click()

        # self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # fe("/html/body/app-root/app-layout/div/div/div/app-automated-response/div/div/div[1]/div/div/div/div").send_keys(Keys.PAGE_DOWN)
        body = self.driver.find_element_by_css_selector('body')
        body.send_keys(Keys.END)
        time.sleep(2)



