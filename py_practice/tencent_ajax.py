import requests
import json
import time
import random


class Tencent(object):
    def __init__(self):
        self.url = 'https://careers.tencent.com/tencentcareer/api/post/Query?timestamp=1592025329451' \
                   '&countryId=&cityId=&bgIds=&productId=' \
                   '&categoryId=40001001,40001002,40001003,40001004,40001005,40001006&parentCategoryId=' \
                   '&attrId=&keyword=&pageIndex={}&pageSize=10&language=zh-cn&area=cn'
        self.headers ={
            'Accept': '*/*',
            # 'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Connection': 'keep-alive',
            'Cookie': 'bid=Maklc92K4wI; __utmz=30149280.1587299063.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); '
                      '__gads=ID=30a10674ca5de1c0:T=1587299064:S=ALNI_MbyccaUW4P8i7HnexxzjS3cr0w6ww; '
                      '__yadk_uid=6BPTtr515chITKZglkkAinZCjP3jmgta; ll="108288"; '
                      'ap_v=0,6.0; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1591972857%2C%22https%3A%2F%2Fwww.baidu.com'
                      '%2Fs%3Fwd%3D%25E8%25B1%2586%25E7%2593%25A3%26rsv_spt%3D1%26rsv_iqid%3D0xe06294ec000507f4%26issp'
                      '%3D1%26f%3D8%26rsv_bp%3D1%26rsv_idx%3D2%26ie%3Dutf-8%26tn%3Dbaiduhome_pg%26rsv_enter%3D1'
                      '%26rsv_dl%3Dtb%26rsv_sug3%3D8%26rsv_sug1%3D6%26rsv_sug7%3D100%26rsv_sug2%3D0%26rsv_btype%3Di'
                      '%26inputT%3D1597%26rsv_sug4%3D2387%22%5D; _pk_ses.100001.4cf6=*; '
                      '__utma=30149280.1611759677.1587299063.1587356869.1591972857.4; __utmb=30149280.0.10.1591972857; '
                      '__utmc=30149280; __utma=223695111.482992593.1587299063.1587356869.1591972857.4; '
                      '__utmb=223695111.0.10.1591972857; __utmc=223695111; '
                      '__utmz=223695111.1591972857.4.2.utmcsr=baidu|utmccn=(organic)|utmcmd=organic|utmctr='
                      '%E8%B1%86%E7%93%A3; _vwo_uuid_v2=D5AC425D9B90094B7A029989FF5CDB514|3a9db65'
                      '1d2ca59a982710443f7a235ab; _pk_id.100001.4cf6='
                      'f88a3c234b26552b.1587299063.4.1591972897.1587356869.',
            'Sec-Fetch-Site': 'same-origin',
            'Referer': 'https://movie.douban.com/typerank?type_name=%E5%89%A7%E6%83%85&type=11&interval_id=100:'
                       '90&action=',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',

            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/83.0.4103.97 Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest',

        }

    def ask_url(self, url):
        html_json = requests.get(url=url, headers=self.headers).json()
        posts = html_json['Data']['Posts']
        for item in posts:
            name = item['RecruitPostName']
            description = item['Responsibility']
            print("职位名称：%s  岗位描述：%s" % (name, description))

    def main(self):
        start_pn = int(input("请输入开始页："))
        end_pn = int(input("请输入终止页："))
        for i in range(start_pn, end_pn):
            url = self.url.format(i)
            self.ask_url(url)
            time.sleep(random.randint(1, 3))


if __name__ == '__main__':
    spider = Tencent()
    spider.main()
