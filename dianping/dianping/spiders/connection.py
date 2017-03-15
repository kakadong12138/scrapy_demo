# -*- coding: utf-8 -*-
import redis  
import six  
  
  
from scrapy.utils.misc import load_object  
  
  
  
  
DEFAULT_REDIS_CLS = redis.StrictRedis  
  
  
  
  
# Sane connection defaults.  
DEFAULT_PARAMS = {  
    'socket_timeout': 30,  
    'socket_connect_timeout': 30,  
    'retry_on_timeout': True,  
}  
  
  
# Shortcut maps 'setting name' -> 'parmater name'.  
SETTINGS_PARAMS_MAP = {  
    'REDIS_URL': 'url',  
    'REDIS_HOST': 'host',  
    'REDIS_PORT': 'port',  
}  
  
def get_redis_from_settings(settings):  
      
    params = DEFAULT_PARAMS.copy()  
    params.update(settings.getdict('REDIS_PARAMS'))  
    # XXX: Deprecate REDIS_* settings.  
    for source, dest in SETTINGS_PARAMS_MAP.items():  
        val = settings.get(source)  
        if val:  
            params[dest] = val  
  
  
    # Allow ``redis_cls`` to be a path to a class.  
    if isinstance(params.get('redis_cls'), six.string_types):  
        params['redis_cls'] = load_object(params['redis_cls'])  
  
  
    return get_redis(**params)  
  
  
# Backwards compatible alias.  
from_settings = get_redis_from_settings  
  
def get_redis(**kwargs):  
      
    redis_cls = kwargs.pop('redis_cls', DEFAULT_REDIS_CLS)  
    url = kwargs.pop('url', None)  
    if url:  
        return redis_cls.from_url(url, **kwargs)  
    else:  
        return redis_cls(**kwargs)  


        