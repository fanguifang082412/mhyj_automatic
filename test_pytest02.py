import pytest
import allure





@pytest.fixture()
def login_d():
    print("我是工厂函数")



# autouse=True, scope="function"

class TestDemo:
    # def setup(self):
    #     print("我是初始化函数")

    # def teardown(self):
    #     print("我是销毁函数")

    def test_fn(self, login_d):
        a = "hello"
        print("pytest练习1")
        assert "hello" == a

    def test_fn1(self, login_d):
        a = "hello"
        print("pytest练习2")
        assert "hello" == a
