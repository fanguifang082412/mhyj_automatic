from page.audit_team_list_page import AuditTeamList

class AuditTeamListHandle(AuditTeamList):

    def tap_view(self):
        self.get_view_ele().click()

    def tap_audit_team_pass(self):
        self.get_audit_team_pass_ele().click()

    def tap_audit_team_reject(self):
        self.get_audit_team_reject_ele().click()

    def switch_iframe_02(self):
        self.driver.switch_to.iframe(self.get_iframe_02_ele())

    def tap_audit_pass_confirm(self):
        self.get_audit_pass_confirm_ele().click()

    def tap_audit_pass(self):
        self.get_audit_pass_btn_ele().click()

    def input_reject_reason(self, reason):
        self.get_audit_team_reject_reason_ele().send_keys(reason)

    def tap_audit_team_reject_confirm(self):
        self.get_audit_team_reject_confirm_ele().click()

    def switch_frame(self):
        self.driver.switch_to.frame(self.get_iframe_ele())

    def get_assert_info(self):
        return self.get_assert_ele().text

    def switch_frame_03(self):
        self.driver.switch_to.frame(self.get_iframe_03_ele())

    def switch_frame_04(self):
        self.driver.switch_to.frame(self.get_iframe_04_ele())