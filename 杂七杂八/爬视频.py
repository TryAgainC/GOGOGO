import requests
import os
import random
import time

headers = {
    'Connection':'Keep-Alive',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:93.0) Gecko/20100101 Firefox/93.0'
}
try:
    for i in range(999999999999999):
        # 1.准备url
        url = "https://z.weilekangnet.com:59666/data6/2E6EFEB76A6934A9/BFE28AC54F62723C/ts1/out%d.ts" % i
        # 视频存放位置
        root = "E:\cartiernn"
        if(i<10):
            # 抓取文件起的名字
            path = root + "\ 00%d.ts" % i
            print(path)
        elif(i<100):
            path = root + "\ 0%d.ts" % i
            print(path)
        else:
            path = root + "\ %d.ts" % i
            print(path)
        if not os.path.exists(root):
            # 如果该目录不存在就创建它
            os.mkdir(root)
        if not os.path.exists(path):
            # 获取到目标视频的所有信息
            r = requests.get(url,headers)
            if(r.status_code != 200):
                break
            # 打印访问的状态码是否为200
            print(r.status_code)
            # 以二进制写的方式将r的二进制内容写入path
            with open(path, 'wb') as f:
                f.write(r.content)
                f.close()
                print("文件保存成功")
        else:
            print("文件已存在")
except:
    print("爬取失败")

