import csv
import re
import time
import random
from urllib import request
import pymysql


class Maoyan(object):
    def __init__(self):
        self.url = "https://maoyan.com/board/4?offset={}"
        self.ua_list = ['Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                        'Chrome/83.0.4103.61 Safari/537.36',
                        'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) '
                        'Version/5.1 Safari/534.50',
                        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) '
                        'Gecko/20100101 Firefox/4.0.1'
                        ]
        self.db = pymysql.connect(host="localhost", user="root", password="root", database="maoyan", charset="utf8")
        self.cursor = self.db.cursor()

    def get_url(self):
        start = int(input("请输入起始页："))
        for page in range(start, 3):
            pn = (page - 1) * 10
            url = self.url.format(pn)
            self.get_html(url)
            time.sleep(random.randint(1, 3))

    def get_html(self, url):
        headers = {'User-Agent': random.choice(self.ua_list)}
        req = request.Request(url=url, headers=headers)
        res = request.urlopen(req)
        html = res.read().decode('utf-8')
        self.get_data(html)

    def get_data(self, html):
        pattern = re.compile('<p class="name">.*?title="(.*?)".*?<p class="star">(.*?)</p>.*?time">(.*?)</p>', re.S)
        items = pattern.findall(html)
        self.save_data(items)

    def save_data(self, items):
        film_list = []
        ins = 'insert into maoyantop values(%s,%s,%s)'
        for item in items:
            one_film = [item[0], item[1].strip(), item[2].strip()[5:15]]
            film_list.append(one_film)
        self.cursor.executemany(ins, film_list)
        self.db.commit()

        # film_dict = {}
        # for item in items:
        #     film_dict['name'] = item[0].strip()
        #     film_dict['star'] = item[1].strip()
        #     film_dict['time'] = item[2].strip()
        # with open('maoyan.csv', 'a', newline='') as f:
        #     for item in items:
        #         writer = csv.writer(f)
        #         writer.writerow([item[0], item[1].strip(), item[2].strip()[5:15]])

        # film_list = []
        # with open('maoyan.csv', 'a') as f:
        #     writer = csv.writer(f)
        #     for item in items:
        #         t = (item[0],item[1].strip(),item[2].strip()[5:15])
        #         film_list.append(t)
        #     writer.writerows(film_list)

    def main(self):
        self.get_url()
        self.cursor.close()
        self.db.close()


if __name__ == "__main__":
    start = time.time()
    maoyan = Maoyan()
    maoyan.main()
    end = time.time()
    print("执行时间：%.2f" % (end - start))
