# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

# 导入库
from appium import webdriver
import time

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

# case
# 消息
el2 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.ImageView")
el2.click()
time.sleep(3)
# 密码登录
# el3 = driver.find_element_by_id("com.czy.hiconmultiscreen:id/login_password")
# /之前的部分可以去掉
el3 = driver.find_element_by_id("login_password")
el3.click()
time.sleep(2)
# 返回
el4 = driver.find_element_by_id("backImageView")
el4.click()
time.sleep(2)
# 返回
el5 = driver.find_element_by_id("backImageView")
el5.click()


# 断言

# driver.quit()


