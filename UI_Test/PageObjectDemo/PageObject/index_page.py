from selenium.webdriver.common.by import By
from selenium import webdriver
from UI_Test.PageObjectDemo.BasePage.base_page import BasePage


class IndexPage(BasePage):
    # 核心元素
    url = 'http://39.98.138.157/shopxo/index.php?s=/index/user/index.html'
    search_input = (By.NAME, 'wd')
    search_button = (By.ID, 'ai-topsearch')

    # 核心业务流
    def search(self, txt):
        self.visit()
        self.input(self.search_input, txt)
        self.click(self.search_button)

# 调试代码
if __name__ == '__main__':
    driver = webdriver.Chrome()
    txt = '手机'
    ip = IndexPage(driver)
    ip.search(txt)