import json

import requests
import execjs

# 1. 获取公钥
public_url = 'https://ec.minmetals.com.cn/open/homepage/public'
response = requests.post(public_url, headers={
    "accept": "application/json, text/plain, */*",
    "accept-encoding": "gzip, deflate, br, zstd",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8",
    "connection": "keep-alive",
    "content-length": "0",
    # "cookie": "SUNWAY-ESCM-COOKIE=46d6d283-3a50-4626-aeac-90fa1a3d4adc; __jsluid_s=2c2a77441565dc208853e5a0cb0663ae; JSESSIONID=73C3654F93E119ACFD587D4ECF605E1E",
    "host": "ec.minmetals.com.cn",
    "origin": "https://ec.minmetals.com.cn",
    "referer": "https://ec.minmetals.com.cn/open/home/purchase-info?tabIndex=0",
    "sec-ch-ua": "\"Google Chrome\";v=\"141\", \"Not?A_Brand\";v=\"8\", \"Chromium\";v=\"141\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36"
})
pubKey = response.text

e = {
    "inviteMethod": "",
    "businessClassfication": "",
    "mc": "",
    "lx": "ZBGG",
    "dwmc": "",
    "pageIndex": 4
}
with open('./解密.js', mode='r', encoding='utf-8') as f:
    js_code = f.read()
    js_func = execjs.compile(js_code)
    res = js_func.call("fn", e, pubKey)

url = 'https://ec.minmetals.com.cn/open/homepage/zbs/by-lx-page'
response = requests.post(url, data=res, headers={
    "accept": "application/json, text/plain, */*",
    "accept-encoding": "gzip, deflate, br, zstd",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8",
    "connection": "keep-alive",
    "content-length": "696",
    "content-type": "application/json",
    # "cookie": "SUNWAY-ESCM-COOKIE=46d6d283-3a50-4626-aeac-90fa1a3d4adc; __jsluid_s=2c2a77441565dc208853e5a0cb0663ae; JSESSIONID=73C3654F93E119ACFD587D4ECF605E1E",
    "host": "ec.minmetals.com.cn",
    "origin": "https://ec.minmetals.com.cn",
    "referer": "https://ec.minmetals.com.cn/open/home/purchase-info?tabIndex=0",
    "sec-ch-ua": "\"Google Chrome\";v=\"141\", \"Not?A_Brand\";v=\"8\", \"Chromium\";v=\"141\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36"
})
print(response.text)
