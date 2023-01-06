class PaypallPayments():
    def __init__(self,driver):
        self.driver=driver
        self.sgclogoforhomepagexpath="/html/body/sgc-web/general-layout/div/div[2]/div[1]/a"
        self.paypallpayemtnxpath="/html/body/sgc-web/general-layout/div/static-layout/div[1]/div/nav/div/ul/li[4]/a"
        self.paypallheadingofpage="/html/body/sgc-web/general-layout/div/app-pay-pal-payment/div[2]/h2"

    def paypall_method(self):
        self.driver.find_element_by_xpath(self.sgclogoforhomepagexpath).click()
        self.driver.find_element_by_xpath(self.paypallpayemtnxpath).click()

        pay=self.driver.find_element_by_xpath(self.paypallheadingofpage)
        pp=pay.is_displayed()

        if pp==True:
            print("Paypall heading is displayed")

        else:
            print("Paypall heading is not displayed")