import time

from selenium.webdriver import ActionChains


class Dashbaord_LMS():

    def __init__(self, driver):
        self.driver=driver

        self.dashboard_icon_xpath="/html/body/app-root/app-layout/div/app-sidebar/div/div/div/div/ul/li[2]/a"
        self.dashboard_text_xpath="/html/body/app-root/app-layout/div/app-sidebar/div/div/div/div/ul/li[2]/a/span[1]"
        self.lms_icon_dashboard="/html/body/app-root/app-layout/div/app-sidebar/div/div/div/div/ul/li[2]/ul/li/a"
        self.lms_heading="/html/body/app-root/app-layout/div/div/div/app-lms/div/app-page-title/div/div/div/h4"
        self.onlineagent_text="/html/body/app-root/app-layout/div/div/div/app-lms/div/div/div[1]/div/div[1]/div[1]/div/div/div/div[1]/p"
        self.activeagennt_text="/html/body/app-root/app-layout/div/div/div/app-lms/div/div/div[1]/div/div[1]/div[2]/div/div/div/div[1]/p"
        self.Agents_on_break="/html/body/app-root/app-layout/div/div/div/app-lms/div/div/div[1]/div/div[1]/div[3]/div/div/div/div[1]/p"
        self.agent_chatting="/html/body/app-root/app-layout/div/div/div/app-lms/div/div/div[1]/div/div[1]/div[4]/div/div/div/div[1]/p"
        self.agent_not_chatting="/html/body/app-root/app-layout/div/div/div/app-lms/div/div/div[1]/div/div[1]/div[5]/div/div/div/div[1]/p"
        self.total_chats="/html/body/app-root/app-layout/div/div/div/app-lms/div/div/div[1]/div/div[1]/div[6]/div/div/div/div[1]/p"
        self.average_speed="/html/body/app-root/app-layout/div/div/div/app-lms/div/div/div[1]/div/div[1]/div[7]/div/div/div/div[1]/p"
        self.occupancy="/html/body/app-root/app-layout/div/div/div/app-lms/div/div/div[1]/div/div[1]/div[8]/div/div/div/div[1]/p"
        self.visitors_text="/html/body/app-root/app-layout/div/div/div/app-lms/div/div/div[1]/div/div[2]/div/div[1]/h5"
        self.agets_list="/html/body/app-root/app-layout/div/div/div/app-lms/div/div/div[2]/div/div/h4"



    def LMS_method(self):
        self.driver.implicitly_wait(30)
        dshb=self.driver.find_element_by_xpath(self.dashboard_icon_xpath).click() #main dahsboard icon
        dshb_text=self.driver.find_element_by_xpath(self.dashboard_text_xpath).click() #dashboardtest click
        lms=self.driver.find_element_by_xpath(self.lms_icon_dashboard).click() #click on lms icon

        # self.driver.find_element_by_xpath(self.dashboard_icon_xpath).click()
        time.sleep(2)
        actions = ActionChains(self.driver)

        # hover form element to element
        # actions.move_to_element(dshb_text).move_to_element(lms).click().perform()

        self.lmshead_v=self.driver.find_element_by_xpath(self.lms_heading).text
        self.onlineag_v=self.driver.find_element_by_xpath(self.onlineagent_text).text
        self.active_v=self.driver.find_element_by_xpath(self.activeagennt_text).text
        self.agents_on_break_V=self.driver.find_element_by_xpath(self.Agents_on_break).text
        self.agent_chatting_V=self.driver.find_element_by_xpath(self.agent_chatting).text
        self.agent_not_chatting_V=self.driver.find_element_by_xpath(self.agent_not_chatting).text
        self.total_chats_V=self.driver.find_element_by_xpath(self.total_chats).text
        self.average_speed_V=self.driver.find_element_by_xpath(self.average_speed).text
        self.occupancy_v=self.driver.find_element_by_xpath(self.occupancy).text
        self.visitors_text_v=self.driver.find_element_by_xpath(self.visitors_text).text
        self.agent_list_v=self.driver.find_element_by_xpath(self.agets_list).text

        s=self.driver.find_element_by_xpath("/html/body/app-root/app-layout/div/div/div/app-lms/div/div/div[1]/div/div[1]").text
        print(s)
        t=self.driver.find_element_by_xpath("/html/body/app-root/app-layout/div/div/div/app-lms/div/div/div[1]/div/div[2]").text
        print(t)



