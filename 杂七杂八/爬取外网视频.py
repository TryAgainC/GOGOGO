import requests
import os
import random
import time

#文件合并  ：  copy b * a.ts
for i in range(999999999999999):
    # 1.准备url
    if(i<10):
        num = "000"+str(i)
    elif(i<100):
        num = "00" + str(i)
    else:
        num = "0" + str(i)
    url = "https://t17.cdn2020.com:12341/video/m3u8/2022/04/03/2ca9e288/"+num+".ts"

    path = "E:/temp/"+num+".ts"

    r = requests.get(url)
    if(r.status_code != 200):
        break
    with open(path, 'wb') as f:
        f.write(r.content)
        f.close()
    print(path,r.status_code)
