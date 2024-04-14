import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import ddddocr
from selenium.webdriver.common.by import By
import methods
for i in range(29):
    try:
        username = methods.generate_number()
        pwd = username

        service = Service('chromedriver.exe')
        driver = webdriver.Chrome(service=service)
        driver.implicitly_wait(10)
        driver.get('https://stresser.su/register')
        time.sleep(3)
        driver.find_element(By.NAME,'username').send_keys(username)
        driver.find_element(By.NAME,'password').send_keys(pwd)
        time.sleep(10)
        driver.find_element(By.XPATH, '/html/body/div/div/div[2]/div/div/div/div/section/div/div[2]/form/div[6]/div/img').screenshot('code_regist.png')
        time.sleep(2)
        # 用ddddocr来识别内容
        ocr = ddddocr.DdddOcr()
        with open('code_regist.png', 'rb') as fp:
            image = fp.read()
        # 拿到验证码catch
        catch = ocr.classification(image)
        driver.find_element(By.NAME,'captcha').send_keys(catch)
        time.sleep(10)
        driver.find_element(By.XPATH,'/html/body/div/div/div[2]/div/div/div/div/section/div/div[2]/form/div[8]/button').click()
        time.sleep(10)
        driver.find_element(By.XPATH,'/html/body/div/div/div[2]/div/div/div/div/section/div/div[2]/form/div[8]/button').click()
        continue
    except:
        pass

    # 定义要写入的文件名
    filename = "hao.txt"

    # 定义要写入的内容
    text_to_write = [f"{username}\n"]

    # 打开文件，使用'a'模式表示追加模式，如果文件不存在将会被创建
    with open(filename, 'a') as file:
        # 遍历要写入的内容列表
        for line in text_to_write:
            # 写入内容，并确保每次写入后都会换到新的一行
            file.write(line)



    driver.quit()
















