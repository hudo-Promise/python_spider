# 多线程适合I/O操作比较多的场景
# 改多进程  改模块 from mulitprocess import process 改语句 Thread --> Process
from copy import deepcopy
from threading import Thread
import requests
import random
from queue import Queue
import json


class xiaomiSpider(object):
    def __init__(self):
        self.url = 'http://app.mi.com/categotyAllListApi?page={}&categoryId=15&pageSize=30'
        self.headers = {"User-Agent": ""}
        self.url_queue = Queue()

    def url_in(self):
        for i in range(10):
            url = self.url.format(i)
            self.url_queue.put(url)

    def get_data(self):
        while True:
            if not self.url_queue.empty():
                url = self.url_queue.get()
                html = requests.get(
                    url=url,
                    headers=self.headers
                ).content.decode('utf-8')
                html = json.loads(html)
                app_dict = {}
                for app in html['data']:
                    app_dict['app_name'] = app['displayName']
                    app_dict['app_link'] = "http://app.mi.com/details?id=" + app["packageName"]
                self.save_data(deepcopy(app_dict))
            else:
                break

    def save_data(self, app_dict):
        print(app_dict)


    def main(self):
        # url入队列
        self.url_in()
        # 创建多线程
        t_list = []
        for i in range(5):
            t = Thread(target=self.get_data())
            t_list.append(t)
            t.start()

        for i in t_list:
            i.join()


if __name__ == "__main__":
    spider = xiaomiSpider()
    spider.main()