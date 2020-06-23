# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql

from douban_music import settings
from douban_music.items import MusicTagsItem, MusicTableItem, MusicDetailItem, MusicUserItem


class DoubanMusicPipeline:

    def __init__(self):
        self.connect = pymysql.connect(
            host=settings.MYSQL_HOST,
            port=settings.MYSQL_PORT,
            db=settings.MYSQL_DBNAME,
            user=settings.MYSQL_USER,
            passwd=settings.MYSQL_PASSWD,
            charset='utf8',
            use_unicode=True,
            cursorclass=pymysql.cursors.DictCursor
        )
        self.cursor = self.connect.cursor()

    def process_item(self, item, spider):

        print("来了老弟")

        if isinstance(item, MusicDetailItem):
            self.process_musicdetail_item(item)

        elif isinstance(item, MusicUserItem):
            self.process_musicuser_item(item)

        elif isinstance(item, MusicTableItem):
            self.process_musictable_item(item)

        elif isinstance(item, MusicTagsItem):
            self.process_musictags_item(item)

        return item

    def process_musictags_item(self, item):
        print("come into tags process")
        print(item['url'])

        pass

    def process_musictable_item(self, item):
        print("come into table process")
        self.cursor.execute('''
                    SELECT * FROM dalongtou_music WHERE music_id = %s
                    ''', (item['music_id']))
        film = self.cursor.fetchone()

        sql_insert1 = '''insert into dalongtou_music(music_id,music_url)
                            value (\"%s\",\"%s\",\"%s\")''', (item['music_id'], item['music_url'])
        sql_insert2 = '''insert into dalongtou_music_comment(music_id,)
                                    value \"%s\")''', (item['music_id'])
        if film is None:
            self.cursor.execute(sql_insert1)
            self.cursor.execute(sql_insert2)
            self.cursor.execute(sql_insert2)
            self.cursor.execute(sql_insert2)

        pass

    def process_musicuser_item(self, item):
        print("come into user process")
        print(item['music_user_site'])
        print(item['music_user_time'])

        self.cursor.execute('''
                            SELECT * FROM dalongtou_music_comment WHERE music_id = \"%s\"
                            ''', (item['music_id']))
        film = self.cursor.fetchone()

        sql_insert1 = '''insert into dalongtou_music_comment(music_user_site,music_user_time)
                            value (\"%s\",\"%s\") WHERE music_id = \"%s\"''', (
            item['music_user_site'], item['music_user_time'], item['music_id'])

        if film is None:
            print("报错！报错！！！！！！！！！！！！comment表: music_id找不到,插入user")
        else:
            self.cursor.execute(sql_insert1)

        pass

    def process_musicdetail_item(self, item):
        print("come into detail process")
        print(item['music_name'])
        print(item['music_rename'])
        print(item['music_time'])
        print(item['music_mark'])

        # 录入music表
        self.cursor.execute('''
                            SELECT * FROM dalongtou_music WHERE music_id = \"%s\"
                            ''', (item['music_id']))
        film = self.cursor.fetchone()

        sql_insert1 = '''insert into dalongtou_music(
                        music_name,music_man,music_rename,music_sect,
                        music_album,music_media,music_time,music_mark,
                        music_vote,music_star1,music_star2,music_star3,
                        music_star4,music_star5)
                        value (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) WHERE music_id = %s''', (
            item['music_name'], item['music_man'], item['music_rename'],
            item['music_sect'], item['music_album'], item['music_media'],
            item['music_time'], item['music_mark'], item['music_vote'],
            item['music_star1'], item['music_star2'], item['music_star3'],
            item['music_star4'], item['music_star5'], item['music_id'])

        if film is None:
            print("报错！报错！！！！！！！！！！！！music表: music_id找不到，插入detail")
        else:
            self.cursor.execute(sql_insert1)

        # 录入comment表
        self.cursor.execute('''
                             SELECT * FROM dalongtou_music_comment WHERE music_id = %s
                            ''', (item['music_id']))
        film = self.cursor.fetchone()

        sql_insert2 = '''insert into dalongtou_music_comment(music_comment,music_comment_star)
                            value (%s,%s) WHERE music_id = %s''', (
            item['music_comment'], item['music_comment_star'], item['music_id'])

        if film is None:
            print("报错！报错！！！！！！！！！！！！comment表: music_id找不到，插入comment")
        else:
            self.cursor.execute(sql_insert2)

        pass
