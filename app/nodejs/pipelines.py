#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import logging
_log = logging.getLogger(__name__)

class MDExporterPipeline(object):
    """
    The purpose of JsonWriterPipeline is just to introduce how to write item pipelines.
    If you really want to store all scraped items into a JSON file you should use the Feed exports.
    """

    def __init__(self):
        # pass
        self.file = open('nodejs.md', 'w')

    def open_spider(self, spider):
        """This method is called when the spider is opened."""
        _log.info('MDExporterPipeline open_spider....')

    def process_item(self, item, spider):
        _log.info('MDExporterPipeline process_item....')
        line = "### "+item['package'] + "\n"
        self.file.write(line)
        return item

    def close_spider(self, spider):
        """This method is called when the spider is closed."""
        _log.info('MDExporterPipeline close_spider....')
        self.file.close()
