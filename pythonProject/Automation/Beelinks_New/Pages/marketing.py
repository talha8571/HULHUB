import random
import time

from selenium.webdriver.common.keys import Keys


class marketing_tab():
    def __init__(self,driver):
        self.driver=driver

        ###############################  Create contact list ###########################################################

        self.huluhb_icon = "/html/body/app-root/app-layout/div/app-topbar/header/div/div[1]/div/a[2]/span[1]/img"  # hulub icon click to land on dasboard
        self.marketting_tab="/html/body/app-root/app-layout/div/app-sidebar/div/div/div/div/ul/li[7]/a"
        self.add_contact_list_button="/html/body/app-root/app-layout/div/div/div/app-marketing/div/div/div/div/div/div/div/app-contact-list/div/div/div/div/div/div[1]/div[2]/div/button"
        self.contact_list_name="/html/body/app-root/app-layout/div/div/div/app-marketing/div/div/div/div/div/div/div/app-add-contact/div/div/div[1]/form/div[1]/div[1]/div/input"
        self.type="/html/body/app-root/app-layout/div/div/div/app-marketing/div/div/div/div/div/div/div/app-add-contact/div/div/div/form/div[1]/div[2]/div/ng-select/div/div/div[2]/input"
        self.business_number="/html/body/app-root/app-layout/div/div/div/app-marketing/div/div/div/div/div/div/div/app-add-contact/div/div/div/form/div[1]/div[3]/div/ng-select/div/div/div[2]/input"
        self.country="/html/body/app-root/app-layout/div/div/div/app-marketing/div/div/div/div/div/div/div/app-add-contact/div/div/div[1]/form/div[1]/div[4]/div/ng-select/div/div/div[2]/input"
        self.region="/html/body/app-root/app-layout/div/div/div/app-marketing/div/div/div/div/div/div/div/app-add-contact/div/div/div[1]/form/div[1]/div[5]/div/ng-select/div/div/div[2]/input"
        self.search_contacts_button="/html/body/app-root/app-layout/div/div/div/app-marketing/div/div/div/div/div/div/div/app-add-contact/div/div/div[1]/form/div[1]/div[6]/div/button"
        self.save_button="/html/body/app-root/app-layout/div/div/div/app-marketing/div/div/div/div/div/div/div/app-add-contact/div/div/div[1]/form/div[2]/button[1]"
        self.name_list_checkbox="/html/body/app-root/app-layout/div/div/div/app-marketing/div/div/div/div/div/div/div/app-add-contact/div/div/div[2]/div/div[3]/div/table/thead/tr/th[1]/input"
        self.searchbar_of_contactlist="/html/body/app-root/app-layout/div/div/div/app-marketing/div/div/div/div/div/div/div/app-contact-list/div/div/div/div/div/div[1]/div[1]/div/div/input"
        self.searched_result_contactlist="/html/body/app-root/app-layout/div/div/div/app-marketing/div/div/div/div/div/div/div/app-contact-list/div/div/div/div/div/div[2]/div/table/tbody/tr/td[1]"

        ################################## CREATE CAMPAIGN #################################################################

        self.campaign_tab_xpath="/html/body/app-root/app-layout/div/div/div/app-marketing/div/div/div/div/div/ul/li[2]/a"
        self.add_new_campaign_button="/html/body/app-root/app-layout/div/div/div/app-marketing/div/div/div/div/div/div/div/app-campaigns/div/div/div/div/div/div[1]/div[2]/div/button"
        self.name_of_campaign="/html/body/app-root/app-layout/div/div/div/app-marketing/div/div/div/div/div/div/div/app-add-campaign/div/div/div[1]/form/div/div[1]/div/input"
        self.type_of_campaign="/html/body/app-root/app-layout/div/div/div/app-marketing/div/div/div/div/div/div/div/app-add-campaign/div/div/div[1]/form/div/div[2]/div/ng-select/div/div/div[2]/input"
        self.searched_Result_of_type="/html/body/app-root/app-layout/div/div/div/app-marketing/div/div/div/div/div/div/div/app-add-campaign/div/div/div[1]/form/div/div[2]/div/ng-select/ng-dropdown-panel/div/div[2]/div"
        self.number_of_campaign="/html/body/app-root/app-layout/div/div/div/app-marketing/div/div/div/div/div/div/div/app-add-campaign/div/div/div[1]/form/app-add-campaign-whatsapp/div[1]/div/div/ng-select/div/div/div[2]/input"
        self.searched_result_of_number="/html/body/app-root/app-layout/div/div/div/app-marketing/div/div/div/div/div/div/div/app-add-campaign/div/div/div[1]/form/app-add-campaign-whatsapp/div[1]/div/div/ng-select/ng-dropdown-panel/div/div[2]/div"
        self.template_type_text="/html/body/app-root/app-layout/div/div/div/app-marketing/div/div/div/div/div/div/div/app-add-campaign/div/div/div[1]/form/app-add-campaign-whatsapp/div[2]/div/div[1]/input"
        self.template_type_image="/html/body/app-root/app-layout/div/div/div/app-marketing/div/div/div/div/div/div/div/app-add-campaign/div/div/div[1]/form/app-add-campaign-whatsapp/div[2]/div/div[2]/input"
        self.template_type_video="/html/body/app-root/app-layout/div/div/div/app-marketing/div/div/div/div/div/div/div/app-add-campaign/div/div/div[1]/form/app-add-campaign-whatsapp/div[2]/div/div[3]/input"
        self.text_in_template="/html/body/app-root/app-layout/div/div/div/app-marketing/div/div/div/div/div/div/div/app-add-campaign/div/div/div[1]/form/app-add-campaign-whatsapp/div[3]/div/div/div/div[1]/div/div[1]/div/div/input"
        self.submit_buton="/html/body/app-root/app-layout/div/div/div/app-marketing/div/div/div/div/div/div/div/app-add-campaign/div/div/div[1]/form/app-add-campaign-whatsapp/div[4]/div/button[1]"
        self.search_bar_of_campaign="/html/body/app-root/app-layout/div/div/div/app-marketing/div/div/div/div/div/div/div/app-campaigns/div/div/div/div/div/div[1]/div[1]/div/div/input"
        self.first_template_of_text="/html/body/app-root/app-layout/div/div/div/app-marketing/div/div/div/div/div/div/div/app-add-campaign/div/div/div[1]/form/app-add-campaign-whatsapp/div[3]/div/div/div/div[1]/div/div[1]"

        #################################### Campaign Execution ####################################################
        self.campaign_execution_tab="/html/body/app-root/app-layout/div/div/div/app-marketing/div/div/div/div/div/ul/li[3]/a"
        self.add_campaign_execution_button="/html/body/app-root/app-layout/div/div/div/app-marketing/div/div/div/div/div/div/div/app-execution/div/div/div/div/div/div[1]/div[2]/div/button[1]"
        self.campaign_dropdown="/html/body/app-root/app-layout/div/div/div/app-marketing/div/div/div/div/div/div/div/app-campaign-execution/div/div/div[1]/div[2]/div[1]/div/ng-select/div/div/div[2]/input"
        self.campaign_caontact_list="/html/body/app-root/app-layout/div/div/div/app-marketing/div/div/div/div/div/div/div/app-campaign-execution/div/div/div[1]/div[2]/div[2]/div/ng-select/div/div/div[3]/input"



    def create_contact_list(self):
        fe = self.driver.find_element_by_xpath
        fe(self.huluhb_icon).click()
        fe(self.marketting_tab).click()
        time.sleep(3)

        ###### navigation on tabs of marketting and verification of url
        url_marketting=self.driver.current_url
        print("url of marketing page is", url_marketting)

        if url_marketting=="https://new.beelinks.solutions/marketing":
            print("url of marketing page is",url_marketting)

        else:
            print("ERRORR!!! URL IS INCORRECT")

        time.sleep(2)

        fe("/html/body/app-root/app-layout/div/div/div/app-marketing/div/div/div/div/div/ul/li[1]/a").click()#contact list
        time.sleep(2)
        fe("/html/body/app-root/app-layout/div/div/div/app-marketing/div/div/div/div/div/ul/li[2]/a").click()#campaign tab
        time.sleep(2)
        fe("/html/body/app-root/app-layout/div/div/div/app-marketing/div/div/div/div/div/ul/li[3]/a").click() #execution tab
        time.sleep(2)
        fe("/html/body/app-root/app-layout/div/div/div/app-marketing/div/div/div/div/div/ul/li[1]/a").click()  #contact list



        fe(self.add_contact_list_button).click()
        self.ran=random.randint(1,884841655)#3generate random number
        contactlistname="automation_contact"+str(self.ran)
        fe(self.contact_list_name).send_keys(contactlistname)
        time.sleep(1)
        fe(self.type).send_keys("whatsapp",Keys.ENTER)
        time.sleep(1)

        fe(self.business_number).click()
        fe(self.business_number).send_keys("facebook test account")
        time.sleep(2)
        fe(self.business_number).click()
        time.sleep(2)
        business_number_field = fe("/html/body/app-root/app-layout/div/div/div/app-marketing/div/div/div/div/div/div/div/app-add-contact/div/div/div/form/div[1]/div[3]/div/ng-select/ng-dropdown-panel/div/div[2]/div/span").text
        print(business_number_field)##this will print the value of business numebr

        if business_number_field=="Facebook Test Account":
            fe("/html/body/app-root/app-layout/div/div/div/app-marketing/div/div/div/div/div/div/div/app-add-contact/div/div/div/form/div[1]/div[3]/div/ng-select/ng-dropdown-panel/div/div[2]/div/span").click() #click on the business number
            print("business number found and selected")
        else:
            time.sleep(5)
            fe("/html/body/app-root/app-layout/div/div/div/app-marketing/div/div/div/div/div/div/div/app-add-contact/div/div/div/form/div[1]/div[3]/div/ng-select/ng-dropdown-panel/div/div[2]/div/span").click() #click on business number

        time.sleep(1)
        fe(self.country).send_keys("Pakistan",Keys.ENTER)
        fe(self.region).send_keys("Pakistan",Keys.ENTER)
        fe(self.search_contacts_button).click()
        fe(self.name_list_checkbox).click()
        fe(self.save_button).click()
        print("contact list created")
        time.sleep(4)
        fe(self.searchbar_of_contactlist).send_keys(contactlistname) #searching the contact list from search bear
        time.sleep(2)
        cl=fe(self.searched_result_contactlist).text
        if cl==contactlistname:
            print("contact list appeared in the searched result")
            fe(self.searchbar_of_contactlist).clear()#clearing the search bar
            print("Searched result cleared from search bar")
        else:
            print("both are different")

    def campaign_creation(self):
        self.driver.implicitly_wait(20)
        fe=self.driver.find_element_by_xpath
        fe(self.campaign_tab_xpath).click()
        fe(self.add_new_campaign_button).click()
        campaign_name="campaign"+str(self.ran)

        fe(self.name_of_campaign).send_keys(campaign_name)
        fe(self.type_of_campaign).click()
        fe(self.searched_Result_of_type).click()
        time.sleep(2)
        fe(self.number_of_campaign).click()
        time.sleep(2)
        fe(self.searched_result_of_number).click()
        fe(self.template_type_image).click()
        time.sleep(2)
        fe(self.template_type_video).click()
        time.sleep(2)
        fe(self.template_type_text).click()
        time.sleep(2)
        fe(self.first_template_of_text).click()
        fe(self.text_in_template).send_keys("from automation script")
        time.sleep(1)

        self.driver.execute_script("window.scrollTo(0,1600)")

        fe(self.submit_buton).click()#submit button of campaign creation

        fe(self.search_bar_of_campaign).send_keys(campaign_name) #searching created campaign
        time.sleep(4)
        campaign_searched_result=fe("/html/body/app-root/app-layout/div/div/div/app-marketing/div/div/div/div/div/div/div/app-campaigns/div/div/div/div/div/div[2]/div/table/tbody/tr[1]/td[1]").text##text of first searched result

        if campaign_searched_result==campaign_name:
            print("Campaign has been created and appeared in the list as well")
            fe(self.search_bar_of_campaign).clear()

        else:
            print("campaign is not appeared in the list")

    def campaign_execution(self):
        fe=self.driver.find_element_by_xpath
        fe(self.campaign_execution_tab).click()
        fe(self.add_campaign_execution_button).click() #cllick on campaign execution button from execution tab
        fe(self.campaign_dropdown).click()
        time.sleep(2)
        fe("/html/body/app-root/app-layout/div/div/div/app-marketing/div/div/div/div/div/div/div/app-campaign-execution/div/div/div[1]/div[2]/div[1]/div/ng-select/ng-dropdown-panel/div/div[2]/div[2]/span").click() #click on the testing campaign from dropdown
        fe(self.campaign_caontact_list).click()
        fe(self.campaign_caontact_list).send_keys("asad testing")
        time.sleep(2)
        fe("/html/body/app-root/app-layout/div/div/div/app-marketing/div/div/div/div/div/div/div/app-campaign-execution/div/div/div[1]/div[2]/div[2]/div/ng-select/ng-dropdown-panel/div/div[2]/div/span").click()#click on the searched result
        time.sleep(2)








