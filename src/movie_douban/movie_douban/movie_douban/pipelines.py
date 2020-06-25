# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
from movie_douban import settings
from movie_douban.items import MovieItem, MovieDetailItem, MovieCommentItem


class MovieDoubanPipeline(object):

    def __init__(self):
        self.connect = pymysql.connect(
            host=settings.MYSQL_HOST,
            port=settings.MYSQL_PORT,
            db=settings.MYSQL_DBNAME,
            user=settings.MYSQL_USER,
            passwd=settings.MYSQL_PASSWD,
            charset='utf8mb4',
            use_unicode=True,
            cursorclass=pymysql.cursors.DictCursor)
        self.cursor = self.connect.cursor()

    def process_item(self, item, spider):


        return item
