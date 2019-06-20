# -*- coding:utf-8 -*-
# __author__ = 'lenovo'

import time
import os
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from utils.config import DRIVER_PATH, REPORT_PATH
from utils.log import logger

CHROMEDRIVER_PATH = DRIVER_PATH + '\chromedriver.exe'
IEDRIVER_PATH = DRIVER_PATH + '\IEDriverServer.exe'

#这里3个主流的浏览器的对象
TYPES = {'firefox': webdriver.Firefox, 'chrome': webdriver.Chrome, 'ie': webdriver.Ie}
#对应的driver地址
EXECUTABLE_PATH = {'firefox': u'没有下载', 'chrome': CHROMEDRIVER_PATH, 'ie': IEDRIVER_PATH}


class UnSupportBrowserTypeError(Exception):
    pass


class Browser(object):
    def __init__(self, browser_type='chrome'):
        self._type = browser_type.lower()
        if self._type in TYPES:
            self.browser = TYPES[self._type]
        else:
            raise UnSupportBrowserTypeError(u'仅支持%s!' % ', '.join(TYPES.keys()))
        self.driver = None

    def get(self, url, maximize_window=True, implicitly_wait=30):
        self.driver = self.browser(executable_path=EXECUTABLE_PATH[self._type])
        self.driver.get(url)

        #会报错（如：Chrome浏览器）浏览器版本太高，导致不兼容。
        #if maximize_window:
        #self.driver.maximize_window()

        #隐式等待，也叫智能等待，是 webdirver 提供的一个超时等待。等待一个元素被发现，或一个命令完成。
        #如果超出了设置时间30秒的则抛出异常，并不是等30秒 。
        self.driver.implicitly_wait(implicitly_wait)
        return self

    def save_screen_shot(self, name='screen_shot'):
        # day = time.strftime('%Y%m%d', time.localtime(time.time()))
        # screenshot_path = REPORT_PATH + '\screenshot_%s' % day
        # if not os.path.exists(screenshot_path):
        #     os.makedirs(screenshot_path)
        #
        # tm = time.strftime('%H%M%S', time.localtime(time.time()))
        # #浏览器截图：driver.save_screenshot
        # screenshot = self.driver.save_screenshot(screenshot_path + '\\%s_%s.png' % (name, tm))
        return screenshot

    #这里定义找
    def find_element(self, *args):
        return self.driver.find_element(*args)

    def find_elements(self, *args):
        return self.driver.find_elements(*args)

    def wait_element(self, args, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(args))

    #判断元素存在一定要catch exception
    #正常来说存在找到马上返回， 不存在的话就会阻塞造成超时， 而且cases 也会失败 。这不是我们想要的。
    #这里也解答了我的疑惑， case运行时 如果任何一个预期的元素找不到 都会返回错误case fail
    #所以尽量判断元素存在，速度快。不存在速度慢。
    def is_element_exist(self,args):
        try:
            self.driver.find_element_by_xpath(args)
            return True
        except NoSuchElementException as msg:
            # 如果不存在，会等待一段时间到这里
            return False
        else:
            return True


    def switch_window(self):
        #等到窗口数大于1
        WebDriverWait(self.driver, 10).until(lambda x: len(self.driver.window_handles)>1)

        windows = self.driver.window_handles
        for window in windows:# 切换窗口
            if window !=  self.driver.current_window_handle:
                self.driver.close() # 关闭第一个窗口
                self.driver.switch_to.window(window) #切换到第二个窗口
                break

        logger.info("switch to new window : "+ self.driver.title)


    def close(self):
        self.driver.close()
        pass

    def quit(self):
        self.driver.quit()
        pass

    def maximize(self):
        self.driver.maximize_window()
        pass

    def get_title(self):
        return self.driver.title