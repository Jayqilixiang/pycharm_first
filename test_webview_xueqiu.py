# -*- coding: utf-8 -*-
# @Author: Kid
# @FileName: test_webview_xueqiu.py
# @Date: 2021/9/21  15:40

from time import sleep
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

# mumu 模拟器 不支持， 改用 夜神， 夜神也不行， 改用  android studio


class TestBrowser():
    def setup(self):  # 设置些 提升速度的设置，如跳过一些服务端安装
        des_caps = {
            'platformName': 'android',
            'platformVersion': '11.0',
            'appPackage': ' com.xueqiu.android',
            'appActivity': '.view.WelcomeActivityAlias',
            # 'browserName': 'Browser',       # 这是 安卓手机 自带的 浏览器，找版本时通过cmd命令得到版本信息
            'noReset': True,
            'deviceName': 'emulator-5554',
            'skipServerInstallation': 'true',
            'chromedriverExecutable': 'C:\google_chrome\driver_version\chromedriverv2.24.exe' # 指定路径,版本一定要配置正确
        }
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", des_caps)
        self.driver.implicitly_wait(10)

    def teardown(self):
        pass
        # self.driver.quit()     # 去掉quit  打印上下文看看


        # 重要的一点是： 要知道 哪个页面要 进行 Webview转换， 且转换前 打印下 上下文，方便分析
    def test_webview(self):
        # 点击 ‘交易’
        self.driver.find_element_by_xpath("//*[@text='交易']").click()  # 常犯错， elements
        A_locator = (By.XPATH, "//*[@text='平安证券']")   # 直接copy xpath


        print(self.driver.contexts) # 转换上下文
        self.driver.switch_to.context(self.driver.contexts[-1])  # 一般来说，最后一位打开都是新打开的webview，但也有可能不是，可以用遍历方式找到这个webview

        # print(self.driver.window_handles)  # 点击 前 打印下  --- 查看下 页面点击后是否有新增 一个页面
        # 打开 开户的页面 加载有点慢，可以加个 显示等待 是否可点击
        # 点击  ‘平安证券，去开户’  --- 因为 点击完 ‘平安证券，去开户’后， chrome映射 会弹出另一个窗口， 需要做窗口切换
        WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable(A_locator))
        self.driver.find_element(*A_locator).click()
        # print(self.driver.window_handles)  # 点击后打印下 -- 打印结果是 新开的页面一般都放在 最后一个，所以切换至最后一个窗口

        kaihu_window = self.driver.window_handles[-1]
        self.driver.switch_to.window(kaihu_window)      # 切换哪个window，需要上面在点击前后都 打印下

        self.driver.find_element(MobileBy.ID, 'phone-number').send_keys('13242008411')
        # 显示等待 手机号码是否 可输入
        A_phonenum = (By.ID, 'phone-number')
        WebDriverWait(self.driver, 5).until(ec.element_to_be_clickable(A_phonenum))
        self.driver.find_element(*A_phonenum).send_keys('13200180021')
        self.driver.find_element(MobileBy.ID, 'code').send_keys('1234')
        self.driver.find_element(MobileBy.XPATH, '/html/body/div/div/div[2]/div/div[2]/h1').click()



