import json
import unittest
from parameterized import parameterized
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from page.add_team_page import AddTeamBusiness
from page.login_page import LoginBusiness
from untils import DriverUntil



def get_add_team_data(filename, function):
    with open("../data/%s.json" %filename, "rb") as f:
        list = []
        data = json.load(f)[function]
        for i in data.values():
            list.append((i.get("team_name"), i.get("team_name_all"), i.get("team_image"), i.get("team_builder"), i.get("team_yunying"), i.get("team_office_address"), i.get("team_connecter"), i.get("team_phone"), i.get("team_introduce"), i.get("assert_info")))
    return list

#团队运营人员为空数据
def get_team_yunying_is_null(function):
    with open("../data/add_team_error.json", "rb") as f:
        list = []
        data = json.load(f)[function]
        for i in data.values():
            list.append((i.get("team_name"), i.get("team_name_all"), i.get("team_image"), i.get("team_builder"), i.get("team_office_address"), i.get("team_connecter"), i.get("team_phone"), i.get("team_introduce"), i.get("assert_info")))
    return list






class AddTeamCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = DriverUntil.get_driver()
        cls.add_team_business = AddTeamBusiness(cls.driver)
        cls.login_business = LoginBusiness(cls.driver)
        cls.driver.get("http://47.102.168.233:8880/")
        cls.login_business.login_bus("admin", "123456")

    @classmethod
    def tearDownClass(cls) -> None:
        DriverUntil.quit_driver()

    def setUp(self) -> None:
        self.driver.get("http://47.102.168.233:8880/")



    # @parameterized.expand(get_add_team_data("add_team_data", "add_team_error"))
    # def test_add_team_error(self, team_name, team_name_all, image_url, team_builder, team_yunying, team_office, team_connecter, team_phone, team_introduce, assert_info):
    #     self.add_team_business.add_team(team_name, team_name_all, image_url, team_builder, team_yunying, team_office, team_connecter, team_phone, team_introduce)
    #     try:
    #         assert_ele = WebDriverWait(self.driver, 5, 1).until(lambda x: x.find_element(By.XPATH, "/html/body/div[7]/p"))
    #     except Exception as e:
    #         assert_ele = WebDriverWait(self.driver, 5, 1).until(lambda x: x.find_element(By.XPATH, '//*[@id="app"]/div[3]/div/div[1]/span'))
    #         self.assertEqual(assert_info, assert_ele.text)
    #     else:
    #         self.assertEqual(assert_info, assert_ele.text)

    @parameterized.expand(get_add_team_data("add_team_data", "add_team_success"))
    def test_add_team_success(self, team_name, team_name_all, image_url, team_builder, team_yunying, team_office, team_connecter, team_phone, team_introduce, assert_info):
        self.add_team_business.add_team(team_name, team_name_all, image_url, team_builder, team_yunying, team_office, team_connecter, team_phone, team_introduce)
        try:
            assert_ele = WebDriverWait(self.driver, 5, 1).until(lambda x: x.find_element(By.XPATH, "/html/body/div[7]/p"))
        except Exception as e:
            assert_ele = WebDriverWait(self.driver, 5, 1).until(lambda x: x.find_element(By.XPATH, '//*[@id="app"]/div[3]/div/div[1]/span'))
            self.assertEqual(assert_info, assert_ele.text)
        else:
            self.assertEqual(assert_info, assert_ele.text)



    # @parameterized.expand(get_team_yunying_is_null("team_yunying"))
    # def test_team_yunying_is_null(self, team_name, team_name_all, image_url, team_builder, team_office, team_connecter, team_phone, team_introduce, assert_info):
    #     self.add_team_business.team_yunying_is_null(team_name, team_name_all, image_url, team_builder, team_office, team_connecter, team_phone, team_introduce)
    #     try:
    #         assert_ele = WebDriverWait(self.driver, 5, 1).until(lambda x: x.find_element(By.XPATH, "/html/body/div[7]/p"))
    #     except Exception as e:
    #         assert_ele = WebDriverWait(self.driver, 5, 1).until(lambda x: x.find_element(By.XPATH, '//*[@id="app"]/div[3]/div/div[1]/span'))
    #         self.assertEqual(assert_info, assert_ele.text)
    #     else:
    #         self.assertEqual(assert_info, assert_ele.text)
    #
    # @parameterized.expand(get_add_team_data("add_team_data", "add_team_success"))
    # def test_team_date_is_null(self, team_name, team_name_all, image_url, team_builder, team_yunying, team_office, team_connecter, team_phone, team_introduce, assert_info):
    #     self.add_team_business.team_date_is_null(team_name, team_name_all, image_url, team_builder, team_yunying, team_office, team_connecter, team_phone, team_introduce)
    #     try:
    #         assert_ele = WebDriverWait(self.driver, 5, 1).until(lambda x: x.find_element(By.XPATH, "/html/body/div[7]/p"))
    #     except Exception as e:
    #         assert_ele = WebDriverWait(self.driver, 5, 1).until(lambda x: x.find_element(By.XPATH, '//*[@id="app"]/div[3]/div/div[1]/span'))
    #         self.assertEqual(assert_info, assert_ele.text)
    #     else:
    #         self.assertEqual(assert_info, assert_ele.text)
    #
    # @parameterized.expand(get_add_team_data("add_team_data", "add_team_success"))
    # def test_team_service_is_null(self, team_name, team_name_all, image_url, team_builder, team_yunying, team_office, team_connecter, team_phone, team_introduce, assert_info):
    #     self.add_team_business.team_service_is_null(team_name, team_name_all, image_url, team_builder, team_yunying, team_office, team_connecter, team_phone, team_introduce)
    #     try:
    #         assert_ele = WebDriverWait(self.driver, 5, 1).until(lambda x: x.find_element(By.XPATH, "/html/body/div[7]/p"))
    #     except Exception as e:
    #         assert_ele = WebDriverWait(self.driver, 5, 1).until(lambda x: x.find_element(By.XPATH, '//*[@id="app"]/div[3]/div/div[1]/span'))
    #         self.assertEqual(assert_info, assert_ele.text)
    #     else:
    #         self.assertEqual(assert_info, assert_ele.text)



if __name__ == "__main__":
    unittest.main()




