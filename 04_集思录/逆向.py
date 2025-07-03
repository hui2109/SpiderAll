from http.client import responses

import requests
import execjs

user_name = "1234567"
password = "1234566"

with open('解密.js', mode='r', encoding='utf-8') as f:
    js_code = f.read()
    js_func = execjs.compile(js_code)

form_data = {
    "return_url": "/",
    "user_name": js_func.call("fn", user_name),
    "password": js_func.call("fn", password),
    "auto_login": "1",
    "aes": "1"
}

url = "https://www.jisilu.cn/webapi/account/login_process/"
headers = {
    "accept": "application/json, text/javascript, */*; q=0.01",
    "accept-encoding": "gzip, deflate, br, zstd",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8",
    "content-length": "118",
    "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
    "cookie": "kbzw__Session=4mhg4215qh1tbden0dou5rpio1; Hm_lvt_164fe01b1433a19b507595a43bf58262=1751532585; HMACCOUNT=F29508CFD81619CE; kbz_newcookie=1; Hm_lpvt_164fe01b1433a19b507595a43bf58262=1751532611",
    "origin": "https://www.jisilu.cn",
    "priority": "u=1, i",
    "referer": "https://www.jisilu.cn/login/",
    "sec-ch-ua": "\"Chromium\";v=\"140\", \"Not=A?Brand\";v=\"24\", \"Google Chrome\";v=\"140\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36",
    "x-requested-with": "XMLHttpRequest"
}

response = requests.post(url=url, data=form_data)
print(response.text)
