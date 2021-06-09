import unittest
from time import sleep

from ddt import data, ddt, unpack
from ..PageObject.index_page import *


@ddt
class PageObjectUnit(unittest.TestCase):
  # 前置条件
  def setup(self) -> None:
    self.tk = TestKeyWords('chrome', 'http://www.baidu.com')

  # 后置条件
  def tearDown(self) -> None:
    self.tk.quit_browser()

  # 测试用例1
  @data(['NBA', 'id'], ['OKC', 'id'])
  @unpack
  def test_1(self, input_value, locator):
    self.tk.input_text(input_value, locator, 'kw')
    self.tk.click_element('id', 'su')
    sleep(3)

  # def test_2(self):
  #   self.tk.input_text('OKC', 'id', 'kw')
  #   self.tk.click_element('id', 'su')
  #   sleep(3)

if __name__ == '__main__':
  unittest.main()
