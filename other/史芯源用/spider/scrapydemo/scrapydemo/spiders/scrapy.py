'''
Created on 2020年6月18日

@author: 44786
'''
# -*- coding: utf-8 -*-
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider,Rule
from spider.scrapydemo.scrapydemo.items import MovieDetailItem,MovieItem

class ScrapySpider(CrawlSpider):
    name = 'move'
    allowed_domains = ['movie.douban.com']
    start_urls = ['https://movie.douban.com/top250']
    rules = (
        Rule(LinkExtractor(allow=r"/subject/\d+/$"),callback='parse_detail',follow=True),
        Rule(LinkExtractor(allow=r'/?start=\d+'),callback='parse_top250',follow=True),
        )

    def parse_detail(self,response):
        detailItem = MovieDetailItem()
        detailItem["direct"] = response.xpath('//*[@rel="v:directedBy"]/text()').extract_first()
        detailItem["vote_num"] = response.xpath('//*[@property="v:votes"]/text()').extract_first()
        yield detailItem
        
    def parse_top250(self,response):
        li_list = response.xpath('//*[@id="content"]/div/div[1]/ol/li')
        for li in li_list:
            item = MovieItem()
            
            item['sort'] = li.xpath('div/div[1]/em/text()').extract_first()
            item['url'] = li.xpath('div/div[1]/a/@href').extract_first()
            item['dbid'] = item['url'].split('/')[-2]
            item['title'] = li.xpath('div/div[2]/div[1]/a/span[1]/text()').extract_first()
            item['other_title'] = li.xpath('div/div[2]/div[1]/a/span[2]/text()').extract_first()
            item['score'] = li.xpath('div/div[2]/div[2]/div/span[2]/text()').extract_first()
            item['motto'] = li.xpath('div/div[2]/div[2]/p[2]/span/text()').extract_first()
            yield item
            
            
        