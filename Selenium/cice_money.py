import requests
import time
from  selenium.webdriver.common.by import  By
from selenium import webdriver
import json
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

# 中能源后台充值金额：用selenium模拟登陆，获取cookie，然后用获取到的cookie去查询充值金额

#无头模式（linux可用）：
# chrome_options = Options()
# chrome_options.add_argument("--headless")  # 运行无头版本的Chrome
# chrome_options.add_argument("ignore-certificate-erros")  # 忽略证书错误
# chrome_options.add_argument("--no-sandbox")  # 在无沙盒模式下运行
# chrome_options.add_argument("--disable-dev-shm-usage")  # overcome limited
# driver = webdriver.Chrome(options=chrome_options)



service = Service('./chromedriver.exe')
driver = webdriver.Chrome(service=service)
# 3. 打开登录页面
login_url = "https://mp.huanqiutong.ciecinfo.com"  # 替换为实际的登录页面URL
driver.get(login_url)

time.sleep(3)

# 4. 定位并填充登录表单
username_field = driver.find_element(By.ID, "account")  # 替换为实际的用户名字段名
password_field = driver.find_element(By.ID, "password")  # 替换为实际的密码字段名
username_field.send_keys("admin@rongshi")  # 替换为你的用户名
password_field.send_keys("Rs110119120")  # 替换为你的密码
# 5. 提交表单
login_button = driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/div[1]/div[2]")  # 替换为实际的登录按钮XPath
login_button.click()

time.sleep(3)

cookies = driver.get_cookies()

# 获取特定名称的cookie
laravel_session_cookie = next((cookie for cookie in cookies if cookie['name'] == 'laravel_session'), None)
PHPSESSID_cookie = next((cookie for cookie in cookies if cookie['name'] == 'PHPSESSID'), None)
SERVERID_cookie = next((cookie for cookie in cookies if cookie['name'] == 'SERVERID'), None)

laravel_session = laravel_session_cookie['value']
PHPSESSID = PHPSESSID_cookie['value']
SERVERID = SERVERID_cookie['value']

cookie = f"PHPSESSID={PHPSESSID};laravel_session={laravel_session};SERVERID={SERVERID}"

url = 'https://caf.huanqiutong.ciecinfo.com/api/cardApi/CardHome/getBalanceSummary'
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
    'cookie':cookie
}

json_str = requests.post(url=url,headers=headers).json().get('data')

# 使用json模块的loads函数将字符串解析为Python对象（列表）
data = json.loads(json_str)
# 遍历解析后的数据列表
for entry in data:
    balance = entry["Balance"]
    requests.get(f'https://api.day.app/LzKC6mQqMS3aKiX2RA3MML/中能源后台充值金额/{balance}')
    break  # 如果只需要第一个匹配项，可以在这里使用break来退出循环


driver.quit()

