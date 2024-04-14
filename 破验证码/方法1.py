import uuid

from PIL import Image
# 导入基于 Tesseract 的文字识别模块 pytesseract
import pytesseract
import requests
import random
"""
@pytesseract：https://github.com/madmaze/pytesseract
"""
session = requests.session()
r = session.get("https://shop.tingyutech.ml/user/captcha/image?action=register")

uuids = uuid.uuid1()

# 打开图片
path = "E:\pythonProject1\image\%d.png" % uuids

with open(path, 'wb') as f:
    f.write(r.content)
    f.close()
im = Image.open("image\%d.png")  % uuids

# 识别图片内容
text = pytesseract.image_to_string(im)

captcha = text.strip()

print(captcha)

qq_num = random.randint(1,999999999999)
qq_password = random.randint(1,999999999999)
data = {
    'username' : qq_num,
    'password' : qq_password,
    'captcha' : captcha
}

resp = session.post("https://shop.tingyutech.ml/user/api/authentication/register",data=data)

print(qq_num,qq_password)

