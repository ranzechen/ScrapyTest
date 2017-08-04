# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class ScrapytestItem(scrapy.Item):
    # define the fields for your item here like:
    # must have ()
    # name = scrapy.Field()
    #pass
    title = scrapy.Field()
    author = scrapy.Field()
    times = scrapy.Field()
    perUrl = scrapy.Field()