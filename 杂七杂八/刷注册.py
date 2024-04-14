import requests
import random
import time
import threading

def regist():
    url = "https://www.misiy.cc/api/v1/passport/auth/register"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:93.0) Gecko/20100101 Firefox/93.0'}

    qq_num = random.randint(1,999999999999)
    qq_email = "%d@qq.com" % qq_num

    data = {
        "email": qq_email,
        "password": "9999999999",
    }

    r = requests.post(url=url,headers=headers,data=data)
    now_time = time.strftime("%Y-%m-%d %X", time.localtime())
    print(qq_email,now_time,r)


while(True):
    t1 = threading.Thread(target=regist())
    t1.start()






