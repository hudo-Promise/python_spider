import requests
import json
import time


class Fenbi():
    def __init__(self):
        self.post_url = 'https://tiku.fenbi.com/api/users/loginV2'
        self.get_url = 'https://tiku.fenbi.com/api/shenlun/solution/papers/91886?format=html&kav=12&app=web'
        self.headers_post = {
            "Accept": "*/*",
            # "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Connection": "keep-alive",
            "Cookie": "sid=3832154295730206433",
            "Origin": "https://www.fenbi.com",
            "Referer": "https://www.fenbi.com/spa/tiku/guide/catalog/xingce?prefix=xingce",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "cross-site",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/"
                          "83.0.4103.97 Safari/537.36",
        }
        self.headers_get = {
            "Accept": "*/*",
            # "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Connection": "keep-alive",
            "Cookie": "sid=3832154295730206433; sess=RczfzBoIRC8u3Qs8lGqdA0s8ubNowR/Zmc0WQvlbv5mOhcgQiioBcP7Qz/WGXpxd6mRH+DDVcKPaJHLA66coHg5vnVQwSZSKvYSMbexhm+U=; userid=69833992; persistent=jFJneNcvoHG3Q6oK5I6Mr60itmByKLa8Mu0znTTWjlZK8JFne8zfLP4ysEMGJMmhXj6YIYkeaZexnJLwRE1mDg==",
            "Origin": "https://www.fenbi.com",
            "Referer": "https://www.fenbi.com/spa/shenlun/zhenti/1000/91731",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-site",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/"
                          "83.0.4103.97 Safari/537.36",
        }
        self.post_data = {
            "phone": 18515361170,
            "password": "12345HUdong"
        }
        self.data = {
            "format": "html",
            "kav": "12",
            "app": "web"
        }
        self.session = requests.session()

    def post_req(self):
        self.session.post(url=self.post_url, data=self.post_data, headers=self.headers_post)
        res = self.session.get(url=self.get_url, data=self.data, headers=self.headers_get)
        res.encoding = 'utf-8'
        html = json.loads(res.text)
        self.parse_html(html)

    def parse_html(self, html):

        mr_list = []
        for i in range(0, 14):
            materials = html['materials'][i]['content']
            mr_list.append(materials)
        for i in range(0, len(mr_list)):
            print(mr_list[i])
        questions_list = []
        solutions_list = []
        analysis_list = []
        for i in range(0, 4):
            questions = html['questions'][i]['content']
            questions_list.append(questions)
            solutions = html['questions'][i]['solutionAccessories'][0]['content']
            solutions_list.append(solutions)
            analysis = html['questions'][i]['solutionAccessories'][1]['content']
            analysis_list.append(analysis)
        for item in range(0, len(questions_list)):
            print(questions_list)
            print(solutions_list)
            print(analysis_list)

    def main(self):
        self.post_req()


if __name__ == "__main__":
    start = time.time()
    spider = Fenbi()
    spider.main()
    end = time.time()
    print("程序运行时间：%s" % str(end - start))
