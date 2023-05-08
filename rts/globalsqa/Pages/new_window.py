class new_window:

    def __init__(self,driver):
        self.driver=driver
        self.open_new_window_button="/html/body/div[1]/div[1]/div[2]/div/div/div[2]/div/div/div[1]/a" ##this button will open new window


    def new_window_method(self):
        self.driver.find_element_by_xpath(self.open_new_window_button).click()##click on the click here button
        print(self.driver.current_url)


        #this code will switch to the new window
        print(self.driver.current_window_handle)  # parent window
        handles = self.driver.window_handles  # return all the handle value of windows
        print(handles)
        for handle in handles:
            print("handle is",handle)
            self.driver.switch_to.window(handle)
            print(self.driver.current_url)

        s = self.driver.current_window_handle
        print(s)
        self.driver.close()


