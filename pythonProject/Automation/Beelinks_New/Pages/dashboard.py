from selenium.webdriver import ActionChains
class dshb():
    def __init__(self, driver):
        self.driver = driver

        self.dashboardicon_xapth="/html/body/app-root/app-layout/div/app-sidebar/div/div/div/div/ul/li[2]/a"
        self.dashboard_xpath="/html/body/app-root/app-layout/div/app-sidebar/div/div/div/div/ul/li[2]/a"
        self.lms_xpath="/html/body/app-root/app-layout/div/app-sidebar/div/div/div/div/ul/li[2]/ul/li/a"

    def hovering(self):
        self.driver.implicitly_wait(30)
        # d=self.driver.find_element_by_xpath(self.dashboardicon_xapth)
        di=self.driver.find_element_by_xpath(self.dashboard_xpath)
        l=self.driver.find_element_by_xpath(self.lms_xpath)
        actions = ActionChains(self.driver)
        self.driver.find_element_by_xpath(self.dashboardicon_xapth).click()
        actions.move_to_element(di).move_to_element(l).click().perform()

        raw=self.driver.find_element_by_xpath("/html/body/app-root/app-layout/div/div/div/app-lms/div/div/div[2]/div/div/app-transaction/div/table/tbody/tr[1]")

        self.driver.execute_script("arguments[0].scrollIntoView();", raw)
        self.driver.save_screenshot('screenshot.png')
