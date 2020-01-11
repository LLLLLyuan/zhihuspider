# -*- coding: utf-8 -*-
import json
import re
from datetime import datetime
from urllib import parse
from scrapy import Request
from scrapy_redis.spiders import RedisSpider
from zhihu.items import ZhihuItem


class ZhihuRedisSpiderSpider(RedisSpider):
    name = 'zhihu_redis_spider'
    allowed_domains = ['zhihu.com']
    redis_key = f"start_urls:{name}"

    def parse(self, response):
        search_key = re.search(r'q=(.*?)&', response.url).group(1)
        search_key = parse.unquote(search_key)
        json_data = response.text
        dict_data = json.loads(json_data)
        if dict_data['paging']['is_end'] is False:
            next_url = dict_data['paging']['next']
            yield Request(url=next_url, callback=self.parse)
        for one in dict_data['data']:
            if one["type"] == "search_result":
                item = ZhihuItem()
                try:
                    title = one["highlight"]["title"].replace("<em>", "").replace("</em>", "").strip()
                    question_id = one["object"]["question"]['id']
                    answer_id = one["object"]['id']
                    description = one["object"]['excerpt'].replace("<em>", "").replace("</em>", "").strip() + "..."
                    content = re.sub('(<.*?>)', '', re.sub('(<br/>)', '\n', one["object"]['content']))
                    href = f"http://www.zhihu.com/question/{question_id}/answer/{answer_id}"
                    create_date = one["object"]['created_time']
                    item['url'] = href
                    item['create_date'] = datetime.fromtimestamp(create_date)
                    item['title'] = title
                    item['description'] = description
                    item['keyword'] = search_key
                    item['content'] = content.strip()
                    item['response_url'] = response.url
                    yield item
                except:
                    try:
                        title = one["highlight"]["title"].replace("<em>", "").replace("</em>", "").strip()
                        answer_type = one["object"]["type"]
                        if answer_type == "article":
                            id = one["object"]["id"]
                            description = one["object"]['excerpt'].replace("<em>", "").replace("</em>","").strip() + "..."
                            content = re.sub('(<.*?>)', '', re.sub('(<br/>)', '\n', one["object"]['content']))
                            href = f"http://zhuanlan.zhihu.com/p/{id}"
                            create_date = one["object"]['created_time']
                            item['url'] = href
                            item['create_date'] = datetime.fromtimestamp(create_date)
                            item['title'] = title
                            item['description'] = description
                            item['keyword'] = search_key
                            item['content'] = content.strip()
                            item['response_url'] = response.url
                            yield item
                    except Exception as e:
                        print('+++++++++++')
                        print(f"报错了：{str(e)}")
                        print('+++++++++++')
