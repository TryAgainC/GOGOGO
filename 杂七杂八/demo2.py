import requests
import random
import time
import threading

def login():

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36',
        'auth_data': "MTc2ODExOTIwMEBxcS5jb206JDJ5JDEwJEFIYlZyWFNHdGovZUNIVUI3S25hdi5BZy52bXpubWxkWjA4N3RhNG5NWWFLTkRYOWs0WWVP",
        'token': "eae71a9d5be875c40aaa67d536f5d70c"
            }


    url = "https://72vpn.xyz/api/v1/passport/auth/register"
    r = requests.get(url,headers)


    print(r,r.text,r.content)

while(True):
    t1 = threading.Thread(target=login())
    t1.start()