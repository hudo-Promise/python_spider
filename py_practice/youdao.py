import requests
import json
import time
import random
from hashlib import md5


class Fanyi(object):
    def __init__(self):
        self.url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
        self.headers = {
            "Accept": "application/json, text/javascript, */*; q=0.01",
            # "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Connection": "keep-alive",
            "Content-Length": "251",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "Cookie": "_ntes_nnid=57bd9b79370638ab7dd994211f5548eb,1585290811458; OUTFOX_SEARCH_USER_ID_NCOO=444570591."
                      "2364726; OUTFOX_SEARCH_USER_ID=-589973386@115.33.64.136; JSESSIONID=aaa51g9u1jfB--E0Jg4kx; "
                      "___rl__"
                      "test__cookies=1592226723731",
            "Host": "fanyi.youdao.com",
            "Origin": "http://fanyi.youdao.com",
            "Referer": "http://fanyi.youdao.com/",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/"
                          "83.0.4103.97 Safari/537.36",
            "X-Requested-With": "XMLHttpRequest",
        }
        self.data = self.get_data()

    def get_data(self):
        word = input("请输入要翻译的内容：")
        ts = int(time.time() * 1000)
        salt = ts * 10 + random.randint(0, 9)
        sign = "fanyideskweb" + word + str(salt) + "mmbP%A-r6U3Nw(n]BjuEU"
        bianyi = md5()
        bianyi.update(sign.encode())
        sign_by = bianyi.hexdigest()
        data = {
            "i": word,
            "from": "AUTO",
            "to": "AUTO",
            "smartresult": "dict",
            "client": "fanyideskweb",
            "salt": salt,
            "sign": sign_by,
            "ts": ts,
            "bv": "c74c03c52496795b65595fdc27140f0f",
            "doctype": "json",
            "version": "2.1",
            "keyfrom": "fanyi.web",
            "action": "FY_BY_REALTlME",
        }
        return data

    def send_request(self):
        res = requests.post(url=self.url, data=self.data, headers=self.headers)
        res.encoding = 'utf-8'
        list = json.loads(res.text)
        self.get_result(list)

    def get_result(self, list):
        try:
            result = list['translateResult'][0][0]['tgt']
            print(result)
        except Exception as e:
            print("翻译不出来了，你要上天啊")
    def main(self):
        self.send_request()


if __name__ == '__main__':
    spider = Fanyi()
    spider.main()


