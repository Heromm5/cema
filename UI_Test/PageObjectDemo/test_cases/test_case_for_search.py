from time import sleep
from selenium import webdriver
import unittest
from ddt import ddt, file_data, data
import warnings

from UI_Test.PageObjectDemo.PageObject.index_page import IndexPage
from UI_Test.PageObjectDemo.PageObject.login_page import LoginPage
# 测试用例的设计



@ddt
class TestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        # warnings.simplefilter('ignore', ResourceWarning)
        cls.driver = webdriver.Chrome()
        cls.lp = LoginPage(cls.driver)
        cls.ip = IndexPage(cls.driver)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

    @file_data('../data/user.yaml')
    def test_1_login(self, username, password):
        txt = self.lp.login(username, password)
        sleep(3)

    @data('手机', '衣服', '电脑')
    def test_2_search(self, txt):
        self.ip.search(txt)
        sleep(3)


if __name__ == '__main__':
    unittest.main()