from selenium.webdriver.common.by import By
from base import HandleElement
from page.add_project_page import AddProjectPage


class AuditProjectPage(HandleElement):

    project_view_feature = By.XPATH, '//*[@id="app"]/div/div/div/div/div/div[1]/div[4]/div[2]/table/tbody/tr[1]/td[8]/div/button[2]/span'
    project_audit_pass_feature = By.XPATH, '//*[@id="app"]/div[1]/div/div/div/div[2]/button[1]/span'
    project_audit_pass_confirm_feature = By.XPATH, '//*[@id="app"]/div[2]/div/div[3]/div/button[2]'
    project_audit_assert_feature = By.XPATH, '/html/body/div[3]/p'
    project_audit_reject = By.XPATH, '//*[@id="app"]/div[1]/div/div/div/div[2]/button[2]'
    project_audit_reject_reason = By.XPATH, '/html/body/div[2]/div/div[2]/div[2]/div[1]/input'
    project_audit_reject_confirm = By.XPATH, '/html/body/div[2]/div/div[3]/button[2]/span'



    def get_project_view_ele(self):
        return self.get_element(self.project_view_feature)

    def get_project_audit_pass_ele(self):
        return self.get_element(self.project_audit_pass_feature)

    def get_project_audit_pass_confirm_ele(self):
        return self.get_element(self.project_audit_pass_confirm_feature)

    def get_project_audit_assert_ele(self):
        return self.get_element(self.project_audit_assert_feature)

    def get_project_audit_reject_ele(self):
        return self.get_element(self.project_audit_reject)

    def get_project_audit_reject_reason_ele(self):
        return self.get_element(self.project_audit_reject_reason)

    def get_project_audit_reject_confirm_ele(self):
        return self.get_element(self.project_audit_reject_confirm)


