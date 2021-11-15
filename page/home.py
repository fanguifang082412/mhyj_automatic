from selenium.webdriver.common.by import By
from base import HandleElement


class HomePage(HandleElement):

    home_feature = By.XPATH, '//a[@href="/notice/hello"]'
    audit_team_feature = By.XPATH, '//*[@id="app"]/div[1]/div[1]/div/div/button/span'
    iframe_01 = By.XPATH, '//*[@id="content-main"]/iframe[2]'

    def get_home_ele(self):
        return self.get_element(self.home_feature)

    def get_iframe_01(self):
        return self.get_element(self.iframe_01)

    def get_audit_team_ele(self):
        return self.get_element(self.audit_team_feature)
