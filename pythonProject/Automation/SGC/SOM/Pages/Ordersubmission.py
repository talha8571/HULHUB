import random
import time

class ordersubmission():
    def __init__(self,driver):
        self.driver=driver

        self.start_new_submission_xpath="/html/body/sgc-web/general-layout/div/div/ul/li[5]/a"
        self.terms_and_conditions_xpath="/html/body/sgc-web/sgc-modal/div/div/terms-alert/div/label/span"
        self.start_new_order_xpath="/html/body/sgc-web/general-layout/div/checkout/div/checkout-order/div/div/select-expertise-tier/div/div/div"
        self.search_bar_of_card_xpath="/html/body/sgc-web/general-layout/div/checkout/div/checkout-order/div/div/add-items/div/div/div[1]/div/input"
        self.click_to_add_card_xpath="/html/body/sgc-web/general-layout/div/checkout/div/checkout-order/div/div/add-items/div/div/div[1]/p/a"
        self.standarad_dayplan_xpath="/html/body/sgc-web/general-layout/div/checkout/div/checkout-order/div/div/select-plan/div/div/div[1]/div"
        self.next_button_xpath="/html/body/sgc-web/general-layout/div/checkout/div/checkout-order/checkout-bottom-nav/div[2]/button"
        self.fedexground_xpath="/html/body/sgc-web/general-layout/div/checkout/div/checkout-order/div/div/select-shipping/div/div/div[3]/div[2]"
        self.clickheretofinish_xpath="/html/body/sgc-web/general-layout/div/checkout/div/checkout-order/div/checkout-side-bar/div/div[9]/button"
        self.checkbox_termsconditions="/html/body/sgc-web/sgc-modal/div/div/app-payment-terms/div/label"
        self.promo_code_text_field="/html/body/sgc-web/general-layout/div/checkout/div/checkout-order/div/checkout-side-bar/div/div[3]/input"
        self.apply="/html/body/sgc-web/general-layout/div/checkout/div/checkout-order/div/checkout-side-bar/div/div[3]/button"
        self.submit_and_paylater="/html/body/sgc-web/general-layout/div/checkout/div/checkout-order/div/checkout-side-bar/div/div[10]/button"

    def sdLessthan1500(self,cardname):
        time.sleep(2)
        self.driver.find_element_by_xpath(self.start_new_submission_xpath).click()  # start new submission
        self.driver.find_element_by_xpath(self.terms_and_conditions_xpath).click()  # terms and conditions
        self.driver.find_element_by_xpath(self.start_new_order_xpath).click() #strat new order
        self.driver.find_element_by_xpath(self.search_bar_of_card_xpath).send_keys(cardname)#cardname
        self.driver.find_element_by_xpath(self.click_to_add_card_xpath).click()  # click here to add you card

        declare_value = random.randrange(1, 1499)
        # declare value of card
        self.driver.find_element_by_xpath("/html/body/sgc-web/general-layout/div/checkout/div/checkout-order/div/div/add-items/div/div/div[3]/added-order-item/added-card-item/div/div[3]/input").send_keys(declare_value)
        time.sleep(2)
        self.driver.find_element_by_xpath("/html/body/sgc-web/general-layout/div/checkout/div/checkout-order/checkout-bottom-nav/div/div").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("/html/body/sgc-web/general-layout/div/checkout/div/checkout-order/checkout-bottom-nav/div[2]/button").click()  # next button of step 2
        time.sleep(1)

    def afteplan(self,promocode):
        self.driver.find_element_by_xpath(self.standarad_dayplan_xpath).click()#immediate x path
        time.sleep(2)
        self.driver.find_element_by_xpath(self.next_button_xpath).click()#next button

        self.driver.find_element_by_xpath(self.fedexground_xpath).click()
        time.sleep(2)
        self.driver.find_element_by_xpath(self.next_button_xpath).click()  # next button

        self.driver.find_element_by_xpath(self.clickheretofinish_xpath).click()#click here to finish
        time.sleep(2)
        self.driver.find_element_by_xpath(self.checkbox_termsconditions).click()#terms and conditions
        time.sleep(2)
        self.driver.find_element_by_xpath(self.promo_code_text_field).send_keys(promocode)
        time.sleep(2)
        self.driver.find_element_by_xpath(self.apply).click()
        time.sleep(2)
        self.driver.find_element_by_xpath(self.submit_and_paylater).click()
        time.sleep(2)





