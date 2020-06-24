from selenium import webdriver
import time


'''
设置chromedriver无界面模式
options = webdriver.ChromeOptions()
options.add_argument('--headless')
browser = webdriver.Chrome(options=options)
'''


class jingdongSpider(object):
    def __init__(self):
        self.browser = webdriver.Chrome()
        self.url = 'https://www.jd.com/'
        self.word = input("请输入你想搜索的内容：")
        self.num = 0

    def get_page(self):
        self.browser.get(self.url)
        self.browser.find_element_by_xpath('//input[@id="key"]').send_keys(self.word)
        self.browser.find_element_by_xpath('//button[@class="button"]').click()
        time.sleep(3)

    def parse_page(self):
        self.browser.execute_script(
            'window.scrollTo(0,document.body.scrollHeight)'
        )
        time.sleep(2)
        li_list = self.browser.find_elements_by_xpath('//div[@id="J_goodsList"]/ul/li')
        time.sleep(3)
        for li in li_list:
            self.num += 1
            info = li.text.split('\n')
            if info[0].startswith('自营每满'):
                price = info[1]
                name = info[2].split(' ')[0]
                number = info[3]
                market = info[4]
            elif info[0] == '单件':
                price = info[2]
                name = info[3].split(' ')[0]
                number = info[4]
                market = info[5]
            elif info[0].startswith('￥') and info[1].startswith('￥'):
                price = info[0]
                name = info[2].split(' ')[0]
                number = info[3]
                market = info[4]
            else:
                price = info[0]
                name = info[1].split(' ')[0]
                number = info[2]
                market = info[3]
            print(price, number, market, name)

    def main(self):
        self.get_page()
        while True:
            self.parse_page()
            if self.browser.page_source.find('pn-next disabled') == -1:
                self.browser.find_element_by_class_name('pn-next').click()
                time.sleep(3)
                print(self.num)
            else:
                break


if __name__ == '__main__':
    spider = jingdongSpider()
    spider.main()
