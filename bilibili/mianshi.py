import requests
from lxml import etree
import json
from queue import Queue
import threading
import re


class Game:
    def __init__(self):
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWeb\
            Kit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"}
        self.cookies = {"UM_distinctid": "17176cf2db315-0269d80e206794-87f133f-144000-17176cf2db429e",
                        "Hm_lvt_f1fb60d2559a83c8fa1ee6125a352bd7": "1586836221,1586928117",
                        "CNZZDATA1000292083": "1074314076-1586833624-https%253A%252"
                                              "F%252Fwww.baidu.com%252F%7C1586927616",
                        "CNZZDATA30039538": "cnzz_eid%3D605489768-1586832036-https%253A%252F%252Fwww.baidu.com%"
                                            "252F%26ntime%3D1586927583",
                        "Hm_lpvt_f1fb60d2559a83c8fa1ee6125a352bd7": "1586928128"}
        self.url_queue = Queue()
        self.html_queue = Queue()
        self.content_queue = Queue()
        self.url = "https://www.3839.com/top/hot.html"

    def parse_url(self):
        """
        请求网站的html页面
        :return: html
        """
        response = requests.get(self.url, headers=self.headers, cookies=self.cookies)
        html = response.content.decode()
        html = etree.HTML(html)
        return html

    @staticmethod
    def get_url(html):
        """
        获取游戏的url
        :return: items
        """
        total_li = html.xpath('//div/ul@[class="ranking-game ranking-list"]/li')
        items = []
        for i in total_li:
            aim_href = "https://" + i.xpath('./a/href') if len(i.xpath('./a/href')) > 0 else None
            item = dict(
                href=aim_href
            )
            items.append(item)
        print(items)
        return items

    def parse_game_url(self, href):
        """
        请求游戏详情的html页面
        :return: html
        """
        response = requests.get(href, headers=self.headers, timeout=10)
        html = response.content.decode()
        html = etree.HTML(html)
        return html

    @staticmethod
    def get_game_detail(html):
        """
        获取游戏详情
        :return:
        """
        game_item = []
        id_href = html.xpath('///html/head/link[@href]')
        game_id = re.findall(r'\d+', str(id_href))[1]
        game_name = html.xpath('//div@[class="des"]/h1/text()')
        logo = html.xpath('//div@[class="gameDesc"]/img/@src')
        introduce = html.xpath('//div@[class="textCon"]/div/text()')
        score = html.xpath('//div@[class="card"]/p@[class="score"]/text()')
        comment_count = html.xpath('//div@[class="tabArea"]/a@[onclick="sel_tab(2)"]/span/text()')
        item = dict(
            game_id=game_id,
            game_name=game_name,
            logo=logo,
            introduce=introduce,
            score=score,
            comment_count=comment_count,
        )
        game_item.append(item)
        return game_item

    @staticmethod
    def get_game_comment(html):
        """
        获取评论详情
        :param html:
        :return:
        """
        comment_item = []
        c_id = html.xpath('//div[@class="item-content"]/p/span[@id]')
        comment_id = re.findall(r'\d+', str(c_id))[0]
        id_src = html.xpath('//div@[class="login_info"]/img[@src]')
        user_id = re.findall(r'\d+', str(id_src))[1]
        username = html.xpath('//div[@class="item-content"]/p/span/text()')
        creat_time = "2020-" + html.xapth('//div[@class="item-content"]/span/text')
        content = html.xpath('//div[@class="comments-txt"]/p[@style="display:none"]/text()')
        like_count = html.xpath('//div[@class="com"]/a[@onclick="show_download();return false;"]/text()')
        replay_count = html.xpath('//div[@class="reply-list-more"]/a/span/text()')
        item = dict(
            comment_id=comment_id,
            user_id=user_id,
            username=username,
            creat_time=creat_time,
            content=content,
            like_count=like_count,
            replay_count=replay_count,
        )
        comment_item.append(item)
        return comment_item

    @staticmethod
    def save_item(item):
        """
        保存数据
        :return:
        """
        if item == "game_item":
            with open("game_detail.txt", "a") as f:
                f.write(json.dumps(item, ensure_ascii=False, indent=2))
                f.write("\n")
        else:
            with open("game_comment.txt", "a") as f:
                f.write(json.dumps(item, ensure_ascii=False, indent=2))
                f.write("\n")

    def run(self):
        html = self.parse_url()
        href_list = self.get_url(html)
        for href in href_list:
            html = self.parse_game_url(href)
            thread_list = []

            thread_game_item = threading.Thread(target=self.get_game_detail(html))
            thread_list.append(thread_game_item)

            thread_game_comment = threading.Thread(target=self.get_game_comment(html))
            thread_list.append(thread_game_comment)

            thread_save_detail = threading.Thread(target=self.save_item(thread_game_item))
            thread_list.append(thread_save_detail)

            thread_save_comment = threading.Thread(target=self.save_item(thread_game_item))
            thread_list.append(thread_save_comment)


if __name__ == "__main__":
    game = Game()
    game.run()

