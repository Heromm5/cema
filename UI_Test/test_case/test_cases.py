
from BiliBiliLearning.cemaxueyuan.pageObject.search_page import SearchPage
import unittest
from selenium import webdriver
from time import sleep

from ddt import data, ddt, unpack

@ddt
class TestCases(unittest.TestCase):
  def setUp(self) -> None:
    driver = webdriver.Chrome()
    self.sp = SearchPage(driver)

  def tearDown(self) -> None:
    self.sp.quit_browser()

  @ddt(['http://www.baidu.com', 'NBA'], ['http://www.baidu.com', 'OKC'])
  @unpack
  def test_1(self, url, text):
    self.sp.check(url, text)
    sleep(2)

if __name__ == '__main__':
  unittest.main()