# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
import codecs
import json

from scrapy.pipelines.images import ImagesPipeline

from book_douban import settings
from book_douban.items import BookItem, CommentItem, CriticItem


class BookDoubanPipeline:
    # 连接数据库
    def __init__(self):
        self.conn = pymysql.connect(
            host=settings.MYSQL_HOST,
            port=settings.MYSQL_PORT,
            user=settings.MYSQL_USER,
            passwd=settings.MYSQL_PASSWD,
            db=settings.MYSQL_DBNAME,
            # host="localhost",
            # port=3306,
            # user="root",
            # passwd="",
            # db='movie_douban',
            charset="utf8",
            use_unicode=True,
            cursorclass=pymysql.cursors.DictCursor)
        self.cursor = self.conn.cursor()
        self.book_file = codecs.open("books.json", "a", encoding="utf-8")
        self.comment_file = codecs.open("comment.json", "a", encoding="utf-8")
        self.critic_file = codecs.open("critic.json", "a", encoding="utf-8")

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
                SELECT * FROM books WHERE id = %s''', (item['id'],))
            book = self.cursor.fetchone()
            if book is None:
                self.cursor.execute('''
                INSERT INTO books(id, book_name, book_author, publisher, date,
                price, tags, intro, page, isbn, rate, rate_pl, five_star, four_star, three_star, two_star, one_star, pic, pic_sha1) 
                value(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)''',
                                    (
                                        item['id'], item['book_name'], item['book_author'], item['publisher'],
                                        item['date'],
                                        item['price'], item['tags'], item['intro'], item['page'], item['isbn'],
                                        item['rate'], item['rate_pl'], item['five_star'], item['four_star'],
                                        item['three_star'], item['two_star'], item['one_star'], item['pic'],
                                        item['pic_sha1']))
            self.conn.commit()
        except Exception as err:
            print("数据库报错==>错误信息为：" + str(err))
            lines = json.dumps(dict(item), ensure_ascii=False) + '\n'
            self.book_file.writelines(lines)
        pass

    def process_comment_item(self, item):
        try:
            self.cursor.execute('''
                SELECT * FROM book_comment WHERE id = %s AND critic = %s AND date = %s''',
                                (item['id'], item['critic'], item['date']))
            comment = self.cursor.fetchone()
            if comment is None:
                self.cursor.execute('''
                INSERT INTO book_comment(ID, critic, date, content, star_num)
                value(%s, %s, %s, %s, %s)''',
                                    (item['id'], item['critic'], item['date'], item['content'], item['star_num']))
            self.conn.commit()
        except Exception as err:
            print("数据库报错==>错误信息为：" + str(err))
            try:
                lines = json.dumps(dict(item), ensure_ascii=False) + '\n'
                self.comment_file.writelines(lines)
            except Exception as err:
                print("写入json失败" + str(err))

        pass

    def process_critic_item(self, item):
        try:
            self.cursor.execute('''
            SELECT * FROM douban_user WHERE user_name = %s''', (item['user_name'],))
            critic = self.cursor.fetchone()
            if critic is None and item['user_name'] is not None:
                self.cursor.execute('''
                INSERT INTO douban_user(user_name, user_address, join_date) value(%s, %s, %s)''',
                                    (item['user_name'], item['user_address'], item['join_date']))
            self.conn.commit()
            pass
        except Exception as err:
            print("数据库报错==>错误信息为：" + str(err))
            lines = json.dumps(dict(item), ensure_ascii=False) + '\n'
            self.critic_file.writelines(lines)
        pass

    def spider_closed(self, spider):
        self.book_file.close()
        self.comment_file.close()
        self.critic_file.close()


class ImagePipeline(ImagesPipeline):
    pass
