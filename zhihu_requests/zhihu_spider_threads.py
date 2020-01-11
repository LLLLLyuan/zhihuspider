# -*- coding: utf-8 -*-
import json
import re
from concurrent.futures.thread import ThreadPoolExecutor
from datetime import datetime
from urllib import parse
import pandas
import requests


class ZhihuSpider():
    headers = {
        'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36",
        'Accept': "*/*",
        'Cache-Control': "no-cache",
        'Accept-Encoding': "gzip",
        'Connection': "keep-alive",
        'cache-control': "no-cache"
    }

    def __init__(self, search_keys, file_path):
        self.url_list = self.get_start_urls(search_keys)
        self.result_list = []
        with ThreadPoolExecutor() as p:  # 使用线程池
            while self.url_list:
                try:
                    p.submit(self.get_result(self.url_list[0]))  # 向线程池里添加任务
                except Exception as e:
                    print(str(e))
        self.sava_to_excel(file_path)

    def get_start_urls(self, search_keys):
        """
        构造初始url
        """
        if isinstance(search_keys, str):
            search_keys = [search_keys]
        urls = []
        for keys in search_keys:
            base_url = "https://www.zhihu.com/api/v4/search_v3"
            querystring = {"t": "general",
                           "q": keys,
                           "correction": "1",
                           "offset": "0",
                           "limit": "20",
                           }
            parms = parse.urlencode(querystring)
            url = f"{base_url}?{parms}"
            urls.append(url)
        return urls

    def get_result(self, url):
        self.url_list.remove(url)  # 每次先把url列表里的url删除掉
        response = requests.get(url, headers=self.headers)
        response.encoding = 'utf-8'
        dict_data = json.loads(response.text)
        for one in dict_data['data']:
            try:
                if one["type"] == "search_result":  # 知乎有时候会有其他推荐，类型不是search_result
                    one_info = {}
                    title = one["highlight"]["title"].replace("<em>", "").replace("</em>", "").strip()
                    question_id = one["object"]["question"]['id']
                    answer_id = one["object"]['id']
                    description = one["object"]['excerpt'].replace("<em>", "").replace("</em>", "").strip() + "..."
                    href = f"http://www.zhihu.com/question/{question_id}/answer/{answer_id}"
                    create_date = one["object"]['created_time']
                    content = re.sub('(<.*?>)', '', re.sub('(<br/>)', '\n', one["object"]['content']))
                    one_info['url'] = href
                    one_info['create_date'] = datetime.fromtimestamp(create_date)
                    one_info['title'] = title
                    one_info['description'] = description
                    one_info['content'] = content.strip()
                    one_info['response_url'] = response.url
                    self.result_list.append(one_info)  # 将每一条数据添加到result列表中
                    print(one_info)
            except Exception as e:
                # print(str(e))
                pass
        if dict_data['paging']['is_end'] is False:
            next_url = dict_data['paging']['next']
            self.url_list.append(next_url)  # 若有下一页，加入到url列表队列中

    def sava_to_excel(self, file_path):
        df = pandas.DataFrame(self.result_list)
        df.to_excel(file_path, index=False, encoding='utf-8-sig')
        print("save ok")


if __name__ == '__main__':
    search_keys = ["英雄联盟手游", "4AM", "2019考研", "春运", "特朗普", "电脑"]
    file_path = "zhuhu.xlsx"
    ZhihuSpider(search_keys=search_keys, file_path=file_path)
