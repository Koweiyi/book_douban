# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql.cursors


class DemoPipeline:

    def __init__(self):
        self.conn = pymysql.connect(
            host="www.91iedu.com",
            port=3391,
            db="team06",
            user="team06",
            passwd="team06",
            charset="utf8mb4",
            cursorclass=pymysql.cursors.DictCursor
        )
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):

        sql = '''insert into kwy_scrapyd_table(cont, tags)
                    values(%s, %s)
        '''
        insert_item = (item['cont'], item['tag'])
        self.cursor.execute(sql, insert_item)
        self.conn.commit()
        return item
