#!/usr/bin/env python
# -*- encoding: utf-8 -*-


from scrapy import signals
from scrapy.contrib.exporter import XmlItemExporter

class XmlExportPipeline(object):

    def __init__(self):
        self.files = {}

     @classmethod
     def from_crawler(cls, crawler):
         pipeline = cls()
         crawler.signals.connect(pipeline.spider_opened, signals.spider_opened)
         crawler.signals.connect(pipeline.spider_closed, signals.spider_closed)
         return pipeline

    def spider_opened(self, spider):
    	# 指定保存的文件名
        file = open('%s_file.xml' % spider.name, 'w+b')
        self.files[spider] = file
        self.exporter = XmlItemExporter(file)
        self.exporter.start_exporting()

    def spider_closed(self, spider):
        self.exporter.finish_exporting()
        file = self.files.pop(spider)
        file.close()

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item

import json
import logging
_log = logging.getLogger(__name__)

class JsonExporterPipeline(object):
    """
    The purpose of JsonWriterPipeline is just to introduce how to write item pipelines.
    If you really want to store all scraped items into a JSON file you should use the Feed exports.
    """

    def __init__(self):
        pass
        self.file = open('items.json', 'wb')

    def open_spider(self, spider):
        """This method is called when the spider is opened."""
        _log.info('open_spider....')

    def process_item(self, item, spider):
        _log.info('process_item....')
        line = json.dumps(dict(item)) + "\n"
        self.file.write(line)
        return item

    def close_spider(self, spider):
        """This method is called when the spider is closed."""
        _log.info('close_spider....')
        self.file.close()

import datetime
from scrapy.exceptions import DropItem
from sqlalchemy.orm import sessionmaker
from coolscrapy.models import News, db_connect, create_news_table
from coolscrapy.utils import session_scope

class NewsDatabasePipeline(object):
    """保存新闻到数据库"""

    def __init__(self):
        """
        Initializes database connection and sessionmaker.
        Creates deals table.
        """
        engine = db_connect()
        create_news_table(engine)
        # 初始化对象属性Session为可调用对象
        self.Session = sessionmaker(bind=engine)
        self.recent_links = None
        self.nowtime = datetime.datetime.now()

    def open_spider(self, spider):
        """This method is called when the spider is opened."""
        _log.info('open_spider[%s]....' % spider.name)
        session = self.Session()
        recent_news = session.query(News).filter(
            News.crawlkey == spider.name,
            self.nowtime - News.pubdate <= datetime.timedelta(days=30)).all()
        self.recent_links = [t.link for t in recent_news]
        _log.info(self.recent_links)

    def process_item(self, item, spider):
        """Save deals in the database.
        This method is called for every item pipeline component.
        """
        # 每次获取到Item调用这个callable，获得一个新的session
        _log.info('mysql->%s' % item['link'])
        if item['link'] not in self.recent_links:
            with session_scope(self.Session) as session:
                news = News(**item)
                session.add(news)
                self.recent_links.append(item['link'])
        return item

    def close_spider(self, spider):
        pass        
