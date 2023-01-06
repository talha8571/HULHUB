import time

from selenium .webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium .webdriver.support.ui import WebDriverWait

class certverification():
    def __init__(self,driver):
        self.driver=driver

        self.cert_page_xapth="/html/body/sgc-web/general-layout/div/div/ul/li[3]/a"
        self.certcode_searhbox_xpath="/html/body/sgc-web/general-layout/div/static-layout/app-check-auth-code/div/div[2]/div[1]/div/form/div/div[1]/input"
        self.check_certcode_button_xpath="/html/body/sgc-web/general-layout/div/static-layout/app-check-auth-code/div/div[2]/div[1]/div/form/div/div[2]/div/button"
        self.front_image_heading_xpath="/html/body/sgc-web/general-layout/div/static-layout/app-check-auth-code/div/div[2]/div[1]/div[2]/div[1]/div[2]/div[1]/h4"
        self.front_image_xpath="/html/body/sgc-web/general-layout/div/static-layout/app-check-auth-code/div/div[2]/div[1]/div[2]/div[1]/div[2]/div[1]/img"
        self.back_image_xpath="/html/body/sgc-web/general-layout/div/static-layout/app-check-auth-code/div/div[2]/div[1]/div[2]/div[1]/div[2]/div[2]/img"
        self.close_button_of_front_image="/html/body/sgc-web/sgc-modal/div/div/app-view-thumbnail-front-image/img"
        self.close_buttn_of_back_image="/html/body/sgc-web/sgc-modal/div/div/app-view-thumbnail-image/img"

    def cert_verification(self,certcode):
        self.driver.find_element_by_xpath(self.cert_page_xapth).click()
        time.sleep(1)
        self.driver.find_element_by_xpath(self.certcode_searhbox_xpath).send_keys(certcode)
        time.sleep(1)
        self.driver.find_element_by_xpath(self.check_certcode_button_xpath).click()
        time.sleep(2)
        # explicits wait
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, self.front_image_xpath)))
        time.sleep(2)

        self.driver.find_element_by_xpath(self.front_image_xpath).click()
        time.sleep(2)
        self.driver.find_element_by_xpath(self.close_button_of_front_image).click()
        self.driver.find_element_by_xpath(self.back_image_xpath).click()
        time.sleep(1)
        self.driver.find_element_by_xpath(self.close_buttn_of_back_image).click()