import time
from tabulate import tabulate


class visitors_class():

    def __init__(self, driver):
        self.driver=driver
        self.huluhb_icon = "/html/body/app-root/app-layout/div/app-topbar/header/div/div[1]/div/a[2]/span[1]/img"  # hulub icon click to land on dasboard
        self.visitors_tab="/html/body/app-root/app-layout/div/app-sidebar/div/div/div/div/ul/li[6]"
        self.browsing_tab_count="/html/body/app-root/app-layout/div/div/div/app-visitors/div/div/div[1]/div[1]/div[1]/div/div/div/div[2]/h5"
        self.unassigned_tab_count="/html/body/app-root/app-layout/div/div/div/app-visitors/div/div/div[1]/div[1]/div[2]/div/div/div/div[2]/h5"
        self.chatting_tab_count="/html/body/app-root/app-layout/div/div/div/app-visitors/div/div/div[1]/div[1]/div[3]/div/div/div/div[2]/h5"
        self.invited_tab_count="/html/body/app-root/app-layout/div/div/div/app-visitors/div/div/div[1]/div[1]/div[4]/div/div/div/div[2]/h5"
        self.inactive_tab_count="/html/body/app-root/app-layout/div/div/div/app-visitors/div/div/div[1]/div[1]/div[5]/div/div/div/div[2]/h5"
        self.left_tab_count="/html/body/app-root/app-layout/div/div/div/app-visitors/div/div/div[1]/div[1]/div[6]/div/div/div/div[2]/h5"




    def visitors_method(self):
        self.driver.implicitly_wait(20)
        fe=self.driver.find_element_by_xpath

        fe(self.huluhb_icon).click()
        fe(self.visitors_tab).click()
        time.sleep(2)

        url=self.driver.current_url
        expectedurl="https://new.beelinks.solutions/visitors"

        if url==expectedurl:
            print("current and expected urls are matched \n","current url =", url, "\n" ,"expected url =",expectedurl)


        else:
            print("ERROR URL IS NOT MATCHED")


        #browsing tab
        fe(self.browsing_tab_count).click()
        browsingcount=fe(self.browsing_tab_count).text
        print("number of user currently browsing = ", browsingcount)


        #unassigned tab
        fe(self.unassigned_tab_count).click()
        untabcount=fe(self.unassigned_tab_count).text
        print("number of unassigned users = ", untabcount)

        #chatting tab
        fe(self.chatting_tab_count).click()
        chattingtabcount=fe(self.chatting_tab_count).text
        print("number of user in chatting = ",chattingtabcount)

        #invited tab
        fe(self.invited_tab_count).click()
        invited=fe(self.invited_tab_count).text
        print("number of users invited  = ", invited)

        #inactive tab
        fe(self.inactive_tab_count).click()
        inactive=fe(self.inactive_tab_count).text
        print("number of inactive users are = ", inactive)


        #left tab
        fe(self.left_tab_count).click()
        left=fe(self.left_tab_count).text
        print("no of user left from the site = ", left)


        # table = fe("/html/body/app-root/app-layout/div/div/div/app-visitors/div/div/div[1]/div[2]/div/div/div/app-left/div/table/tbody/tr[1]").text
        # print(tabulate(table, tablefmt='html'))

        raw1=fe("/html/body/app-root/app-layout/div/div/div/app-visitors/div/div/div[1]/div[2]/div/div/div/app-left/div/table/tbody/tr[1]").text
        # raw1 = raw1.replace('\n', '')
        raw1 = '  '.join(raw1.split())
        print(raw1)
