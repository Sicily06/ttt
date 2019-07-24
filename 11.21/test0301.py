# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
import HTMLTestRunner
import fun


class Baidu(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "http://www.baidu.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_baidu(self):
        '''百度'''
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_id("kw").send_keys("selenium")
        driver.find_element_by_id("su").click()

    def test_HB(self):
        '''睿恒项目管理登录页面'''
        driver = self.driver
        driver.get('http://daily.chinacaring.com/w/com/login')

        try:
            driver.find_element_by_id('email').send_keys('zhanghh@chinacaring.com')
            driver.find_element_by_id('password').send_keys('Zhh123456')
            driver.find_element_by_id('button555').click()   # 这边刻意定位出错，走下面的except分支
        except:
            # 这里的图片可以使用成变量
            driver.get_screenshot_as_file(r".\sss.png")  # 若上面不能顺利执行，则会截图失败界面

    def is_element_present(self, how, what):
        try:    # 异常处理
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False

        return True    # return语句只会执行1次，若是except里面执行了，这边就不会执行了

    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    testunit = unittest.TestSuite()
    testunit.addTest(Baidu("test_baidu"))
    testunit.addTest(Baidu("test_HB"))
    file_name = r'.\0301result.html'
    fp = open(file_name, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=fp,
        title='报告标题',
        description='报告描述')
    runner.run(testunit)
