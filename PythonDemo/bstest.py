import requests
import re
from bs4 import BeautifulSoup
url="http://www.cntour.cn"
header={'User-Agent', 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36'}
# strhtml=requests.get(url, headers=header)  #加了这句要报错
strhtml=requests.get(url)
soap=BeautifulSoup(strhtml.text,'lxml')
data=soap.select('#main > div > div.mtop.firstMod.clearfix > div.centerBox > ul.newsList > li > a')
for item in data:
    result={
        'title':item.get_text(),
        'link':item.get('href'),
        'ID':re.findall('\d+',item.get('href'))
    }
    print(result) 