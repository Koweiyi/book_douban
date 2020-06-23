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
        print(item['music_url'])
        print(item['music_id'])
        pass

    def process_musicuser_item(self, item):
        print("come into user process")

        pass

    def process_musicdetail_item(self, item):
        print("come into detail process")

        pass
    
