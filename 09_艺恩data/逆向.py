import requests
import execjs

url = 'https://www.endata.com.cn/API/GetData.ashx'
headers = {
    "accept": "text/plain, */*; q=0.01",
    "accept-encoding": "gzip, deflate, br, zstd",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8",
    "connection": "keep-alive",
    "content-length": "51",
    "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
    "host": "www.endata.com.cn",
    "origin": "https://www.endata.com.cn",
    "sec-ch-ua": "\"Google Chrome\";v=\"141\", \"Not?A_Brand\";v=\"8\", \"Chromium\";v=\"141\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36",
    "x-requested-with": "XMLHttpRequest"
}
params = {
    "tdate": "2025-09-07",
    "MethodName": "BoxOffice_GetPcHomeList"
}

response = requests.post(url, headers=headers, data=params)
# print(response.text)

with open('./解密.js', mode='r', encoding='utf-8') as f:
    js_code = f.read()
    js_func = execjs.compile(js_code)
    res = js_func.call("fn", response.text)

print(res)
