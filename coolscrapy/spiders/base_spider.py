#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
Topic: 爬取虎嗅网首页
Desc : 
"""
import logging
import scrapy
from coolscrapy.items import HuxiuItem


class BaseSpider(scrapy.Spider):
    name = "base"
    allowed_domains = ["huxiu.com"]
    start_urls = [
        # "http://www.baidu.com"
        "http://www.huxiu.com"
    ]

    def parse(self, response):
        for sel in response.xpath('//div[@class="mod-info-flow"]/div/div[@class="mob-ctt"]'):
            item = HuxiuItem()
            item['title'] = sel.xpath('h2/a/text()')[0].extract()
            item['link'] = sel.xpath('h2/a/@href')[0].extract()
            
            sub = sel.xpath('div[contains(@class, "mob-sub")]')
            
            if len(sub.xpath('span')) > 0:
                item['desc'] = sub.xpath('span/text()')[0].extract()
            else:
                item['desc'] = sub.xpath('text()')[0].extract()
            url = response.urljoin(item['link'])
            yield scrapy.Request(url, callback=self.parse_article)

    def parse_article(self, response):
        detail = response.xpath('//div[@class="article-wrap"]')

        item = HuxiuItem()
        item['title'] = detail.xpath('h1/text()')[0].extract()
        item['url'] = response.url
        item['body'] = response.url
        item['source_site'] = response.url
        item['published'] = detail.xpath(
            'div[@class="article-author"]/span[@class="article-time"]/text()')[0].extract()
        
        # logging.info(item['title'],item['link'],item['published'])
        yield item
