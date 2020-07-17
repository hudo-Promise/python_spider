# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class MaoyanPipeline:
    def process_item(self, item, spider):
        print(item['name'])
        print(item['star'])
        print(item['time'])
        return item


import pymysql
from .settings import *


class MaoyanMysqlPipline(object):
    def __init__(self, spider):
        self.db = pymysql.connect(
            host=MYSQL_HOST,
            user=MYSQL_USER,
            password=MYSQL_PWD,
            database=MYSQL_DB,
            charset=MYSQl_CHAR
        )
        self.cursor = self.db.cursor()

    def process_item(self, item, spider):
        ins = 'insert into maoyan values(%s, %s, %s,)'
        film_list = [
            item['name'],
            item['star'],
            item['time']
        ]
        self.cursor.execute(ins, film_list)
        self.db.commit()

        return item

    def close_spider(self, spider):
        self.cursor.close()
        self.db.close()
