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

    # 测试用例1：进入登录页面
    def test_login(self):
        el2 = self.driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.ImageView")
        el2.click()
        time.sleep(3)
        # 密码登录
        el3 = self.driver.find_element_by_id("login_password")
        el3.click()
        time.sleep(2)
        # 返回
        el4 = self.driver.find_element_by_id("backImageView")
        el4.click()
        time.sleep(2)
        # 返回
        el5 = self.driver.find_element_by_id("backImageView")
        el5.click()

        # 断言

    # 测试用例2：进入搜索页面
    def test_search(self):
        # 定位到搜索框，点击
        self.driver.find_element_by_xpath("//*[contains(@resource-id,'search_ll')]//*[@text='乘风破浪的姐姐2']").click()

    # 测试用例3：使用swipe滑动
    def test_swipe(self):
        for i in range(5):
            self.driver.swipe(1000, 1000, 200, 200)
            time.sleep(2)

    # 测试用例4：使用TouchAction滑动
    def test_action(self):
        # self.driver.find_element_by_xpath("//*[contains(@resource-id,'search_ll')]//*[@text='乘风破浪的姐姐2']")
        action = TouchAction(self.driver)
        for i in range(5):
            # action.press(x=1000, y=1000)
            # action.move_to(x=500, y=500)
            # action.release()
            # action.perform()
            action.long_press(x=200, y=1000).move_to(x=200, y=200).release().perform()
            time.sleep(2)

    def test_action_p(self):
        # self.driver.find_element_by_xpath("//*[contains(@resource-id,'search_ll')]//*[@text='乘风破浪的姐姐2']")
        size = self.driver.get_window_size()
        action = TouchAction(self.driver)
        for i in range(5):
            # action.press(x=size['width'] * 0.8, y=size['height'] * 0.8).move_to(x=size['width'] * 0.2, y=size[
            action.long_press(x=size['width']*0.8, y=size['height']*0.8).move_to(x=size['width']*0.2, y=size['height']*0.2).release().perform()
            time.sleep(2)

    def test_window_size(self):
        print(self.driver.get_window_size())

    # 每次都执行，case完成，退出
    def teardown_method(self):
        # 不加也没有关系，如果不quit，启动appium会自动quit之前的session
        self.driver.quit()

    @classmethod
    # 返回的是什么，3.6中用法
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
        # 不重置app信息
        caps['noReset'] = True

        # 初始化实例，调用导入库的方法
        driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        driver.implicitly_wait(2)
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





