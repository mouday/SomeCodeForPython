# -*- coding: utf-8 -*-
import scrapy
from demo import items

class DmozSpiderSpider(scrapy.Spider):
    name = 'dmoz_spider'
    allowed_domains = ['blog.sina.com.cn']
    start_urls = [
    'http://blog.sina.com.cn/s/articlelist_2559711405_0_1.html'

    ]

    def parse(self, response):
        # 保存网页
        filename = response.url.split("/")[-1]
        with open(filename, "wb") as f:
            f.write(response.body)

        # 解析网页
        lis = response.css('.atc_title')
        print(len(lis))
        for li in lis:        
            item = items.DemoItem()
            item["title"] = li.xpath('a/text()').extract()[0]
            item["link"] = li.xpath('a/@href').extract()[0]
            print("[item]", item)
            yield item
