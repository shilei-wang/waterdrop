# -*- coding:utf-8 -*-
# __author__ = 'lenovo'

"""
日志类。通过读取配置文件，定义日志级别、日志文件名、日志格式等。
一般直接把logger import进去
from utils.log import logger
logger.info('test log')
"""
import os
import logging
from logging.handlers import TimedRotatingFileHandler
from utils.config import LOG_PATH, Config

class Logger(object):
    def __init__(self, logger_name='framework'):
        self.logger = logging.getLogger(logger_name)
        self.logger.setLevel(logging.DEBUG)  #这里如果设置NOTSET 控制台会不输出

        c = Config().get('log')      #得到log的字典格式
        self.log_file_name = c.get('file_name') # 日志文件
        self.backup_count = c.get('backup')  # 保留的日志数量
        self.console_output_level = c.get('console_level') # 日志输出级别
        self.file_output_level = c.get('file_level')
        self.pattern = c.get('pattern')  # 日志输出格式
        self.formatter = logging.Formatter(self.pattern)


    def get_logger(self):
        if not self.logger.handlers: # 避免重复日志

            """
            添加两个句柄，一个输出日志到控制台，另一个输出到日志文件。
            两个句柄的日志级别可以不同
           """

            #第一个控制台输出，只输出级别INFO， DEBUG级别的不在这里输出，只在log文件里输出
            #Logging中有NOTSET < DEBUG < INFO < WARNING < ERROR < CRITICAL这几种级别，日志会记录设置级别以上的日志
            #self.logger.info("123")可以输出。 self.logger.debug("456")不可以输出。
            console_handler = logging.StreamHandler()
            console_handler.setFormatter(self.formatter)
            console_handler.setLevel(self.console_output_level) #级别在配置文件里 可以配置
            self.logger.addHandler(console_handler)

            #第二个文件输出，输出级别DEBUG （就是debug以上都输出 包括info）
            #每天重新创建一个日志文件，最多保留backup_count份
            file_handler = TimedRotatingFileHandler(filename=os.path.join(LOG_PATH, self.log_file_name),
                                                    when='D',  #天的单位
                                                    interval=1, #1天，每天重新创建一个日志文件
                                                    backupCount=self.backup_count, #最多5个备份
                                                    delay=True,
                                                    encoding='utf-8'
                                                    )
            file_handler.setFormatter(self.formatter)
            file_handler.setLevel(self.file_output_level)
            self.logger.addHandler(file_handler)
        return self.logger

logger = Logger().get_logger()