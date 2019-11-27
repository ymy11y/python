import requests
import json
import time
url = 'https://search.heweather.net/top?group=cn&key=41f16cb75020482d8132ccec9332f04c&number=10'
strhtml = requests.get(url)
strhtml.encoding = 'utf8'
data = strhtml.text
print(data)

dic = strhtml.json()
print(dic)
for item in dic["HeWeather6"][0]["basic"]:
    print(item["location"])  #获取城市名称
    url = 'https://free-api.heweather.net/s6/weather/forecast?location=' + item["location"] + '&key=41f16cb75020482d8132ccec9332f04c'
    strhtml = requests.get(url)
    strhtml.encoding = 'utf8'
    time.sleep(1)
    dic = strhtml.json()
    print(dic["HeWeather6"][0]["daily_forecast"])
    for item in dic["HeWeather6"][0]["daily_forecast"]:
        print(item["tmp_max"])
