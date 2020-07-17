# -*- coding: utf-8 -*-
import scrapy
from ..items import MaoyanItem


class MaoyanSpider(scrapy.Spider):
    name = 'maoyan3'
    allowed_domains = ['maoyan.com']

    def start_requests(self):
        for offset in range(0, 91, 10):
            url = 'https://maoyan.com/board/4?offset={}'.format(offset)
            yield scrapy.Request(
                url=url,
                callback=self.parse
            )

    def parse(self, response):
        dd_list = response.xpath('//div[@class="content"]//dl[@class="board-wrapper"]/dd')
        for dd in dd_list:
            item = MaoyanItem()
            item['name'] = dd.xpath('./a/@title').extract_first()
            item['star'] = dd.xpath('.//p[@class="star"]/text()').extract_first().strip()
            item['time'] = dd.xpath('.//p[@class="releasetime"]/text()').extract_first().strip()
            yield item


