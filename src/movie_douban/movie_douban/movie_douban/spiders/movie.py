# -*- coding: utf-8 -*-
import scrapy


class MovieSpider(scrapy.Spider):
    name = 'movie'
    allowed_domains = ['movie.douban.com/explore']
    start_urls = ['http://movie.douban.com/explore/']

    def parse(self, response):
        pass
