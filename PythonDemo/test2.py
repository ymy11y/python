from selenium import webdriver
import time
import requests
from lxml import etree
import base64
#操作浏览器
def getheaders():
    driver = webdriver.Chrome()
    #这是要访问的网站
    url = 'https://wx.pplon.cn/a/ord/ordOrder/list?m=632d606a4abb4270ba6246d284db5435'
    time.sleep(2)
    #访问网站
    driver.get(url)
    time.sleep(2)
    #找到地方放入登录用户名密码
    driver.find_element_by_id('username').send_keys('"戏宝贝"')
    driver.find_element_by_id('password').send_keys('tanmiao2019')
    #有验证码的情况
    try:
        #用xpath定位到验证码图片
        html_ele = etree.HTML(driver.page_source)
        html_img = html_ele.xpath('//img[@id="captcha_image"]/@src')[0]
        #获取图片的内容
        response = requests.get(html_img)
        #先用64把他转换成需要的格式
        b64_str = base64.b64encode(response.content)
        v_type = 'cn'
        # post 提交打码平台的数据
        form = {
            'v_pic': b64_str,
            'v_type': v_type,
        }
        #打码平台的headers
        headers = {
            'Authorization':'APPCODE 5c3fb1*****2c6b7e297cc7'
        }
        #阿里云打码的提交地址
        url = 'http://yzmplus.market.alicloudapi.com/fzyzm'
        #获取返回值的验证码
        response = requests.post(url,data=form,headers=headers)
        res_vcode = response.json()['v_code']
        print(res_vcode)
        #放入验证码到地方
        driver.find_element_by_id('captcha_field').send_keys(res_vcode)
    except:
        print('don`t need')
    #提交登录
    driver.find_element_by_id('login').click()


    #获取登录以后的cookie
    cookie = driver.get_cookies()
    print(cookie)
    #下面几步把cookie转换成自己需要的格式
    cookie_list = []
    for cookie_dict in cookie:
        cookie_res = cookie_dict['name'] +'='+ cookie_dict['value']
        cookie_list.append(cookie_res)
    cookie = ';'.join(cookie_list)

    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
        'Cookie':cookie

    }

    for i in range(5):
        # pageBtns= driver.find_element_by_xpath("html/body/section/div[2]/div[2]/div[0]")
        pageBtns = driver.find_element_by_id("dynamic-table")
        if pageBtns == []:
            break

if __name__ == '__main__':
    headers = getheaders()

    #这个路径是登录过后的页面
    url_info = 'https://wx.pplon.cn/a/ord/ordOrder/list?m=632d606a4abb4270ba6246d284db5435'

    response = requests.get(url_info,headers=headers)

