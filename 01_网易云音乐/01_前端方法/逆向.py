import requests
import execjs
import json

song_id = 569212211  # 毛不易 - 盛夏
ming_dict = {
    "ids": f"[{song_id}]",
    "level": "exhigh",
    "encodeType": "aac",
    "csrf_token": "7504cd49c72afbbb958a4e8e1d128273"
}

ming = json.dumps(ming_dict, separators=(',', ':'))

with open('解密.js', mode='r', encoding='utf-8') as f:
    js_code = f.read()
    js_func = execjs.compile(js_code)
    res = js_func.call("fn", ming)

url = 'https://music.163.com/weapi/song/enhance/player/url/v1?csrf_token=7504cd49c72afbbb958a4e8e1d128273'
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36"
}
form_data = {
    'params': res['encText'],
    'encSecKey': res['encSecKey']
}

response = requests.post(url, headers=headers, data=form_data)

song_url = response.json()['data'][0]['url']
with open(f'../assets/{song_id}.m4a', mode='wb') as f:
    response = requests.get(song_url, headers=headers)
    f.write(response.content)
