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

        next_page = response.css('li.next a[href]').extract_first()
        if next_page is not None:
            urL = "https://music.douban.com" + next_page
            yield scrapy.Request(url=urL, callback=self.parse_table, dont_filter=True)
        pass

    def parse_detail(self, response):
        print("come into detail_table")
        detailItem = MusicDetailItem()
        detailItem['music_name'] = ''
        detailItem['music_rename'] = ''
        detailItem['music_man'] = ''
        detailItem['music_time'] = ''
        detailItem['music_sect'] = ''
        detailItem['music_album'] = ''
        detailItem['music_sect'] = ''
        detailItem['music_mark'] = ''
        detailItem['music_vote'] = ''
        detailItem['music_comment'] = ''
        detailItem['music_comment_star'] = ''

        # 以下是爬取歌曲基本信息
        detailItem['music_name'] = response.xpath('//*[@id="wrapper"]/h1/span/text()').extract_first()
        info = response.xpath('//*[@id="info"]/span/text()').extract()
        lis = ["又名:", "发行时间:", "流派:", "专辑类型:", "介质:"]
        lis_item = ['music_rename', 'music_time', 'music_sect', 'music_album', 'music_media']

        for i in range(0, 5):
            if lis[i] in info:
                detailItem[lis_item[i]] = response.css('#info').re('.+{}</span>.+'.format(lis[i]))[0].split(">")[-1] \
                    .replace("\xa0", "").replace("\n", "").rstrip()
        detailItem['music_man'] = "|".join(response.css('#info span>a').xpath('string()').extract())


        # for i in range(0, len(info)):
        #     if "又名" in info[i]:
        #         detailItem['music_rename'] = response.css('#info').re('.+又名:</span>.+')[0].split(">")[-1] \
        #             .replace("\xa0", "").replace("\n", "").rstrip()
        #     elif "表演者" in info[i]:
        #         detailItem['music_man'] = "|".join(response.xpath('//*[@id="info"]/span[{}]/span/a/text()'.format(i + 1)).extract())
        #     elif "发行时间" in info[i]:
        #         detailItem['music_time'] = response.css('#info').re('.+发行时间:</span>.+')[0].split(">")[-1] \
        #             .replace("\xa0", "").replace("\n", "").rstrip()
        #     elif "流派" in info[i]:
        #         detailItem['music_sect'] = response.css('#info').re('.+流派:</span>.+')[0].split(">")[-1] \
        #             .replace("\xa0", "").replace("\n", "").rstrip()
        #     elif "专辑类型" in info[i]:
        #         detailItem['music_album'] = response.css('#info').re('.+专辑类型:</span>.+')[0].split(">")[-1] \
        #             .replace("\xa0", "").replace("\n", "").rstrip()
        #     elif "介质" in info[i]:
        #         detailItem['music_media'] = response.css('#info').re('.+介质:</span>.+')[0].split(">")[-1] \
        #             .replace("\xa0", "").replace("\n", "").rstrip()
        detailItem['music_mark'] = response.xpath('//*[@id="interest_sectl"]/div/div[2]/strong/text()').extract_first()
        detailItem['music_vote'] = response.xpath(
            '//*[@id="interest_sectl"]/div/div[2]/div/div[2]/a/span/text()').extract_first()
        detailItem['music_star5'] = response.xpath('//*[@id="interest_sectl"]/div/span[2]/text()').extract_first()
        detailItem['music_star4'] = response.xpath('//*[@id="interest_sectl"]/div/span[4]/text()').extract_first()
        detailItem['music_star3'] = response.xpath('//*[@id="interest_sectl"]/div/span[6]/text()').extract_first()
        detailItem['music_star2'] = response.xpath('//*[@id="interest_sectl"]/div/span[8]/text()').extract_first()
        detailItem['music_star1'] = response.xpath('//*[@id="interest_sectl"]/div/span[10]/text()').extract_first()

        # 以下是爬取评论信息
        def star(str):
            if str == "力荐":
                return 5
            if str == "推荐":
                return 4
            if str == "还行":
                return 3
            if str == "很差":
                return 1
            return 2

        comment_list = response.xpath('//*[@id="comments"]/ul/li')
        if len(comment_list) < 3:
            a = len(comment_list)
        else:
            a = 3

        for i in range(0, a):
            li = comment_list[i]
            detailItem['music_comment'] = li.xpath(
                '//*[@id="comments"]/ul/li[{}]/div/p/span/text()'.format(i + 1)).extract_first()
            if li.xpath('//*[@id="comments"]/ul/li[{}]/div/h3/span[2]/span[1]/@title'.format(
                    i + 1)).extract_first() is not None:
                detailItem['music_comment_star'] = star(li.xpath(
                    '//*[@id="comments"]/ul/li[{}]/div/h3/span[2]/span[1]/@title'.format(i + 1)).extract_first())
            yield detailItem

            if response.xpath(
                    '//*[@id="comments"]/ul/li[{}]/div/h3/span[2]/a/text()'.format(
                        i + 1)).extract_first() != "[已注销]" or None:
                user_href = response.xpath(
                    '//*[@id="comments"]/ul/li[{}]/div/h3/span[2]/a/@href'.format(i + 1)).extract_first()
                yield scrapy.Request(url=user_href, callback=self.parse_user, dont_filter=True)
        # comment_list = response.xpath('//*[@id="comments"]/ul/li')
        # li1 = comment_list[0]
        # li2 = comment_list[1]
        # li3 = comment_list[2]
        # detailItem['music_comment1'] = li1.xpath('//*[@id="comments"]/ul/li[1]/div/p/span/text()').extract_first()
        # detailItem['music_comment2'] = li2.xpath('//*[@id="comments"]/ul/li[2]/div/p/span/text()').extract_first()
        # detailItem['music_comment3'] = li3.xpath('//*[@id="comments"]/ul/li[3]/div/p/span/text()').extract_first()
        # if li1.xpath('//*[@id="comments"]/ul/li[1]/div/h3/span[2]/span[1]/@title').extract_first() is not None:
        #     detailItem['music_comment1_star'] = star(li1.xpath(
        #         '//*[@id="comments"]/ul/li[1]/div/h3/span[2]/span[1]/@title').extract_first())
        #
        # if li2.xpath('//*[@id="comments"]/ul/li[2]/div/h3/span[2]/span[1]/@title').extract_first() is not None:
        #     detailItem['music_comment2_star'] = star(li2.xpath(
        #         '//*[@id="comments"]/ul/li[2]/div/h3/span[2]/span[1]/@title').extract_first())
        #
        # if li3.xpath('//*[@id="comments"]/ul/li[3]/div/h3/span[2]/span[1]/@title').extract_first() is not None:
        #     detailItem['music_comment3_star'] = star(li3.xpath(
        #         '//*[@id="comments"]/ul/li[3]/div/h3/span[2]/span[1]/@title').extract_first())
        #
        # yield detailItem
        # # 以下是跳转user
        # if response.xpath('//*[@id="comments"]/ul/li[1]/div/h3/span[2]/a/text()').extract_first() != "[已注销]" or None:
        #     user1_href = response.xpath('//*[@id="comments"]/ul/li[1]/div/h3/span[2]/a/@href').extract_first()
        #     yield scrapy.Request(url=user1_href, callback=self.parse_user, dont_filter=True)
        # if response.xpath('//*[@id="comments"]/ul/li[2]/div/h3/span[2]/a/text()').extract_first() != "[已注销]" or None:
        #     user2_href = response.xpath('//*[@id="comments"]/ul/li[2]/div/h3/span[2]/a/@href').extract_first()
        #     yield scrapy.Request(url=user2_href, callback=self.parse_user, dont_filter=True)
        # if response.xpath('//*[@id="comments"]/ul/li[3]/div/h3/span[2]/a/text()').extract_first() != "[已注销]" or None:
        #     user3_href = response.xpath('//*[@id="comments"]/ul/li[3]/div/h3/span[2]/a/@href').extract_first()
        #     yield scrapy.Request(url=user3_href, callback=self.parse_user, dont_filter=True)
        pass

    def parse_user(self, response):
        userItem = MusicUserItem()
        userItem['music_user_site'] = ''
        userItem['music_user_time'] = ''
        if response.xpath('//*[@id="profile"]/div/div[2]/div[1]/div/a/text()') is not None:
            userItem['music_user_site'] = response.xpath(
                '//*[@id="profile"]/div/div[2]/div[1]/div/a/text()').extract_first()
        if response.xpath('//*[@id="profile"]/div/div[2]/div[1]/div/div/text()[2]') is not None:
            userItem['music_user_time'] = response.xpath(
                '//*[@id="profile"]/div/div[2]/div[1]/div/div/text()[2]').extract_first()

        yield userItem

        pass
