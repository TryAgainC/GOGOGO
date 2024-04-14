import uuid
import requests
import random
import ddddocr
import threading
import os
"""
@pytesseract：https://github.com/madmaze/pytesseract
"""
def regist():
    uuids = str(uuid.uuid1())
    session = requests.session()
    r = session.get("https://shop.tingyutech.ml/user/captcha/image?action=register")
    # 打开图片
    path = "../image/" + uuids + ".png"

    with open(path, 'wb') as f:
        f.write(r.content)
        f.close()

    ocr = ddddocr.DdddOcr()
    with open(path, 'rb') as f:
        img_bytes = f.read()
    captcha = ocr.classification(img_bytes)

    qq_num = random.randint(1,999999999999)
    qq_password = random.randint(1,999999999999)
    data = {
        'username' : qq_num,
        'password' : qq_password,
        'captcha' : captcha
    }

    resp = session.post("https://shop.tingyutech.ml/user/api/authentication/register",data=data)
    os.remove(path)
    print(qq_num,qq_password,captcha)

while(True):
    t1 = threading.Thread(target=regist())
    t1.start()
