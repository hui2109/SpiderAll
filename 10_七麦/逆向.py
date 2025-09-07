import requests
import execjs

url = "https://api.qimai.cn/indexV2/getIndexRank"
headers = {
    "accept": "application/json, text/plain, */*",
    "accept-encoding": "gzip, deflate, br, zstd",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8",
    "connection": "keep-alive",
    # "cookie": "synct=1757226147.942; syncd=-1448; PHPSESSID=k8q4l2580krjef44boqaf77csc; qm_check=A1sdRUIQChtxen8pI0dANi8zcX5zHBl+YnEhLyZIPxw8WkVRVRliYGBFUldQSFkpYGd3YhkYBEBVVldYSk5KBx4SdFBCUVsRVSNZSVkMRmgHbwkQREs6UzhYVFk+BnMDARASGBoGDgILE1tAFwceABUAGAhJVkUV; gr_user_id=5eee11eb-6fc9-4f23-9c73-df85ad151686; ada35577182650f1_gr_session_id=3e412f43-2883-4924-9542-2e2f7def979e",  不检测cookie
    "host": "api.qimai.cn",
    "origin": "https://www.qimai.cn",
    "sec-ch-ua": "\"Google Chrome\";v=\"141\", \"Not?A_Brand\";v=\"8\", \"Chromium\";v=\"141\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36"
}
params = {
    "setting": 0,
    "genre": 36
}

params_for_analysis = {
    "url": "/indexV2/getIndexRank",
    "params": {
        "setting": params["setting"],
        "genre": str(params["genre"])
    },
    "baseURL": "https://api.qimai.cn",
}
with open('./解密.js', mode='r', encoding='utf-8') as f:
    js_code = f.read()
    js_func = execjs.compile(js_code)
    res = js_func.call("fn", params_for_analysis)

params["analysis"] = res

response = requests.get(url, headers=headers, params=params)
print(response.json())
