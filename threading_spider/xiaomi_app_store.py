import requests
import json
from py_practice import user_agent
import random
from copy import deepcopy


class XmAppStore(object):
    def __init__(self):
        self.url = "http://app.mi.com/categotyAllListApi?page=0&categoryId=15&pageSize=30"
        self.headers = {
                        "Accept": "application/json, text/javascript, */*; q=0.01",
                        # "Accept-Encoding": "gzip, deflate",
                        "Accept-Language": "zh-CN,zh;q=0.9",
                        "Connection": "keep-alive",
                        "Cookie": "JSESSIONID=aaahOP78xuKuM5qTqe8kx; __utma=127562001.531149837.1592639080.1592639080.1592639080.1; __utmc=127562001; __utmz=127562001.1592639080.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; Hm_lvt_765fefc2c357bae3970cea72e714811b=1592639080,1592639315,1592641151; __utmb=127562001.20.10.1592639080; Hm_lpvt_765fefc2c357bae3970cea72e714811b=1592643249",
                        "Host": "app.mi.com",
                        "Referer": "http://app.mi.com/category/15",
                        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36",
                        "X-Requested-With": "XMLHttpRequest",
                        }
        # self.data = {
        #     "page": "{}",
        #     "categoryId": 15,
        #     "pageSize": 30
        # }

    # def page(self):
    #     start_pn = int(input("请输入开始页码："))
    #     end_pn = int(input("请输入结束页码："))
    #     data_list = []
    #     for i in range(start_pn, end_pn):
    #         data_list.append(self.data["page"].format(i))
    #         self.send_req(data_list)

    def send_req(self):
        # for i in range(len(data_list)):
            res = requests.post(url=self.url, headers=self.headers).content.decode('utf-8')
            print(res)
            # html = json.loads(res.text)
            # self.parse_html(html)

    # def parse_html(self, html):
    #     data_dict = {}
    #     game_list = []
    #     for i in range(0, len(html["data"])):
    #         data_dict["id"] = i
    #         data_dict["游戏名称"] = html["data"][i]["displayName"]
    #         data_dict["下载链接"] = "http://app.mi.com/details?id=" + html["data"][i]["packageName"]
    #         game_list.append(data_dict)
    #         print(game_list)

    def main(self):
        self.send_req()


if __name__ == '__main__':
    spider = XmAppStore()
    spider.main()