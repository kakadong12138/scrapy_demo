# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup
import base64
from scrapy.http import Request
import traceback
import time
import pymongo
import re
import json
import copy
from MyBaseSpider import RedisSpider


class RestaurantIdSpider(RedisSpider):
    name = "test1"
    allowed_domains = ["dianping.com"]
    handle_httpstatus_list = [301,302,403,404,500,12138]
    retry_mode = False
    custom_settings = {
        #"USER_AGENT":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:45.0) Gecko/20100101 Firefox/45.0",
        "REDIS_START_URLS_KEY":"dianping_test2"}


    def make_request_from_data(self, data):  
        city_id = data.get("city_id")
        url = "http://www.dianping.com/search/category/1/%s"%(city_id)
        return Request(url,meta={"task_json":data},callback=self.parse_1)

    def parse_1(self,response):
        meta = response.meta
        if response.status == 12138:
            item = self.parse_error(response)
            print item
            yield item
        






