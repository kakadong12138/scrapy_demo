# scrapy_demo
改动说明
1.重写RFPDupeFilter，取消了保存每个request并去重的功能
2.任务改为从redis读取，需要在settings中配置redis信息，redis的key，在spider中配置
3.当队列为空时，不会关闭spider，而是一直等待新任务（所以需要关闭去重功能）
4.重试次数满的request，不会丢弃，而是存入redis中，key为原来的key后面加上_error
5.保存失败的request不会自动开启，需要自己在parse中写，例子如下
if response.status == 12138:
        item = self.parse_error(response)
	yield item
#DealUnsuccessRequestMiddleware这个中间件中，遇到重试次数满的request，会返回一个http code为12138的response，parse_error生成的item，会由RedisPipeline写入redis




