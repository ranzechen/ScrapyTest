# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
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
        info = response.xpath("//div[@class='data_div_login']/section[@id='Cominfo']/table")
        list = info.xpath("tr/td/text()").extract()
        if info.xpath("tr/td/a/text()").extract() != "":
            farendaibiao = info.xpath("tr/td/a/text()").extract()[0]
        else:
            farendaibiao = ""
        name = response.xpath("//div[@class='col-md-12 m-b-md m-t-md no-padding m-l ']/span[2]/span/div[1]/div/text()").extract()[0]
        for i in range(0,len(list)):
            data = {
                list[0].replace("：","").strip():list[1].strip(),
                list[2].replace("：","").strip():list[3].strip(),
                list[4].replace("：","").strip():list[5].strip(),
                list[6].replace("：","").strip(): list[7].strip(),
                list[8].replace("：","").strip(): farendaibiao.strip(),
                list[10].replace("：","").strip(): list[11].strip(),
                list[12].replace("：","").strip(): list[13].strip(),
                list[14].replace("：","").strip(): list[15].strip(),
                list[16].replace("：","").strip(): list[17].strip(),
                list[18].replace("：","").strip(): list[19].strip(),
                list[20].replace("：","").strip(): list[21].strip(),
                list[22].replace("：","").strip(): list[23].strip(),
                list[24].replace("：", "").strip(): list[25].strip(),
                list[26].replace("：", "").strip(): list[27].strip(),
                list[28].replace("：", "").strip(): list[29].strip(),
                list[30].replace("：", "").strip(): list[31].strip(),
                list[32].replace("：", "").strip(): list[33].strip(),
                #list[34].replace("：", "").strip(): list[35].strip(),
                "公司名称":name.strip()
            }
        data.pop('')
        print(data)
        with open('qichacha.txt', 'a',encoding="utf-8") as f:
            f.write(str(data) + '\n')





