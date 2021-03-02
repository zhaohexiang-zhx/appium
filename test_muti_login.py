# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

import time

# 导入库
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction


class TestAndroid(object):

    @classmethod
    def setup_class(cls):
        print('setup class 当前类下的所有用例执行之前执行一次')
        # 当前没有被调用到
        cls.driver = cls.install_app()

    def setup_method(self):
        print('setup method 在每个测试用例执行之前执行一次')
        TestAndroid.driver = self.restart_app()
        # 获取启动的appium的driver实例，用于后续每个case的driver
        self.driver = TestAndroid.driver

        # 点击我的，触发登录
        el2 = self.driver.find_element_by_id("index_livePart")
        el2.click()
        time.sleep(2)

    # 测试用例1：进入登录页面
    def test_login_password(self):
        # 密码登录
        el3 = self.driver.find_element_by_id("login_password")
        el3.click()
        time.sleep(2)
        # 断言

    def test_login_findPassword(self):
        # 密码登录
        el3 = self.driver.find_element_by_id("login_password")
        el3.click()
        time.sleep(2)
        # 找回密码
        el3 = self.driver.find_element_by_id("findPassword")
        el3.click()
        time.sleep(2)

    # 测试用例2：进入搜索页面

    @classmethod
    def install_app(cls):
        # 类级别变量
        caps = {}
        # 如果有必要，进行第一次安装
        # caps["app"] = ""
        caps["platformName"] = "Android"
        caps["deviceName"] = "demo"
        caps["appActivity"] = "com.czy.hiconmultiscreen.mvp.ui.splash.SplashActivity"
        caps["appPackage"] = "com.czy.hiconmultiscreen"
        # 解决第一次启动权限问题
        caps["autoGrantPermissions"] = "true"
        caps["ensureWebviewsHavePages"] = True

        # 初始化实例，调用导入库的方法
        driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        driver.implicitly_wait(2)

        # 同意协议
        el0 = driver.find_element_by_id("btn_agree")
        el0.click()
        return driver

    @classmethod
    def restart_app(cls):
        # 类级别变量
        caps = {}
        caps["platformName"] = "Android"
        caps["deviceName"] = "demo"
        caps["appActivity"] = "com.czy.hiconmultiscreen.mvp.ui.splash.SplashActivity"
        caps["appPackage"] = "com.czy.hiconmultiscreen"
        caps["ensureWebviewsHavePages"] = True
        # 为了更快的启动，并保留之前的数据，从而可以保存在上个case的数据
        caps['noReset'] = True

        # 初始化实例，调用导入库的方法
        driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        driver.implicitly_wait(2)
        return driver





