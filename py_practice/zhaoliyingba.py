from urllib import request
from urllib import parse
import random
import time


class Tieba(object):
    def __init__(self):
        self.url = "https://tieba.baidu.com/f?kw={}&pn={}"
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
                                      ' Chrome/83.0.4103.61 Safari/537.36'}

    # 处理url
    def get_url(self):
        name = input("请输入贴吧名:")
        pn_start = int(input("请输入起始页："))
        pn_end = int(input("请输入终止页："))
        for page in range(pn_start, pn_end + 1):
            pn = (page - 1) * 50
            url = self.url.format(parse.quote(name), pn)
            filename = "{}-第{}页.html".format(name, page)
            print("第{}页获取成功".format(page))
            time.sleep(random.randint(0, 3))
            html = self.get_html(url)
            self.save_data(filename, html)

    # 获取响应
    def get_html(self, url):
        req = request.Request(url=url, headers=self.headers)
        res = request.urlopen(req)
        html = res.read().decode('utf-8')

        return html

    # 提取数据
    def get_item(self):
        pass

    # 保存数据
    def save_data(self, filename, html):
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(html)

    # 主函数
    def main(self):
        self.get_url()


if __name__ == "__main__":
    tieba = Tieba()
    tieba.main()
