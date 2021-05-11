# 调用安装好的Selenium模块

from selenium import webdriver
from time import sleep
import time

# 去掉黄条
option = webdriver.ChromeOptions()
option.add_argument('disable-infobars')

# 静默模式
option.add_argument('headless')

# 生成一个ChromeDriver
driver = webdriver.Chrome(chrome_options=option)
# 访问指定的URL
driver.get('http://www.baidu.com')

# 输入
driver.find_element_by_id('kw').send_keys('NBA')

# 点击
driver.find_element_by_id('su').click()

# 等待
sleep(2)

# 点击链接
driver.find_element_by_xpath('//*[@id="2"]/h3/a[1]').click()

time.implicitly_wait(5)

# 结束释放资源
driver.quit()