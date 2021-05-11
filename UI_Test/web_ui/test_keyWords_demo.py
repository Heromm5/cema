# 关键字驱动框架

from selenium import webdriver

class TestKeyWords(object):
  # 初始化
  def __init__(self, browser_type, url):
    self.driver = self.open_browser(browser_type)
    self.driver.get(url)

  # 调用浏览器
  def open_browser(self, browser_type):
    if browser_type == 'chrome':
      driver = webdriver.Chrome()
      return driver
    elif browser_type == 'firefox':
      driver = webdriver.Firefox()
      return driver
    else:
      print('browser type error')

  # 定位元素
  def element_locate(self, locate_type, value):
    if locate_type == 'id':
      el = self.driver.find_element_by_id(value)
      return el
    elif locate_type == 'name':
      el = self.driver.find_element_by_name(value)
      return el
    elif locate_type == 'xpath':
      el = self.driver.find_element_by_xpath(value)
      return el

  # 输入
  def input_text(self, text, locate_type, value):
    self.element_locate(locate_type, value).send_keys(text)

  # 点击
  def click_element(self, locate_type, value):
    self.element_locate(locate_type, value).click()

  # 关闭
  def quit_browser(self):
    self.driver.quit()

if __name__ == '__main__':
  tk = TestKeyWords('chrome', 'http://www.baidu.com')
  tk.input_text('NBA', 'id', 'kw')
  tk.click_element('id', 'su')
  tk.quit_browser()
  
