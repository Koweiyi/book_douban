# -*- coding: utf-8 -*-
import scrapy


class BookSpider(scrapy.Spider):
    name = 'book'
    tag = ''
    custom_settings = {
        'ITEM_PIPELINES': {'douban.pipelines.BookItemPipeline': 100,
                           'douban.pipelines.BookTagsPipeline': 200}
    }

    def __init__(self, tag = None, *args, **kwargs):
        super(BookSpider, self).__init__(*args, **kwargs)
        self.start_urls = ['https://book.douban.com/tag/' + tag]
        self.tag = tag

    def parse(self, response):
        sel = scrapy.Selector(response)
        book_list = sel.css('#subject_list > ul > li')
        for book in book_list:
            try:
                book_id = book.xpath('div[@class="info"]/h2/a/@href').split('/')[-2]

            except Exception as e:
                print("Yield Book Error!")


        pass
