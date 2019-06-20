# -*- coding: utf-8 -*- #

import os
import unittest
from utils.config import Config, DATA_PATH,REPORT_PATH
from utils.file_reader import ExcelReader
from utils.mail import Email
from utils.generator import generator
from selenium.webdriver.common.by import By

from common.lenovo_main_page import LenovoMainPage
from common.info_page import InfoPage
