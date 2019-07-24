'''调用登录的主方法'''
from selenium import webdriver

from pub_login import Login


class LoginTest():
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.get("https://zdmdt.chinacaring.com")   # 打开网址

    '''登录函数'''

    # 可以将登录的用户名&密码 放在csv文件里面读取
    def test(self):
        username = 'admin'
        password = 'admin111111'
        Login().login(self.driver, username, password)
        # self.driver.quit()    # 有无此行效果一样(python代码执行在python的虚拟机里面，程序跑完了就自动关闭了)

    '''登出函数'''

    def testlogout(self):
        self.test()  # 先执行登录(直接内部调用即可)
        Login().logout(self.driver)  # 执行登出
        # self.driver.quit()


'''用例执行'''
# LoginTest().test()    # 登录
LoginTest().testlogout()  # 登出
