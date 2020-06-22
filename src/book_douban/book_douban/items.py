# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field


class BookItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    ID = Field()  # 书本在豆瓣中的subject ID
    book_name = Field()  # 书本名称
    book_author = Field()   # 作者
    publisher = Field()  # 出版社
    date = Field()  # 出版日期
    price = Field()  # 价格
    tags = Field()  # 书本标签
    intro = Field()  # 书本简介
    rate = Field()  # 评分
    rate_pl = Field()  # 评分人数
    five_star = Field()  # 五星比率
    for_star = Field()  # 四星比率
    three_star = Field()  # 三星比率
    two_star = Field()  # 二星比率
    one_star = Field()  # 一星比率


class CommentItem(Item):
    ID = Field()  # 评论对应subject ID
    critic = Field()  # 评论人
    date = Field()  # 评论时间
    content = Field()  # 评论内容
    critic_address = Field()  # 评论人地址
    star_num = Field()  # 评论星数
