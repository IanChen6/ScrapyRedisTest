#基于redis的scrapy

from scrapy_redis.spiders import RedisSpider

class JinRiSpider(RedisSpider):
    name = 'JinRiSpider'
    allowed_domains = ['www.toutiao.com']


    #重写redis_key
    redis_key = 'JinRiSpider:start_urls'

    def parse(self, response):
        # do stuff
        response.css(".feed-infinite-wrapper ")
        pass