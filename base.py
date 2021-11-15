from selenium.webdriver.support.wait import WebDriverWait
from untils import DriverUntil




class HandleElement:
    def __init__(self, driver):
        self.driver = driver
    def get_element(self, ele_feature):
        ele = WebDriverWait(self.driver, 10, 0.5).until(lambda x: x.find_element(*ele_feature))
        return ele




