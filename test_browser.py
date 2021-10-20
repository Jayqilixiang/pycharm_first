# -*- coding: utf-8 -*-
# @Author: Kid
# @FileName: test_browser.py
# @Date: 2021/9/19  20:46

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
            # 'platformVersion': '5.1.1',
            # 'browserName': 'Chrome',
            'browserName': 'Browser',       # 这是 安卓手机 自带的 浏览器，找版本时注意不是找 chrome的版本
            'noReset': True,
            'deviceName': '127.0.0.1:7555',
            # 'deviceName': '127.0.0.1:62001',
            'chromedriverExecutable': 'C:\google_chrome\driver_version\chromedriverv2.24.exe'   # 指定路径，需与browser版本一致
        }
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", des_caps)
        self.driver.implicitly_wait(10)

    def teardown(self):
        self.driver.quit()

    def test_browser(self):
        self.driver.get("http://m.baidu.com")
        sleep(5)
        self.driver.find_element_by_class_name('fake-placeholder').click()  # 点击百度搜索框
        self.driver.find_element_by_id('index-kw').send_keys('爱在哈佛')
        search_locator = (By.ID, 'index-bn')   # 由于是 页面的，不能用 mobile by，  --- 是个元组
        WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(search_locator))  # 要求里面是元组
        self.driver.find_element(*search_locator).click()  # 加了个 * ， 解元组操作. --- 注意这里不是调用find.. id(),不然报错---关键字多了一个