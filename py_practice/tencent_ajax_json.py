import requests
import json
import random
import time
from py_practice import user_agent


class Tencent(object):
    def __init__(self):
        self.one_url = 'https://careers.tencent.com/tencentcareer/api/post/Query?timestamp=1592148191723&countryId=' \
                       '&cityId=&bgIds=&productId=&categoryId=&parentCategoryId=40001&attrId=&keyword=&pageIndex={}' \
                       '&pageSize=10&language=zh-cn&area=cn'
        self.two_url = 'https://careers.tencent.com/tencentcareer/api/post/ByPostId?timestamp=1592148269236&postId={}' \
                       '&language=zh-cn'
        self.headers = {'User-Agent': random.choice(user_agent.ua_list)}

    def get_page(self, url):
        res = requests.get(url, headers=self.headers)
        res.encoding = 'utf-8'

        return json.loads(res.text)

    def parse_html(self, html):
        job_info = {}
        for job in html['Data']['Posts']:
            job_info['name'] = job['RecruitPostName']
            post_id = job['PostId']
            two_url = self.two_url.format(post_id)
            job_info['job_duty'], job_info['require'] = self.parse_two_html(two_url)
        print(job_info)

    def parse_two_html(self, two_url):
        two_html = self.get_page(two_url)
        duty = two_html['Data']['Responsibility']
        require = two_html['Data']['Requirement']
        return duty, require

    def main(self):
        for index in range(1, 11):
            url = self.one_url.format(index)
            one_html = self.get_page(url)
            self.parse_html(one_html)
            time.sleep(random.uniform(0.5, 2))


if __name__ == '__main__':
    spider = Tencent()
    spider.main()
