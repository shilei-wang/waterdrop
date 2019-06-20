# -*- coding:utf-8 -*-
# __author__ = 'lenovo'
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from browser import Browser
import time

class InfoPage(Browser):

    loc_item_yetlogin =  (By.XPATH, '//div[contains(@class, "yetlogin")]/a') #登录以后 按钮会从loginbtn 变成 yetlogin
    loc_item_address =  (By.XPATH, '//a[contains(@mcode, "f212417cda71")]')
    loc_item_new_address =  (By.XPATH, u'//a[contains(@title, "新增收货地址")]')
    loc_item_name =  (By.XPATH, '//input[contains(@id, "name")]')
    loc_item_mobile =  (By.XPATH, '//input[contains(@id, "mobile")]')
    loc_item_phone =  (By.XPATH, '//input[contains(@id, "phone")]')
    loc_item_goodsStreet =  (By.XPATH, '//input[contains(@id, "goodsStreet")]')
    loc_item_mail =  (By.XPATH, '//input[contains(@id, "mail")]')
    loc_item_province =  (By.XPATH, '//select[contains(@id, "goodsProvince")]')
    loc_item_city =  (By.XPATH, '//select[contains(@id, "goodsCity")]')
    loc_item_county =  (By.XPATH, '//select[contains(@id, "goodsCounty")]')
    loc_item_submit =  (By.XPATH, u'//input[contains(@value, "保存收货地址")]')
    loc_item_address_list =  (By.XPATH, '//div[contains(@class, "address_list")]/ul/li/em')

    def __init__(self, page=None, browser_type='chrome'):
        if page:
            #这个实例里面唯一 一个重要对象就是这个driver，page之间传递的也就是这个driver
            self.driver = page.driver
        else:
            #如果初次创建 调用父类生成driver
            super(InfoPage, self).__init__(browser_type)

    def click_item(self,item):
        #self.wait_element(item).send_keys(Keys.ENTER)
        time.sleep(3)

    def wait_loading(self):
        self.wait_element(self.loc_item_address)

    #添加成功后页面没有任何变化(数据可能会被查在后面的页)，所以只能返回1，
    #不是所有的case都可以显式验证，这个也是自动化的不足之处,但是这里做压力测试，负载测试很不错
    def add_address(self, datas):
        #{"name":"shelwin","mobile":"13866668888","phone":"58542974","add":"road haha","mail":"shelwin@hotmail.com"}
        self.wait_element(self.loc_item_address).send_keys(Keys.ENTER)
        self.wait_element(self.loc_item_new_address).send_keys(Keys.ENTER)
        self.wait_element(self.loc_item_name).send_keys(datas["name"])
        self.wait_element(self.loc_item_mobile).clear()
        self.wait_element(self.loc_item_mobile).send_keys(datas["mobile"])
        self.wait_element(self.loc_item_phone).send_keys(datas["phone"])
        #这3个暂时不用参数化
        Select(self.wait_element(self.loc_item_province)).select_by_value("090")
        Select(self.wait_element(self.loc_item_city)).select_by_index(3)
        Select(self.wait_element(self.loc_item_county)).select_by_index(2)
        self.wait_element(self.loc_item_goodsStreet).send_keys(datas["add"])
        self.wait_element(self.loc_item_mail).send_keys(datas["mail"])
        self.wait_element(self.loc_item_submit).send_keys(Keys.ENTER)

        time.sleep(3)
        #有条件的话可以读出列表，返回列表再check一遍

        return 1



        #上层li可以用click()事件 ：不稳定
        #内层a可以用send_keys(Keys.ENTER)事件：稳定
        # link.send_keys(Keys.ENTER)
        #
        # self.switch_window()
        # self.maximize()
        # time.sleep(3)