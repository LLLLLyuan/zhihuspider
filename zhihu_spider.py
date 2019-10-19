# -*- coding: utf-8 -*-
import json
from datetime import datetime

import pandas
import requests


class ZhihuSpider():

    def __init__(self,search_key,file_path):
        response = self.get_response(search_key)
        dict_data = self.json_to_dict(response.text)
        result_list = []
        url, self.result_list = self.get_result(dict_data,result_list)
        while url:
            response = requests.get(url, headers=self.headers)
            dict_data = self.json_to_dict(response.text)
            url, result_list = self.get_result(dict_data, self.result_list)
        self.sava_to_excel(file_path)


    def get_response(self, search_key):
        url = "https://www.zhihu.com/api/v4/search_v3"
        self.headers = {
            'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36",
            'Accept': "*/*",
            'Cache-Control': "no-cache",
            'Accept-Encoding': "gzip",
            'Connection': "keep-alive",
            'cache-control': "no-cache"
        }
        querystring = {"t": "general",
                       "q": search_key,
                       "correction": "1",
                       "offset": "0",
                       "limit": "20",
                       }
        response = requests.request("GET", url, headers=self.headers, params=querystring)
        response.encoding = response.apparent_encoding
        return response

    def json_to_dict(self, json_data):
        dict_data = json.loads(json_data, encoding="utf_8_sig")
        return dict_data

    def get_result(self, dict_data, result_list):
        if dict_data['paging']['is_end'] is False:
            next_url = dict_data['paging']['next']
        else:
            next_url = None
        for one in dict_data['data']:
            try:
                if one["type"] == "search_result":     # 知乎有时候会有其他推荐，类型不是search_result
                    one_info = {}
                    title = one["highlight"]["title"].replace("<em>", "").replace("</em>", "").strip()
                    question_id = one["object"]["question"]['id']
                    answer_id = one["object"]['id']
                    description = one["object"]['excerpt'].replace("<em>", "").replace("</em>", "").strip() + "..."
                    href = f"http://www.zhihu.com/question/{question_id}/answer/{answer_id}"
                    create_date = one["object"]['created_time']
                    one_info['url'] = href
                    one_info['create_date'] = datetime.fromtimestamp(create_date)
                    one_info['title'] = title
                    one_info['description'] = description
                    result_list.append(one_info)
                    print(one_info)
            except Exception as e:
                # print(str(e))
                pass
        return next_url,result_list

    def sava_to_excel(self, file_path):
        df = pandas.DataFrame(self.result_list)
        df.to_csv(file_path, index=False, encoding='utf-8')
        print("save ok")

if __name__ == '__main__':
    search_key = "英雄联盟手游"
    file_path = "zhuhu.csv"
    ZhihuSpider(search_key=search_key,file_path=file_path)



