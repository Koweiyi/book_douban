# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql
from twisted.enterprise import adbapi
from scrapy.utils.project import get_project_settings
import pymysql.cursors


# 图书信息管道
class BookItemPipeline(object):
    def __init__(self, db_pool):
        settings = get_project_settings()
        self.db_pool = db_pool

    @classmethod
    def from_settings(cls, settings):
        # 连接数据库
        adb_parm = dict(
            host=settings.get('MYSQL_HOST'),
            port=settings.get('MYSQL_PORT'),
            db=settings.get('MYSQL_DATABASE'),
            user=settings.get('MYSQL_USER'),
            passwd=settings.get('MYSQL_PASSWORD'),
            charset=settings.get('MYSQL_CHARSET'),
            use_unicode=True,
            cursorclass=pymysql.cursors.DictCursor
        )
        # 连接数据池
        db_pool = adbapi.ConnectionPool('pymysql', **adb_parm)
        return cls(db_pool)

    def process_item(self, item):
        # 指定操作方法和操作数据
        query = self.db_pool.runInteraction(self.insert, item)
        # 处理异常
        query.addCallback(self.hand_error)
        return item

    @staticmethod
    def insert(self, cursor, item):
        # 对数据库进行插入操作，twisted会自动commit
        book_values = (
            item['book_id'],
            item['book_img'],
            item['book_name'],
            item['book_star'],
            item['book_commentCount'],
            item['book_author'],
            item['book_publish'],
            item['book_date'],
            item['book_price']
        )
        sql = 'INSERT INTO book_Asyn VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        cursor.execute(sql, book_values)

    @staticmethod
    def handle_error(self, failure):
        if failure:
            print("BookItem Insert to DB failed")
            print(failure)


# 标签信息管道
class TagItemPipeline(object):
    def __init__(self, db_pool):
        self.db_pool = db_pool

    @classmethod
    def from_settings(cls, settings):
        adb_parm = dict(
            host=settings.get('MYSQL_HOST'),
            port=settings.get('MYSQL_PORT'),
            db=settings.get('MYSQL_DATABASE'),
            user=settings.get('MYSQL_USER'),
            passwd=settings.get('MYSQL_PASSWORD'),
            charset=settings.get('MYSQL_CHARSET'),
            use_unicode=True,
            cursorclass=pymysql.cursors.DictCursor
        )
        db_pool = adbapi.ConnectionPool('pymysql', **adb_parm)
        return cls(db_pool)

    def process_item(self, item, spider):
        query = self.db_pool.runInteraction(self.insert, item)
        query.addCallback(self.handle_error)
        return item

    def insert(self, cursor, item):
        tag_values = (
            item['tag_name'],
            item['tag_isHot']
        )
        sql = 'REPLACE INTO tag_Asyn VALUES(%s,%s)'
        cursor.execute(sql, tag_values)

    def handle_error(self, failure):
        if failure:
            print("TagItem to DB failed")
            print(failure)


# 图书对应标签信息管道
class BookTagPipeline(object):
    def __init__(self, db_pool):
        self.db_pool = db_pool

    @classmethod
    def from_settings(cls, settings):
        adb_parm = dict(
            host=settings.get('MYSQL_HOST'),
            port=settings.get('MYSQL_PORT'),
            db=settings.get('MYSQL_DATABASE'),
            user=settings.get('MYSQL_USER'),
            passwd=settings.get('MYSQL_PASSWORD'),
            charset=settings.get('MYSQL_CHARSET'),
            use_unicode=True,
            cursorclass=pymysql.cursors.DictCursor
        )
        db_pool = adbapi.ConnectionPool('pymysql', **adb_parm)
        return cls(db_pool)

    def process_item(self, item):
        query = self.db_pool.runInteraction(self.insert, item)
        query.addCallback(self.hand_error)
        return item

    @staticmethod
    def insert(self, cursor, item):
        tag_values = (
            item['tag_name'],
            item['tag_isHot']
        )
        sql = 'INSERT INTO book_tag VALUES(%s,%s)'
        cursor.execute(sql, tag_values)

    @staticmethod
    def handle_error(self, failure):
        if failure:
            print("BookTags Insert to DB failed")
            print(failure)

