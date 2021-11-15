from selenium.webdriver.common.by import By
from base import HandleElement



class AddProjectPage(HandleElement):

        volunteer_service = By.XPATH, "//span[contains(text(),'志愿服务')]"
        volunteer_project = By.XPATH, '//a[@href="/project"]'
        iframe_01 = By.XPATH, '//iframe[@data-id="/project"]'
        create_project = By.XPATH, "//span[contains(text(), '创建项目')]"
        iframe_02 = By.XPATH, '//*[@id="content-main"]/iframe[3]'
        project_name = By.XPATH, '//input[@placeholder="输入项目名称"]'
        project_image = By.XPATH, '//input[@id="uploads"]'
        project_image_confirm = By.XPATH, '//*[@id="app"]/div[3]/div/div[3]/div/button[2]'
        project_leader = By.XPATH, '//input[@placeholder="请选择项目负责人"]'
        team_leader = By.XPATH, '//*[@id="app"]/div[2]/div/div[2]/div/div[2]/div[2]/div/input'
        team_leader_select = By.XPATH, '//*[@id="app"]/div[2]/div/div[2]/div/div[2]/button/i'
        team_leader_name = By.XPATH, '//*[@id="app"]/div[2]/div/div[2]/div/div[2]/div[3]/div[3]/table/tbody/tr/td[2]'
        team_leader_confirm = By.XPATH, '//*[@id="app"]/div[2]/div/div[3]/div/button[2]/span'
        project_start_date_input = By.XPATH, '//*[@id="app"]/div[1]/div/div/div/form/div[4]/div/div[1]/input'
        project_start_date = By.XPATH, '/html/body/div[3]/div[1]/div/div[2]/table[1]/tbody/tr[3]/td[7]/div/span'
        project_end_date_input = By.XPATH, '//*[@id="app"]/div[1]/div/div/div/form/div[4]/div/div[2]/input'
        project_end_date = By.XPATH, '/html/body/div[4]/div[1]/div/div[2]/table[1]/tbody/tr[6]/td[3]/div/span'
        project_laber = By.XPATH, "//span[contains(text(), '残障人士')]"
        project_zhu_ban = By.XPATH, '//input[@placeholder="请选择项目主办方"]'
        project_volunteer_demo = By.XPATH, '//*[@id="tab-personal"]'
        project_volunteer_input = By.XPATH, '//*[@id="app"]/div[2]/div/div[2]/div/div[2]/div[4]/div[1]/input'
        project_volunteer_select = By.XPATH, '//*[@id="app"]/div[2]/div/div[2]/div/div[2]/button'
        project_volunteer_name = By.XPATH, '//*[@id="app"]/div[2]/div/div[2]/div/div[2]/div[5]/div[3]/table/tbody/tr/td[2]'
        project_volunteer_confirm = By.XPATH, '//*[@id="app"]/div[2]/div/div[3]/div/button[2]/span'
        project_payer = By.XPATH, '//input[@placeholder="请选择项目付款人"]'
        project_payer_demo = By.XPATH, '//*[@id="tab-personal"]'
        project_payer_input = By.XPATH, '//*[@id="app"]/div[2]/div/div[2]/div/div[2]/div[4]/div/input'
        project_payer_select = By.XPATH, '//*[@id="app"]/div[2]/div/div[2]/div/div[2]/button'
        project_payer_name = By.XPATH, '//*[@id="app"]/div[2]/div/div[2]/div/div[2]/div[5]/div[3]/table/tbody/tr/td[2]'
        project_payer_confirm = By.XPATH, '//*[@id="app"]/div[2]/div/div[3]/div/button[2]'
        project_area = By.XPATH, '//*[@id="app"]/div[1]/div/div/div/form/div[9]/div/div/label[1]/span[2]'
        project_introduce = By.XPATH, '//*[@style="padding-right: 0.1px;"]'
        project_create_btn = By.XPATH, '//*[@id="app"]/div[1]/div/div/div/footer/button/span'

        def get_volunteer_service_ele(self):
            return self.get_element(self.volunteer_service)

        def get_volunteer_project_ele(self):
            return self.get_element(self.volunteer_project)

        def get_switch_iframe_01(self):
            return self.get_element(self.iframe_01)

        def get_create_project(self):
            return self.get_element(self.create_project)

        def get_switch_iframe_02(self):
            return self.get_element(self.iframe_02)

        def get_project_name(self):
            return self.get_element(self.project_name)

        def get_project_image(self):
            return self.get_element(self.project_image)

        def get_project_image_confirm(self):
            return self.get_element(self.project_image_confirm)

        def get_project_leader(self):
            return self.get_element(self.project_leader)

        def get_team_leader(self):
            return self.get_element(self.team_leader)

        def get_team_leader_select(self):
            return self.get_element(self.team_leader_select)

        def get_team_leader_name(self):
            return self.get_element(self.team_leader_name)

        def get_team_leader_confirm(self):
            return self.get_element(self.team_leader_confirm)

        def get_project_start_date_input(self):
            return self.get_element(self.project_start_date_input)

        def get_project_start_date(self):
            return self.get_element(self.project_start_date)

        def get_project_end_date_input(self):
            return self.get_element(self.project_end_date_input)

        def get_project_end_date(self):
            return self.get_element(self.project_end_date)

        def get_project_label(self):
            return self.get_element(self.project_laber)

        def get_project_zhu_ban(self):
            return self.get_element(self.project_zhu_ban)

        def get_project_volunteer_demo(self):
            return self.get_element(self.project_volunteer_demo)

        def get_project_volunteer_input(self):
            return self.get_element(self.project_volunteer_input)

        def get_project_volunteer_select(self):
            return self.get_element(self.project_volunteer_select)

        def get_project_volunteer_name(self):
            return self.get_element(self.project_volunteer_name)

        def get_project_volunteer_confirm(self):
            return self.get_element(self.project_volunteer_confirm)

        def get_project_payer(self):
            return self.get_element(self.project_payer)

        def get_project_payer_demo(self):
            return self.get_element(self.project_payer_demo)

        def get_project_payer_input(self):
            return self.get_element(self.project_payer_input)

        def get_project_payer_select(self):
            return self.get_element(self.project_payer_select)

        def get_project_payer_name(self):
            return self.get_element(self.project_payer_name)

        def get_project_payer_confirm(self):
            return self.get_element(self.project_payer_confirm)

        def get_project_area(self):
            return self.get_element(self.project_area)

        def get_project_introduce(self):
            return self.get_element(self.project_introduce)

        def get_project_create_btn(self):
            return self.get_element(self.project_create_btn)


