import requests
import random
import time
import threading


url = "https://piercecloud.org/api/v1/passport/auth/register"

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:93.0) Gecko/20100101 Firefox/93.0'}

data = {
    "email": '4mn44zjz@idrrate.com',
    "password": "qweqweqwe",
    'email_code': '496032'
}

r = requests.post(url=url,headers=headers,data=data)

str = r.content

print(str)








