from page.home import HomePage




class HomeHandle(HomePage):

    def tap_home_ele(self):
        self.get_home_ele().click()

    def switch_to_iframe_01(self):
        self.driver.switch_to.frame(self.get_iframe_01())

    def tap_audit_team(self):
        self.get_audit_team_ele().click()

    def tap_audit_project(self):
        self.get_audit_project_ele().click()