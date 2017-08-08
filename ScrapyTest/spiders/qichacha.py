# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from ScrapyTest.items import ScrapyqichachaItem
from datetime import time
class QichachaSpider(scrapy.Spider):
    name = 'qichacha'
    allowed_domains = ['qichacha.com']
    start_urls = ['http://www.qichacha.com/']

    def parse(self, response):
        arealink = response.xpath("//div[@id='area']/ul/li/a/@href").extract()
        for i in range(0,len(arealink)):
            completeLink = "http://www.qichacha.com"+str(arealink[i])
            yield Request(url = completeLink,callback = self.getNextPage)

    def getNextPage(self,response):
        companylink = response.xpath("//div[@class='row']/div[2]/section/a/@href").extract()
        for i in range(0,len(companylink)):
            completeCompanylink = "http://www.qichacha.com"+str(companylink[i])
            yield Request(url=completeCompanylink,callback=self.getCompanyInfo)

    def getCompanyInfo(self,response):
        #item['name'] = response.xpath("//div[@class='text-big font-bold company-top-name']/text()").extract()
        #item['phone'] = response.xpath("//small[@class='clear text-ellipsis m-t-xs text-md text-black ma_line2']/text()").extract()
        #item['email'] = response.xpath("//small[@class='clear text-ellipsis m-t-xs text-md text-black ma_line2']/a/text()").extract()
        items = []
        info = response.xpath("//div[@class='data_div_login']/section[@id='Cominfo']/table")
        for i in range(0,len(info)):
            item = ScrapyqichachaItem()
            item['unifiedSocialCreditCode'] = info.xpath("tr[1]/td[2]/text()").extract()[i].strip()
            item['taxpayerIdentificationNumber'] = info.xpath("tr[1]/td[4]/text()").extract()[i].strip()
            item['registrationNumber'] = info.xpath("tr[2]/td[2]/text()").extract()[i].strip()
            item['organizationCode'] = info.xpath("tr[2]/td[4]/text()").extract()[i].strip()
            item['regalRepresentative'] = info.xpath("tr[3]/td[2]/a[1]/text()").extract()[i].strip()
            item['registeredCapital'] = info.xpath("tr[3]/td[4]/text()").extract()[i].strip()
            item['operatingState'] = info.xpath("tr[4]/td[2]/text()").extract()[i].strip()
            item['setupDate'] = info.xpath("tr[4]/td[4]/text()").extract()[i].strip()
            item['companyType'] = info.xpath("tr[5]/td[2]/text()").extract()[i].strip()
            item['staffSize'] = info.xpath("tr[5]/td[4]/text()").extract()[i].strip()
            item['businessTerm'] = info.xpath("tr[6]/td[2]/text()").extract()[i].strip()
            item['registrationAuthority'] = info.xpath("tr[6]/td[4]/text()").extract()[i].strip()
            item['approvalDate'] = info.xpath("tr[7]/td[2]/text()").extract()[i].strip()
            item['companyEnglishName'] = info.xpath("tr[7]/td[4]/text()").extract()[i].strip()
            item['industry'] = info.xpath("tr[8]/td[4]/text()").extract()[i].strip()
            item['address'] = info.xpath("tr[9]/td[2]/text()").extract()[i].strip()
            item['scopeOfBusiness'] = info.xpath("tr[10]/td[2]/text()").extract()[i].strip()
            items.append(item)
        print(items)





