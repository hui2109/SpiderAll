import requests
import execjs
import json

url = "https://www.hfhuizhan.com/prod-api/hfhz-exhibition/back/exhibition/listExhibitionNotPage"
headers = {
    "accept": "application/json",
    "accept-encoding": "gzip, deflate, br, zstd",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8",
    "authorization": "null",
    "content-length": "55",
    "content-type": "application/json;charset=UTF-8, application/json;charset=UTF-8",
    "origin": "https://www.hfhuizhan.com",
    "priority": "u=1, i",
    "referer": "https://www.hfhuizhan.com/schedule",
    "sec-ch-ua": "\"Chromium\";v=\"140\", \"Not=A?Brand\";v=\"24\", \"Google Chrome\";v=\"140\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36"
}

with open('解密.js', mode='r', encoding='utf-8') as f:
    js_code = f.read()
    js_func = execjs.compile(js_code)

data = {"yyyyMM": "2025-07"}
data_json = json.dumps(data, separators=(',', ':'))

payload = {
    "data": js_func.call("sr", data_json)
}

response = requests.post(url=url, data=json.dumps(payload, separators=(',', ':')), headers=headers)

ret = js_func.call("mr", response.text)
print(ret)
