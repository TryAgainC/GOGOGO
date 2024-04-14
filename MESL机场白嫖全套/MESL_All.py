import random
from lxml import etree
import re
import requests
import time
import base64

#机场地址:https://in.mesl.cloud

for i in range(1,6):
    #1.申请邮箱
    def apply_email(email):
        url = "https://rootsh.com/applymail"
        payload = "mail={}%40bccto.cc".format(email)
        headers = {
            'cookie': '__gads=ID=b9092103f6ab5d78-229b55f2eede0075:T=1680229261:RT=1680229261:S=ALNI_MY7Do4zbhh9NOQhai5ENppyXTnmbA; __gpi=UID=00000be91ff53173:T=1680229261:RT=1680229261:S=ALNI_MYsdTIOV-rDipmcNcvbIIu6Y5jZow; mail="2|1:0|10:1680229282|4:mail|36:Y2M5OTIzQGJjY3RvLmNjfDE2ODAyMjkyODI=|1c9d225d19571ef9afaf360f895c6a24ece684d526be8a4503c55b290712b7d8"; time="2|1:0|10:1680229282|4:time|16:MTY4MDIyOTI4Mg==|84f17c4117b2da4fd902b2641bb6be7d3106f8a87d5ee7188f8d1b75485f3245"',
            'origin': 'https://rootsh.com',
            'accept-language': 'zh-CN,zh;q=0.9',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3877.400 QQBrowser/10.8.4533.400 chrome-extension',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',

        }
        try:
            response = requests.post(url, headers=headers, data=payload).json()
            if response['success'] == 'true':
                print("临时邮箱：{}@bccto.cc，申请成功！".format(email))
        except:
            print("临时邮箱：{}@bccto.cc，申请失败！".format(email))
    ema = random.randint(1, 9999999)
    email = str(ema)
    apply_email(email)

    #2.发送邮件
    url_sendemail = 'https://in.mesl.cloud/api/v1/passport/comm/sendEmailVerify'

    data_sendemail = {
        'email' : email+'@bccto.cc'
    }

    r1 = requests.post(url_sendemail,data_sendemail)

    print(email,r1)

    #3.获取验证码
    def get_email(email):
        url = "https://rootsh.com/getmail"
        payload = "mail={}%40bccto.cc".format(email)
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        }

        try:
            for i in range(1,10):
                time.sleep(6)
                resp = requests.post(url, headers=headers, data=payload).text
                # 验证有没有收到邮件，收到邮件的话，没有收到邮件就只有一个[
                a = resp.count('[')
                if a!=1:
                    response = requests.post(url, headers=headers, data=payload).json()
                    uid = response["mail"][0][-2]
                    return pase_html(email, uid)
                else:
                    continue
        except:
            pass


    # 解析html
    def pase_html(email, uid):
        url = "https://rootsh.com/win/{}(a)bccto-_-cc/{}".format(email, uid)
        print(url)
        headers = {

            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-language': 'zh-CN,zh;q=0.9'
        }
        html = requests.get(url, headers=headers).content
        dom = etree.HTML(html)

        div1 = dom.xpath("/html/body/div/table/tbody/tr/td/div[1]/table/tbody/tr[2]/td/text()")

        str2=''.join(div1)

        #把取出来的字符串的数字拿出来
        num = re.findall(r'\d', str2)
        #去掉最后一个数字(因为最后一个数字是验证时间)
        num.pop()
        #把列表合成一个字符串
        final_num = ''.join(num)
        print(final_num)
        return final_num

    #拿到验证码
    final_num = get_email(email)


    #4.注册
    url_regist= 'https://in.mesl.cloud/api/v1/passport/auth/register'

    data_regist = {
        'email' : email+'@bccto.cc',
        'password' : 'qweqweqwe',
        'email_code' : final_num
    }

    r2 = requests.post(url_regist,data_regist)

    if (r2.status_code == 200):
        f = open("MESL邮箱.txt", "a+")
        f.write(email+"@bccto.cc")
        f.write('\n')
        f.close()

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


