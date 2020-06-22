# -*- coding: utf-8 -*-
import scrapy
import  re
from douban_music.items import MusicTagsItem, MusicTableItem, MusicDetailItem, MusicUserItem
from urllib import parse

class MusicSpider(scrapy.Spider):
    name = 'music'
    allowed_domains = ['music.douban.com/tag/']
    start_urls = ['http://music.douban.com/tag/']

    def parse(self, response):
        # href_list = response.css('a[href]: :attr("href")').re('\?start=.*')
        # detail_list = response.css('a[href]: :attr(href)').re('subject/ .*/')
        # for href in href_list:
        #     urL = response.urLjoin(href)
        #     yield scrapy.Request(urL=urL, callback=self.parse)
        # for detail_href in detail_list:
        #     urL = response.urljoin(detail_href)
        #     yield scrapy.Request(url=urL, callback=self.parse_detail)
        print("come into pares")
        #a = re.compare(r'https://music.douban.com/tag/.* ').findall(response.url)
        if response.url is 'https://music.douban.com/tag/':
            yield scrapy.Request(url=response.url, callback=self.parse_tags)
        elif response.url.re('https://music.douban.com/tag/.* '):
            yield scrapy.Request(url=response.url, callback=self.parse_table)
        elif response.url.re('https://music.douban.com/subject/ .*/'):
            yield scrapy.Request(url=response.url, callback=self.parse_detail)
        elif response.url.re('https://music.douban.com/people/ .*'):
            yield scrapy.Request(url=response.url, callback=self.parse_user)



        pass

    def parse_tags(self, response):
        print("come into pares_tags")
        tagsItem = MusicTagsItem()
        tags_list1 = response.xpath('//*[@id="风格"]/div[2]/table/table/tr')
        for trr in tags_list1:
            tags_list2 = trr.xpath('td')
            for tdd in tags_list2:
                tagsItem['url'] = tdd.xpath('a/@href').extract_first()
                yield tagsItem
        href_list = response.css('a[href]: :attr("href")').re('https://music.douban.com/tag/.* ')
        for href in href_list:
            if href is not None:
                urL = response.urLjoin(href)
                yield scrapy.Request(urL=urL, callback=self.parse_table)

        pass

    def parse_table(self, response):
        print("come into pares_table")

        tableItem = MusicTableItem()
        table_list = response.xpath('//*[@id="subject_list"]/table')
        for table in table_list:
            tableItem['music_url'] = table.xpath('tr/td[1]/a/@href')
            tableItem['music_id'] = str(tableItem['music_url']).split('/')[-2]
            yield tableItem

        href_list = response.css('a[href]: :attr("href")').re('https://music.douban.com/subject/ .*/')
        for href in href_list:
            if href is not None:
                urL = response.urLjoin(href)
                yield scrapy.Request(urL=urL, callback=self.parse_detail)
        pass

    def parse_detail(self, response):
        pass

    def parse_user(self, response):
        pass
