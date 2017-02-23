# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class NodePackageItem(scrapy.Item):
    """nodejs内置包Item"""
    package = scrapy.Field()      # 包名
    desc = scrapy.Field()       # 描述