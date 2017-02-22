#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from scrapy.contrib.exporter import BaseItemExporter


class MyExporter(BaseItemExporter):
	"""
	scrapy 内置支持的item exporter有
	XmlItemExporter
	CsvItemExporter
	PickleItemExporter
	PprintItemExporter
	JsonItemExporter(输出 JSON 文件格式, 所有对象将写进一个对象的列表)
	JsonLinesItemExporter(输出 JSON 文件格式, 每行写一个 JSON-encoded 项,可用来处理大量数据)
	"""
	fields_to_export = []

    def serialize_field(self, field, name, value):
        if field == 'price':
            return '$ %s' % str(value)
        return super(Product, self).serialize_field(field, name, value)

    def start_exporting():
    	pass

    def export_item(item):
    	pass

    def finish_exporting():
    	pass

