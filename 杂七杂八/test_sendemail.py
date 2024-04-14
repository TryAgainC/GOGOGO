import requests
import os
import random
import threading



url = 'https://piercecloud.org/api/v1/passport/comm/sendEmailVerify'

data = {
    'email' : '4mn44zjz@idrrate.com'
}

r = requests.post(url,data)

print(r)




