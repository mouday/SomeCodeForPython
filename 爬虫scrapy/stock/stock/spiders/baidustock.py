# -*- coding: utf-8 -*-
import scrapy
import re
import random

# 请求头
user_agent_list = [
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
        "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
        "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
        ]

class BaidustockSpider(scrapy.Spider):
    name = 'baidustock'
    start_urls = ['http://quote.eastmoney.com/stocklist.html']

    def parse(self, response):
        hrefs  = response.css("a::attr(href)").extract()
        for href in hrefs:
            try:
                stock = re.findall(r"[s][zh]\d{6}", href)[0]
                # print(stock)
                # https://gupiao.baidu.com/stock/sh600271.html
                url = "https://gupiao.baidu.com/stock/" + stock + ".html"
                ua = random.choice(user_agent_list)#随机抽取User-Agent
                headers = {
                          'Accept-Encoding':'gzip, deflate, sdch, br',
                          'Accept-Language':'zh-CN,zh;q=0.8',
                          'Connection':'keep-alive',
                          'Referer':'https://gupiao.baidu.com/',
                          'User-Agent':ua
                          }#构造请求头
                yield scrapy.Request(url=url, callback=self.parse_stock, headers=headers)
            except:
                continue

    def parse_stock(self, response):
        stock_info = response.css(".stock-info")
        name = stock_info.css(".bets-name::text")[0].extract()
        code = stock_info.css(".bets-name span::text")[0].extract()
        dls = response.css(".bets-content dl")
        info = {}
        for dl in dls:
            key = dl.css("dt::text")[0].extract()
            try:
                val = dl.css("dd::text")[0].extract()
            except:
                val = "--"
            info[key]=val
        item={}
        item["name"] = name.replace("(", "").strip()
        item["code"] = code
        # item["info"] = info
        print(item["name"])
        yield item

