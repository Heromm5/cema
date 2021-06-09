from selenium.webdriver.common.by import By
from selenium import webdriver
from AutomatedTestingFramework.PageObjectModel.BasePage.base_page import BasePage


class LoginPage(BasePage):
    # 核心元素
    url = 'http://39.98.138.157/shopxo/index.php?s=/index/user/logininfo.html'
    user = (By.NAME, 'accounts')
    password = (By.NAME, 'pwd')
    login_button = (By.XPATH, '/html/body/div[4]/div/div[2]/div[2]/form/div[3]/button')

    # 核心业务流
    def login(self, username, password):
        self.visit()
        self.input(self.user, username)
        self.input(self.password, password)
        self.click(self.login_button)

# 调试代码
if __name__ == '__main__':
    driver = webdriver.Chrome()
    username = 'xuzhu666'
    password = '123456'
    lp = LoginPage(driver)
    lp.login(username, password)