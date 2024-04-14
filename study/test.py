import requests
from selenium import webdriver

url = 'https://caf.huanqiutong.ciecinfo.com/index?_code=5KgUxExppbhNK7N5JZCyomHjevenRqnZA33QcrYgOHGaT1jDwlS8b4kLdf2cY0WU'

r = requests.get(url).text
print(r)
