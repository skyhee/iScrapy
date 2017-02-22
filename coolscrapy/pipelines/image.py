#!/usr/bin/env python
# -*- encoding: utf-8 -*-

class MyImagesPipeline(ImagesPipeline):
    """先安装：pip install Pillow"""

    def item_completed(self, results, item, info):
        image_paths = [x['path'] for ok, x in results if ok]
        if not image_paths:
            raise DropItem("Item contains no images")
        return item
