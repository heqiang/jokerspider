import datetime
import re

import scrapy
from jokerspidr.items import JokerspidrItem


class IshuoSpider(scrapy.Spider):
    name = 'ishuo'
    start_urls = ['https://duanzixing.com/']

    def start_requests(self):
        url = self.start_urls[0]
        yield scrapy.Request(url=url, callback=self.parselist)

    def parselist(self, response):
        for x in response.xpath('//div[@class="content"]/article//h2/a/@href').extract():
            yield scrapy.Request(x, callback=self.parse)

    def parse(self, response, **kwargs):
        item = JokerspidrItem()
        item["domain"] = "duanzixing.com"
        item["url"] = response.url
        item["title"] = response.xpath('//h1[@class="article-title"]/a/text()').extract_first()
        item["author"] = "matthua"
        item["content"] = "\n".join(response.xpath('//article[@class="article-content"]//p/text()').extract())
        timeinfo = response.xpath('//div[@class="article-meta"]/span[1]/text()').extract_first()
        item["pubtime"] = str(datetime.datetime.strptime(timeinfo,"%Y-%m-%d"))
        clickName = response.xpath('//span[@class="item post-views"]/text()').extract_first()
        item["clickNum"] = int(re.findall("\d+", clickName)[0])
        item["category"] = response.xpath('//span[@class="item"]/a/text()').extract_first()
        yield item
