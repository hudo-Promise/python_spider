from urllib import request
import re
import time
import random
from py_practice import user_agent


class Dytt(object):
    def __init__(self):
        self.first_url = "https://www.dygod.net/html/gndy/dyzz/index.html"
        self.not_first_url = "https://www.dygod.net/html/gndy/dyzz/index_{}.html"

    def get_url(self):
        start_pn = int(input("请输入你想从哪一页开始："))
        end_pn = int(input("请输入你想到哪一页结束："))
        if start_pn == 1:
            self.get_html(self.first_url)
            for i in range(start_pn+1, end_pn):
                self.get_html(self.not_first_url.format(i))
        else:
            for i in range(start_pn, end_pn):
                self.get_html(self.not_first_url)

    def get_html(self, url):
        req = request.Request(url, headers={'User-Agent': random.choice(user_agent.ua_list)})
        res = request.urlopen(req)
        html = res.read().decode('gbk', 'ignore')
        # time.sleep(random.randint(1, 3))
        self.get_data(html)

    def get_level_two_html(self, url):
        req = request.Request(url, headers={'User-Agent': random.choice(user_agent.ua_list)})
        res = request.urlopen(req)
        html = res.read().decode('gbk', 'ignore')
        # time.sleep(random.randint(1, 3))
        pattern = re.compile('<td style="WORD-WRAP: break-word".*?href="(.*?)">', re.S)
        href = pattern.findall(html)
        return href

    def get_data(self, html):
        dy_dict = {}
        pattern = re.compile('<td height="26">.*?href="(.*?)".*?title="(.*?)">', re.S)
        dy_list = pattern.findall(html)
        for dy_item in dy_list:
            film_name = dy_item[1]
            film_link = 'https://www.dygod.net' + dy_item[0]
            download_link = self.get_level_two_html(film_link)
            dy_dict['电影名称'] = film_name
            dy_dict["下载链接"] = download_link
            print(dy_dict)

    def main(self):
        self.get_url()


if __name__ == "__main__":
    start = time.time()
    spider = Dytt()
    spider.main()
    end = time.time()
    print("执行时间：%.2f" %(end - start))
