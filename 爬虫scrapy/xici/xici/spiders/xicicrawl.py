# -*- coding: utf-8 -*-
import scrapy
from xici.items import XiciItem

class XicicrawlSpider(scrapy.Spider):
    name = 'xicicrawl'
    allowed_domains = ['xicidaili.com']
    start_urls = ['http://www.xicidaili.com/']

    def start_requests(self):
        reqs = []
        headers={"User-Agent":"Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36"}
        for i in range(1, 2814): #2814
            req = scrapy.Request("http://www.xicidaili.com/nn/%s"%i,headers=headers)
            reqs.append(req)
        return reqs

    def parse(self, response):
        ip_list = response.xpath("//table[@id='ip_list']")
        trs = ip_list[0].xpath("tr")

        items = []
        print("trs:", len(trs))
        for tr in trs[1:]:
            item = XiciItem()
            item["ip"] = tr.xpath("td[2]/text()")[0].extract()
            item["port"] = tr.xpath("td[3]/text()")[0].extract()
            item["address"] = tr.xpath("string(td[4])")[0].extract().strip()
            item["typ"] = tr.xpath("td[6]/text()")[0].extract()
            item["speed"] = tr.xpath("td[7]/div[@class='bar']/@title").re("\d{0,2}\.\d{0,}")[0]
            item["check_time"] = tr.xpath("td[10]/text()")[0].extract()

            items.append(item)

        return items