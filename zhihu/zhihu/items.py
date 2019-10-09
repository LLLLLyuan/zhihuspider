# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ZhihuItem(scrapy.Item):
    page_url = scrapy.Field()  # 详细页地址
    created_time = scrapy.Field()  # 爬取时间
    version = scrapy.Field()  # 版本

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for key in self.fields.keys():
            self.setdefault(key, None)
