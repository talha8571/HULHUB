class scroll():
    def __init__(self, driver):
        self.driver=driver
        self.agent_tab_xpath="/html/body/app-root/app-layout/div/app-sidebar/div/div/div/div/ul/li[8]/a"
        self.lisst="/html/body/app-root/app-layout/div/div/div/app-agents/div/div/div[1]/div/div[3]/app-agent-list-sidebar/div[2]"


    def sc(self):
        self.driver.find_element_by_xpath(self.agent_tab_xpath).click()
        ss=self.driver.find_element_by_xpath(self.lisst)
        self.driver.execute_script("arguments[0].scrollIntoView();", ss)