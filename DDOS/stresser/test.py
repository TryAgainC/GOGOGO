
# DDOS
# 网站：https://stresser.su

import ddddocr

ocr = ddddocr.DdddOcr()
with open('code.png', 'rb') as fp:
    image = fp.read()
# 拿到验证码catch
catch = ocr.classification(image)

print(catch)