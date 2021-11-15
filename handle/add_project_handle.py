import allure
import pytest

from page.add_project_page import AddProjectPage
from untils import DriverUntil


class HandleProject(AddProjectPage):
    @allure.step("点击志愿者服务")
    def tap_get_volunteer_service(self):
        self.get_volunteer_service_ele().click()

    def tap_volunteer_project(self):
        self.get_volunteer_project_ele().click()

    def switch_iframe_01(self):
        DriverUntil.get_driver().switch_to.frame(self.get_switch_iframe_01())

    def tap_create_project(self):
        self.get_create_project().click()

    def switch_iframe(self):
        DriverUntil.get_driver().switch_to.default_content()

    def switch_iframe_02(self):
        # print(self.get_switch_iframe_02())
        DriverUntil.get_driver().switch_to.frame(self.get_switch_iframe_02())

    def input_project_name(self, project_name):
        self.get_project_name().send_keys(project_name)

    def input_project_image(self, project_image):
        self.get_project_image().send_keys(project_image)

    def tap_project_leader(self):
        self.get_project_leader().click()

    def tap_project_image_confirm(self):
        self.get_project_image_confirm().click()

    def input_team_leader(self, team_leader):
        self.get_team_leader().send_keys(team_leader)

    def tap_team_leader_select(self):
        self.get_team_leader_select().click()

    def tap_team_leader_name(self):
        self.get_team_leader_name().click()

    def tap_team_leader_confirm(self):
        self.get_team_leader_confirm().click()

    def tap_project_start_date_input(self):
        self.get_project_start_date_input().click()

    def tap_project_start_date(self):
        self.get_project_start_date().click()

    def tap_project_end_date_input(self):
        self.get_project_end_date_input().click()

    def tap_project_end_date(self):
        self.get_project_end_date().click()

    def tap_project_label(self):
        self.get_project_label().click()

    def tap_project_zhu_ban(self):
        self.get_project_zhu_ban().click()

    def tap_project_volunteer_demo(self):
        self.get_project_volunteer_demo().click()

    def input_project_volunteer(self, project_volunteer):
        self.get_project_volunteer_input().send_keys(project_volunteer)

    def tap_project_volunteer_select(self):
        self.get_project_volunteer_select().click()

    def tap_project_volunteer_name(self):
        self.get_project_volunteer_name().click()

    def tap_project_volunteer_confirm(self):
        self.get_project_volunteer_confirm().click()

    def tap_project_payer(self):
        self.get_project_payer().click()

    def tap_project_payer_demo(self):
        self.get_project_payer_demo().click()

    def input_project_payer(self, project_payer):
        self.get_project_payer_input().send_keys(project_payer)

    def tap_project_payer_select(self):
        self.get_project_payer_select().click()

    def tap_project_payer_name(self):
        self.get_project_payer_name().click()

    def tap_project_payer_confirm(self):
        self.get_project_payer_confirm().click()

    def tap_project_area(self):
        self.get_project_area().click()

    def input_project_introduce(self, introduce):
        self.get_project_introduce().send_keys(introduce)

    def tap_project_create_btn(self):
        self.get_project_create_btn().click()