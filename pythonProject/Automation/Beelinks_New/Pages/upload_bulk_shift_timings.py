class shift_timings():
    def __init__(self, driver):
        self.driver=driver
        self.huluhb_icon = "/html/body/app-root/app-layout/div/app-topbar/header/div/div[1]/div/a[2]/span[1]/img"  # hulub icon click to land on dasboard
        self.agentstab = "/html/body/app-root/app-layout/div/app-sidebar/div/div/div/div/ul/li[8]/a"  # agents tab from left panel
        self.arrow_icon_upload_files="/html/body/app-root/app-layout/div/div/div/app-agents/div/div/div[1]/div/div[1]/div[1]/div/div[1]/button" # arrow icon
        self.upload_bulk_shift_timings_text="/html/body/app-root/app-layout/div/div/div/app-agents/div/div/div[1]/div/div[1]/div[1]/div/div[2]/a[1]" #
        self.download_sample_file_button="/html/body/div[2]/div[2]/div/mat-dialog-container/app-update-shift-timing-dialog/div[2]/a/span"
        self.choose_file_field="/html/body/div[2]/div[2]/div/mat-dialog-container/app-update-shift-timing-dialog/div[2]/form/div/input"
        self.submit_button="/html/body/div[2]/div[2]/div/mat-dialog-container/app-update-shift-timing-dialog/div[3]/mat-dialog-actions/button[1]"



    def upload_shift_timings_method(self):
        fe=self.driver.find_element_by_xpath
        fe(self.huluhb_icon).click()
        fe(self.agentstab).click()
        fe(self.arrow_icon_upload_files).click()
        fe(self.upload_bulk_shift_timings_text).click()
        fe(self.download_sample_file_button).click() #download buton of sample file

        url = self.driver.current_url
        if url== "https://elasticbeanstalk-us-west-1-021594099427.s3-us-west-1.amazonaws.com/demo.xlsx":
            print("Page redirected on the correct page due to automation restriction its not downloading")
            self.driver.back()
            fe(self.arrow_icon_upload_files).click()
            fe(self.upload_bulk_shift_timings_text).click()

        fe(self.choose_file_field).send_keys("C:/Users/1154-Talha/PycharmProjects/pythonProject/Automation/Beelinks_New/Files/uploadshifttimings.xlsx")
        print("file has been uploaded")
        fe(self.submit_button).click()
        print("clicked on submit button")


