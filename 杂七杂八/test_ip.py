import requests
proxies = {
    "https" : "https://220.248.70.237:9002"
}
url = "https://www.baidu.com/"

r = requests.get(url=url,proxies=proxies)

print(r.text)