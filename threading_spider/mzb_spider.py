import requests
from lxml import etree
from py_practice import user_agent
import random
import re
import pymysql


class Mzb(object):
    def __init__(self):
        self.url = 'http://www.mca.gov.cn/article/sj/xzqh/2020'
        self.headers = {'User-Agent': random.choice(user_agent.ua_list)}
        self.db = pymysql.connect('localhost', 'root', 'root', 'xzqm', charset='utf8')
        self.cursor = self.db.cursor()

    def get_false_href(self):
        html = requests.get(url=self.url,
                            headers=self.headers
                            ).content.decode('utf-8', 'ignore')
        parse_html = etree.HTML(html)
        a_list = parse_html.xpath('//a[@class="artitlelist"]')

        for a in a_list:
            # title = a.xpath('./@title')[0]
            title = a.get('title')
            if re.findall('.*中华人民共和国县以上行政区划代码', title, re.S):
                two_false_link = self.url + a.get('href')
                return two_false_link

    def get_true_link(self):
        two_false_link = self.get_false_href()
        print(two_false_link)
        html = requests.get(url=two_false_link, headers=self.headers).text
        # pattern = re.compile(r'window.location.href="(.*?)"')
        # real_link = pattern.findall(html)[0]

        
        print(html)
        # with open('response.html', 'w') as f:
        #     f.write(html)

    def get_data(self):
        pass

    def main(self):
        self.get_true_link()


if __name__ == '__main__':
    spider = Mzb()
    spider.main()
