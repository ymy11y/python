import requests
import json

import time
import os
from selenium import webdriver
# 先安装pywin32，才能导入下面两个包
import win32api
import win32con
# 导入处理alert所需要的包
from selenium.common.exceptions import NoAlertPresentException
import traceback

def get_data(word=None):
# 	url="https://wx.pplon.cn/a/ord/ordOrder/list?m=632d606a4abb4270ba6246d284db5435"
# 	Form_data={'order': 'asc', 'offset': 0, 'limit': 25, ')offsetReset': 'false'}
# # 	Form_data='i=%E6%88%91%E7%88%B1%E4%B8%AD%E5%9B%BD&from=AUTO&to=AUTO&smartresult=dict&client=fanyideskweb&salt=15739878298470&sign=cf7be6339f10872cde2cefa102743346&ts=1573987829847&bv=ab57a166e6a56368c9f95952de6192b5&doctype=json&version=2.1&keyfrom=fanyi.web&action=FY_BY_CLICKBUTTION'
#
# 	response = requests.post(url,data=Form_data)
#
# 	content = json.loads(response.text)

	# print(content['translateResult'][0]['tgt'])

	# 环境配置
	# chromedriver = "C:\Program Files (x86)\Google\Chrome\Application"
	chromedriver = r"C:\Users\Administrator\AppData\Local\Google\Chrome\Application"
	os.environ["webdriver.ie.driver"] = chromedriver

	driver = webdriver.Chrome()  # 选择Chrome浏览器

	# driver.get('https://fnzz.aoyang.com/login')  # 打开网站
	driver.get('https://wx.pplon.cn/a/ord/ordOrder/list?m=632d606a4abb4270ba6246d284db5435')  # 打开网站
	driver.maximize_window()  # 最大化谷歌浏览器
	# 处理alert弹窗
	try:
		# alert1 = driver.switch_to.alert  # switch_to.alert点击确认alert
		username = "戏宝贝"  # 请替换成你的用户名
		password = "tanmiao2019"  # 请替换成你的密码

		driver.find_element_by_id('username').click()  # 点击用户名输入框
		driver.find_element_by_id('username').clear()  # 清空输入框
		driver.find_element_by_id('username').send_keys(username)  # 自动敲入用户名

		driver.find_element_by_id('password').click()  # 点击密码输入框
		driver.find_element_by_id('password').clear()  # 清空输入框
		driver.find_element_by_id('password').send_keys(password)  # 自动敲入密码

		time.sleep(5)
		# 采用class定位登陆按钮
		# driver.find_element_by_class_name('ant-btn').click() # 点击“登录”按钮
		driver.find_element_by_id('login').click()
		# driver.find_element_by_class_name('login').click()  # 点击“登录”按钮
		# 采用xpath定位登陆按钮，
		# driver.find_element_by_xpath('//*[@id="root"]/div/div[3]/form/button').click()

		time.sleep(1)


		# url = "https://wx.pplon.cn/a/ord/ordOrder/list?m=632d606a4abb4270ba6246d284db5435"
		# Form_data = {'order': 'asc', 'offset': 0, 'limit': 25, ')offsetReset': 'false'}
		# # 	Form_data='i=%E6%88%91%E7%88%B1%E4%B8%AD%E5%9B%BD&from=AUTO&to=AUTO&smartresult=dict&client=fanyideskweb&salt=15739878298470&sign=cf7be6339f10872cde2cefa102743346&ts=1573987829847&bv=ab57a166e6a56368c9f95952de6192b5&doctype=json&version=2.1&keyfrom=fanyi.web&action=FY_BY_CLICKBUTTION'
		#
		# response = requests.post(url, data=Form_data)
		#
		# content = json.loads(response.text)
		for i in range(5):
			# pageBtns= driver.find_element_by_xpath("html/body/section/div[2]/div[2]/div[0]")
			pageBtns= driver.find_element_by_id("dynamic-table")
			if pageBtns == []:
				break
			routes=driver.find_elements_by_xpath("html/body/div[2]/div[2]/div[7]/div[2]/div")

	except NoAlertPresentException as e:
		print("no alert")
		traceback.print_exc()
	# else:
	# 	at_text1 = alert1.text
	# 	print("at_text:" + at_text1)

	time.sleep(1)

	# driver.find_element_by_link_text('登录').click() # 点击“账户登录”

	# username = "戏宝贝"  # 请替换成你的用户名
	# password = "tanmiao2019"  # 请替换成你的密码
	#
	# driver.find_element_by_id('username').click()  # 点击用户名输入框
	# driver.find_element_by_id('username').clear()  # 清空输入框
	# driver.find_element_by_id('username').send_keys(username)  # 自动敲入用户名
	#
	# driver.find_element_by_id('password').click()  # 点击密码输入框
	# driver.find_element_by_id('password').clear()  # 清空输入框
	# driver.find_element_by_id('password').send_keys(password)  # 自动敲入密码
	#
	# # 采用class定位登陆按钮
	# # driver.find_element_by_class_name('ant-btn').click() # 点击“登录”按钮
	# driver.find_element_by_class_name('login').click() # 点击“登录”按钮
	# # 采用xpath定位登陆按钮，
	# # driver.find_element_by_xpath('//*[@id="root"]/div/div[3]/form/button').click()
	#
	# time.sleep(1)

	# driver.find_element_by_id('signIn').click() # 点击“签到”

	win32api.keybd_event(122, 0, 0, 0)  # F11的键位码是122，按F11浏览器全屏
	win32api.keybd_event(122, 0, win32con.KEYEVENTF_KEYUP, 0)  # 释放按键


# driver.close()

# 代码调用：
# python.exe JDSignup.py



if __name__=='__main__':
	get_data('我爱数据')