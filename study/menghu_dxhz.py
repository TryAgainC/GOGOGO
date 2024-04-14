import requests
import time
while(True):
    time.sleep(5)
    phone1 = 18610309118
    phone2 = 18055484729
    phone3 = 15232669970
    phone = [phone1,phone2,phone3]

    url_list = 'http://mehu.65n.icu/index/ajax/order/act/list.html?page=1&limit=15'

    headers = {
        "cookie": "PHPSESSID=de5391b09d6ecea94d5b88571ab36ae9; Let_IndexUsername=953777955; Let_IndexPassword=747a941d40a04442f4bb668de8772f1d; Hm_lvt_d97abf6d61c21d773f97835defbdef4e=1712252900; Hm_lpvt_d97abf6d61c21d773f97835defbdef4e=1712252964",
    }
    try:
        rp_json = requests.get(url=url_list,headers=headers).json()

        time_list = int(rp_json.get('data')[0].get('time'))
    except Exception as e:
        flag = False
    else:
        flag = time_list != 0


    if flag:
        continue
    else:
        url_add = 'http://mehu.65n.icu/index/ajax/order/act/add.html'

        for i in range(3):
            time.sleep(3)
            data = {
                'phone' : phone[i],
                'time' : 20
            }

            resp = requests.post(url=url_add,headers=headers,data=data)

