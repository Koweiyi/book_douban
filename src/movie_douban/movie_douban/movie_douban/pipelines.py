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

        if isinstance(item,MovieItem):
            self.process_movie_item(item)
            #print(item[])
        elif isinstance(item,MovieDetailItem):
            self.process_movie_detail_item(item)
        elif isinstance(item,MovieCommentItem):
            self.process_movie_comment_item(item)

        return item

    def process_movie_item(self, item):
        try:
            self.cursor.execute('''
                SELECT * FROM hzc_movie WHERE dbid = %s
                    ''',(item['dbid'],))
            film = self.cursor.fetchone()
            if film == None:
                self.cursor.execute(
                    """insert into hzc_movie(title,dbid,score)
                    value (%s,%s,%s)""",
                    (item['title'],
                     item['dbid'],
                     item['score']))
            else:
                self.cursor.execute('''
                    UPDATE hzc_movie
                        SET title = %s,
                            dbid = %s,
                            score = %s
                        WHERE dbid = %s
                ''',
                                    (item['title'],
                                     item['dbid'],
                                     item['score'],
                                     film['dbid']))
            self.connect.commit()
        except Exception as err:
            print("数据库报错==》错误信息为:"+str(err))

    def process_movie_detail_item(self,item):
        try:
            self.cursor.execute('''
                SELECT * FROM hzc_movie_detail WHERE dbid = %s
                    ''',(item['dbid'],))
            film = self.cursor.fetchone()
            if film == None:
                self.cursor.execute(
                    """insert into hzc_movie_detail(dbid,other_title,direct,country,movie_time,movie_type,vote_num,five_star,four_star,three_star,two_star,one_star)
                    value (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""",
                    (item['dbid'],
                     item['other_title'],
                     item['direct'],
                     item['country'],
                     item['movie_time'],
                     item['movie_type'],
                     item['vote_num'],
                     item['five_star'],
                     item['four_star'],
                     item['three_star'],
                     item['two_star'],
                     item['one_star']))
            else:
                self.cursor.execute('''
                    UPDATE hzc_movie_detail
                        SET dbid = %s,
                            other_title = %s,
                            direct = %s,
                            country = %s,
                            movie_time = %s,
                            movie_type = %s,
                            vote_num = %s,
                            five_star = %s,
                            four_star = %s,
                            three_star = %s,
                            two_star = %s,
                            one_star = %s
                        WHERE dbid = %s
                ''',               (item['dbid'],
                                    item['other_title'],
                                    item['direct'],
                                    item['country'],
                                    item['movie_time'],
                                    item['movie_type'],
                                    item['vote_num'],
                                    item['five_star'],
                                    item['four_star'],
                                    item['three_star'],
                                    item['two_star'],
                                    item['one_star'],
                                    film['dbid']))
            self.connect.commit()
        except Exception as err:
            print("数据库报错==》错误信息为:"+str(err))

    def process_movie_comment_item(self,item):
        try:
            self.cursor.execute('''
                SELECT * FROM hzc_movie_comment WHERE dbid = %s
                    ''',(item['dbid'],))
            film = self.cursor.fetchone()
            if film == None:
                self.cursor.execute(
                    """insert into hzc_movie_comment(dbid,content,comment_time,comment_people,comment_star)
                    value (%s,%s,%s,%s,%s)""",
                    (item['dbid'],
                     item['content'],
                     item['comment_time'],
                     item['comment_people'],
                     item['comment_star']))
            else:
                self.cursor.execute('''
                    UPDATE hzc_movie_comment
                        SET dbid = %s,
                            content = %s,
                            comment_time = %s,
                            comment_people = %s,
                            comment_star = %s
                        WHERE dbid = %s
                ''',               (item['dbid'],
                                    item['content'],
                                    item['comment_time'],
                                    item['comment_people'],
                                    item['comment_star'],
                                    film['dbid']))
            self.connect.commit()
        except Exception as err:
            print("数据库报错==》错误信息为:" + str(err))