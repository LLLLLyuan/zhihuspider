# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ZhihuItem(scrapy.Item):
    url = scrapy.Field()  # 问题链接
    create_date = scrapy.Field()  # 问题创建时间
    title = scrapy.Field()  # 标题
    description = scrapy.Field()  # 描述
    keyword = scrapy.Field()  # 搜索的关键字
    content = scrapy.Field()  # 内容
    response_url = scrapy.Field()  # 请求原链接
