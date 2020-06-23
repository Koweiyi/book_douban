# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
from book_douban import settings
from book_douban.items import BookItem, CommentItem, CriticItem


class BookDoubanPipeline:
    # 连接数据库
    def __init__(self):
        self.conn = pymysql.connect(
            host="localhost",
            user="root",
            passwd="",
            db="movie_douban",
            charset="utf-8",
            use_unicode=True,
            cursorclass=pymysql.cursors.DictCursor)
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):

        if isinstance(item, BookItem):
            self.process_book_item(item)
        elif isinstance(item, CommentItem):
            self.process_comment_item(item)
        elif isinstance(item, CriticItem):
            self.process_critic_item(item)
        return item

    def process_book_item(self, item):
        pass

    def process_comment_item(self, item):
        pass

    def process_critic_item(self, item):
        pass
