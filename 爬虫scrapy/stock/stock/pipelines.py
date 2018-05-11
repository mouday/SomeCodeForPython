# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json

class StockPipeline(object):
    def process_item(self, item, spider):
        return item

class BaiduStockPipeline(object):
    def open_spider(self, spider):
        self.file = open("baidustock.txt", "w")

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        self.file.write(str(dict(item)))
        return item