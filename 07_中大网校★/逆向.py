# 爬取逻辑:
# 访问文档, 获取cookie -> 拿到验证码图片 -> 识别验证码 -> 获取时间 -> 登录

import requests
import execjs
import base64
import ddddocr
import json

# 1. 登录页发请求, 获取本次会话的id
session = requests.session()
login_page_url = "https://user.wangxiao.cn/login?url=https%3A%2F%2Fks.wangxiao.cn%2F"
session.get(login_page_url, headers={
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "accept-encoding": "gzip, deflate, br, zstd",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8",
    "cache-control": "no-cache",
    "connection": "keep-alive",
    "host": "user.wangxiao.cn",
    "pragma": "no-cache",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36"
})
# print(session.cookies)

# 2. 获取验证码图片
captcha_url = "https://user.wangxiao.cn/apis//common/getImageCaptcha"
captcha_resp = session.post(captcha_url, headers={
    "accept": "application/json, text/javascript, */*; q=0.01",
    "accept-encoding": "gzip, deflate, br, zstd",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8",
    "connection": "keep-alive",
    "content-length": "0",
    "content-type": "application/json;charset=UTF-8",
    "host": "user.wangxiao.cn",
    "origin": "https://user.wangxiao.cn",
    "referer": "https://user.wangxiao.cn/login?url=https%3A%2F%2Fks.wangxiao.cn%2F",
    "source": "pc",
    "token": "user-agent",
    "Mozilla/5.0": "(Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36",
    "x-requested-with": "XMLHttpRequest"
})
captcha_img_data = captcha_resp.json()["data"].split(",")[-1]
captcha_img_bs = base64.b64decode(captcha_img_data)
# 验证码图片写入文件
with open('./captcha_img.png', 'wb') as f:
    f.write(captcha_img_bs)
# 识别验证码
dddd = ddddocr.DdddOcr()

# 3. 识别验证码
# 这行会报错, 将源代码改一下: image = image.resize((int(image.size[0] * (64 / image.size[1])), 64), Image.Resampling.LANCZOS).convert('L')
captcha_result = dddd.classification(captcha_img_bs)
print(captcha_result)

# 4. 获取时间
getTime_url = 'https://user.wangxiao.cn/apis//common/getTime'
response = session.post(getTime_url, headers={
    "accept": "application/json, text/javascript, */*; q=0.01",
    "accept-encoding": "gzip, deflate, br, zstd",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8",
    "connection": "keep-alive",
    "content-length": "0",
    "content-type": "application/json;charset=UTF-8",
    # "eagleeye-pappname": "ihuy5j2ab7@7cd9bc63da81d1d",
    # "eagleeye-sessionid": "nOmhye02it3mgXy9kizns16qO23h",
    # "eagleeye-traceid": "14bbc3821755613960582100381d1d",
    "host": "user.wangxiao.cn",
    "origin": "https://user.wangxiao.cn",
    "referer": "https://user.wangxiao.cn/login?url=https%3A%2F%2Fks.wangxiao.cn%2F",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "sessionid": "1755613513948",
    "source": "pc",
    "token": "",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36",
    "x-requested-with": "XMLHttpRequest"
})
time_data = response.json()['data']

# 5. 登录
# 先对请求参数进行RSA加密
password = "1234qweR"
with open('./解密.js', mode='r', encoding='utf-8') as f:
    js_code = f.read()
    js_func = execjs.compile(js_code)
    res = js_func.call("fn", password + time_data)

data = {
    "userName": "13688012109",
    "password": res,
    "imageCaptchaCode": captcha_result
}
login_url = "https://user.wangxiao.cn/apis//login/passwordLogin"
response = session.post(login_url, data=json.dumps(data, separators=(',', ':')), headers={
    "accept": "application/json, text/javascript, */*; q=0.01",
    "accept-encoding": "gzip, deflate, br, zstd",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8",
    "connection": "keep-alive",
    "content-length": "238",
    "content-type": "application/json;charset=UTF-8",
    "eagleeye-pappname": "ihuy5j2ab7@7cd9bc63da81d1d",
    "eagleeye-sessionid": "y5m5kebXi8noq5ojUl1abCw7Iaq7",
    "eagleeye-traceid": "1af774351755616426384100481d1d",
    "host": "user.wangxiao.cn",
    "origin": "https://user.wangxiao.cn",
    "referer": "https://user.wangxiao.cn/login?redirect_uri=https://ks.wangxiao.cn/",
    "sec-ch-ua": "\"Google Chrome\";v=\"141\", \"Not?A_Brand\";v=\"8\", \"Chromium\";v=\"141\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "sessionid": "1755613513948",
    "source": "pc",
    "token": "",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36",
    "x-requested-with": "XMLHttpRequest"
})
login_data = response.json()

# 6. 登录成功后设置cookie
session.cookies['autoLogin'] = 'null'
session.cookies['userInfo'] = json.dumps(login_data['data'], separators=(',', ':'))
session.cookies['token'] = login_data['data']['token']
session.cookies['UserCookieName'] = login_data['data']['userName']
session.cookies['OldUsername2'] = login_data['data']['userNameCookies']
session.cookies['OldUsername'] = login_data['data']['userNameCookies']
session.cookies['OldPassword'] = login_data['data']['passwordCookies']
session.cookies['UserCookieName_'] = login_data['data']['userName']
session.cookies['OldUsername2_'] = login_data['data']['userNameCookies']
session.cookies['OldUsername_'] = login_data['data']['userNameCookies']
session.cookies['OldPassword_'] = login_data['data']['passwordCookies']
session.cookies[f'{login_data['data']['userName']}' + "_exam"] = login_data['data']['sign']

# 7. 尝试加载数据
kaoshi_url = 'https://ks.wangxiao.cn/TestPaper/getPaperRuleQuestions'
data = {
    'id': '1E8C3E93-889F-4EA8-BA04-7C74E2DA325B'
}
response = session.post(kaoshi_url, data=json.dumps(data, separators=(',', ':')), headers={
    "accept": "application/json, text/javascript, */*; q=0.01",
    "accept-encoding": "gzip, deflate, br, zstd",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8",
    "connection": "keep-alive",
    "content-length": "45",
    "content-type": "application/json; charset=UTF-8",
    "host": "ks.wangxiao.cn",
    "origin": "https://ks.wangxiao.cn",
    "referer": "https://ks.wangxiao.cn/TestPaper/exam?s=1&ne=1&iid=29253&pt=",
    "sec-ch-ua": "\"Google Chrome\";v=\"141\", \"Not?A_Brand\";v=\"8\", \"Chromium\";v=\"141\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36",
    "x-requested-with": "XMLHttpRequest"
})
print(response.text)
