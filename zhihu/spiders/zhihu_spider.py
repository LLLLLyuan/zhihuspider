# -*- coding: utf-8 -*-
import json
import re
from datetime import datetime
from urllib import parse

import scrapy
from scrapy import Request

from zhihu.items import ZhihuItem


class ZhihuSpider(scrapy.Spider):
    name = 'zhihu_spider'
    allowed_domains = ['zhihu.com']

    search_keys = ["雪莉", "S9", "海贼王狂热行动", "爬虫", "数据分析"]
    start_urls = []
    for search_key in search_keys:
        base_url = "https://www.zhihu.com/api/v4/search_v3"
        querystring = {"t": "general",
                       "q": search_key,
                       "correction": "1",
                       "offset": "0",
                       "limit": "20",
                       }
        url = f"{base_url}?{parse.urlencode(querystring)}"
        start_urls.append(url)

    def parse(self, response):
        # print(response.status,response.url)
        search_key = re.search(r'q=(.*?)&', response.url).group(1)
        search_key = parse.unquote(search_key)
        # print(parse.unquote(search_key))
        json_data = response.text
        dict_data = json.loads(json_data, encoding="utf_8_sig")
        if dict_data['paging']['is_end'] is False:
            next_url = dict_data['paging']['next']
            yield Request(url=next_url, callback=self.parse)
        for one in dict_data['data']:
            try:
                if one["type"] == "search_result":
                    item = ZhihuItem()
                    title = one["highlight"]["title"].replace("<em>", "").replace("</em>", "").strip()
                    question_id = one["object"]["question"]['id']
                    answer_id = one["object"]['id']
                    description = one["object"]['excerpt'].replace("<em>", "").replace("</em>", "").strip() + "..."
                    href = f"http://www.zhihu.com/question/{question_id}/answer/{answer_id}"
                    create_date = one["object"]['created_time']
                    item['url'] = href
                    item['create_date'] = datetime.fromtimestamp(create_date)
                    item['title'] = title
                    item['description'] = description
                    item['keyword'] = search_key
                    yield item
            except Exception as e:
                # print(str(e))
                pass
