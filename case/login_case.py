import json
import time
import unittest
from parameterized import parameterized
from selenium.webdriver.common.by import By
import untils
from congfig.log import init_logging_config
from page.login_page import LoginBusiness
from untils import DriverUntil
import base




def get_login_data():
    with open("../data/login_data.json", encoding="utf-8") as f:
        list = []
        data = json.load(f)
        for dict in data.values():
            list.append((dict.get("username"), dict.get("password"), dict.get("assert_text")))

        return list





# init_logging_config()


class Login(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.base_ele = base.Base()
        cls.login_business = LoginBusiness()
        cls.driver = DriverUntil.get_driver()


    @classmethod
    def tearDownClass(cls) -> None:
        DriverUntil.quit_driver()

    def setUp(self) -> None:
        self.driver.get("http://47.102.168.233:8880/")

    @parameterized.expand(get_login_data())
    def test_login(self, username, password, assert_text):
        time.sleep(3)
        self.login_business.login_bus(username, password)
        time.sleep(3)
        try:
            assert_feature = By.XPATH, "/html/body/div/form/h4"
            assert_ele = self.base_ele.get_element(assert_feature)

        except Exception as e:
            assert_feature = By.XPATH, "//strong[contains(@class,'font-bold')]"
            assert_ele = self.base_ele.get_element(assert_feature)
            untils.assert_demo(self, assert_text, assert_ele.text)
            # self.assertEqual(assert_text, assert_ele.text)
        else:
            untils.assert_demo(self, assert_text, assert_ele.text)
            # self.assertEqual(assert_text, assert_ele.text)



if __name__ == "__main__":
    unittest.main()







