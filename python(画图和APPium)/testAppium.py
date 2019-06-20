# -*- coding:utf-8 -*-
# __author__ = 'QC'

import os
import unittest
from appium import webdriver
from time import sleep
from appium.webdriver.common.touch_action import TouchAction


#设置路径信息
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)



class LoginAndroidTests(unittest.TestCase):
    def setUp(self):
        #初始化测试平台
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '7.0.9.0'   #Android版本
        desired_caps['deviceName'] = 'ac164a28'#告诉appium 夜神的地址
        desired_caps['appPackage'] = 'ai.bianjie.rainbow.dev'#包名
        desired_caps['appActivity'] = 'ai.bianjie.rainbow.dev.MainActivity'#activity名称
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)#连接appium 4723是appium

    def tearDown(self):
        self.driver.quit()
        print("teardown")

    def getSize(self):
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        return (x, y)

    def swipeUp(self, t):
        l = self.getSize()
        x1 = int(l[0] * 0.5)    #x坐标
        y1 = int(l[1] * 0.75)   #起始y坐标
        y2 = int(l[1] * 0.25)   #终点y坐标
        self.driver.swipe(x1, y1, x1, y2,t)



    def test(self):
        print("start test...")

        #判断是否安装爱壁纸APP
        exist = self.driver.is_app_installed("ai.bianjie.rainbow.dev")
        if exist:
            print("start test...")

            sleep(6)
            self.driver.find_element_by_name("下次再说").click()
            sleep(3)
            self.driver.find_element_by_name("我").click()
            sleep(2)
            self.driver.find_element_by_name("关于").click()
            sleep(2)
            self.driver.find_element_by_name("服务协议").click()
            sleep(2)




            self.find_PrivacyPolicy()






            sleep(10)

            """
            self.driver.find_element_by_name("导入钱包").click()
            sleep(3)
            self.driver.find_element_by_name("请输入助记词（按空格分隔）").send_keys("While there is a life, then there is a hope!")
            sleep(3)
            self.driver.find_element_by_name("钱包名称").send_keys("Rich people do not care")
            sleep(3)
            self.driver.find_element_by_name("密码（不少于9位，数字与字母的组合）").set_text("12345678")
            sleep(3)
            self.driver.find_element_by_name("确认密码").set_text("12345678")
            sleep(3)
            self.driver.find_element_by_name("H0F5+26D7KN5kjt04smM7ioct2h6OpYEexftXgAEA9iwY389i7NwAAAAASUVORK5CYII=").click()


            sleep(15)

            #点击主页
            self.driver.find_element_by_id("com.lovebizhi.wallpaper:id/nav_home_ll").click()
            sleep(8)

            #点击某一壁纸图片，注意这里是elements list
            self.driver.find_elements_by_id("com.lovebizhi.wallpaper:id/thumb")[8].click()
            sleep(8)

            # 点击设置壁纸
            self.driver.find_element_by_id("com.lovebizhi.wallpaper:id/set_wp_btn").click()
            sleep(5)

            self.driver.find_element_by_id("com.lovebizhi.wallpaper:id/set_wp_btn").click()
            sleep(5)
            """
        else:
            print("没安装")
            sleep(30)


if __name__ == '__main__':
    suite =unittest.TestLoader().loadTestsFromTestCase(LoginAndroidTests)
    unittest.TextTestRunner(verbosity=2).run(suite)

