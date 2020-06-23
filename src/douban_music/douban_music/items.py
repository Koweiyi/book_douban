# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MusicTagsItem(scrapy.Item):
    url = scrapy.Field()
    pass


class MusicTableItem(scrapy.Item):
    music_url = scrapy.Field()
    music_id = scrapy.Field()
    pass


class MusicDetailItem(scrapy.Item):
    music_name = scrapy.Field()
    music_man = scrapy.Field()
    music_rename = scrapy.Field()
    music_sect = scrapy.Field()
    music_media = scrapy.Field()
    music_time = scrapy.Field()
    music_mark = scrapy.Field()
    music_vote = scrapy.Field()
    music_star1 = scrapy.Field()
    music_star2 = scrapy.Field()
    music_star3 = scrapy.Field()
    music_star4 = scrapy.Field()
    music_star5 = scrapy.Field()
    music_comment1 = scrapy.Field()
    music_comment2 = scrapy.Field()
    music_comment3 = scrapy.Field()
    music_comment1_star = scrapy.Field()
    music_comment2_star = scrapy.Field()
    music_comment3_star = scrapy.Field()



    pass


class MusicUserItem(scrapy.Item):
    music_user_site1 = scrapy.Field()
    music_user_site2 = scrapy.Field()
    music_user_site3 = scrapy.Field()
    music_user_time1 = scrapy.Field()
    music_user_time2 = scrapy.Field()
    music_user_time3 = scrapy.Field()
    pass
