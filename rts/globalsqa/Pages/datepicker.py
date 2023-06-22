import time

from selenium.webdriver.common.action_chains import ActionChains

class datePicker():


    def __init__(self,driver):
        self.driver=driver
        self.previous_button="/html/body/div/div/a[1]/span"
        self.next_button="/html/body/div/div/a[2]/span"
        self.date_month="/html/body/div/div/div/span[1]"
        self.year="/html/body/div/div/div/span[2]"
        self.date_field_id="datepicker"
        self.date_iframe="/html/body/div/div[1]/div[2]/div/div/div[2]/div/div/div[1]/p/iframe"




    def date_picker_method(self):

        self.driver.implicitly_wait(10)

        self.driver.switch_to.frame(self.driver.find_element_by_xpath(self.date_iframe))

        self.driver.find_element_by_id(self.date_field_id).click()#click on the date field

        current_month=self.driver.find_element_by_xpath(self.date_month).text #capturing the month
        current_year=self.driver.find_element_by_xpath(self.year).text #capturing the year
        print("current month = " ,current_month)
        print("current year = ", current_year)


        converted_year=int(current_year)#converting the year into integer for subtraction
        expected_year=converted_year-1 #performing subtraction
        expected_year_1=converted_year+1
        print("expcted year",expected_year) #printing the expected year


         ##loop for the previous month and year
        while True:
            captured_month=self.driver.find_element_by_xpath(self.date_month).text #capturing the month
            captured_year=self.driver.find_element_by_xpath(self.year).text #capturing the year

            if captured_month==current_month and captured_year==str(expected_year):
                print("Expected Date Found ",current_month,expected_year, "=" ,captured_month, captured_year)
                time.sleep(2)
                break

            else:
                print(captured_month,captured_year)
                self.driver.find_element_by_xpath(self.previous_button).click()

        #loop of rthe next month and year
        while True:
            captured_month = self.driver.find_element_by_xpath(self.date_month).text  # capturing the month
            captured_year = self.driver.find_element_by_xpath(self.year).text  # capturing the year

            if captured_month==current_month and captured_year==str(expected_year_1):
                print("Expected Date Found ",current_month,expected_year_1, "=" ,captured_month, captured_year)
                time.sleep(2)
                break

            else:
                print(captured_month, captured_year)
                self.driver.find_element_by_xpath(self.next_button).click()
