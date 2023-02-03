class visitors():

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

