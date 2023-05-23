import json
import time
import requests


def get_pic(prompt, style='2'):
    s = requests.session()
    login_url = 'https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key' \
                '=AIzaSyDCvp5MTJLUdtBYEKYWXJrlLzu1zuKM6Xw '
    url = 'https://paint.api.wombo.ai/api/tasks/'
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
    }
    payload = {
        "returnSecureToken": True,
        "email": "zinan2inc@163.com",
        "password": "crzinan666"
    }
    payload = json.dumps(payload)
    login_respone = s.request('POST', url=login_url, headers=headers, data=payload)
    idtoken = login_respone.json()['idToken']
    headers['authorization'] = 'bearer ' + idtoken
    respone = s.request('POST', url=url, headers=headers)
    new_headers = respone.json()
    print(new_headers)
    new_id = new_headers['id']
    param = {
        'input_spec': {
            "style": str(style),
            "prompt": prompt,
            "display_freq": '10'
        }
    }
    param = json.dumps(param)
    respone2 = s.put(url=url + new_id, headers=headers, data=param)
    result = respone2.json()
    while True:
        time.sleep(4)
        respone2 = s.request('GET', url=url + new_id, headers=headers, data=new_headers)
        result = respone2.json()
        print(result)
        if result['result'] is not None:
            break
    pic_url = result['result']['final']
    pic = s.request('GET', url=pic_url, headers=headers).content
    img_path = 'test.jpg'
    with open(img_path, 'wb') as f:
        f.write(pic)
    print('下载完毕')


if __name__ == '__main__':
    get_pic("千钟美酒，一曲满庭芳", '10')