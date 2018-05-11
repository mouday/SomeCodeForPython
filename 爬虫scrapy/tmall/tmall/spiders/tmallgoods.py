# -*- coding: utf-8 -*-
import scrapy
from tmall.items import TmallItem

class TmallgoodsSpider(scrapy.Spider):
    name = 'tmallgoods'
    allowed_domains = ['tmall.com']
    #女装
    start_urls = ['https://list.tmall.com/search_product.htm?q=%C5%AE%BF%E3&type=p&spm=a220m.1000858.a2227oh.d100&xl=%C5%AE_7&from=.list.pc_1_suggest']

    # 记录处理的页数
    count = 0

    def parse(self, response):
        
        divs = response.xpath('//div[@id="J_ItemList"]/div[@class="product  "]/div')

        if not divs:
            self.log("List page error %s"% response.url)

        for div in divs:
            item = TmallItem()
            #商品价格
            item["goods_price"] = div.xpath("p[@class='productPrice']/em/@title")[0].extract()
            #商品名称
            item["goods_name"] = div.xpath("p[@class='productTitle']/a/@title")[0].extract() 
            #商品url
            goods_url = div.xpath("p[@class='productTitle']/a/@href")[0].extract() 

            item["goods_url"] = goods_url if "http:" in goods_url else "http:" + goods_url

            # 图片链接
            # div/div[1]/a/img
            # //*[@id="J_ItemList"]/div[10]/div/div[1]/a/img
            try:
                file_urls = div.xpath("div[@class='productImg-wrap']/a[1]/img/@src|"
                    "div[@class='productImg-wrap']/a[1]/img/@data-ks-lazyload")[0].extract()
                print("file_urls:", file_urls)
                item["file_urls"] =["http:" + file_urls] 
            except Exception as e:
                import logging
                logging.debug(e) 
                # import pdb; pdb.set_trace()  # 跟踪路径
                
            print("[item]", item["goods_price"], item["goods_name"])
            yield scrapy.Request(url=item["goods_url"], meta={"item": item},
                dont_filter=True, callback=self.parse_detail)

    def parse_detail(self, response):
        TmallgoodsSpider.count += 1
        print(TmallgoodsSpider.count)

        item = response.meta["item"]
        
        # 店铺名称
        item["shop_name"]=response.xpath("//div[@id='shopExtra']/div[1]/a/strong/text()")[0].extract()
        
        # 店铺url
        item["shop_url"]=response.xpath("//div[@id='shopExtra']/div[1]/a/@href")[0].extract()

        # 公司地址
        # item["company_address"]=response.xpath("//*[@id='ks-component2498']/div/div/div/div[2]/ul/li[4]/div/text()")[0].extract()
        
        yield item