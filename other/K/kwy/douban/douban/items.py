# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BookItem(scrapy.Item):
    book_id = scrapy.Field()
    book_img = scrapy.Field()
    book_name = scrapy.Field()
    book_star = scrapy.Field()
    book_commentCount = scrapy.Field()
    book_author = scrapy.Field()
    book_publish = scrapy.Field()
    book_date = scrapy.Field()
    book_price = scrapy.Field()
    book_tag = scrapy.Field()


class Tag(scrapy.Item):
    tag_name = scrapy.Field()
    tag_isHot = scrapy.Field()


