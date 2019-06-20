# -*- coding:utf-8 -*-
# __author__ = 'lenovo'

import os
import unittest
from utils.generator import generator
from utils.log import logger
from utils.config import Config, DATA_PATH,REPORT_PATH
from selenium.webdriver.common.by import By
from common.lenovo_main_page import LenovoMainPage
from common.item_page import ItemPage
from common.shopcart_page import ShopcartPage

logger.info("test_2_purchase.py")

class Test(unittest.TestCase):
    URL = Config().get('URL')
    loc_item_item1 =  (By.XPATH, '//li[contains(@latag, "100715")]/a')

    def setUp(self):
        self.page = LenovoMainPage(browser_type='ie').get(self.URL, maximize_window=False)
        pass

    def tearDown(self):
        self.page.quit()
        pass

    def test(self):
        #上层li可以用click()事件 ：不稳定
        #内层a可以用send_keys(Keys.ENTER)事件：稳定
        self.page.click_item(self.loc_item_item1)

        self.page = ItemPage(self.page)
        self.page.switch_window()
        self.page.wait_loading()
        self.page.maximize()
        self.page.purchase()

        self.page = ShopcartPage(self.page)
        self.page.wait_loading()
        #找到控件说明成功，找不到失败
        result = self.page.deleteItem()

        self.assertEqual(result, 1, "删除购物车失败！")
        pass
