import time
import requests
from  selenium.webdriver.common.by import  By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import ddddocr
from selenium.webdriver.common.proxy import Proxy, ProxyType
import test

# 创建随机账号密码
usrName = test.generate_number()
pwd = test.generate_password()

# 获取代理ip
# url_xiaoxiang = 'https://api.xiaoxiangdaili.com/ip/get?appKey=1095776986175262720&appSecret=RNiO642t&cnt=1&wt=text&method=https&city=&province='
url_xiaoxiang = 'https://api.xiaoxiangdaili.com/ip/get?appKey=1095788822345961472&appSecret=OR76Uxa7&cnt=1&wt=text&method=https&city=&province='
proxy_ip = requests.get(url=url_xiaoxiang).text

# 设置代理ip
proxy = Proxy()
proxy.proxy_type = ProxyType.MANUAL
# proxy.http_proxy = f"{proxy_ip}:{proxy_port}"
proxy.http_prox = proxy_ip
proxy.ssl_proxy = proxy_ip
Chrome_options = webdriver.ChromeOptions()
Chrome_options.add_argument(f"--proxy-server=http://{proxy_ip}")

url = 'https://www.ipuu.net/ipuu/user/getIP'

proxys = {
    # 'https' : '42.236.73.11:45367'   117.147.96.22
    # 'https' : '42.236.82.20:45336'
    'https': proxy_ip
}

print(requests.get(url=url, proxies=proxys).text)

service = Service('./chromedriver.exe')
driver = webdriver.Chrome(service=service,options=Chrome_options)
driver.get('http://www.bfsms.xyz/')
time.sleep(3)
# 先看下有没有注册的按钮，有的话说明在登陆页面，先跳转到注册页面
try:
    driver.find_element(By.ID,'rg').click()
except:
    pass

driver.find_element(By.ID,'userName').send_keys(usrName)
driver.find_element(By.ID,'password').send_keys(pwd)
driver.find_element(By.ID,'password2').send_keys(pwd)
time.sleep(5)
# 抓到验证码，并且截图
driver.find_element(By.XPATH,'/html/body/div/div/div/div/form/div[4]/img').screenshot('code.png')
time.sleep(1)
# 用ddddocr来识别内容
ocr = ddddocr.DdddOcr()
with open('code.png','rb') as fp:
    image = fp.read()
# 只保留后四位，拿到验证码传到catch
catch = ocr.classification(image)[-4:]
driver.find_element(By.ID,'imagecode').send_keys(catch)
time.sleep(1)
driver.find_element(By.ID,'reg').click()

time.sleep(1)
# 登陆

driver.get(f'https://www.bfsms.xyz/weblogin?userName={usrName}&password={pwd}&loginType=login&type=sms1')
time.sleep(3)
driver.find_element(By.XPATH,'/html/body/div[3]/div/div[2]/div/button').click()
driver.find_element(By.ID,'phoneNumber').send_keys(phone)
time.sleep(1)
driver.find_element(By.ID,'sendButton').click()
time.sleep(2)
driver.save_screenshot('msg.png')

time.sleep(30)

driver.quit()

