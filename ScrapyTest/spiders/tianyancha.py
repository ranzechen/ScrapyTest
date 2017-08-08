# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from ScrapyTest.items import ScrapytianyanchaItem
class TianyanchaSpider(scrapy.Spider):
    name = 'tianyancha'
    allowed_domains = ['tianyancha.com']
    start_urls = ['http://tianyancha.com/']
#根据start_urls获取每个地区的url，并加入list最后yield返回请求每个url
    def parse(self, response):
        href = response.xpath("//div[@class='industry_container js-industry-container hidden bace_box']")
        hrefList = []
        beijing_href = href.xpath("div[1]/div[1]/a[1]/@href").extract()[0]
        tianjin_href = href.xpath("div[1]/div[2]/a[1]/@href").extract()[0]
        shanghai_href = href.xpath("div[1]/div[3]/a[1]/@href").extract()[0]
        chongqing_href = href.xpath("div[1]/div[4]/a[1]/@href").extract()[0]
        hebei_href = href.xpath("div[1]/div[5]/a[1]/@href").extract()[0]
        shanxi_href = href.xpath("div[1]/div[6]/a[1]/@href").extract()[0]
        neimenggu_href = href.xpath("div[1]/div[7]/a[1]/@href").extract()[0]
        liaoning_href = href.xpath("div[2]/div[1]/a[1]/@href").extract()[0]
        jilin_href = href.xpath("div[2]/div[2]/a[1]/@href").extract()[0]
        heilongjiang_href = href.xpath("div[2]/div[3]/a[1]/@href").extract()[0]
        jiangsu_href = href.xpath("div[2]/div[4]/a[1]/@href").extract()[0]
        zhejiang_href = href.xpath("div[3]/div[2]/a[1]/@href").extract()[0]
        anhui_href = href.xpath("div[3]/div[3]/a[1]/@href").extract()[0]
        fujian_href = href.xpath("div[3]/div[3]/a[1]/@href").extract()[0]
        jiangxi_href = href.xpath("div[4]/div[1]/a[1]/@href").extract()[0]
        shandong_href = href.xpath("div[4]/div[2]/a[1]/@href").extract()[0]
        henan_href = href.xpath("div[4]/div[3]/a[1]/@href").extract()[0]
        hubei_href = href.xpath("div[5]/div[1]/a[1]/@href").extract()[0]
        hunan_href = href.xpath("div[5]/div[2]/a[1]/@href").extract()[0]
        guangdong_href = href.xpath("div[5]/div[3]/a[1]/@href").extract()[0]
        guangxi_href = href.xpath("div[6]/div[1]/a[1]/@href").extract()[0]
        hainan_href = href.xpath("div[6]/div[2]/a[1]/@href").extract()[0]
        sichuan_href = href.xpath("div[6]/div[3]/a[1]/@href").extract()[0]
        guizhou_href = href.xpath("div[7]/div[1]/a[1]/@href").extract()[0]
        yunnan_href = href.xpath("div[7]/div[2]/a[1]/@href").extract()[0]
        xizang_href = href.xpath("div[7]/div[3]/a[1]/@href").extract()[0]
        shanxi2_href = href.xpath("div[7]/div[4]/a[1]/@href").extract()[0]
        gansu_href = href.xpath("div[8]/div[1]/a[1]/@href").extract()[0]
        qinghai_href = href.xpath("div[8]/div[2]/a[1]/@href").extract()[0]
        ningxia_href = href.xpath("div[8]/div[3]/a[1]/@href").extract()[0]
        xinjiang_href = href.xpath("div[8]/div[4]/a[1]/@href").extract()[0]
        hrefList.append(beijing_href)
        hrefList.append(tianjin_href)
        hrefList.append(shanghai_href)
        hrefList.append(chongqing_href)
        hrefList.append(hebei_href)
        hrefList.append(shanxi_href)
        hrefList.append(neimenggu_href)
        hrefList.append(liaoning_href)
        hrefList.append(jilin_href)
        hrefList.append(heilongjiang_href)
        hrefList.append(jiangsu_href)
        hrefList.append(zhejiang_href)
        hrefList.append(anhui_href)
        hrefList.append(fujian_href)
        hrefList.append(jiangxi_href)
        hrefList.append(shandong_href)
        hrefList.append(henan_href)
        hrefList.append(hubei_href)
        hrefList.append(hunan_href)
        hrefList.append(guangdong_href)
        hrefList.append(guangxi_href)
        hrefList.append(hainan_href)
        hrefList.append(sichuan_href)
        hrefList.append(guizhou_href)
        hrefList.append(yunnan_href)
        hrefList.append(xizang_href)
        hrefList.append(shanxi2_href)
        hrefList.append(gansu_href)
        hrefList.append(qinghai_href)
        hrefList.append(ningxia_href)
        hrefList.append(xinjiang_href)
        for j in range(0,len(hrefList)):
            yield Request(url = hrefList[j],callback = self.nextPage)

#获取到每个地区的url后获取分页数并yield返回请求每一页
    def nextPage(self,response):
        pageNums = response.xpath("//div[@class='total ng-binding']/text()").extract()[1].strip()
        for i in range(1,int(pageNums)+1):
            pageLink = "https://yn.tianyancha.com/search/p"+str(i)
            yield Request(url = pageLink,callback = self.companyLink)

#获取到每一页的数据后获取每页中公司的url并yield返回请求每个公司的url
    def companyLink(self,response):
        link = response.xpath("//div[@class='b-c-white search_result_container']")
        linkList = []
        for i in range(0,len(link)):
            for j in range(1,21):
                linkList.append(link.xpath("div["+str(j)+"]/div[2]/div[1]/div[1]/a/@href").extract()[i])
        for n in range(0,1):#len(linkList)
            yield Request(url=linkList[n],callback=self.getCompanyInfo)

#获取到每个公司的url后并解析公司的信息数据并放入item中
    def getCompanyInfo(self,response):
        headInfo = response.xpath("//div[@class='company_header_width ie9Style']")
        item = ScrapytianyanchaItem()
        for info in headInfo:
            item['name'] = info.xpath("div/span/text()").extract()[0].strip()
            item['phone'] = info.xpath("div/div[3]/div[1]/span[2]/text()").extract()[0].strip()
            item['email'] = info.xpath("div/div[3]/div[2]/span[2]/text()").extract()[0].strip()
            item['address'] = info.xpath("div/div[4]/div[2]/span[2]/text()").extract()[0].strip()

        item['regalRepresentative'] = response.xpath("//div[@class='new-c3 f18 overflow-width']/a/text()").extract()[0].strip()
        item['registeredCapital'] = response.xpath("//div[@class='new-border-bottom']/div[2]/div/text()").extract()[0].strip()
        item['registeredTime'] = response.xpath("//div[@class='new-border-bottom pt10']/div[2]/div/text()").extract()[0].strip()

        detailInfo = response.xpath("//div[@class='row b-c-white base2017']")
        for info2 in detailInfo:
            item['registrationNumber'] = info2.xpath("table/tbody/tr[1]/td[1]/div/span/text()").extract()[0].strip()
            item['organizationCode'] = info2.xpath("table/tbody/tr[1]/td[2]/div/span/text()").extract()[0].strip()
            item['unifiedSocialCreditCode'] = info2.xpath("table/tbody/tr[2]/td[1]/div/span/text()").extract()[0].strip()
            item['companyType'] = info2.xpath("table/tbody/tr[2]/td[2]/div/span/text()").extract()[0].strip()
            item['taxpayerIdentificationNumber'] = info2.xpath("table/tbody/tr[3]/td/div/span/text()").extract()[0].strip()
            item['industry'] = info2.xpath("table/tbody/tr[4]/td[1]/div/span/text()").extract()[0].strip()
            item['businessTerm'] = info2.xpath('table/tbody/tr[4]/td[2]/div/span/text()').extract()[0].strip()
            item['approvalDate'] = info2.xpath('table/tbody/tr[5]/td[1]/div/span/text()').extract()[0].strip()
            item['registrationAuthority'] = info2.xpath("table/tbody/tr[5]/td[2]/div/span/text()").extract()[0].strip()
            item['scopeOfBusiness'] = info2.xpath("table/tbody/tr[7]/td/div/span/span/span[1]/text()").extract()[0].strip()
            yield item




