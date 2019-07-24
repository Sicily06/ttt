'''中大的登录、登出函数封装'''
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait


class Login():

    def login(self , driver,username,password):
        driver.find_element_by_xpath("//*[@id='login']/div[1]/div[3]/div/input").clear()
        driver.find_element_by_xpath("//*[@id='login']/div[1]/div[3]/div/input").send_keys(username)
        driver.find_element_by_xpath("//*[@id='login']/div[1]/div[4]/div/input").clear()
        driver.find_element_by_xpath("//*[@id='login']/div[1]/div[4]/div/input").send_keys(password)
        driver.find_element_by_xpath("//*[@id='login']/div[1]/div[5]/div/div/span/span/i").click()
        time.sleep(1)
        driver.find_element_by_xpath("//*[@id='html']/body/div[3]/div[1]/div[1]/ul/li[2]").click()
        driver.find_element_by_xpath("// *[ @ id = 'login'] / div[1] / div[6] / button").click()

        '''判断是否登录成功'''
        # 方法1.等待页面加载出来,判断是否登录成功
        WebDriverWait(driver,10).until(lambda the_driver:driver.find_element_by_xpath("//*[@id='navigate']/section/section/header/div[1]/div").is_displayed())
        print("登录成功！")

        # 方法2.判断标签元素是否加载完全
        # time.sleep(3)
        # txt = driver.find_element_by_xpath("//*[@id='navigate']/section/section/header/div[1]/div").text
        # if (txt =='东南大学附属中大医院 MDT多学科会诊'):
            # print("登录成功！")

        # 方法3.判断是否有【登录成功】的message，这个控件3秒消失，所以不好定位位置
        # 暂未实现

    def logout(self,driver):
        # 鼠标悬停在【管理员】退出按钮
        position = driver.find_element_by_xpath("//*[@id='navigate']/section/section/header/div[2]/div[3]/span/span[1]")
        ActionChains(driver).move_to_element(position).perform()
        time.sleep(1)
        # popover组件加载出来后点击【退出登录】
        # 注意，这里不能直接用id定位，因为id是变化的，class又不是唯一的，所以用路径拼接，绝对路径（定位到第二个类）+相对路径
        driver.find_element_by_xpath("/html/body/ul[@class='el-dropdown-menu el-popper']/li[2]").click()
        time.sleep(1)
        # 操作alert弹窗,点击【确定】退出
        driver.find_element_by_xpath("//*[@id='html']/body/div[3]/div/div[3]/button[2]").click()
        time.sleep(1)
        # 判断是否退出（通过当前页面的url比较得出）
        except_url = "http://zdmdt.chinacaring.com:18082/1035/MDT/#/login"
        real_url = driver.current_url    # 获取当前页面的url
        if real_url == except_url:
            print("登出成功！")








