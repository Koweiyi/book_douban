# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MovieItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    url = scrapy.Field()
    dbid = scrapy.Field()
    title = scrapy.Field()
    score = scrapy.Field()


class MovieDetailItem(scrapy.Item):
    other_title = scrapy.Field()
    direct = scrapy.Field()
    country = scrapy.Field()
    time = scrapy.Field()
    type = scrapy.Field()
    vote_num = scrapy.Field()
    five_star = scrapy.Field()
    four_star = scrapy.Field()
    three_star = scrapy.Field()
    two_star = scrapy.Field()
    one_star = scrapy.Field()


class MovieCommentItem(scrapy.Item):
    content = scrapy.Field()
    comment_time = scrapy.Field()
    comment_people = scrapy.Field()
    comment_star = scrapy.Field()
