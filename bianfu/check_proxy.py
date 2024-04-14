import requests

# 小象代理的api
url_xiaoxiang = 'https://api.xiaoxiangdaili.com/ip/get?appKey=1095776986175262720&appSecret=RNiO642t&cnt=1&wt=text&method=https&city=&province='

# 验证ip的链接
url = 'https://www.ipuu.net/ipuu/user/getIP'

r = requests.get(url_xiaoxiang).text


proxys = {
    # 'https' : '42.236.73.11:45367'   117.147.96.22
    # 'https' : '42.236.82.20:45336'
    'https': r
}

print(requests.get(url=url, proxies=proxys).text)

