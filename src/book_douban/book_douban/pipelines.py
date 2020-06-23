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
        try:
            self.cursor.execute('''
                SELECT * FROM books WHERE ID = %s''', (item['ID'],))
            book = self.cursor.fetchone()
            if book is None:
                self.cursor.execute('''
                INSERT INTO books(ID, book_name, book_author, publisher, date,
                price, tags, intro, rate, rate_pl, five_star, four_star, three_star, two_star, one_star) 
                value(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)''',
                                    (item['ID'], item['book_name'], item['book_author'], item['publisher'],
                                     item['date'], item['price'], item['tags'], item['intro'], item['rate'],
                                     item['rate_pl'], item['five_star'], item['four_star'], item['three_star'],
                                     item['two_star'], item['one_star']))
            self.conn.commit()
        except Exception as err:
            print("数据库报错==>错误信息为：" + str(err))
        pass

    def process_comment_item(self, item):
        try:
            self.cursor.execute('''
                SELECT * FROM book_comment WHERE ID = %s''', (item['ID'],))
            comment = self.cursor.fetchone()
            if comment is None:
                self.cursor.execute('''
                INSERT INTO book_comment(ID, critic, date, content, star_num)
                value(%s, %s, %s, %s, %s)''',
                                    (item['ID'], item['critic'], item['date'], item['content'], item['star_num']))
            self.conn.commit()
        except Exception as err:
            print("数据库报错==>错误信息为：" + str(err))
        pass

    def process_critic_item(self, item):
        try:
            self.cursor.execute('''
            SELECT * FROM douban_user WHERE user_name = %s''', (item['user_name'],))
            critic = self.cursor.fetchone()
            if critic is None:
                self.cursor.execute('''
                INSERT INTO douban_user(user_name, user_address, join_date)''',
                                    (item['user_name'], item['user_address'], item['join_date']))
            self.conn.commit()
            pass
        except Exception as err:
            print("数据库报错==>错误信息为：" + str(err))
        pass
