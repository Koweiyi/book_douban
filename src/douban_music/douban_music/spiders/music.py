# -*- coding: utf-8 -*-
from scrapy.linkextractors import LinkExtractor

import scrapy
import re
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
        a = re.match("https://music.douban.com/tag/.*", response.url)
        b = re.match("https://music.douban.com/subject/.*/", response.url)
        c = re.match("https://music.douban.com/people/.*", response.url)
        if response.url == "https://music.douban.com/tag/":
            print("====")
            yield scrapy.Request(url=response.url, callback=self.parse_tags, dont_filter=True)
        elif a:
            yield scrapy.Request(url=response.url, callback=self.parse_table, dont_filter=True)
        elif b:
            yield scrapy.Request(url=response.url, callback=self.parse_detail, dont_filter=True)
        elif c:
            yield scrapy.Request(url=response.url, callback=self.parse_user, dont_filter=True)

        pass

    def parse_tags(self, response):
        print("come into pares_tags")
        tagsItem = MusicTagsItem()
        tags_list1 = response.xpath('//*[@id="风格"]/div[2]/table/tbody/tr')
        for trr in tags_list1:
            tags_list2 = trr.xpath('td')
            for tdd in tags_list2:
                tagsItem['url'] = tdd.xpath('a/@href').extract_first()
                yield tagsItem
        href_list = response.css('a[href]').re('/tag/[A-Za-z0-9%]+')  # re('/tag/[A-Za-z0-9%]+')
        for href in href_list:
            if href is not None:
                urL = "http://music.douban.com" + href  # response.urLjoin(href)
                yield scrapy.Request(url=urL, callback=self.parse_table, dont_filter=True)

        pass

    def parse_table(self, response):
        print("come into pares_table")

        tableItem = MusicTableItem()
        table_list = response.xpath('//*[@id="subject_list"]/table')
        for table in table_list:
            tableItem['music_url'] = table.xpath('tr/td[1]/a/@href').extract_first()
            tableItem['music_id'] = str(tableItem['music_url']).split('/')[-2]
            yield tableItem

        href_list = response.css('a[href]').re('https://music.douban.com/subject/.*/')
        for href in href_list:
            if href is not None:
                urL = href
                yield scrapy.Request(url=urL, callback=self.parse_detail, dont_filter=True)

        next_page = response.css('li.next a[@href]').extract_first()
        if next_page is not None:
            urL = "https://music.douban.com" + next_page
            yield scrapy.Request(url=urL, callback=self.parse_table, dont_filter=True)
        pass

    def parse_detail(self, response):
        print("come into detail_table")
        detailItem = MusicDetailItem()

        detailItem['music_name'] = response.xpath('//*[@id="wrapper"]/hi/span/text()').extract_first()
        info = response.xpath('//*[@id="info"]/span').extract()
        for i in range(0, len(info)):
            if "又名" in info[i]:
                detailItem['music_rename'] = response.xpath('//*[@id="info"]/text()') \
                    .extract()[i+1].replace("\xa0", "").replace("\n", "").rstrip()
            elif "表演者" in info[i]:
                detailItem['music_man'] = "|".join(response.xpath('//*[@id="info"]/span[%s]/a/text()'.format(i+1)) )
            elif "发行时间" in info[i]:
                detailItem['music_time'] = response.xpath('//*[@id="info"]/text()') \
                    .extract()[i+1].replace("\xa0", "").replace("\n", "").rstrip()
            elif "流派" in info[i]:
                detailItem['music_sect'] = response.xpath('//*[@id="info"]/text()') \
                    .extract()[i+1].replace("\xa0", "").replace("\n", "").rstrip()
            elif "专辑类型" in info[i]:
                detailItem['music_album'] = response.xpath('//*[@id="info"]/text()') \
                    .extract()[i+1].replace("\xa0", "").replace("\n", "").rstrip()
            elif "介质" in info[i]:
                detailItem['music_sect'] = response.xpath('//*[@id="info"]/text()') \
                    .extract()[i+1].replace("\xa0", "").replace("\n", "").rstrip()
        detailItem['music_mark'] = response.xpath('//*[@id="interest_sectl"]/div/div[2]/strong/text()').extract_first()
        detailItem['music_voit'] = response.xpath('//*[@id="interest_sectl"]/div/div[2]/div/div[2]/a/span/text()').extract_first()
        detailItem['music_voit'] = response.xpath('').extract_first()
        detailItem['music_star5'] = response.xpath('//*[@id="interest_sectl"]/div/span[2]/text()').extract_first()
        detailItem['music_star4'] = response.xpath('//*[@id="interest_sectl"]/div/span[4]/text()').extract_first()
        detailItem['music_star3'] = response.xpath('//*[@id="interest_sectl"]/div/span[6]/text()').extract_first()
        detailItem['music_star2'] = response.xpath('//*[@id="interest_sectl"]/div/span[8]/text()').extract_first()
        detailItem['music_star1'] = response.xpath('//*[@id="interest_sectl"]/div/span[10]/text()').extract_first()
        yield detailItem

        comment_list = response.xpath('//*[@id="comments"]/ul/li')
        li1 = comment_list[0]
        li2 = comment_list[1]
        li3 = comment_list[2]
        detailItem['music_comment1'] = li1.xpath('').extract_first()
        detailItem['music_comment2'] = li2.xpath('').extract_first()
        detailItem['music_comment3'] = li3.xpath('').extract_first()








        href_list = response.css('a[href]').re('https://music.douban.com/subject/.*/')
        for href in href_list:
            if href is not None:
                urL = href
                yield scrapy.Request(url=urL, callback=self.parse_detail, dont_filter=True)
        pass

    def parse_user(self, response):
        pass
