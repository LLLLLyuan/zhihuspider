import json
from datetime import datetime
from urllib import parse

from scrapy import Request
from scrapy_redis_sentinel.spiders import RedisSpider
from searchengine.items import QuickSearchItem


class ZhihuSpider(RedisSpider):
    name = 'searchengine_zhihu_topic'

    redis_key = "start_urls:" + name
    custom_settings = {
        'DOWNLOADER_MIDDLEWARES': {
            'searchengine.middlewares.ZhihuBrotliMiddleware': 5,
        },
    }

    def make_request_from_data(self, data):
        value = eval(data)['values']
        lc_idx = offset = (int(value['page']) - 1) * 20
        ##https://www.zhihu.com/api/v4/search_v3?t=general&q=%E4%B8%AD%E8%88%B9%E9%87%8D%E5%B7%A5&correction=1&offset=20&limit=20&lc_idx=20&show_all_topics=0
        querystring = {
            "correction": "1",
            "lc_idx": lc_idx,
            "limit": "20",
            "offset": offset,
            "q": value['searchWord'],
            "show_all_topics": "0",
            "t": "topic",
        }
        url = "http://www.zhihu.com/api/v4/search_v3"
        url = f'{url}?{parse.urlencode(querystring, encoding="utf-8")}'
        return Request(
            url=url,
            dont_filter=True,
            meta={'data': value}
        )

    def parse(self, response):
        data = response.meta['data']
        items = QuickSearchItem()
        search_at = data.get('searchAt', None)
        items['searchAt'] = datetime.strptime(data.get('searchAt'),
                                              '%Y-%m-%dT%H:%M:%S.%f') if search_at else datetime.now()
        items['priority'] = 1
        items['subject'] = []
        items['page'] = int(data.get('page', 1))
        items['jobId'] = data.get('jobId', None)
        items["origin"] = data.get("origin", None)
        items["semanticTransformation"] = data.get("semanticTransformation", None)
        items['userId'] = data.get('userId', None)
        items['industry'] = data.get('industry', None)
        items['category'] = data.get('category', None)
        items['searchWord'] = data.get('searchWord', None)
        items['language'] = data.get('language', None)
        items['version'] = data.get('version', datetime.now())
        items['domain'] = parse.urlparse(response.url).netloc
        items["realPage"] = int(data.get("realPage", 1))
        data_list = json.loads(response.text, encoding="utf-8").get('data', None)
        if data_list:
            for one in data_list:
                if one["type"] == "search_result":
                    try:
                        title = one["object"]["name"].replace("<em>", "").replace("</em>", "").strip()
                        topic_id = one["object"]['id']
                        description = one["object"]['excerpt'].replace("<em>", "").replace("</em>", "").strip()
                        href = f"http://www.zhihu.com/topic/{topic_id}/hot"
                        items['tag'] = '知乎-话题'
                        items['target'] = href
                        items['source'] = None
                        items['releaseAt'] = None
                        items['title'] = title
                        items['description'] = description
                        items['returnAt'] = data.get("returnAt", datetime.now())
                        if items['title'] not in ["", None]:
                            print(items)
                            # yield items
                    except Exception as e:
                        pass
                        # print(str(e))
