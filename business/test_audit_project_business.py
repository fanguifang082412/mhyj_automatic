import time
import pytest
from selenium.webdriver.common.by import By
from handle.audit_project_list_handle import AuditProjectListHandle
from handle.audit_team_list_handle import AuditTeamListHandle
from handle.home_handle import HomeHandle
from page.login_page import LoginBusiness
from untils import DriverUntil


class TestAuditProject:

    def setup_class(cls):
        cls.driver = DriverUntil.get_driver()
        cls.audit_project_list_handle = AuditProjectListHandle(cls.driver)
        cls.audit_team_list_handle = AuditTeamListHandle(cls.driver)
        cls.home_handle = HomeHandle(cls.driver)
        cls.login_business = LoginBusiness(cls.driver)
        cls.driver.get("http://47.102.168.233:8880/")
        cls.login_business.login_bus("admin", "123456")

    def teardown_class(cls):
        DriverUntil.quit_driver()

    def setup(self):
        self.driver.get("http://47.102.168.233:8880/")

    def test_audit_project_pass(self):
        self.home_handle.tap_home_ele()
        self.home_handle.switch_to_iframe_01()
        self.home_handle.tap_audit_project()
        self.driver.switch_to.default_content()
        self.audit_team_list_handle.switch_frame()
        time.sleep(1)
        self.audit_project_list_handle.tap_project_view()
        self.driver.switch_to.default_content()
        frame_06_feature = By.XPATH, '//*[@id="content-main"]/iframe[4]'
        frame_06_ele = self.driver.find_element(*frame_06_feature)
        self.driver.switch_to.frame(frame_06_ele)
        time.sleep(1)
        self.audit_project_list_handle.tap_project_audit_pass()
        time.sleep(1)
        self.audit_project_list_handle.tap_project_audit_pass_confirm()
        time.sleep(1)
        asset_info = self.audit_project_list_handle.get_project_audit_assert_text()
        assert "操作成功!" == asset_info

    def test_audit_project_fail(self):
        self.home_handle.tap_home_ele()
        self.home_handle.switch_to_iframe_01()
        self.home_handle.tap_audit_project()
        self.driver.switch_to.default_content()
        self.audit_team_list_handle.switch_frame()
        time.sleep(1)
        self.audit_project_list_handle.tap_project_view()
        self.driver.switch_to.default_content()
        frame_08_feature = By.XPATH, '//*[@id="content-main"]/iframe[4]'
        frame_08_ele = self.driver.find_element(*frame_08_feature)
        self.driver.switch_to.frame(frame_08_ele)
        time.sleep(1)
        self.audit_project_list_handle.tap_project_audit_reject()
        self.audit_project_list_handle.input_project_audit_reject_reason('测试用例')
        self.audit_project_list_handle.tap_project_audit_reject_confirm()
        asset_info = self.audit_project_list_handle.get_project_audit_assert_text()
        assert "操作成功!" == asset_info






