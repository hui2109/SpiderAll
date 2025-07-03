import json

import requests
import execjs

url = 'https://data-server.cbaleague.com/api/player-official/sort?pageNumber=1&pageSize=20'
headers = {
    "accept": "application/json, text/plain, */*",
    "accept-encoding": "gzip, deflate, br, zstd",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8",
    "cache-control": "no-cache",
    "content-length": "83",
    "content-type": "application/json;charset=UTF-8",
    "isencrypt": "encrypt",
    "origin": "https://www.cbaleague.com",
    "priority": "u=1, i",
    "referer": "https://www.cbaleague.com/",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36"
}
payload = {
    "season": 2023,
    "matchtypeid": 1,
    "direction": 2,
    "range": 1,
    "sortField": "pointsAverage"
}

response = requests.post(url=url, headers=headers, data=json.dumps(payload, separators=(',', ':')))  # {"season":2023,"matchtypeid":1,"direction":2,"range":1,"sortField":"pointsAverage"}
# response = requests.post(url=url, headers=headers, json=payload)  # b'{"season": 2023, "matchtypeid": 1, "direction": 2, "range": 1, "sortField": "pointsAverage"}'
print(response.request.body)
mi = response.text.strip('"')

with open('解密.js', mode='r', encoding='utf-8') as f:
    js_code = f.read()
    js_func = execjs.compile(js_code)
    res = js_func.call("a5e", mi)

print(res)
