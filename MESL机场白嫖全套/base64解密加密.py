# import base64
# import requests
#
# f = open("订阅链接.txt",encoding='utf-8')
# q = open("base64解密.txt","wb+") #wb+打开会删光之前的内容
#
# #解密，然后把订阅链接放一起
# while True:
#     url = f.readline()
#     if url:
#         #访问订阅链接，以'utf-8'拿到订阅链接的base64编码
#         r = requests.get(url).content.decode('utf-8')
#         #解码，把base64编码变成节点链接
#         jiedian_link = base64.b64decode(r)
#         #把拿到的节点链接写到一个文件里
#         q.write(jiedian_link)
#     else:
#         break
# f.close()
# q.close()
#
# #加密
# w = open("base64解密.txt","rb+")
# c = open("MESL","wb+")
# str1 = w.read()
# str64 = base64.b64encode(str1)
# c.write(str64)
#
# w.close()
# c.close()
