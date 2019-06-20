# -*- coding:utf-8 -*-
# __author__ = 'lenovo'
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from browser import Browser
import time

class ShopcartPage(Browser):
    loc_item_submit= (By.XPATH, '//a[contains(@id, "submit")]')
    loc_item_del_goods = (By.XPATH, '//a[contains(@latag, "100715")]') # css selector 写法 css = "a[latag*='100715']"
    loc_item_del_confirm = (By.XPATH, '//a[contains(@class, "btn now")]')
    loc_item_no_item = (By.XPATH, '//div[contains(@class, "bc_no_btn")]')

    xpath_item_del_goods =  '//a[contains(@latag, "100715")]'

    def __init__(self, page=None, browser_type='chrome'):
        if page:
            #这个实例里面唯一 一个重要对象就是这个driver，page之间传递的也就是这个driver
            self.driver = page.driver
        else:
            #如果初次创建 调用父类生成driver
            super(ShopcartPage, self).__init__(browser_type)

    def click_item(self,item):
        time.sleep(2)

    def wait_loading(self):
        self.wait_element(self.loc_item_submit)


    def deleteItem(self):
        self.wait_element(self.loc_item_del_goods).send_keys(Keys.ENTER)
        self.wait_element(self.loc_item_del_confirm).click()


        #self.wait_element(self.loc_item_no_item)
        # 判断元素存在要用try，否则不存在会报错
        # if self.is_element_exist(self.xpath_item_del_goods):
        #     return 0
        # else:
        #     return 1

        return 1








