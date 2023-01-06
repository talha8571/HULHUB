import time

from selenium .webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium .webdriver.support.ui import WebDriverWait

class popreport():
    def __init__(self,driver):
        self.driver=driver

        self.popreport_tab_xpath="/html/body/sgc-web/general-layout/div/div/ul/li[2]/a"
        self.search_bar_of_popreport="/html/body/sgc-web/general-layout/div/static-layout/pop-reports/div[3]/input"
        self.search_button_of_search_bar="/html/body/sgc-web/general-layout/div/static-layout/pop-reports/div[3]/button"
        self.first_resultofsearch_xpath="/html/body/sgc-web/general-layout/div/static-layout/pop-reports/div[4]/div/ejs-grid/div[3]/div/table/tbody/tr[1]/td[1]/a"
        self.sgc_logo="/html/body/sgc-web/general-layout/div/div[2]/div[1]/a"
        self.setnamefromtable="/html/body/sgc-web/general-layout/div/static-layout/pop-reports/div[4]/div/ejs-grid/div[2]/div/table/thead/tr/th[1]/div[1]/span[2]"


    def search_pop(self,setname,setname2,setname3):
        self.driver.find_element_by_xpath(self.popreport_tab_xpath).click()#tab of popreport
        time.sleep(1)
        self.driver.find_element_by_xpath(self.search_bar_of_popreport).send_keys(setname)
        time.sleep(1)
        self.driver.find_element_by_xpath(self.search_button_of_search_bar).click()
        time.sleep(2)

    #explicits wait
        wait=WebDriverWait(self.driver,10)
        element=wait.until(EC.element_to_be_clickable((By.XPATH,self.setnamefromtable)))
        time.sleep(2)

        self.driver.find_element_by_xpath(self.sgc_logo).click()
        self.driver.find_element_by_xpath(self.popreport_tab_xpath).click()


        #t205
        self.driver.find_element_by_xpath(self.search_bar_of_popreport).send_keys(setname2)
        time.sleep(1)
        self.driver.find_element_by_xpath(self.search_button_of_search_bar).click()

        # explicits wait
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, self.setnamefromtable)))
        time.sleep(2)

        self.driver.find_element_by_xpath(self.sgc_logo).click()
        self.driver.find_element_by_xpath(self.popreport_tab_xpath).click()


        #t206
        self.driver.find_element_by_xpath(self.search_bar_of_popreport).send_keys(setname3)
        time.sleep(1)
        self.driver.find_element_by_xpath(self.search_button_of_search_bar).click()

        # explicits wait
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, self.setnamefromtable)))
        time.sleep(2)







