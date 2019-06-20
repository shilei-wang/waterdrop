# -*- coding:utf-8 -*-
# __author__ = 'lenovo'
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from browser import Browser
import time

class LenovoMainPage(Browser):
    # xxx.find_element_by_xpath("//标签[@属性==‘属性值’]")
    # driver.find_element_by_xpath(str).click("//input[@id='su']")

    loc_item_top_loginbtn = (By.XPATH, '//li[contains(@class, "top_loginbtn")]/a')
    loc_item_logintitle =  (By.XPATH, '')
    loc_item_account =  (By.XPATH, '//input[contains(@class, "account")]')
    loc_item_pwd =  (By.XPATH, '//input[contains(@class, "pwd")]')
    loc_item_autoLogin =  (By.XPATH, '//input[contains(@latag, "autologin")]')
    loc_item_submit =  (By.XPATH, '//a[contains(@class, "submit")]')
    loc_item_error =  (By.XPATH, '//p[contains(@class, "error-msg")]')
    loc_item_yetlogin =  (By.XPATH, '//div[contains(@class, "yetlogin")]/a') #登录以后 按钮会从loginbtn 变成 yetlogin


    loc_item_1 = (By.XPATH, '//li[contains(@latag, "96593")]/a')

    def __init__(self, page=None, browser_type='chrome'):
        if page:
            #这个实例里面唯一 一个重要对象就是这个driver，page之间传递的也就是这个driver
            self.driver = page.driver
        else:
            #如果初次创建 调用父类生成driver
            super(LenovoMainPage, self).__init__(browser_type)


    # 如果子类没有定义自己的初始化函数，父类的初始化函数会被默认调用；
    # 如果子类定义了自己的初始化函数，而在子类中没有显示调用父类的初始化函数，则父类的属性不会被初始化
    # 如果子类定义了自己的初始化函数，在子类中显示调用父类，子类和父类的属性都会被初始化

    # #这里定义找到后的动作
    # def search(self, kw):
    #     """搜索功能"""
    #     self.find_element(*self.loc_search_input).send_keys(kw)
    #     self.find_element(*self.loc_search_button).click()

    def click_item(self,item):
        self.wait_element(item).send_keys(Keys.ENTER)
        time.sleep(2)

    def login(self, user, pwd):
        self.wait_element(self.loc_item_top_loginbtn).send_keys(Keys.ENTER)

        self.wait_element(self.loc_item_account).send_keys(user)
        self.find_element(*self.loc_item_pwd).send_keys(pwd)
        self.find_element(*self.loc_item_autoLogin).click()
        self.find_element(*self.loc_item_submit).send_keys(Keys.ENTER)

        #这里强制等待和智能等待要组合使用
        time.sleep(2)
