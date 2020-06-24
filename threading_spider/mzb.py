from selenium import webdriver
import time
import pymysql


class Mzb(object):
    def __init__(self):
        self.url = 'http://www.mca.gov.cn/article/sj/xzqh/2020/'
        self.db = pymysql.connect(
            'localhost', 'root', 'root', 'xzqm', charset='utf8'
        )
        self.cursor = self.db.cursor()
        self.browser = webdriver.Chrome()
        self.province = []
        self.city = []
        self.county = []

    def get_page(self):
        self.browser.get(self.url)
        td_list = self.browser.find_elements_by_xpath(
            '//td[@class="arlisttd"]/a[contains(@title,"中华人民共和国县以上行政区划代码")]'
        )
        if td_list:
            two_url_element = td_list[0]
            two_url = two_url_element.get_attribute('href')
            sel = 'select * from version where link="%s"'
            self.cursor.execute(sel, [two_url])
            result = self.cursor.fetchall()
            if result:
                print("数据无需更新！")
            else:
                two_url_element.click()
                time.sleep(5)
                all_handles = self.browser.window_handles
                self.browser.switch_to_window(all_handles[1])
                self.get_data()
                ins = 'insert into version values(%s)'
                self.cursor.execute(ins, [two_url])
                self.db.commit()

    def get_data(self):
        tr_list = self.browser.find_elements_by_xpath('//tr[@height="19"]')
        for tr in tr_list:
            code = tr.find_element_by_xpath('./td[2]').text.strip()
            name = tr.find_element_by_xpath('./td[3]').text.strip()
            if code[-4:] == '0000':
                if name in ('北京市', '天津市', '上海市', '重庆市'):
                    city = [name, code, code[:2] + '0000']
                    self.city.append(city)
                self.province.append([name, code])
            elif code[-2:] == '00':
                city = [name, code, code[:2] + '0000']
                self.city.append(city)
            else:
                county = [name, code, code[:4] + '00']
                self.county.append(county)
        self.insert_mysql()

    def insert_mysql(self):
        clear_province = 'delete from province'
        self.cursor.execute(clear_province)
        clear_city = 'delete from city'
        self.cursor.execute(clear_city)
        clear_county = 'delete from county'
        self.cursor.execute(clear_county)
        ins_province = 'insert into province values(%s,%s)'
        self.cursor.executemany(ins_province, self.province)
        ins_city = 'insert into city values(%s,%s,%s)'
        self.cursor.executemany(ins_city, self.city)
        ins_county = 'insert into county values(%s,%s,%s)'
        self.cursor.executemany(ins_county, self.county)
        self.db.commit()
        print("数据抓取完成，成功存入数据库")

    def main(self):
        self.get_page()
        self.cursor.close()
        self.db.close()


if __name__ == "__main__":
    spider = Mzb()
    spider.main()
