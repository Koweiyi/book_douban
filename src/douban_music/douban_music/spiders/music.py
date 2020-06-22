# -*- coding: utf-8 -*-
import scrapy


class MusicSpider(scrapy.Spider):
    name = 'music'
    allowed_domains = ['music.douban.com/tag/']
    start_urls = ['http://music.douban.com/tag//']

    def parse(self, response):
        pass
