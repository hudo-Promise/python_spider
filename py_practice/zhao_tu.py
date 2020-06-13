import requests
from lxml import etree
from py_practice import user_agent
import random
import time


class Zhaotu(object):
    def __init__(self):
        self.url = "https://tieba.baidu.com/f?kw=%E8%B5%B5%E4%B8%BD%E9%A2%96&traceid="

    def get_level_one_html(self):
        req = requests.get(url=self.url, headers={"User-Agent": random.choice(user_agent.ua_list)})
        req.encoding = 'utf-8'
        html = req.text
        self.parse_html(html)

    def parse_html(self, html):
        html_str = etree.HTML(html)
        src_list = html_str.xpath('//div[@class="threadlist_title pull_left j_th_tit"]/a/@href')
        print(src_list)

    # def get_level_two_html

    def main(self):
        self.get_level_one_html()


if __name__ == "__main__":
    zhao = Zhaotu()
    zhao.main()
