import requests
url='http://www.cntour.cn/'
strhtml=requests.get(url)
data=strhtml.text
print(data.encode("GBK","ignore"))