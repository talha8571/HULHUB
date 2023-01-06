class login():

    def __init__(self,driver):
        self.driver=driver
        self.username_xpath="/html/body/div[1]/div/div[2]/div/div/form/div[2]/input"
        self.passwordxpath="/html/body/div[1]/div/div[2]/div/div/form/div[3]/input"
        self.loginbuttonnxpath="/html/body/div[1]/div/div[2]/div/div/form/div[4]/button"



    def login_action(self,username,password):
        self.driver.find_element_by_xpath(self.username_xpath).send_keys(username)
        self.driver.find_element_by_xpath(self.passwordxpath).send_keys(password)
        self.driver.find_element_by_xpath(self.loginbuttonnxpath).click()


