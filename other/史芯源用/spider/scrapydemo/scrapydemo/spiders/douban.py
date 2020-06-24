'''
Created on 2020年6月22日

@author: 44786
'''
# -*- coding: utf-8 -*-
import scrapy
import json
class JsonspiderSpider(scrapy.Spider):
    name = 'jsonSpider'
    allowed_domains = ['movie.douban.com']
    
    start_urls = ['''https://movie.douban.com/j/search_subjects?
        type=movie&
        tag=%E7%83%AD%E9%97%A8&
        sort=recommend&
        page_limit=20&
        page_start=0'''.replace('\n', '').replace('', '')]
    
    __slots__ = ('__page_count',)
    def __init__(self):
        self.__page_count = 1
    @property
    def page_count(self):
        return self.__page_count
    @page_count.setter
    def page_count(self, page_count):
        self.__page_count = page_count
    def parse(self, response):
        info = json.loads(response.text)
        for i in info['subjects']:
            print(i["title"])
            response.urljoin(i["url"])
            yield scrapy.Request(url=i["url"],callback=self.parse_detail)
        if self .page_count <= 25:
            next_url ='''https://movie.douban.com/j/search_subjects?
                type=movie&
                tag=%E7%83%AD%E9%97%A8&
                sort=recommend&page_limit=20&
                page_start={0}'''\
                . format((self.page_count * 20))\
                . replace('\n', '') . replace(' ','')
            self .page_count += 1
            yield scrapy.Request(url=next_url,callback=self.parse)
        pass
    def parse_detail(self,response):
        print(response.xpath('//*[@re1="v:directedBy"]/text()').extract_first())
        pass