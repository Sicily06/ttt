# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
import HTMLTestRunner
import fun


class Login():
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "http://daily.chinacaring.com/w/man/index"

    def test_HB(self):
        '''睿恒项目管理登录页面'''
        driver = self.driver
        driver.get(self.base_url)
        driver.add_cookie({'name':'proj_mUserNm','value':'zhanghh@chinacaring.com'})
        driver.add_cookie({'name': 'proj_mPassword', 'value': 'Chinacaring_'})
        # driver.add_cookie({'name': 'JSESSIONID', 'value': '9DEF5066D183617DC3B921C8DE50C65E'})   # 验证码可变

        driver.get(self.base_url)

        time.sleep(1)

        txt = driver.find_element_by_xpath('/html/body/div[1]/div/div/dl/dt/span').text
        if txt == '张海红(普通成员)':
            print('登录成功！')


'''
        try:
            driver.find_element_by_id('email').send_keys('zhanghh@chinacaring.com')
            driver.find_element_by_id('password').send_keys('Zhh123456')
            driver.find_element_by_id('button').click()   # 这边刻意定位出错，走下面的except分支
        except:
            # 这里的图片可以使用成变量
            driver.get_screenshot_as_file(r".\erro.png")  # 若上面不能顺利执行，则会截图失败界面
'''


Login().test_HB()


