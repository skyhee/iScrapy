#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
Topic: 爬取虎嗅网首页
Desc : 
"""
import logging
import scrapy
from app.nodejs.items import NodePackageItem


class NodeSpider(scrapy.Spider):
    name = "node"
    allowed_domains = ["nodejs.cn"]
    start_urls = [
        # "http://www.baidu.com"
        "http://nodejs.cn/doc/node"
    ]

    def parse(self, response):
        for pkgSel in response.xpath('//div[@id="column2"]/ul[position()=2]/li'):
            item = NodePackageItem()

            item['package'] = pkgSel.xpath('a/text()')[0].extract()
            item['desc'] = ""
            logging.info(item)
            yield item

    def parse_package(self, response):
        pass
