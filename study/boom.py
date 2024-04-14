import requests

#pyinstaller --onefile xxx.py  把xxx.py打包成.exe文件可以直接执行  C:\Users\小蔡\Desktop

#pyinstaller  hz_robot.py --distpath=C:\Users\小蔡\Desktop  //制定输出位置(桌面)

pwd_url = 'https://gitee.com/czt953777956/pwd/raw/master/password'

pwd = requests.get(url=pwd_url).text

password = input("请输入密码：\n")


if password == pwd:
    phonenum = input("请输入手机号：\n")

    url = 'http://www.hongzhaji.top/index/ajax/order/act/add.html'

    headers = {

        "cookie": "Let_IndexUsername=953777956; Let_IndexPassword=747a941d40a04442f4bb668de8772f1d; guard=9fa5e92dgGiT99; mk_encrypt_c21f969b5f03d33d43e04f8f136e7682=12e2de20d36b3ef894ea1e88e97b5c05; PHPSESSID=37b4f225d08bb5ecba616aaabeceda16; Hm_lvt_d97abf6d61c21d773f97835defbdef4e=1711347727,1711349456,1711889822; Hm_lpvt_d97abf6d61c21d773f97835defbdef4e=1711889822",

    }

    data = {
        'phone' : phonenum
    }

    json_respon = requests.post(url,headers=headers,data=data).json()

    msg = json_respon.get("msg")

    print(msg)
else:
    print('密码错误')