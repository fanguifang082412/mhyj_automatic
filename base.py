from selenium.webdriver.support.wait import WebDriverWait
from untils import DriverUntil




class Base:
    def get_element(self, ele_feature):
        ele = WebDriverWait(DriverUntil.get_driver(), 15, 1).until(lambda x: x.find_element(*ele_feature))
        return ele



# def get_element1(ele_feature):
#     try:
#         ele = WebDriverWait(DriverUntil.get_driver(), 5, 1).until(lambda x: x.find_element(*ele_feature))
#
#     except Exception as e:
#         return None
#     else:
#         return ele
