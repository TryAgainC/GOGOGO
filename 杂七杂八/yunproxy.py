import requests
import parsel
import time

file =open("proxy.txt", "a+")
for i in range(1,8):
    # time.sleep(1)
    url = f'http://www.ip3366.net/free/?stype=1&page={i}'
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:93.0) Gecko/20100101 Firefox/93.0'}

    r = requests.get(url=url,headers=headers)
    html_data = r.text

    selctor = parsel.Selector(html_data)
    trs = selctor.xpath('//table[@class="table table-bordered table-striped"]/tbody/tr')

    for tr in trs:
        ip_num = tr.xpath('./td[1]/text()').get()
        ip_port = tr.xpath('./td[2]/text()').get()
        ip = ip_num +":"+ip_port
        file.write(ip+'\n')
for j in range(1,8):
    # time.sleep(1)
    url = f'http://www.ip3366.net/free/?stype=2&page={j}'
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:93.0) Gecko/20100101 Firefox/93.0'}

    r = requests.get(url=url,headers=headers)
    html_data = r.text

    selctor = parsel.Selector(html_data)
    trs = selctor.xpath('//table[@class="table table-bordered table-striped"]/tbody/tr')

    for tr in trs:
        ip_num = tr.xpath('./td[1]/text()').get()
        ip_port = tr.xpath('./td[2]/text()').get()
        ip = ip_num +":"+ip_port
        file.write(ip+'\n')
file.close()
