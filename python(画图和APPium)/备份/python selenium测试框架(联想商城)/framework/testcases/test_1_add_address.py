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

logger.info("test_1_add_address.py")

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
        self.page.click_item(self.loc_item_yetlogin)
        self.page = InfoPage(self.page)

        datas = {"name":generator.random_name(),"mobile":generator.random_phone_number(),
                 "phone":generator.random_phone_number(),"add":generator.random_address(),
                 "mail":generator.random_email()}
        self.page.add_address(datas)
