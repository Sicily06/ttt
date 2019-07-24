''' 测试 HTMLTestRunnner（HTML 测试报告）'''
from selenium import webdriver
import unittest
from HTMLTestRunner import HTMLTestRunner

class Baidu(unittest.TestCase):
    '''百度搜索测试'''

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.base_url = "http://www.baidu.com/"

    def test_baidu_search(self):
        '''搜索关键字 HTML'''
        driver = self.driver
        driver.get(self.base_url)
        driver.find_element_by_id("kw").clear()
        driver.find_element_by_id("kw").send_keys("HTML")
        driver.find_element_by_id("su").click()

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':

    testunit = unittest.TestSuite()
    testunit.addTest(Baidu("test_baidu_search"))

    # 报告存放
    fp = open('./result.html','wb')
    runner = HTMLTestRunner(fp, title='百度搜索测试报告',description='用例执行情况：')

    runner.run(testunit)    # 运行测试用例
    fp.close()         # 关闭文件报告

