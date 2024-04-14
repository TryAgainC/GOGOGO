import requests
import random
import threading

#机场地址:https://in.mesl.cloud


url_sendemail = 'https://in.mesl.cloud/api/v1/passport/comm/sendEmailVerify'

email = input("输入邮箱:")

data_sendemail = {
    'email' : email
}

r1 = requests.post(url_sendemail,data_sendemail)

print(email,r1)

email_code = input("请输入验证码:")

url_regist= 'https://in.mesl.cloud/api/v1/passport/auth/register'

data_regist = {
    'email' : email,
    'password' : 'qweqweqwe',
    'email_code' : email_code
}

r2 = requests.post(url_regist,data_regist)

if (r2.status_code == 200):
    f = open("MESL邮箱.txt", "a+")
    f.write(email)
    f.write('\n')
    f.close()


