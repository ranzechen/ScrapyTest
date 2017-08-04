# -*- coding: utf-8 -*-
import scrapy
from ScrapyTest.items import ScrapytestItem

class JiexintbSpider(scrapy.Spider):
    name = 'jiexinTB'
    allowed_domains = ['jiexinTB.com']
    start_urls = ["http://tieba.baidu.com/f?kw=捷信金融&ie=utf-8&pn=0"]

    def parse(self, response):
        items = []
        for info in response.xpath("//div[@class='t_con cleafix']"):
            item = ScrapytestItem()
            item['author'] = str(info.xpath("div[2]/div[1]/div[2]/span[1]/@title").extract()).replace("['","").replace("']","").replace("主题作者: ","")
            item['title'] = info.xpath("div[2]/div[1]/div[1]/a/text()").extract()
            item['times'] = info.xpath("div[1]/span[1]/text()").extract()
            item['perUrl'] = "http://tieba.baidu.com" + str(info.xpath("div[2]/div[1]/div[1]/a/@href").extract()).replace("['","").replace("']","")
            items.append(item)
            yield item
        print(items)