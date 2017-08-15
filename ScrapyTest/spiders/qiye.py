# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request

class QiyeSpider(scrapy.Spider):
    name = 'qiye'
    allowed_domains = ['shenzhen.11467.com/']
    start_urls = ['http://shenzhen.11467.com']
    def parse(self, response):
        table = response.xpath("//div[@id='main']/div[1]/div[1]/div")
        for link in table.xpath("div/dl/dt/a/@href").extract():
            print("第一层:"+link)
            yield Request(url=link,callback=self.getPageInfo,dont_filter=True)

    def getPageInfo(self,response):
        pageNum = response.xpath("//div[@class='pages']/a/text()").extract()[-3]
        baseurl = response.xpath("//div[@class='pages']/a[1]/@href").extract()[0]
        for page in range(1,int(pageNum)+1):#
            url = baseurl+'pn'+str(page)
            print("第二层:"+url)
            yield Request(url=url,callback=self.getComInfo,dont_filter=True)

    def getComInfo(self,response):
        link = response.xpath("//ul[@class='companylist']/li/div/h4/a/@href").extract()
        for perComLink in link:
            print("第三层:"+perComLink)
            yield Request(url=perComLink,callback=self.detailInfo,dont_filter=True)

    def detailInfo(self,response):
        print("当前请求页面->   "+str(response))
        dataList = []
        name_key = "公司名称"
        name_value = response.xpath("//div[@id='nav']/div/div/a/text()").extract()[-1]
        name = {
            name_key:name_value
        }
        dataList.append(name)
        info = response.xpath("//div[@id='contact']/div/dl")
        keyList = info.xpath("dt/text()").extract()
        valueList = info.xpath("dd//text()").extract()
        if keyList[0] == '公司地址：':
            data = {
                "公司地址":valueList[0]
            }
            dataList.append(data)
        if keyList[1] == '固定电话：':
            data = {
                "固定电话":valueList[1]
            }
            dataList.append(data)
        if keyList[2] == '经理：':
            data={
                "经理":valueList[2]
            }
            dataList.append(data)
        if response.xpath("//div[@id='gongshang']/div/dl/dt/text()").extract()[0] == '法人名称：':
            data = {
                "法人名称":response.xpath("//div[@id='gongshang']/div/dl/dd/text()").extract()[0]
            }
            dataList.append(data)

        print("当前界面数据->   "+str(dataList))
        with open('qiye.txt', 'a',encoding="utf-8") as f:
            f.write(str(dataList) + '\n')





