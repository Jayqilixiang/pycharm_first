# -*- coding: utf-8 -*-
# @Author: Kid
# @FileName: test_webview_ApiDemo2.py
# @Date: 2021/9/21  13:08

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
            'appPackage': 'io.appium.android.apis',
            'appActivity': '.ApiDemos',
            # 'browserName': 'Browser',       # 这是 安卓手机 自带的 浏览器，找版本时注意不是找 chrome的版本
            'noReset': True,
            'deviceName': '127.0.0.1:7555',
            'chromedriverExecutable': 'C:\google_chrome\driver_version\chromedriverv2.24.exe'   # 指定路径
        }
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", des_caps)
        self.driver.implicitly_wait(10)

    def teardown(self):
        self.driver.quit()

    def test_webview(self):
        self.driver.find_element_by_accessibility_id("Views").click()    # 根据content-desc定位， Accessibility ID在Android上面就等同于contentDescription
        webview = "WebView"
        self.driver.find_element_by_android_uiautomator(
                                 'new UiScrollable(new UiSelector().'  # 滚动并点击, 定位控件通过 text
                                 'scrollable(true).instance(0)).'
                                 f'scrollIntoView(new UiSelector().text("{webview}")'
                                 '.instance(0));').click()

        self.driver.find_element_by_xpath("//*[@text='i has no focus']").send_keys('This is Denny')   # content-desc 有内容
        self.driver.find_element_by_accessibility_id('i am a link').click()
        print(self.driver.page_source)      # 打印 源码



