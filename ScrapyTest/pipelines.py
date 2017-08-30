# -*- coding: utf-8 -*-

# Don't forget to add your pipeline to the ITEM_PIPELINES setting
from twisted.enterprise import adbapi
import pymysql
import pymysql.cursors
import json
import codecs

class JsonPipeline(object):
     def __init__(self):
         self.file = codecs.open('C:\\Users\\dell\\Desktop\\result.json', 'w', encoding='utf-8')
     def process_item(self, item, spider):
         line = json.dumps(dict(item), ensure_ascii=False) + "\n"
         self.file.write(line)
         return item
     def spider_closed(self, spider):
         self.file.close()


class ScrapyqichachaPipeline(object):
    def process_item(self, item, spider):
        return item

class ScrapytianyanchaPipeline(object):
    # 数据库参数
    def __init__(self):
        dbargs = dict(
            host='168.33.222.97',
            db='scrapy',
            user='root',
            passwd='123456',
            cursorclass=pymysql.cursors.DictCursor,
            charset='utf8',
            use_unicode=True
        )
        self.dbpool = adbapi.ConnectionPool('pymysql', **dbargs)

    def process_item(self, item, spider):
        res = self.dbpool.runInteraction(self.insert_into_table, item)
        print(item)
        return item
        # 插入的表，此表需要事先建好

    def insert_into_table(self, conn, item):
        conn.execute('insert into tianyancha(name,email,phone,address,regalRepresentative,registeredCapital,registeredTime,registrationNumber,organizationCode,unifiedSocialCreditCode,companyType,taxpayerIdentificationNumber,industry,businessTerm,approvalDate,registrationAuthority,scopeOfBusiness) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)', (
        item['name'],
        item['email'],
        item['phone'],
        item['address'],
        item['regalRepresentative'],
        item['registeredCapital'],
        item['registeredTime'],
        item['registrationNumber'],
        item['organizationCode'],
        item['unifiedSocialCreditCode'],
        item['companyType'],
        item['taxpayerIdentificationNumber'],
        item['industry'],
        item['businessTerm'],
        item['approvalDate'],
        item['registrationAuthority'],
        item['scopeOfBusiness']
        )
                     )


