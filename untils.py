import unittest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


class DriverUntil:
    __driver = None

    @classmethod
    def get_driver(cls):
        if cls.__driver is None:
            cls.__driver = webdriver.Chrome()
            cls.__driver.maximize_window()
        return cls.__driver

    @classmethod
    def quit_driver(cls):
        if cls.__driver:
            cls.__driver.quit()
            cls.__driver = None



def assert_demo(self, expect, fact):
    self.assertEqual(expect, fact)























