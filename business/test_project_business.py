import time
import pytest
from selenium.webdriver import ActionChains

from handle.add_project_handle import HandleProject
from page.add_project_page import AddProjectPage
from page.login_page import LoginBusiness
from untils import DriverUntil
from selenium.webdriver.common.keys import Keys


class TestAddProject:

    driver = DriverUntil.get_driver()
    handle_project = HandleProject(driver)
    login_business = LoginBusiness(driver)
    page = AddProjectPage(driver)

    def setup(self):
        self.driver.get("http://47.102.168.233:8880/")
        self.login_business.login_bus("admin", "123456")

    def test_add_project(self):
        time.sleep(2)
        self.handle_project.tap_get_volunteer_service()
        time.sleep(1)
        self.handle_project.tap_volunteer_project()
        time.sleep(1)
        self.handle_project.switch_iframe_01()
        self.handle_project.tap_create_project()
        time.sleep(2)
        self.handle_project.switch_iframe()
        time.sleep(1)
        self.handle_project.switch_iframe_02()
        self.handle_project.input_project_name("测试项目")
        time.sleep(2)
        self.handle_project.input_project_image(r"C:\Users\Administrator\Desktop\image\1.png")
        self.handle_project.tap_project_image_confirm()
        time.sleep(2)
        self.handle_project.tap_project_leader()
        time.sleep(1)
        self.handle_project.input_team_leader("刘小小")
        time.sleep(2)
        self.handle_project.tap_team_leader_select()
        time.sleep(2)
        self.handle_project.tap_team_leader_name()
        time.sleep(2)
        self.handle_project.tap_team_leader_confirm()
        time.sleep(1)
        self.handle_project.tap_project_start_date_input()
        time.sleep(1)
        self.handle_project.tap_project_start_date_input()
        self.handle_project.tap_project_start_date()
        time.sleep(1)
        self.handle_project.tap_project_end_date_input()
        time.sleep(1)
        self.handle_project.tap_project_end_date()
        time.sleep(1)
        self.handle_project.tap_project_label()
        self.handle_project.tap_project_zhu_ban()
        self.handle_project.tap_project_volunteer_demo()
        time.sleep(1)
        self.handle_project.input_project_volunteer("")
        time.sleep(1)
        self.handle_project.tap_project_volunteer_select()
        self.handle_project.tap_project_volunteer_name()
        self.handle_project.tap_project_volunteer_confirm()
        time.sleep(1)
        self.handle_project.tap_project_payer()
        self.handle_project.tap_project_payer_demo()
        self.handle_project.input_project_payer("")
        self.handle_project.tap_project_payer_select()
        self.handle_project.tap_project_payer_name()
        self.handle_project.tap_project_payer_confirm()
        time.sleep(1)
        self.handle_project.tap_project_area()
        # js = "window.scrollTo(0,1000)"
        # self.driver.execute_script(js)
        time.sleep(2)
        # js = "return document.getElementsByClassName('CodeMirror-scroll')[0].innerText='项目介绍';"
        # ele = self.driver.find_element_by_css_selector('#app > div.el-row > div > div > div > form > div:nth-child(12) > div > div.CodeMirror.cm-s-paper.CodeMirror-wrap > div.CodeMirror-scroll > div.CodeMirror-sizer > div > div > div > div.CodeMirror-code > pre > span > span')
        # ActionChains(self.driver).move_to_element(ele)
        js = "return document.querySelector('#app > div.el-row > div > div > div > form > div:nth-child(12) > div > div.CodeMirror.cm-s-paper.CodeMirror-wrap > div.CodeMirror-scroll > div.CodeMirror-sizer > div > div > div > div.CodeMirror-code > pre > span > span').innerText='项目介绍项目介绍项目介绍项目介绍项目介绍'"
        self.driver.execute_script(js)
        time.sleep(2)
        self.handle_project.tap_project_create_btn()

