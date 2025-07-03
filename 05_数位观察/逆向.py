import requests
import execjs

url = 'https://app.swguancha.com/client/v1/cPublic/consumer/property/type/search'
headers = {
    "accept": "application/json, text/plain, */*",
    "accept-encoding": "gzip, deflate, br, zstd",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8",
    "connection": "keep-alive",
    "devicetype": "1",
    "host": "app.swguancha.com",
    "origin": "https://www.swguancha.com",
    "referer": "https://www.swguancha.com/",
    "sec-ch-ua": "\"Chromium\";v=\"140\", \"Not=A?Brand\";v=\"24\", \"Google Chrome\";v=\"140\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36"
}

response = requests.get(url=url)

with open('解密.js', mode='r', encoding='utf-8') as f:
    js_code = f.read()
    js_func = execjs.compile(js_code)
    res = js_func.call("fn", response.text)

print(res)
