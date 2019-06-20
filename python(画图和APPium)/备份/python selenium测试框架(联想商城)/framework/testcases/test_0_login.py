# -*- coding:utf-8 -*-
# __author__ = 'lenovo'

import os
import unittest
from utils.generator import generator
from utils.log import logger
from utils.config import Config, DATA_PATH,REPORT_PATH
from selenium.webdriver.common.by import By
from common.lenovo_main_page import LenovoMainPage
from common.info_page import InfoPage


logger.info("test_0_login.py")

class Test(unittest.TestCase):
    URL = Config().get('URL')
    loc_item_yetlogin =  (By.XPATH, '//div[contains(@class, "yetlogin")]/a')

    def setUp(self):
        self.page = LenovoMainPage(browser_type='ie').get(self.URL, maximize_window=False)
        pass

    def tearDown(self):
        self.page.quit()
        pass

    #@unittest.skip("")
    def test(self):
        #主页面登录
        self.page.login("13817968590", "abcd1234")
        #点击“用户”按钮
        self.page.click_item(self.loc_item_yetlogin)

        self.page = InfoPage(self.page)
        self.page.wait_loading()
        #获取新页面的title
        title = self.page.get_title()

        self.assertEqual(title.find(u"个人中心"), 0, "验证登录失败！")





