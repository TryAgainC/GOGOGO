import requests
import os
import base64

url = "https://in.mesl.cloud/api/v1/passport/auth/login"

headers = {
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36",
    # "accept-language" : "zh-CN,zh;q=0.9",
    # "referer" : "https://in.mesl.cloud"
}

#打开文件，批量获取MESL机场的账号
#以utf-8的格式打开文件
f = open("MESL邮箱.txt",encoding="utf-8")
q = open("MESL订阅链接.txt","w")
while True:
    email = f.readline()
    #判断email是不是空的，如果不是空的再继续操作
    if email:
        data = {
            "email": email,
            "password": "qweqweqwe"
        }

        resp = requests.post(url=url,headers=headers,data=data)

        #取出返回值的data里的token
        resp_token = resp.json()['data']['token']
        sub_lianjie = "https://in.mesl.cloud/api/v1/client/subscribe?token=" + resp_token
        q.write(sub_lianjie)
        #换行
        q.write('\n')
    else:
        break
q.close()
f.close()



# base64的解密和加密

o = open("MESL订阅链接.txt",encoding='utf-8')
l = open("base64解密.txt","wb+") #wb+打开会删光之前的内容

#解密，然后把订阅链接放一起
while True:
    url = o.readline()
    if url:
        #访问订阅链接，以'utf-8'拿到订阅链接的base64编码
        r = requests.get(url).content.decode('utf-8')
        #解码，把base64编码变成节点链接
        jiedian_link = base64.b64decode(r)
        #把拿到的节点链接写到一个文件里
        l.write(jiedian_link)
    else:
        break
o.close()
l.close()

#加密
w = open("base64解密.txt","rb+")
c = open("MESL","wb+")
str1 = w.read()
str64 = base64.b64encode(str1)
c.write(str64)

w.close()
c.close()
