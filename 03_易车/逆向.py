import requests
import execjs
import json

serialId = "11108"  # serialId是车型号码
p_dict = {
    "cityId": "2501",
    "serialId": serialId
}
js_str = json.dumps(p_dict, separators=(',', ':'))

url = "https://mhapi.yiche.com/hcar/h_car/api/v1/param/get_param_details"
params = {
    "cid": 508,
    "param": js_str
}

with open('解密.js', mode='r', encoding='utf-8') as f:
    js_code = f.read()
    js_func = execjs.compile(js_code)
    res = js_func.call("fn", serialId)
    # {'x-platform': 'pc', 'x-timestamp': 1751527692552, 'cid': '508', 'x-sign': '8afa457cb1a9aba27cd637444588077c', 'x-city-id': '2501', 'x-ip-address': '175.152.181.225', 'x-user-guid': 'a49e4841-0183-4562-a299-29fb1a49d8ac'}

headers = {
    "accept": "*/*",
    "accept-encoding": "gzip, deflate, br, zstd",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8",
    "cid": res['cid'],
    "content-type": "application/json;charset=UTF-8",
    "cookie": "CIGUID=a49e4841-0183-4562-a299-29fb1a49d8ac; selectcity=510100; selectcityid=2501; selectcityName=%E6%88%90%E9%83%BD; selectcityPinyin=chengdu; auto_id=7518a0dabdee35588d62105f4d02ce0d; UserGuid=a49e4841-0183-4562-a299-29fb1a49d8ac; CIGDCID=SfRitGcJYsD3WGyTAs4twkST8fBCtyfF; Hm_lvt_610fee5a506c80c9e1a46aa9a2de2e44=1751375963; pageCount=2; isWebP=true; locatecity=510100; bitauto_ipregion=175.152.181.225%3A%E5%9B%9B%E5%B7%9D%E7%9C%81%E6%88%90%E9%83%BD%E5%B8%82%3B2501%2C%E6%88%90%E9%83%BD%E5%B8%82%2Cchengdu; csids=11108_1868",
    "origin": "https://car.yiche.com",
    "priority": "u=1, i",
    "referer": "https://car.yiche.com/xiaomimx11/peizhi/",
    "reqid": res['reqid'],
    "sec-ch-ua": "\"Chromium\";v=\"140\", \"Not=A?Brand\";v=\"24\", \"Google Chrome\";v=\"140\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36",
    "x-city-id": res['x-city-id'],
    "x-ip-address": res['x-ip-address'],
    "x-platform": res['x-platform'],
    "x-sign": res['x-sign'],
    "x-timestamp": str(res["x-timestamp"]),
    "x-user-guid": res["x-user-guid"]
}

response = requests.get(url=url, params=params, headers=headers)
# print(response.request.headers)
# print(response.request.url)
print(response.json())
