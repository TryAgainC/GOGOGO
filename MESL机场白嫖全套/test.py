from lxml import etree
import re
import requests

# 由于网站规则：@bccto.cc 邮箱名只支持字母和数字
def apply_email(email):
    url = "https://rootsh.com/applymail"
    payload = "mail={}%40bccto.cc".format(email)
    headers = {
        'cookie': '__gads=ID=b9092103f6ab5d78-229b55f2eede0075:T=1680229261:RT=1680229261:S=ALNI_MY7Do4zbhh9NOQhai5ENppyXTnmbA; __gpi=UID=00000be91ff53173:T=1680229261:RT=1680229261:S=ALNI_MYsdTIOV-rDipmcNcvbIIu6Y5jZow; mail="2|1:0|10:1680229282|4:mail|36:Y2M5OTIzQGJjY3RvLmNjfDE2ODAyMjkyODI=|1c9d225d19571ef9afaf360f895c6a24ece684d526be8a4503c55b290712b7d8"; time="2|1:0|10:1680229282|4:time|16:MTY4MDIyOTI4Mg==|84f17c4117b2da4fd902b2641bb6be7d3106f8a87d5ee7188f8d1b75485f3245"',
        'origin': 'https://rootsh.com',
        'accept-language': 'zh-CN,zh;q=0.9',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3877.400 QQBrowser/10.8.4533.400 chrome-extension',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',

    }
    try:
        response = requests.post(url, headers=headers, data=payload).json()
        if response['success'] == 'true':
            print("临时邮箱：{}@bccto.cc，申请成功！".format(email))
    except:
        print("临时邮箱：{}@bccto.cc，申请失败！".format(email))
email = 'aa996'
apply_email(email)


# 获取邮件
def get_email(email):
    url = "https://rootsh.com/getmail"
    payload = "mail={}%40bccto.cc".format(email)
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    }

    try:
        response = requests.post(url, headers=headers, data=payload).json()
        uid = response["mail"][0][-2]
        return pase_html(email, uid)
    except:
        pass


# 解析html
def pase_html(email, uid):
    url = "https://rootsh.com/win/{}(a)bccto-_-cc/{}".format(email, uid)
    print(url)
    headers = {

        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-language': 'zh-CN,zh;q=0.9'
    }
    html = requests.get(url, headers=headers).content
    dom = etree.HTML(html)

    div1 = dom.xpath("/html/body/div/table/tbody/tr/td/div[1]/table/tbody/tr[2]/td/text()")

    str2=''.join(div1)

    #把取出来的字符串的数字拿出来
    num = re.findall(r'\d', str2)
    #去掉最后一个数字(因为最后一个数字是验证时间)
    num.pop()
    #把列表合成一个字符串
    final_num = ''.join(num)
    print(final_num)
    return final_num

a = get_email(email)
print(a,type(a))