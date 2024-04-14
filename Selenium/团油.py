import requests
import time
from  selenium.webdriver.common.by import  By
from selenium import webdriver
import json
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service


service = Service('./chromedriver.exe')
driver = webdriver.Chrome(service=service)

login_url = 'https://gs.newlink.com/login'

driver.get(login_url)
driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div/div/form/div[1]/div/div/input').send_keys('rongshi')
driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div/div/form/div[2]/div/div/input').send_keys('rongshi2023')
driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div/div/form/div[5]/div/button').click()
time.sleep(3)

jiaoban_url = 'https://gs.newlink.com/handover/handoverRecord'
driver.get(jiaoban_url)
driver.find_element(By.XPATH,'/html/body/div[1]/div/div[2]/section/div/div[2]/div/div[1]/div[4]/div[2]/table/tbody/tr[1]/td[12]/div/div/button[1]/span').click()
a = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[2]/section/div/div[4]/div[3]/div/div[7]/div')

print(a)
print(type(a))

time.sleep(2)
driver.quit()

