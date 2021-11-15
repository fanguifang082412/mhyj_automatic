import time
import pytest

from congfig.log import init_logging_config
from handle.audit_team_list_handle import AuditTeamListHandle
from handle.home_handle import HomeHandle
from page.login_page import LoginBusiness
from untils import DriverUntil
init_logging_config()


class TestAuditTeam:
    driver = DriverUntil.get_driver()
    home_handle = HomeHandle(driver)
    login_business = LoginBusiness(driver)
    audit_team_handle = AuditTeamListHandle(driver)

    def setup(self):
        self.driver.get("http://47.102.168.233:8880/")

    def teardown_class(cls):
        DriverUntil.quit_driver()

    # @pytest.mark.skip()
    def test_audit_team_pass(self):
        self.login_business.login_bus("admin", "123456")
        self.home_handle.tap_home_ele()
        self.home_handle.switch_to_iframe_01()
        self.home_handle.tap_audit_team()
        self.driver.switch_to.default_content()
        self.audit_team_handle.switch_frame()
        self.audit_team_handle.tap_view()
        self.driver.switch_to.default_content()
        self.audit_team_handle.switch_frame_04()
        time.sleep(1)
        self.audit_team_handle.tap_audit_team_pass()
        self.audit_team_handle.tap_audit_pass_confirm()
        self.audit_team_handle.tap_audit_pass()
        time.sleep(2)
        assert_text = self.audit_team_handle.get_assert_info()
        assert assert_text == "组建完成"

    def test_audit_team_reject(self):
        self.home_handle.tap_home_ele()
        self.home_handle.switch_to_iframe_01()
        self.home_handle.tap_audit_team()
        self.driver.switch_to.default_content()
        self.audit_team_handle.switch_frame()
        self.audit_team_handle.tap_view()
        self.driver.switch_to.default_content()
        self.audit_team_handle.switch_frame_04()
        self.audit_team_handle.tap_audit_team_reject()
        self.audit_team_handle.input_reject_reason("测试拒绝")
        self.audit_team_handle.tap_audit_team_reject_confirm()
        time.sleep(2)
        assert_text = self.audit_team_handle.get_assert_info()
        assert assert_text == "组建失败"












