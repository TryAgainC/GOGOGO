import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
def dxhz_bingfeng(phonenum):
    try:
        service = Service('./chromedriver.exe')
        driver = webdriver.Chrome(service=service)
        driver.get('https://love666.link/index/index/login.html')
        wait = WebDriverWait(driver, 10)
        try:
            driver.find_element(By.ID,'access').click()
        except:
            pass
        wait.until(EC.visibility_of_element_located((By.NAME, "username")))
        driver.find_element(By.NAME,'username').send_keys('953777955')
        driver.find_element(By.NAME,'password').send_keys('qweqweqwe')
        driver.find_element(By.XPATH,'/html/body/div/div/form/div[5]/button').click()

        wait.until(EC.visibility_of_element_located((By.NAME, "phone")))
        driver.find_element(By.NAME, 'phone').send_keys(phonenum)
        driver.find_element(By.NAME, 'time').send_keys('10')
        time.sleep(3)
        driver.find_element(By.XPATH,'/html/body/div[1]/div[5]/div[2]/div[2]/div/div/div[1]/div/div[1]/form/div/div[3]/button').click()
        driver.quit()
        return '[冰封]提交成功'
    except:
        return '[冰封]提交失败'




a = dxhz_bingfeng('13985764518')
print(a)