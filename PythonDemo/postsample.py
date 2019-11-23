import requests
import json
def get_translate_date(word=None):
	url="http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"
	Form_data={'i': word, 'from': 'AUTO', 'to': 'AUTO', 'smartresult': 'dict', 'client': 'fanyideskweb','salt': '15736583138650', 'sign': '8c20b1e3abceb3470f5eba6faf937e3a', 'doctype': 'json', 'version': '2.1', 'keyfrom': 'fanyi.web', 'action': 'FY_BY_REALTlME'}
			   # 'ts': '1573658313865','bv': 'd2685b66b612e42764cb7b20e19ecbe4',

# 	Form_data='i=%E6%88%91%E7%88%B1%E4%B8%AD%E5%9B%BD&from=AUTO&to=AUTO&smartresult=dict&client=fanyideskweb&salt=15739878298470&sign=cf7be6339f10872cde2cefa102743346&ts=1573987829847&bv=ab57a166e6a56368c9f95952de6192b5&doctype=json&version=2.1&keyfrom=fanyi.web&action=FY_BY_CLICKBUTTION'

	response = requests.post(url,data=Form_data)

	content = json.loads(response.text)

	print(content['translateResult'][0]['tgt'])

if __name__=='__main__':
	get_translate_date('我爱数据')
