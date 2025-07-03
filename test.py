import json
from urllib.parse import quote

aa = json.dumps({
    "cityId": "2501",
    "serialId": "11108"
}, separators=(',', ':'))

print(aa)
print(quote(aa))
