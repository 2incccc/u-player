#一言
import requests
import json

api_url = 'https://v1.hitokoto.cn/?c=b&encode=json'
response = requests.get(api_url)
res = json.loads(response.text)
a_word = res['hitokoto']+' _____'+'《'+res['from']+'》'
print(a_word)
pause = input()