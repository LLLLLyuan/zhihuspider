# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from pymongo import MongoClient


class ZhihuPipeline(object):

    def __init__(self):
        self.client = MongoClient(host="localhost", port=27017)

    def process_item(self, item, spider):
        mongo_db = "zhihu"
        mongo_collection = "zhihu_answer"
        self.client[mongo_db][mongo_collection].update_one(
            filter={"url": item["url"]},
            update={"$set": dict(item)},
            upsert=True
        )
        return item

    def close_spider(self, spider):
        self.client.close()
