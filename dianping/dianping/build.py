# -*- coding: utf-8 -*-
import redis 
import settings
import json
from  spiders.connection import from_settings
from scrapy.utils.project import get_project_settings

s = get_project_settings()

key = settings.REDIS_START_URLS_KEY
key = "dianping_test2"
db = from_settings(s)

city_ids = range(1,10)
for city_id in city_ids:
    j = {"city_id":city_id}
    db.rpush(key,json.dumps(j))  #加在最右边，lpush是加在左边

