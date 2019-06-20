# -*- coding:utf-8 -*-
# __author__ = 'lenovo'
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from browser import Browser
import time

class ItemPage(Browser):
    loc_item_1jgm = (By.XPATH, '//button[contains(@id, "ljgm")]')
    loc_item_jrgwc = (By.XPATH, '//button[contains(@id, "jrgwc")]')
    loc_item_pj_1 = (By.XPATH, '//div[contains(@data-code, "94139")]')
    loc_item_pj_2 = (By.XPATH, '//div[contains(@data-code, "93523")]')
    loc_item_pj_3 = (By.XPATH, '//div[contains(@data-code, "51452")]')
    loc_item_pj_4 = (By.XPATH, '//div[contains(@data-code, "1000247")]')
    loc_item_pj_5 = (By.XPATH, '//div[contains(@data-code, "1000248")]')
    loc_item_pj_6 = (By.XPATH, '//div[contains(@data-code, "1000249")]')

    def __init__(self, page=None, browser_type='chrome'):
        if page:
            #这个实例里面唯一 一个重要对象就是这个driver，page之间传递的也就是这个driver
            self.driver = page.driver
        else:
            #如果初次创建 调用父类生成driver
            super(ItemPage, self).__init__(browser_type)

    def click_item(self,item):
        self.wait_element(item).send_keys(Keys.ENTER)
        time.sleep(2)

    def wait_loading(self):
        self.wait_element(self.loc_item_1jgm)


    def purchase(self):
        self.wait_element(self.loc_item_pj_1).click()
        time.sleep(0.5) #可以0.5
        self.wait_element(self.loc_item_pj_2).click()
        time.sleep(0.5)
        self.wait_element(self.loc_item_pj_3).click()
        time.sleep(0.5)
        self.wait_element(self.loc_item_pj_4).click()
        time.sleep(0.5)
        self.wait_element(self.loc_item_pj_6).click()
        time.sleep(0.5)
        self.wait_element(self.loc_item_pj_5).click()
        time.sleep(0.5)

        self.wait_element(self.loc_item_jrgwc).send_keys(Keys.ENTER)
        time.sleep(3)




