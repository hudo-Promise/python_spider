# -*- coding: utf-8 -*-
import scrapy
from ..items import MaoyanItem


class MaoyanSpider(scrapy.Spider):
    name = 'maoyan2'
    allowed_domains = ['maoyan.com']
    start_urls = ['https://maoyan.com/board/4?offset=0']
    offset = 0

    def parse(self, response):
        for offset in range(0, 91, 10):
            url = 'https://maoyan.com/board/4?offset={}'.format(offset)
            # 交给调度器
            yield scrapy.Request(
                url=url,
                callback=self.parse_html
            )

    def parse_html(self, response):
        dd_list = response.xpath('//div[@class="content"]//dl[@class="board-wrapper"]/dd')
        for dd in dd_list:
            item = MaoyanItem()
            item['name'] = dd.xpath('./a/@title').extract_first()
            item['star'] = dd.xpath('.//p[@class="star"]/text()').extract_first().strip()
            item['time'] = dd.xpath('.//p[@class="releasetime"]/text()').extract_first().strip()
            yield item

