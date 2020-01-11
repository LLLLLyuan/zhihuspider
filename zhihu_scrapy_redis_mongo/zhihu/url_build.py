from urllib import parse

import redis

REDIS_HOST = 'localhost'
REDIS_PASSWORD = ""
REDIS_DB = 0
REDIS_PORT = 6379


class UrlBuild(object):
    def __init__(self):
        pool = redis.ConnectionPool(host=REDIS_HOST, port=REDIS_PORT, db=REDIS_DB, password=REDIS_PASSWORD)
        self.client = redis.Redis(connection_pool=pool)

    def build(self, search_keys, spider_name):
        base_url = "https://www.zhihu.com/api/v4/search_v3"
        successful_num = 0
        failed_num=0
        try:
            for key in search_keys:
                querystring = {"t": "general",
                               "q": key,
                               "correction": "1",
                               "offset": "0",
                               "limit": "20",
                               }
                parms = parse.urlencode(querystring)
                url = f"{base_url}?{parms}"
                self.client.rpush(f"start_urls:{spider_name}", url)
                successful_num += 1
                print(url)
        except:
            failed_num+=1
        print(f"共{len(search_keys)}条url，成功{successful_num}条，失败{failed_num}条。")


if __name__ == '__main__':
    search_keys = ["英雄联盟手游", "4AM", "2019考研", "春运", "特朗普", "电脑"]
    UrlBuild().build(search_keys=search_keys, spider_name="zhihu_redis_spider")
