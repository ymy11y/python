import requests
import urllib
import time
url = 'https://touch.dujia.qunar.com/depCities.qunar'
strhtml = requests.get(url)
dep_dict = strhtml.json()
for dep_item in dep_dict['data']:
    for dep in dep_dict['data'][dep_item]:
        a=[]
        print(dep)
        url = 'https://m.dujia.qunar.com/golfz/sight/arriveRecommend?dep={}&exclude=&extensionImg=255,175'.format(urllib.request.quote(dep))
        time.sleep(1)
        strhtml=requests.get(url)
        arrive_dict=strhtml.json()
        for arr_item in arrive_dict['data']:
            for arr_item_1 in arr_item['subModules']:
                for query in arr_item_1['items']:
                    if query['query'] not in a:
                        a.append(query['query'])
                    # print(query['query'])
        print(a) # 去重以后，针对某个出发地，其目的地的集合