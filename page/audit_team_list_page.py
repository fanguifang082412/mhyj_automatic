from selenium.webdriver.common.by import By
from base import HandleElement


class AuditTeamList(HandleElement):
    view_feature = By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div[4]/div[2]/table/tbody/tr[1]/td[8]/div/button[1]'
    audit_team_pass_feature = By.XPATH,  '//*[@id="app"]/div[2]/div/div/button[1]/span'
    audit_team_reject_feature = By.XPATH, '//*[@id="app"]/div[2]/div/div/button[2]/span'
    iframe_02 = By.XPATH, '//*[@id="content-main"]/iframe[4]'
    audit_pass_confirm_feature = By.XPATH, '//*[@id="app"]/div[3]/div/div[2]/button[2]/span'
    audit_pass_btn_feature = By.XPATH, '/html/body/div[2]/div/div[3]/button[2]/span'
    audit_team_reject_reason_feature = By.XPATH, '/html/body/div[2]/div/div[2]/div[2]/div[1]/textarea'
    audit_team_reject_confirm_feature = By.XPATH, '/html/body/div[2]/div/div[3]/button[2]/span'
    iframe_feature = By.XPATH, '//*[@id="content-main"]/iframe[3]'
    assert_ele_feature = By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div/div[3]/span[2]'
    iframe_03 = By.XPATH, '//*[@id="content-main"]/iframe[5]'
    iframe_04 = By.XPATH, '//*[@id="content-main"]/iframe[4]'


    def get_view_ele(self):
        return self.get_element(self.view_feature)

    def get_audit_team_pass_ele(self):
        return self.get_element(self.audit_team_pass_feature)

    def get_audit_team_reject_ele(self):
        return self.get_element(self.audit_team_reject_feature)

    def get_iframe_02_ele(self):
        return self.get_element(self.iframe_02)

    def get_audit_pass_confirm_ele(self):
        return self.get_element(self.audit_pass_confirm_feature)

    def get_audit_pass_btn_ele(self):
        return self.get_element(self.audit_pass_btn_feature)

    def get_audit_team_reject_reason_ele(self):
        return self.get_element(self.audit_team_reject_reason_feature)

    def get_audit_team_reject_confirm_ele(self):
        return self.get_element(self.audit_team_reject_confirm_feature)

    def get_iframe_ele(self):
        return self.get_element(self.iframe_feature)

    def get_assert_ele(self):
        return self.get_element(self.assert_ele_feature)

    def get_iframe_03_ele(self):
        return self.get_element(self.iframe_03)

    def get_iframe_04_ele(self):
        return self.get_element(self.iframe_04)