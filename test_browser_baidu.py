# -*- coding: utf-8 -*-
# @Author: Kid
# @FileName: test_browser_baidu.py
# @Date: 2021/9/20  21:02
from time import sleep

from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class TestBrowser():
    def setup(self):
        des_caps = {
            'platformName': 'android',
            'platformVersion': '6.0',
            # 'platformVersion': '5.1.1',           # 夜神
            # 'browserName': 'Chrome',
            'browserName': 'Browser',       # 这是 安卓手机 自带的 浏览器，找版本时注意不是找 chrome的版本
            'noReset': True,
            'deviceName': '127.0.0.1:7555',
            # 'deviceName': '127.0.0.1:62001',   # 夜神
            'chromedriverExecutable': 'Users\Administrator\google_chrome\driver_version\chromedriverv2.24.exe'
        }
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", des_caps)
        self.driver.implicitly_wait(10)

    def teardown(self):
        self.driver.quit()

    def test_browser(self):
        self.driver.get("http://m.baidu.com")
        sleep(5)
