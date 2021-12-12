# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class JokerspidrItem(scrapy.Item):
    domain = scrapy.Field()
    url = scrapy.Field()
    title = scrapy.Field()
    author = scrapy.Field()
    content = scrapy.Field()
    pubtime = scrapy.Field()
    clickNum = scrapy.Field()
    category = scrapy.Field()
