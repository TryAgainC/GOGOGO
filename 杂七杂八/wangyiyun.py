import requests
import time
# while(True):

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:93.0) Gecko/20100101 Firefox/93.0'}

url="http://different-violet-fall.glitch.me/?do=daka"

cookie = "MUSIC_U=d36f3ecab23c2aa0d81224f305336d58ab859ce0b8b0467da2d095dfd95b5552993166e004087dd3d78b6050a17a35e705925a4e6992f61d07c385928f88e8de;__csrf=19a78231ac834083a6552e17f531e81d"

cookie_dict = {i.split("=")[0]:i.split("=")[-1] for i in cookie.split("; ")}

response = requests.get(url, headers = headers, cookies = cookie_dict)

    # time.sleep(28800)

# http://different-violet-fall.glitch.me/?do=login&uin=13599029430&pwd=4a56c90336f4da4c856907009cb5000d