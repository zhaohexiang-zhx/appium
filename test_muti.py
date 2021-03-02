# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

# 导入库
import pytest
from appium import webdriver
import time

from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.webdriver import WebDriver


class TestAndroid(object):
    # 指定driver类型，后面可以调用webdriver中的方法
    driver = WebDriver

    @classmethod
    def setup_class(cls):
        print('setup class')
        # 3.6中用法
        # 初始化，只执行一次，即第一次执行，完成所有加载
        # cls.driver = cls.init_appium()

    def setup_method(self):
        print('setup method')
        # 每次都执行，接下来每次执行都保留状态
        TestAndroid.driver = self.restart_appium()
        self.driver = TestAndroid.driver

    def test_login(self):
        el2 = TestAndroid.driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.ImageView")
        el2.click()
        time.sleep(3)
        # 密码登录
        el3 = TestAndroid.driver.find_element_by_id("login_password")
        el3.click()
        time.sleep(2)
        # 返回
        el4 = TestAndroid.driver.find_element_by_id("backImageView")
        el4.click()
        time.sleep(2)
        # 返回
        el5 = TestAndroid.driver.find_element_by_id("backImageView")
        el5.click()

        # 断言


    def test_search(self):
        # 定位到搜索框，点击
        TestAndroid.driver.find_element_by_xpath("//*[contains(@resource-id,'search_ll')]//*[@text='乘风破浪的姐姐2']").click()

    # 滑动
    # def test_swipe(self):
    #     for i in range(5):
    #         self.driver.swipe(1000, 1000, 200, 200)
    #         time.sleep(2)

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
        TestAndroid.driver.quit()

    @classmethod
    # 返回的是什么，3.6中用法
    def init_appium(cls):
        # 类级别变量
        caps = {}
        caps["platformName"] = "Android"
        caps["deviceName"] = "demo"
        caps["appActivity"] = "com.czy.hiconmultiscreen.mvp.ui.splash.SplashActivity"
        caps["appPackage"] = "com.czy.hiconmultiscreen"
        caps["autoGrantPermissions"] = "true"
        caps["ensureWebviewsHavePages"] = True
        # 不重置app信息
        caps['noReset'] = True

        # 初始化实例，调用导入库的方法
        driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        driver.implicitly_wait(2)
        return driver

    @classmethod
    def restart_appium(cls):
        # 类级别变量
        caps = {}
        caps["platformName"] = "Android"
        caps["deviceName"] = "demo"
        caps["appActivity"] = "com.czy.hiconmultiscreen.mvp.ui.splash.SplashActivity"
        caps["appPackage"] = "com.czy.hiconmultiscreen"
        # caps["autoGrantPermissions"] = "true"
        caps["ensureWebviewsHavePages"] = True
        # 不重置app信息
        caps['noReset'] = True

        # 初始化实例，调用导入库的方法
        driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        driver.implicitly_wait(2)
        return driver





