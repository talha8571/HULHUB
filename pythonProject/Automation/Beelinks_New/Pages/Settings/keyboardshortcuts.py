import time


class Keyboard_shortcuts():

    def __init__(self,driver):
        self.driver=driver

        self.huluhb_icon = "/html/body/app-root/app-layout/div/app-topbar/header/div/div[1]/div/a[2]/span[1]/img"  # hulub icon click to land on dasboard
        self.settings_icon = "/html/body/app-root/app-layout/div/app-topbar/header/div/div[2]/div[5]/button"
        self.general_tab = "/html/body/app-root/app-layout/div/div/div/app-settings/div/div/div/div[1]/div/ul/li[1]/a/div"
        self.keyboard_shortcuts_card="/html/body/app-root/app-layout/div/div/div/app-settings/div/div/div/div[2]/div/div/div/div/div[2]/div[1]/div[2]/div[4]/div/div"


    def shortcuts_Page(self):
        fe = self.driver.find_element_by_xpath

        fe(self.huluhb_icon).click()
        fe(self.settings_icon).click()
        fe(self.general_tab).click()
        fe(self.keyboard_shortcuts_card).click()
        time.sleep(3)


        ##data of raw 1
        raw1 = fe("/html/body/app-root/app-layout/div/div/div/app-keyboard-shortcuts/div/div/div/div/div/div[2]/table/tbody/tr[1]").text
        raw1 = raw1.replace('\n', ' ')
        # raw1 = '  '.join(raw1.split())
        print(raw1)

        ##data of raw 2
        raw2 = fe("/html/body/app-root/app-layout/div/div/div/app-keyboard-shortcuts/div/div/div/div/div/div[2]/table/tbody/tr[2]").text
        raw2 = raw2.replace('\n', ' ')
        # raw2 = '  '.join(raw2.split())
        print(raw2)

        ##data of raw 3
        raw3 = fe("/html/body/app-root/app-layout/div/div/div/app-keyboard-shortcuts/div/div/div/div/div/div[2]/table/tbody/tr[3]").text
        raw3 = raw3.replace('\n', ' ')
        # raw3 = '  '.join(raw3.split())
        print(raw3)


        ##data of raw 4
        raw4 = fe("/html/body/app-root/app-layout/div/div/div/app-keyboard-shortcuts/div/div/div/div/div/div[2]/table/tbody/tr[4]").text
        raw4 = raw4.replace('\n', ' ')
        # raw4 = '  '.join(raw4.split())
        print(raw4)

        ##data of raw 5
        raw5 = fe("/html/body/app-root/app-layout/div/div/div/app-keyboard-shortcuts/div/div/div/div/div/div[2]/table/tbody/tr[5]").text
        raw5 = raw5.replace('\n', ' ')
        # raw5 = '  '.join(raw5.split())
        print(raw5)


        ##data of raw 6
        raw6 = fe("/html/body/app-root/app-layout/div/div/div/app-keyboard-shortcuts/div/div/div/div/div/div[2]/table/tbody/tr[6]").text
        raw6 = raw6.replace('\n', ' ')
        # raw6 = '  '.join(raw6.split())
        print(raw6)


