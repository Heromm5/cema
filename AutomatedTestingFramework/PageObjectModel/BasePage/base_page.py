from selenium import webdriver

# 定义页面的基础类，所有的页面都需要继承这个基础类
class BasePage(object):

  # 初始化基础类
  def __init__(self, driver):
    self.driver = driver

  # 访问url
  def visit(self):
    self.driver.maximize_window()
    self.driver.get(self.url)

  # 元素定位
  def element_locator(self, locator):
    return self.driver.find_element(*locator)

  # 输入
  def input(self, locator, txt):
    self.element_locator(locator).send_keys(txt)

  # 点击
  def click(self, locator):
    self.element_locator(locator).click()

  # 关闭
  def quit_browser(self):
    self.driver.quit()