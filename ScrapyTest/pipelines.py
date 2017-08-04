# -*- coding: utf-8 -*-

# Don't forget to add your pipeline to the ITEM_PIPELINES setting
from twisted.enterprise import adbapi
import pymysql
import pymysql.cursors

class ScrapytestPipeline(object):

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
        return item
        # 插入的表，此表需要事先建好
    def insert_into_table(self, conn, item):
        conn.execute('insert into jiexin_tieba(author,title,times) values(%s,%s,%s,%s)', (
            item['author'][0],
            item['title'][0],
            item['times'][0],
            item['perUrl'][0]
            )
        )
