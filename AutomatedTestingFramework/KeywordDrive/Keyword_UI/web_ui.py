'''
    关键字驱动封装类：
        1、提供所有的基础操作行为，封装为关键字
            元素定位、点击、输入、等待、切换句柄、切换iframe、悬停、断言
            。。。。。。
        2、定义驱动类的使用规范
'''
from selenium import webdriver

# 创建driver对象
def browser(type_):
    try:
        if type_ == 'Chrome':
            driver = webdriver.Chrome()
        else:
            driver = getattr(webdriver, type_)()
        return driver
    except Exception as e:
        print(e)
        return webdriver.Chrome()


class WebDemo:
    #driver = webdriver.Chrome()
    # 构造函数
    def __init__(self, type_):
        self.driver = browser(type_)

    # 访问Url
    def visit(self, url):
        self.driver.get(url)

    # 关闭浏览器
    def quit(self):
        self.driver.quit()

    # 元素定位
    def locator(self, name, value):
       return self.driver.find_element(name, value)

    # 输入
    def input_text(self, name, value, txt):
        self.locator(name, value).send_keys(txt)

    # 点击
    def click(self, name, value):
        self.locator(name, value).click()