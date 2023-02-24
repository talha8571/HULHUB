import time


class bulk_supervisor():
    def __init__(self, driver):
        self.driver=driver
        self.huluhb_icon = "/html/body/app-root/app-layout/div/app-topbar/header/div/div[1]/div/a[2]/span[1]/img"  # hulub icon click to land on dasboard
        self.agentstab = "/html/body/app-root/app-layout/div/app-sidebar/div/div/div/div/ul/li[8]/a"  # agents tab from left panel
        self.arrow_icon_upload_files = "/html/body/app-root/app-layout/div/div/div/app-agents/div/div/div[1]/div/div[1]/div[1]/div/div[1]/button"  # arrow icon
        self.upload_bulk_supervisor="/html/body/app-root/app-layout/div/div/div/app-agents/div/div/div[1]/div/div[1]/div[1]/div/div[2]/a"
        self.click_download_sample_data_button="/html/body/div[2]/div[2]/div/mat-dialog-container/app-upload-supervisors-dialog/div[2]/a/span"
        self.choose_file_field="/html/body/div[2]/div[2]/div/mat-dialog-container/app-upload-supervisors-dialog/div[2]/form/div/input"
        self.submit_button="/html/body/div[2]/div[2]/div/mat-dialog-container/app-upload-supervisors-dialog/div[3]/mat-dialog-actions/button[1]"



    def bulk_supervisor(self):
        fe = self.driver.find_element_by_xpath
        fe(self.huluhb_icon).click()
        fe(self.agentstab).click()
        fe(self.arrow_icon_upload_files).click()
        fe(self.upload_bulk_supervisor).click()
        fe(self.click_download_sample_data_button).click() #download button of sample file
        time.sleep(1)
        url=self.driver.current_url

        if url== "https://elasticbeanstalk-us-west-1-021594099427.s3-us-west-1.amazonaws.com/manager_sample_file.xlsx":
            print("Page redirected on the correct page due to automation restriction its not downloading")
            self.driver.back()
            time.sleep(2)
            fe(self.arrow_icon_upload_files).click()
            fe(self.upload_bulk_supervisor).click()

        else:
            print("url is different")

        fe(self.choose_file_field).send_keys("C:/Users/1154-Talha/PycharmProjects/pythonProject/Automation/Beelinks_New/Files/managersample.xlsx")#upload file
        print("file has been uploaded")
        fe(self.submit_button).click()
        print("Agent's supervisor has been updated")