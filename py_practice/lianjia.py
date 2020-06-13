import requests
from lxml import etree
from py_practice import user_agent
import random
import pymysql
from copy import deepcopy


class Lianjia(object):
    def __init__(self):
        self.first_url = "https://bj.lianjia.com/ershoufang/"
        self.other_url = "https://bj.lianjia.com/ershoufang/pg{}"
        self.db = pymysql.connect(host="localhost", user="root", password="root", database="maoyan", charset="utf8")
        self.cursor = self.db.cursor()

    def parse_url(self):
        start_pn = int(input("开始页："))
        end_pn = int(input("结束页："))
        if start_pn == 1:
            self.get_html(self.first_url)
            for i in range(start_pn + 1, end_pn):
                self.get_html(self.other_url.format(i))
        else:
            for i in range(start_pn, end_pn):
                self.get_html(self.other_url.format(i))

    def get_html(self, url):
        req = requests.get(url, headers={"User-Agent": random.choice(user_agent.ua_list)})
        req.encoding = 'utf-8'
        html = req.text
        self.parse_data(html)

    def parse_data(self, html):
        dict = {}
        items = []
        r_list = etree.HTML(html)
        name_list = r_list.xpath('//div[@class="title"]/a/text()')
        house_list = r_list.xpath('//div[@class="address"]/div/text()')
        total_price = r_list.xpath('//div[@class="priceInfo"]/div[@class="totalPrice"]/span/text()')
        unit_price = r_list.xpath('//div[@class="priceInfo"]/div[@class="unitPrice"]//text()')
        for i in range(0, len(name_list)):
            dict["name"] = name_list[i]
            dict["house"] = house_list[i]
            dict["totalPrice"] = total_price[i] + "万"
            dict["unitPrice"] = unit_price[i]
            items.append(deepcopy(dict))
        print(items)
        self.save_data(items)

    def save_data(self, items):
        data_list = []
        ins = 'insert into esflianjia values(%s,%s,%s,%s)'
        for i in items:
            one_data = [i["name"], i["house"], i["totalPrice"], i["unitPrice"]]
            data_list.append(one_data)

        self.cursor.executemany(ins, data_list)
        self.db.commit()

    def main(self):
        self.parse_url()
        self.cursor.close()
        self.db.close()


if __name__ == "__main__":
    lianjia = Lianjia()
    lianjia.main()
