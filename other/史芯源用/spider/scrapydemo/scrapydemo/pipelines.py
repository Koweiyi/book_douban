# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
from spider.scrapydemo.scrapydemo.items import MovieDetailItem,MovieItem
from spider.scrapydemo.scrapydemo import settings
from scrapy import item
class ScrapydemoPipeline(object):
    
    def __init__(self):
        self.connect = pymysql.connect(
            host="www.91iedu.com",
            port=3391,
            db="team06",
            user="team06",
            passwd="team06",
            charset="utf8mb4",
            use_unicode=True
            )
        self.cursor = self.connect.cursor()
        
    def process_item(self,item, spider):
        if isinstance(item,MovieItem):
            self.process_movie_top250_item(item)
            print(item["sort"])
        elif isinstance(item, MovieDetailItem):
            self.process_movie_detail_item(item)
            print(item["direct"])
        return item
    
    def process_movie_detail_item(self,item):
        pass
    
    def process_movie_top250_item(self,item):
            
            self.cursor.execute('''select * from sxy_douban_films2 where film_dbid = %s''',(item['dbid'],))
            film = self.cursor.fetchone()
            if film ==None:
                self.cursor.execute(
                    """insert into sxy_douban_films2(id,film_title,film_score,
                                              film_motto,film_dbid,film_db_sort,
                                              film_other_title)
                        value(uuid(),%s,%s,%s,%s,%s,%s)
                    """,
                    (
                        item['title'],
                        item['score'],
                        item['motto'],
                        item['dbid'],
                        item['sort'],
                        item['other_title']
                        )
                    )
            else:
                self.cursor.execute(
                    """update sxy_douban_films2
                        set film_title = %s
                            film_score=  %s
                            film_motto = %s
                            film_dbid = %s
                            film_db_sort = %s
                            film_other_title = %s
                        where id = %s
                        """,
                        (
                            item['title'],
                        item['score'],
                        item['motto'],
                        item['dbid'],
                        item['sort'],
                        item['other_title'],
                        film['id']
                            )
                    )
            self.connect.commit()

