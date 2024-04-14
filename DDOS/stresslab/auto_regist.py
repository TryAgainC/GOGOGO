import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import ddddocr
from selenium.webdriver.common.by import By
import utils

for i in range(10):
    path = Service('./chromedriver.exe')
    driver = webdriver.Chrome(service=path)
    try:
        url = 'https://stresslab.su/u/register'
        # 生成随机账号密码
        username = utils.generate_random_string()
        pwd = username
        # 打开注册页面
        driver.get(url)
        driver.find_element(By.ID,'username').send_keys(username)
        driver.find_element(By.ID,'password').send_keys(pwd)
        driver.find_element(By.ID,'repassword').send_keys(pwd)
        driver.find_element(By.XPATH,'//*[@id="img"]').screenshot('regist.png')
        ocr = ddddocr.DdddOcr()
        with open('regist.png', 'rb') as fp:
            image = fp.read()
        # 拿到验证码catch
        catch = ocr.classification(image)
        driver.find_element(By.ID,'captcha').send_keys(catch)
        driver.find_element(By.ID,'toc').click()
        driver.find_element(By.ID,'_register').click()
        time.sleep(8)
        # 注册成功就不会再有这个regist的按钮了，所以报错代表注册成功
        driver.find_element(By.ID, '_register')
    except:
        filename = 'account'
        # 注册成功了，把账号写到account文件里
        text_to_write = [f"{username}\n"]
        # 打开文件，使用'a'模式表示追加模式，如果文件不存在将会被创建
        with open(filename, 'a') as file:
            # 遍历要写入的内容列表
            for line in text_to_write:
                # 写入内容，并确保每次写入后都会换到新的一行
                file.write(line)
    finally:
        driver.quit()

