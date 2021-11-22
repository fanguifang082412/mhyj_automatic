from page.audit_project_page import AuditProjectPage


class AuditProjectListHandle(AuditProjectPage):

    def tap_project_view(self):
        self.get_project_view_ele().click()

    def tap_project_audit_pass(self):
        self.get_project_audit_pass_ele().click()

    def tap_project_audit_pass_confirm(self):
        self.get_project_audit_pass_confirm_ele().click()

    def get_project_audit_assert_text(self):
        return self.get_project_audit_assert_ele().text

    def tap_project_audit_reject(self):
        self.get_project_audit_reject_ele().click()

    def input_project_audit_reject_reason(self, reason):
        self.get_project_audit_reject_reason_ele().send_keys(reason)

    def tap_project_audit_reject_confirm(self):
        self.get_project_audit_reject_confirm_ele().click()
