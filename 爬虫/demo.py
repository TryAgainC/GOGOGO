import requests

for i in range(1,10):
    url = "https://api.shadiao.app/nmsl?level=max"
    # 访问api,得到返回值,是json
    resp = requests.get(url)

    # 把返回的值转换为json格式的数据
    json_data = resp.json()

    # 把中间需要的语句取出
    maren = json_data.get("data").get("text")

    print(maren)