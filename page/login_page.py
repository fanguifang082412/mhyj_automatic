from selenium.webdriver.common.by import By

from base import HandleElement
from untils import DriverUntil




class LoginPage(HandleElement):

    username = By.XPATH, "//form[@class='m-t']/div/input[@placeholder='用户名']"
    password = By.XPATH, "//form[@class='m-t']/div/input[@placeholder='密码']"
    login = By.XPATH, "//button[@type='submit']"

    def get_username(self):
        return self.get_element(self.username)

    def get_password(self):
        return self.get_element(self.password)

    def get_login(self):
        return self.get_element(self.login)


class LoginAction(LoginPage):

    def input_username(self, username):
        self.get_username().send_keys(username)

    def input_password(self, password):
        self.get_password().send_keys(password)

    def click_login(self):
        self.get_login().click()



class LoginBusiness:
    def __init__(self, driver):
        self.login_action = LoginAction(driver)

    def login_bus(self, username, password):
        self.login_action.input_username(username)
        self.login_action.input_password(password)
        self.login_action.click_login()




