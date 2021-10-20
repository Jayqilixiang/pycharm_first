# -*- coding: utf-8 -*-
# @Author: Kid
# @FileName: test_webview_apidemo.py
# @Date: 2021/9/20  21:19


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
            'appPackage': 'com.touchboarder.android.api.demos',
            'appActivity': 'com.example.android.apis.ApiDemos',
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
        self.driver.find_element_by_xpath("//*[@text='Views']").click()    # 根据content-desc定位，但我的为空，没有.所以不用asscessbilly_id。 Accessibility ID在Android上面就等同于contentDescription
        webview = "WebView"
        self.driver.find_element_by_android_uiautomator(
                                 'new UiScrollable(new UiSelector().'  # 滚动并点击  text 为 打卡 
                                 'scrollable(true).instance(0)).'
                                 'scrollIntoView(new UiSelector().'
                                 f'text("{webview}").instance(0));').click()

        self.driver.find_element_by_accessibility_id('Hello World! - 1').click()    # content-desc 有内容
        print(self.driver.page_source)      # 打印 源码
        # 分析源码结果 看到了  webview， 这里我自己的并 渲染成 原生的内容 content-desc, 老师的 ApiDemo 就有


