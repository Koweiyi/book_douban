# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from pyasn1.type import tag


class MovieItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    dbid = scrapy.Field()
    sort = scrapy.Field()
    url = scrapy.Field()
    title = scrapy.Field()
    score = scrapy.Field()
    motto = scrapy.Field()
    other_title = scrapy.Field()
class MovieDetailItem(scrapy.Item):
    direct = scrapy.Field()
    vote_num = scrapy.Field()
