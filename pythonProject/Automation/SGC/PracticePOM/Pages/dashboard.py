class dsh():
    def __init__(self,driver):
        self.driver=driver
        self.xpath="sjfhasflasfas"



    def ping(self,a):
        self.driver.find_element_by_xpath(self.xpath).send_keys(a)
