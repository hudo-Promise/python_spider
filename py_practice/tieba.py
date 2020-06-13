import random
from urllib import request
from urllib import parse
import time


class BaiduSpider(object):
    def __init__(self):
        self.url = "https://tieba.baidu.com/f?kw={}&pn={}"
        self.headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/83.0.4103.61 Safari/537.36'}

    # 获取响应
    def get_page(self, url):
        req = request.Request(url=url, headers=self.headers)
        res = request.urlopen(req)
        html = res.read().decode('utf-8')

        return html

    # 提取数据
    def parse_page(self):
        pass

    # 保存数据
    def save_html(self, filename, html):
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(html)

    # 主函数
    def main(self):
        name = input('请输入贴吧名：')
        start = int(input('请输入起始页：'))
        end = int(input('请输入终止页：'))

        for page in range(start, end+1):
            pn = (page - 1) * 50
            kw = parse.quote(name)
            url = self.url.format(kw, pn)
            html = self.get_page(url)
            filename = '{}-第{}页.html'.format(name, page)
            self.save_html(filename, html)
            print('第{}页爬取成功'.format(page))
            time.sleep(random.randint(1, 3))


if __name__ == "__main__":
    spider = BaiduSpider()
    spider.main()
