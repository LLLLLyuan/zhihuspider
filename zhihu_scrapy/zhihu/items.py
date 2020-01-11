# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ZhihuItem(scrapy.Item):
    url = scrapy.Field()
    create_date = scrapy.Field()
    title = scrapy.Field()
    description = scrapy.Field()
    keyword = scrapy.Field()
