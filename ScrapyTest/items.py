# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class ScrapyqichachaItem(scrapy.Item):
    name = scrapy.Field()
    email = scrapy.Field()
    phone = scrapy.Field()
    unifiedSocialCreditCode = scrapy.Field()#统一社会信用代码
    taxpayerIdentificationNumber = scrapy.Field()#纳税人识别号
    registrationNumber = scrapy.Field()#注册号
    regalRepresentative = scrapy.Field()#法定代表人
    organizationCode = scrapy.Field()#组织机构代码
    registeredCapital = scrapy.Field()#注册资本
    operatingState = scrapy.Field()#经营状态
    setupDate = scrapy.Field()#成立日期
    companyType = scrapy.Field()#公司类型
    staffSize = scrapy.Field()#人员规模
    businessTerm = scrapy.Field()#营业期限
    registrationAuthority  = scrapy.Field()#登记机关
    approvalDate = scrapy.Field()#核准日期
    companyEnglishName = scrapy.Field()#公司英文名称
    industry = scrapy.Field()#所属行业
    address = scrapy.Field()#公司地址
    scopeOfBusiness = scrapy.Field()#经营范围

class ScrapytianyanchaItem(scrapy.Item):
    name = scrapy.Field()
    email = scrapy.Field()
    phone = scrapy.Field()
    address = scrapy.Field()
    regalRepresentative = scrapy.Field()  # 法定代表人
    registeredCapital = scrapy.Field()#注册资本
    registeredTime = scrapy.Field()  # 成立日期
    registrationNumber = scrapy.Field()#注册号
    organizationCode = scrapy.Field()#组织机构代码
    unifiedSocialCreditCode = scrapy.Field()#统一社会信用代码
    companyType = scrapy.Field()#公司类型
    taxpayerIdentificationNumber = scrapy.Field()#纳税人识别号
    industry = scrapy.Field()#所属行业
    businessTerm = scrapy.Field()  # 营业期限
    approvalDate = scrapy.Field()  # 核准日期
    registrationAuthority  = scrapy.Field()#登记机关
    scopeOfBusiness = scrapy.Field()#经营范围

class ScrapyqiyeItem(scrapy.Item):
    name = scrapy.Field()
    address = scrapy.Field()
    phone = scrapy.Field()
    boss = scrapy.Field()
    buiness = scrapy.Field()
    license = scrapy.Field()
    fazhengjiguan = scrapy.Field()
    hezhunriqi = scrapy.Field()
    jingyingzhuangtai = scrapy.Field()
    chengliriqi = scrapy.Field()
    zhuceziben = scrapy.Field()
    suoshufenlei = scrapy.Field()
    renqizhi = scrapy.Field()