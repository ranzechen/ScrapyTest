# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
import urllib.request

class TianyanchaSpider(scrapy.Spider):
    name = 'tianyancha'
    allowed_domains = ['tianyancha.com']
    start_urls = ['https://www.tianyancha.com/']
    website_possible_httpstatus_list = [404]
#根据start_urls获取每个地区的url，并拼出每个地区url的10页数据
    def parse(self, response):
        info = response.xpath("//div[@class='industry_container js-industry-container hidden bace_box']")
        hrefList = info.xpath("div/div/a[1]/@href").extract()
        for url in hrefList:
            for i in range(1,21):#指定每个地区爬取的页数
                link = url + "/p" + str(i)
                yield Request(url=link,callback=self.companyLink)
#获取到每一页的数据后获取每页中公司的url并yield返回请求每个公司的url
    def companyLink(self,response):
        for link in response.xpath("//div[@class='b-c-white search_result_container']/div/div/div/div/a/@href").extract():
            yield Request(url=link,callback=self.getCompanyInfo)
#获取到每个公司的url后并解析公司的信息数据并放入item中
    def getCompanyInfo(self,response):
        headInfo = response.xpath("//div[@class='company_header_width ie9Style']")
        info = headInfo.xpath("div/div/div/span/text()").extract()
        name = headInfo.xpath("div/span/text()").extract()[0].strip()
        data = {}
        data[info[0].replace("：", "").strip()] = str(headInfo.xpath("div/div[2]/div[1]/span[2]/text()").extract()).replace("：", "").replace("'[","").replace("]'","").replace("['","").replace("']","").strip()
        data[info[2].replace("：", "").strip()] = str(headInfo.xpath("div/div[2]/div[2]/span[2]/text()").extract()).replace("：", "").replace("'[","").replace("]'","").replace("['","").replace("']","").strip()
        data[info[4].replace("：", "").strip()] = str(headInfo.xpath("div/div[3]/div[1]/a/text()").extract()).replace("：", "").replace("'[","").replace("]'","").replace("['","").replace("']","").strip()
        data[info[6].replace("：", "").strip()] = str(headInfo.xpath("div/div[3]/div[2]/span[2]/text()").extract()).replace("：", "").replace("'[","").replace("]'","").replace("['","").replace("']","").strip()
        data["公司名称"] = name
        data["法人代表"] = response.xpath("//div[@class='new-c3 f18 overflow-width']/a/text()").extract()[0].strip()
        data["注册资本"] = response.xpath("//div[@class='new-border-bottom']/div[2]/div/text()").extract()[0].strip()
        data["注册时间"] = response.xpath("//div[@class='new-border-bottom pt10']/div[2]/div/text()").extract()[0].strip()

        detailInfo = response.xpath("//div[@class='row b-c-white base2017']")
        detaildata = detailInfo.xpath("table/tbody/tr/td/div/span/text()").extract()
        data["工商注册号"] = detaildata[0].strip()
        data["组织机构代码"] = detaildata[1].strip()
        data["统一信用代码"] = detaildata[2].strip()
        data["企业类型"] = detaildata[3].strip()
        data["纳税人识别号"] = detaildata[4].strip()
        data["行业"] = detaildata[5].strip()
        data["营业期限"] = detaildata[6].replace("\n","").replace(" ","")
        data["核准日期"] =detaildata[7].strip()
        data["登记机关"] = detaildata[8].strip()
        data["注册地址"] = detaildata[9].strip()
        data["经营范围"] = str(response.xpath("//span[@class='js-full-container hidden']/text()").extract()).replace("'[","").replace("]'","").replace("['","").replace("']","").strip()
        print(data)
        with open('tianyancha.txt', 'a', encoding="utf-8") as f:
            f.write(str(data) + '\n')




