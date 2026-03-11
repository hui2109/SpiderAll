import requests
import execjs

url = 'https://dict.youdao.com/webtranslate'
headers = {
    "accept": "application/json, text/plain, */*",
    "accept-encoding": "gzip, deflate, br, zstd",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8",
    "connection": "keep-alive",
    "content-length": "335",
    "content-type": "application/x-www-form-urlencoded",
    # "cookie": "OUTFOX_SEARCH_USER_ID_NCOO=506424618.54122555; OUTFOX_SEARCH_USER_ID=1609832668@112.193.118.3; _uetsid=eb436dc0af1411f0b6e0690bd7539f5a; _uetvid=ece426d0ad6611f0ad04fd0213bb4377; DICT_DOCTRANS_SESSION_ID=ZWU1MThhYzItN2YzNy00YjJjLWFkN2UtOTA0ZjE1ZTMyZDFi",
    "host": "dict.youdao.com",
    "origin": "https://fanyi.youdao.com",
    "referer": "https://fanyi.youdao.com/",
    "sec-ch-ua": "\"Google Chrome\";v=\"143\", \"Chromium\";v=\"143\", \"Not A(Brand\";v=\"24\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36"
}
words = "我滴家在东北"
with open('解密.js', mode='r', encoding='utf-8') as f:
    js_code = f.read()
    js_func = execjs.compile(js_code)
    res = js_func.call("fn", words)

response = requests.post(url, headers=headers, data=res)
# print(response.text)
# Z21kD9ZK1ke6ugku2ccWu4n6eLnvoDT0YgGi0y3g-v0B9sYqg8L9D6UERNozYOHqnYdl2efZNyM6Trc_xS-zKtfTK4hb6JP8XwCzNh0avc8qItQUiIU_4wKKXJlIpvMvfKvJaaZzaX6VEtpkr2FdkfoT_Jgbm2GRSVj3r40autIdlImENG8hC0ZH4ww7utwuTt3Oo_ZpXg0BSq9wePSAB75-ChkiGKF9HTIPeCl2bl84SBD1XDfFCZpkKQhecYSs0JLoXOqP2ltavxRrg58Hp1q5uIgZZ_Oo2-Jmd-t1r4es40drcAq5bjmS62M2VJF8D6ojtOh9JTfNwgzD3CxYn-Pd7-TgHMyNEJEkFXTAyxzpjlFqtrCYDE3SZUYlENkqsL8Wrra1hM-1nTfiB-BLcWAdRBynNpP5_54aq_-GBsq8bB_9yEX5ovzDB4_Ry_spVVuUnb39iplMHCdCnjOD3ngiIDbl9SUz-9npjBX05ZYRdPmFPAl424qdoaxeVqnVoH8jQFPZVqaHMzu4mJg0SICDWFH7GP1zqGRbXd3ESjT_iBInl3gICt2XVuhh_nubcELkTEC6xbqEDRQkPUNMp9oC8N7JQ4SkgJyCbsmhC6FGgffKDIzkoWbb9njBHMJMR77gXDYHt9APzmKYS_IDH14bOC6UYJTGYBdBd8q0Q8qe1YSspmpPAC3P5Su6MA1XbhHu24vyCQAdW9RAUnlDiHQeDGtgN4gvMNWvZ6C8t42LSjMoNh5nok9D36xxu0fvnHcXySwzpY6ZwDyS0QXaoA==

##################################################
# 解密响应内容
##################################################

with open('解密.js', mode='r', encoding='utf-8') as f:
    js_code = f.read()
    js_func = execjs.compile(js_code)
    res = js_func.call("fn_d", response.text)

print(res)
