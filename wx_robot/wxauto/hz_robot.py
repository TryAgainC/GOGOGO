from wxauto import *
import time
import requests
#pyinstaller  hz_robot.py --distpath=C:\Users\小蔡\Desktop  //制定输出位置(桌面)
wx = WeChat()

# who = '相亲相爱眯眯眼'
# wx.AddListenChat(who=who, savepic=False)

who = [
    '相亲相爱眯眯眼',
    '辉'
]
for i in who:
    # 添加监听对象
    wx.AddListenChat(who=i, savepic=False)

hz_url = 'http://mehu.65n.icu/index/ajax/order/act/add.html'

headers = {
    "cookie": "Let_IndexUsername=953777955; Let_IndexPassword=747a941d40a04442f4bb668de8772f1d; PHPSESSID=ec9065d35f2192dcd8d58175ed12557a; Hm_lvt_d97abf6d61c21d773f97835defbdef4e=1712252900,1712332022; Hm_lpvt_d97abf6d61c21d773f97835defbdef4e=1712332022",
}

wait = 1
while True:
    msgs = wx.GetListenMessage()
    for chat in msgs:
        msg = msgs.get(chat)
        print(msg)
        # 获取每个人发的消息
        hz_num = msg[-1][1]
        print(hz_num)
        # 判断字符串里是不是全数字
        flag = wxauto.is_all_digits(hz_num)
        if flag:
            if len(hz_num) == 11:
                data = {
                    'phone' : hz_num,
                    'time' : 5
                }
                rp = requests.post(url=hz_url,headers=headers,data=data).json().get('msg')
                chat.SendMsg(rp)

    time.sleep(wait)


