import time

from selenium.webdriver.common.by import By
from base import HandleElement
from untils import DriverUntil





class AddTeamPage(HandleElement):


    volunteer_service = By.XPATH, "//span[contains(text(),'志愿服务')]"
    volunteer_team = By.XPATH, "//a[@href='/volunteer_team']"
    add_team_iframe = By.XPATH, "//iframe[@src='/volunteer_team']"
    create_team = By.XPATH, "//button/span[contains(text(),  '创建团队')]"
    team_name = By.XPATH, '//*[@id="app"]/div[3]/div/div[2]/form/div[1]/div/div[1]/input'
    team_name_all = By.XPATH, "//*[@id='app']/div[3]/div/div[2]/form/div[2]/div/div[1]/input"
    team_image = By.XPATH, "//input[@name='file']"
    team_builder = By.XPATH, "//*[@id='app']/div[3]/div/div[2]/form/div[4]/div/div/input"
    team_yunying_select = By.XPATH, "// button / span[contains(text(), '选择')]"
    team_yunying_input = By.XPATH, '//input[ @ placeholder = "请输入志愿者姓名/手机号"]'
    team_yunying_select_btn = By.XPATH, '/html/body/div[2]/div/div[2]/form/div[2]/div/button/span'
    team_yunying_select_confirm = By.XPATH, '/html/body/div[2]/div/div[2]/div[1]/div[4]/div[2]/table/tbody/tr/td[5]/div/button/span'
    team_date = By.XPATH, '//input[@placeholder="选择日期"]'
    team_date_comfirm = By.XPATH, '/html/body/div[4]/div[1]/div/div[2]/table[1]/tbody/tr[2]/td[2]/div/span'
    team_province = By.XPATH, '//*[@id="app"]/div[3]/div/div[2]/form/div[7]/div/div[1]/div/div/div/div/input'
    team_province_comfirn = By.XPATH, '/html/body/div[5]/div[1]/div[1]/ul/li[1]/span'
    team_shi = By.XPATH, '//*[@id="app"]/div[3]/div/div[2]/form/div[7]/div/div[2]/div/div/div/div/input'
    team_shi_comfirn = By.XPATH, '/html/body/div[6]/div[1]/div[1]/ul/li'
    team_qu = By.XPATH, '//*[@id="app"]/div[3]/div/div[2]/form/div[7]/div/div[3]/div/div/div/div/input'
    team_qu_comfirn = By.XPATH, '/html/body/div[7]/div[1]/div[1]/ul/li[1]/span'
    team_office = By.XPATH, '//*[@id="app"]/div[3]/div/div[2]/form/div[8]/div/div[1]/input'
    team_connecter = By.XPATH, '//*[@id="app"]/div[3]/div/div[2]/form/div[9]/div/div[1]/input'
    team_phone = By.XPATH, '//*[@id="app"]/div[3]/div/div[2]/form/div[10]/div/div[1]/input'
    team_service = By.XPATH, '//*[@id="app"]/div[3]/div/div[2]/form/div[11]/div/div[1]/label[1]/span[2]'
    team_introduce = By.XPATH, '//*[@id="app"]/div[3]/div/div[2]/form/div[12]/div/div[1]/textarea'
    team_create_now = By.XPATH, '//*[@id="app"]/div[3]/div/div[2]/form/div[13]/div/button[1]/span'

    def get_volunteer_service(self):
        return self.get_element(self.volunteer_service)

    def get_volunteer_team(self):
        return self.get_element(self.volunteer_team)

    def get_add_team_iframe(self):
        return self.get_element(self.add_team_iframe)

    def get_create_team(self):
        return self.get_element(self.create_team)

    def get_team_name(self):
        return self.get_element(self.team_name)

    def get_team_name_all(self):
        return self.get_element(self.team_name_all)

    def get_team_image(self):
        return self.get_element(self.team_image)

    def get_team_builder(self):
        return self.get_element(self.team_builder)

    def get_team_yunying_select(self):
        return self.get_element(self.team_yunying_select)

    def get_team_yunying_input(self):
        return self.get_element(self.team_yunying_input)

    def get_team_yunying_select_btn(self):
        return self.get_element(self.team_yunying_select_btn)

    def get_team_yunying_select_confirm(self):
        return self.get_element(self.team_yunying_select_confirm)

    def get_team_date(self):
        return self.get_element(self.team_date)

    def get_team_date_comfirm(self):
        return self.get_element(self.team_date_comfirm)

    def get_team_province(self):
        return self.get_element(self.team_province)

    def get_team_province_comfirn(self):
        return self.get_element(self.team_province_comfirn)

    def get_team_shi(self):
        return self.get_element(self.team_shi)

    def get_team_shi_comfirn(self):
        return self.get_element(self.team_shi_comfirn)

    def get_team_qu(self):
        return self.get_element(self.team_qu)

    def get_team_qu_comfirn(self):
        return self.get_element(self.team_qu_comfirn)

    def get_team_office(self):
        return self.get_element(self.team_office)

    def get_team_connecter(self):
        return self.get_element(self.team_connecter)

    def get_team_phone(self):
        return self.get_element(self.team_phone)

    def get_team_service(self):
        return self.get_element(self.team_service)

    def get_team_introduce(self):
        return self.get_element(self.team_introduce)

    def get_team_create_now(self):
        return self.get_element(self.team_create_now)



class AddTeamAction(AddTeamPage):

    def click_get_volunteer_service(self):
        self.get_volunteer_service().click()

    def click_volunteer_team(self):
        self.get_volunteer_team().click()

    def switch_add_team_iframe(self):
        DriverUntil.get_driver().switch_to.frame(self.get_add_team_iframe())

    def click_create_team(self):
        self.get_create_team().click()

    def input_team_name(self, team_name):
        self.get_team_name().send_keys(team_name)

    def input_team_name_all(self, team_name_all):
        self.get_team_name_all().send_keys(team_name_all)

    def input_team_image(self, image_url):
        self.get_team_image().send_keys(image_url)

    def input_team_builder(self, team_builder):
        self.get_team_builder().send_keys(team_builder)

    def click_team_yunying_select(self):
        self.get_team_yunying_select().click()

    def input_team_yunying_input(self, team_yunying):
        self.get_team_yunying_input().send_keys(team_yunying)

    def click_team_yunying_select_btn(self):
        self.get_team_yunying_select_btn().click()

    def click_team_yunying_select_confirm(self):
        self.get_team_yunying_select_confirm().click()

    def click_team_date(self):
        self.get_team_date().click()

    def click_team_date_comfirm(self):
        self.get_team_date_comfirm().click()

    def click_team_province(self):
        self.get_team_province().click()

    def click_team_province_comfirn(self):
        self.get_team_province_comfirn().click()

    def click_team_shi(self):
        self.get_team_shi().click()

    def click_team_shi_comfirn(self):
        self.get_team_shi_comfirn().click()

    def click_team_qu(self):
        self.get_team_qu().click()

    def click_team_qu_comfirn(self):
        self.get_team_qu_comfirn().click()

    def input_team_office(self, team_office):
        self.get_team_office().send_keys(team_office)

    def input_team_connecter(self, team_connecter):
        self.get_team_connecter().send_keys(team_connecter)

    def input_team_phone(self, team_phone):
        self.get_team_phone().send_keys(team_phone)

    def click_team_service(self):
        self.get_team_service().click()

    def input_team_introduce(self, team_introduce):
        self.get_team_introduce().send_keys(team_introduce)

    def click_team_create_now(self):
        self.get_team_create_now().click()




class AddTeamBusiness:

    def __init__(self, driver):
        self.add_team_action = AddTeamAction(driver)

    def add_team(self, team_name, team_name_all, image_url, team_builder, team_yunying, team_office, team_connecter, team_phone, team_introduce):
        self.add_team_action.click_get_volunteer_service()
        time.sleep(2)
        self.add_team_action.click_volunteer_team()
        self.add_team_action.switch_add_team_iframe()
        self.add_team_action.click_create_team()
        time.sleep(1)
        self.add_team_action.input_team_name(team_name)
        self.add_team_action.input_team_name_all(team_name_all)
        self.add_team_action.input_team_image(image_url)
        self.add_team_action.input_team_builder(team_builder)
        self.add_team_action.click_team_yunying_select()
        time.sleep(2)
        self.add_team_action.input_team_yunying_input(team_yunying)
        time.sleep(2)
        self.add_team_action.click_team_yunying_select_btn()
        time.sleep(2)
        self.add_team_action.click_team_yunying_select_confirm()
        time.sleep(1)
        self.add_team_action.click_team_date()
        time.sleep(1)
        self.add_team_action.click_team_date_comfirm()
        time.sleep(1)
        self.add_team_action.click_team_province()
        time.sleep(1)
        self.add_team_action.click_team_province_comfirn()
        time.sleep(1)
        self.add_team_action.click_team_shi()
        time.sleep(1)
        self.add_team_action.click_team_shi_comfirn()
        time.sleep(1)
        self.add_team_action.click_team_qu()
        time.sleep(1)
        self.add_team_action.click_team_qu_comfirn()
        time.sleep(1)
        self.add_team_action.input_team_office(team_office)
        time.sleep(1)
        self.add_team_action.input_team_connecter(team_connecter)
        time.sleep(1)
        self.add_team_action.input_team_phone(team_phone)
        self.add_team_action.click_team_service()
        self.add_team_action.input_team_introduce(team_introduce)
        self.add_team_action.click_team_create_now()

    def team_yunying_is_null(self, team_name, team_name_all, image_url, team_builder, team_office, team_connecter, team_phone, team_introduce):
        self.add_team_action.click_get_volunteer_service()
        time.sleep(2)
        self.add_team_action.click_volunteer_team()
        self.add_team_action.switch_add_team_iframe()
        self.add_team_action.click_create_team()
        time.sleep(2)
        self.add_team_action.input_team_name(team_name)
        self.add_team_action.input_team_name_all(team_name_all)
        self.add_team_action.input_team_image(image_url)
        self.add_team_action.input_team_builder(team_builder)
        time.sleep(1)
        self.add_team_action.click_team_date()
        time.sleep(3)
        self.add_team_action.click_team_date_comfirm()
        time.sleep(2)
        self.add_team_action.click_team_province()
        time.sleep(1)
        self.add_team_action.click_team_province_comfirn()
        time.sleep(1)
        self.add_team_action.click_team_shi()
        time.sleep(1)
        self.add_team_action.click_team_shi_comfirn()
        time.sleep(1)
        self.add_team_action.click_team_qu()
        time.sleep(1)
        self.add_team_action.click_team_qu_comfirn()
        time.sleep(1)
        self.add_team_action.input_team_office(team_office)
        time.sleep(1)
        self.add_team_action.input_team_connecter(team_connecter)
        time.sleep(1)
        self.add_team_action.input_team_phone(team_phone)
        self.add_team_action.click_team_service()
        self.add_team_action.input_team_introduce(team_introduce)
        self.add_team_action.click_team_create_now()

    def team_date_is_null(self, team_name, team_name_all, image_url, team_builder, team_yunying, team_office, team_connecter, team_phone, team_introduce):
        self.add_team_action.click_get_volunteer_service()
        time.sleep(2)
        self.add_team_action.click_volunteer_team()
        self.add_team_action.switch_add_team_iframe()
        self.add_team_action.click_create_team()
        time.sleep(1)
        self.add_team_action.input_team_name(team_name)
        self.add_team_action.input_team_name_all(team_name_all)
        self.add_team_action.input_team_image(image_url)
        self.add_team_action.input_team_builder(team_builder)
        self.add_team_action.click_team_yunying_select()
        time.sleep(2)
        self.add_team_action.input_team_yunying_input(team_yunying)
        time.sleep(2)
        self.add_team_action.click_team_yunying_select_btn()
        time.sleep(2)
        self.add_team_action.click_team_yunying_select_confirm()
        time.sleep(1)
        self.add_team_action.click_team_province()
        time.sleep(1)
        self.add_team_action.click_team_province_comfirn()
        time.sleep(1)
        self.add_team_action.click_team_shi()
        time.sleep(1)
        self.add_team_action.click_team_shi_comfirn()
        time.sleep(1)
        self.add_team_action.click_team_qu()
        time.sleep(1)
        self.add_team_action.click_team_qu_comfirn()
        time.sleep(1)
        self.add_team_action.input_team_office(team_office)
        time.sleep(1)
        self.add_team_action.input_team_connecter(team_connecter)
        time.sleep(1)
        self.add_team_action.input_team_phone(team_phone)
        self.add_team_action.click_team_service()
        self.add_team_action.input_team_introduce(team_introduce)
        self.add_team_action.click_team_create_now()

    def team_service_is_null(self, team_name, team_name_all, image_url, team_builder, team_yunying, team_office, team_connecter, team_phone, team_introduce):
        self.add_team_action.click_get_volunteer_service()
        time.sleep(2)
        self.add_team_action.click_volunteer_team()
        self.add_team_action.switch_add_team_iframe()
        self.add_team_action.click_create_team()
        time.sleep(1)
        self.add_team_action.input_team_name(team_name)
        self.add_team_action.input_team_name_all(team_name_all)
        self.add_team_action.input_team_image(image_url)
        self.add_team_action.input_team_builder(team_builder)
        self.add_team_action.click_team_yunying_select()
        time.sleep(2)
        self.add_team_action.input_team_yunying_input(team_yunying)
        time.sleep(2)
        self.add_team_action.click_team_yunying_select_btn()
        time.sleep(2)
        self.add_team_action.click_team_yunying_select_confirm()
        time.sleep(1)
        self.add_team_action.click_team_date()
        time.sleep(1)
        self.add_team_action.click_team_date_comfirm()
        time.sleep(1)
        self.add_team_action.click_team_province()
        time.sleep(1)
        self.add_team_action.click_team_province_comfirn()
        time.sleep(1)
        self.add_team_action.click_team_shi()
        time.sleep(1)
        self.add_team_action.click_team_shi_comfirn()
        time.sleep(1)
        self.add_team_action.click_team_qu()
        time.sleep(1)
        self.add_team_action.click_team_qu_comfirn()
        time.sleep(1)
        self.add_team_action.input_team_office(team_office)
        time.sleep(1)
        self.add_team_action.input_team_connecter(team_connecter)
        time.sleep(1)
        self.add_team_action.input_team_phone(team_phone)
        self.add_team_action.input_team_introduce(team_introduce)
        self.add_team_action.click_team_create_now()


