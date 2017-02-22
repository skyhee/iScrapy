#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from scrapy.exceptions import DropItem

import codecs

class FilterWordsPipeline(object):
    """A pipeline for filtering out items which contain certain words in their
    description"""

    # put all words in lowercase
    # words_to_filter = ['pilgrim']

    # def process_item(self, item, spider):
    #     for word in self.words_to_filter:
    #         if False:
    #             raise DropItem("Contains forbidden word: %s" % word)
    #     else:
    #         return item
    def __init__(self):
        self.file = codecs.open(
            'scraped_data_utf8.json', 'w', encoding='utf-8')
    
    def spider_closed(self, spider):
        self.file.close()

import redis
Redis = redis.StrictRedis(host='localhost', port=6379, db=0)

class FilterDuplicatesPipeline(object):
    """Item去重复, 先安装redis，通过redis set去重复机制"""
    def process_item(self, item, spider):
        if Redis.exists('url:%s' % item['url']):
            raise DropItem("Duplicate item found: %s" % item)
        else:
            Redis.set('url:%s' % item['url'], 1)
            return item