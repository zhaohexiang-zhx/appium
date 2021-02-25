# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

# 导入库
from appium import webdriver

caps = {}
caps["platformName"] = "Android"
caps["deviceName"] = "demo"
caps["appActivity"] = "com.czy.hiconmultiscreen.mvp.ui.splash.SplashActivity"
caps["appPackage"] = "com.czy.hiconmultiscreen"
caps["autoGrantPermissions"] = "true"
caps["ensureWebviewsHavePages"] = True

# 初始化实例，调用导入库的方法
driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)

# case
el1 = driver.find_element_by_id("com.czy.hiconmultiscreen:id/btn_agree")
el1.click()
el2 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.ImageView")
el2.click()

# 断言

driver.quit()