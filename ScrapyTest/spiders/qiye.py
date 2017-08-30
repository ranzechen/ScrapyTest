# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
class QiyeSpider(scrapy.Spider):
    name = 'qiye'
    allowed_domains = ['shenzhen.11467.com/']
    start_urls = ['http://shenzhen.11467.com']
    website_possible_httpstatus_list = [404,502,301,403]
    def parse(self, response):
        if response.body == "banned":
            req = response.request
            req.meta["change_proxy"] = True
            yield req
        else:
            table = response.xpath("//div[@id='main']/div[1]/div[1]/div")
            for link in table.xpath("div/dl/dt/a/@href").extract():
                print("第一层:"+link)
                yield Request(url=link,callback=self.getAreaInfo,dont_filter=True)

    def getAreaInfo(self,response):
        for i in response.xpath("//div[@id='main']/div/div[1]/div/dl/dd/a/@href").extract():
            url = 'http://shenzhen.11467.com'+i
            yield Request(url=url,callback=self.getPageInfo,dont_filter=True)

    def getPageInfo(self,response):
        try:
            pageNum = response.xpath("//div[@class='pages']/a/text()").extract()[-3]
            baseurl = response.xpath("//div[@class='pages']/a[1]/@href").extract()[0]
            for page in range(1,int(pageNum)+1):#
                url = baseurl+'pn'+str(page)
                print("第二层:"+url)
                yield Request(url=url,callback=self.getComInfo,dont_filter=True)
        except Exception as e:
                print(e)
                pass

    def getComInfo(self,response):
        link = response.xpath("//ul[@class='companylist']/li/div/h4/a/@href").extract()
        for perComLink in link:
            print("第三层:"+perComLink)
            yield Request(url=perComLink,callback=self.info,dont_filter=True)

    def info(self,response):
        data = []
        body = response.body.decode("utf-8","ignore")
        if body.split("，")[0] == "可能您访问的有点快了":
            req = response.request
            req.meta["change_proxy"] = True
            yield req
        else:
            companyName = str(response.xpath("//title/text()").extract()).replace("['","").replace("']","")
            info1 = str(response.xpath("//div[@id='contact']/div/dl//text()").extract()).replace("[","").replace("]","").replace("：',","':")
            info2 = str(response.xpath("//div[@id='gongshang']//tr//text()").extract()).replace("[","").replace("]","").replace("：',","':")
            data.append(companyName+"#"+info1+","+info2)
            print(data)
            with open('qiyedata.txt', 'a', encoding="utf-8") as f:
               f.write(str(data) + '\n')




