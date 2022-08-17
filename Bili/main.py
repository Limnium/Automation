import requests, json, os, time

if __name__ == '__main__':
    cookie = os.environ["BILI_COOKIE"]
    headers={   
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36',
    'Cookie':cookie
    }
    response = requests.session().get('http://api.bilibili.com/x/space/myinfo',headers=headers)
    rejson = json.loads(response.text)
    code = rejson['code']
    msg = rejson['message']
    if code == 0:
        print(time.strftime("%H:%M:%S", time.localtime())+'登录成功')
    else:
        raise Exception(time.strftime("%H:%M:%S", time.localtime())+'哔哩哔哩签到失败')
