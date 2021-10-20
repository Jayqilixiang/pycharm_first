# -*- coding: utf-8 -*-
# @Author: Kid
# @FileName: test_webview_ApiDemo3.py
# @Date: 2021/9/21  13:28

# WebView 技术另一种方法

from time import sleep
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
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
            'chromedriverExecutable': 'C:\google_chrome\driver_version\chromedriverv2.24.exe'   # 指定路径,一定要配置成功
        }
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", des_caps)
        self.driver.implicitly_wait(10)

    def teardown(self):
        pass
        # self.driver.quit()     # 去掉quit  打印上下文看看

    def test_webview(self):
        self.driver.find_element_by_accessibility_id("Views").click()    # 根据content-desc定位， Accessibility ID在Android上面就等同于contentDescription
        webview = "WebView"
        print(self.driver.contexts)  # 点击前打印下 上下文
        self.driver.find_element_by_android_uiautomator(
                                 'new UiScrollable(new UiSelector().'  # 滚动并点击, 定位控件通过 text
                                 'scrollable(true).instance(0)).'
                                 f'scrollIntoView(new UiSelector().text("{webview}")'
                                 '.instance(0));').click()

        # self.driver.find_element_by_xpath("//*[@text='i has no focus']").send_keys('This is Denny')   # content-desc 没有内容
        # self.driver.find_element_by_accessibility_id('i am a link').click()
        # print(self.driver.page_source)      # 打印 源码
        # 上面是通过渲染之后的页面，定义混合应用，即： accessibility_id   ---- 但这种方式不稳定，正规的是下面的 --- 切换上下文 方式

        print(self.driver.contexts)     # 点击后打印，即第二次打印 --- 查看运行结果 与第一次打印对比 ，是 显示 原生的，还是 webview
        self.driver.switch_to.context(self.driver.contexts[-1])    # 想要webview的上下文，通过 switch切换到 webview的上下文
        # 最终页面 展示的就是 HTML 的页面， 就不是 原生APP 的页面
        self.driver.find_element(MobileBy.ID, 'i_am_a_textbox').send_keys('This is Damon')
        self.driver.find_element(MobileBy.ID, 'i am a link').click()
        print(self.driver.page_source)






