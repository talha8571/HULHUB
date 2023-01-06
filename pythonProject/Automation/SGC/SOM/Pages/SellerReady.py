class sellerReady:
    def __init__(self,driver):
        self.driver=driver
        self.sgc_logo_xpath="/html/body/sgc-web/general-layout/div/div/div[1]/a/img"
        self.seller_ready_fromdashboard='//*[@id="menu"]/li[3]/a'
        self.view_seller_readyimages_xpath="/html/body/sgc-web/general-layout/div/app-seller-ready/div[2]/div/div/p/a/strong"





    def sellerReadypage(self):
        self.driver.implicitly_wait(20)
        # self.driver.find_element_by_xpath(self.sgc_logo_xpath).click()
        self.driver.find_element_by_xpath(self.seller_ready_fromdashboard).click()
        self.driver.find_element_by_xpath(self.view_seller_readyimages_xpath).click()
