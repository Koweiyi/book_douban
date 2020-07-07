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
        try:
            self.connect = pymysql.Connect(
                host=settings.MYSQL_HOST,
                port=settings.MYSQL_PORT,
                db=settings.MYSQL_DBNAME,
                user=settings.MYSQL_USER,
                passwd=settings.MYSQL_PASSWD,
                charset='utf8-mb4',
                use_unicode=True,
                cursorclass=pymysql.cursors.DictCursor
            )
            self.cursor = self.connect.cursor()
            self.cursor.execute("SELECT VERSION()")
            data = self.cursor.fetchone()
            print(data)
        except:
            print("数据库连接失败")
            print()

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
        # self.cursor.ping()
        self.cursor.execute('''
                    SELECT * FROM dalongtou_music WHERE music_id = \"%s\"
                    ''', (item['music_id']))
        film = self.cursor.fetchone()

        sql_insert1 = '''insert into dalongtou_music(music_id,music_url)value (\"%s\",\"%s\")'''
        sql_insert2 = '''UPDATE dalongtou_music set music_url = \"%s\" WHERE music_id = \"%s\"'''

        if film is None:
            self.cursor.execute(sql_insert1, (item['music_id'], item['music_url']))

        else:
            self.cursor.execute(sql_insert2, (item['music_url'], item['music_id']))

        self.connect.commit()

        pass

    def process_musicuser_item(self, item):
        print("come into user process")
        print(item['music_user_site'])
        print(item['music_user_time'])
        # self.cursor.ping()

        self.cursor.execute('''
                            SELECT * FROM dalongtou_music_comment WHERE music_user_name = \"%s\"
                            ''', (item['music_user_name']))
        film = self.cursor.fetchone()

        sql_insert1 = '''UPDATE dalongtou_music_comment 
                        SET music_user_site = \"%s\", music_user_time = \"%s\" WHERE music_user_name = \"%s\"'''

        if film is None:
            print("报错！报错！！！！！！！！！！！！comment表: music_user_name找不到,插入user")
        else:
            self.cursor.execute(sql_insert1,
                                (item['music_user_site'], item['music_user_time'], item['music_user_name']))
            self.connect.commit()

        pass

    def process_musicdetail_item(self, item):
        print("come into detail process")
        print(item['music_name'])
        print(item['music_rename'])
        print(item['music_time'])
        print(item['music_mark'])
        # self.cursor.ping()

        # 录入music表
        self.cursor.execute('''
                            SELECT * FROM dalongtou_music WHERE music_id = \"%s\"
                            ''', (item['music_id']))
        film = self.cursor.fetchone()

        sql_insert1 = '''UPDATE dalongtou_music
                            SET 
                                music_name = \"%s\",
                                music_man = \"%s\",
                                music_rename = \"%s\",
                                music_sect = \"%s\",
                                music_album = \"%s\",
                                music_media = \"%s\",
                                music_time = \"%s\",
                                music_mark = \"%s\",
                                music_vote = \"%s\",
                                music_star1 = \"%s\",
                                music_star2 = \"%s\",
                                music_star3 = \"%s\",
                                music_star4 = \"%s\",
                                music_star5 = \"%s\"
                                WHERE music_id = \"%s\"'''

        sql_insert1_1 = '''INSERT INTO dalongtou_music( 
                            music_name ,
                            music_man ,
                            music_rename,
                            music_sect ,
                            music_album ,
                            music_media ,
                            music_time ,
                            music_mark ,
                            music_vote ,
                            music_star1 ,
                            music_star2 ,
                            music_star3 ,
                            music_star4 ,
                            music_star5 )
                            VALUE (\"%s\", \"%s\", \"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\", \"%s\")'''

        if film is None:
            print("报错！报错！！！！！！！！！！！！music表: music_id找不到，插入detail")
            self.cursor.execute(sql_insert1_1, (
                item['music_name'], item['music_man'], item['music_rename'],
                item['music_sect'], item['music_album'], item['music_media'],
                item['music_time'], item['music_mark'], item['music_vote'],
                item['music_star1'], item['music_star2'], item['music_star3'],
                item['music_star4'], item['music_star5'], item['music_id']))
        else:
            self.cursor.execute(sql_insert1, (
                item['music_name'], item['music_man'], item['music_rename'],
                item['music_sect'], item['music_album'], item['music_media'],
                item['music_time'], item['music_mark'], item['music_vote'],
                item['music_star1'], item['music_star2'], item['music_star3'],
                item['music_star4'], item['music_star5'], item['music_id']))
            self.connect.commit()

        # 录入comment表

        self.cursor.execute('''
                             SELECT * FROM dalongtou_music_comment WHERE music_user_name = \"%s\" and music_id = \"%s\"
                            ''', (item['music_comment_name'], item['music_id']))
        film = self.cursor.fetchone()

        sql_insert2 = '''insert into dalongtou_music_comment(
                                                music_id,music_user_name)
                                                value (\"%s\",\"%s\")'''

        sql_insert3 = '''UPDATE dalongtou_music_comment
                            SET music_comment = \"%s\",
                            music_comment_star = \"%s\" 
                            WHERE music_id = \"%s\" and music_user_name = \"%s\"'''

        if film is None:
            print("comment表: music_id找不到，插入comment")
            self.cursor.execute(sql_insert2, (item['music_id'], item['music_comment_name']))
            self.connect.commit()

        self.cursor.execute(sql_insert3, (
            item['music_comment'], item['music_comment_star'], item['music_id'], item['music_comment_name']))
        self.connect.commit()
        pass
