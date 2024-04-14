
import requests

file = open("maren_yulu.txt", "a+", encoding="utf-8")
for i in range(1, 30000):
    # url = 'https://api.shadiao.app/nmsl?level=max'
    # yang = requests.get(url)  # 这里返回的json数据
    # result = open('a.txt', 'w')
    # result.write(yang.text)  # yang.text将yang这个json数据以字符形式使用
    # result.close()  # 这里一定要关闭文件，不然写不进去
    # open_json = open('a.txt', 'r', encoding='utf-8')
    # zd_json = json.loads(open_json)  # json.load()将json转为python字典
    # open_json.close()  # 到这里zd_json是一个python字典
    url = "https://api.oddfar.com/yl/q.php?c=1009&encode=text"
    yulu = str(requests.get(url).text)
    file.write(yulu + "\n")
file.close()
        # url = "https://nmsl.shadiao.app/api.php?level=min&lang=zh_cn"



