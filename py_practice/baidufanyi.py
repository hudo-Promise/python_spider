import requests
import re
import execjs


class BaiduTranslateSpider(object):
    def __init__(self):
        self.get_url = 'https://fanyi.baidu.com/?aldtype=16047'
        self.headers ={}

    # 获取token
    def get_token(self):
        html = requests.get(
            url=self.get_url,
            headers=self.headers
        ).text
        pattern = re.compile("token: '(.*?)'", re.S)
        token = pattern.findall(html)[0]
        return token

    # 获取sign
    def get_sign(self):
        pass

    # 获取翻译结果
    def get_result(self):

        return result


if __name__ == "__main__":
    spider = BaiduTranslateSpider()
    word = input("请输入要翻译的内容：")
    result = spider.get_result(word)
    print(result)
