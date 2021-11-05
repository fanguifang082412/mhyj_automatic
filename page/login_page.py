from selenium.webdriver.common.by import By
from base import Base
from untils import DriverUntil




class LoginPage(Base):

    def __init__(self):
        self.username = By.XPATH, "//form[@class='m-t']/div/input[@placeholder='用户名']"
        self.password = By.XPATH, "//form[@class='m-t']/div/input[@placeholder='密码']"
        self.login = By.XPATH, "//button[@type='submit']"

    def get_username(self):
        return self.get_element(self.username)

    def get_password(self):
        return self.get_element(self.password)

    def get_login(self):
        return self.get_element(self.login)


class LoginAction:
    def __init__(self):
        self.login_page = LoginPage()

    def input_username(self, username):
        self.login_page.get_username().send_keys(username)

    def input_password(self, password):
        self.login_page.get_password().send_keys(password)

    def click_login(self):
        self.login_page.get_login().click()



class LoginBusiness:
    def __init__(self):
        self.login_action = LoginAction()

    def login_bus(self, username, password):
        self.login_action.input_username(username)
        self.login_action.input_password(password)
        self.login_action.click_login()




