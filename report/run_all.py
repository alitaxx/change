"""

"""
import time
import unittest
from BeautifulReport import BeautifulReport
from setting import REPORT_PATH, CASE_PATH

file_name=time.strftime('%Y-%m-%d-%H-%M-%S') #文件名

discover=unittest.defaultTestLoader.discover(start_dir=CASE_PATH,
                                             pattern='test_l*.py')

BeautifulReport(discover).report(
    description='自动化报告',
    log_path=REPORT_PATH,
    filename=file_name)