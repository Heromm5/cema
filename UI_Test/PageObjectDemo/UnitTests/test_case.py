import unittest
from time import sleep
from ddt import ddt, file_data, data, unpack
from selenium import webdriver

from UI_Test.PageObjectDemo.PageObject.index_page import IndexPage
from UI_Test.PageObjectDemo.PageObject.login_page import LoginPage

@ddt
class TestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome()
        cls.lp = LoginPage(cls.driver)
        cls.ip = IndexPage(cls.driver)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

    @file_data('../Data/user.yaml')
    def test_1_login(self, username, password):
        self.lp.login(username, password)
        sleep(3)

    @data('手机', '电脑')
    def test_2_index(self, txt):
        self.ip.search(txt)
        sleep(3)

if __name__ == '__main__':
    unittest.main()
