# -*- coding: utf-8 -*-
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from movie_douban.items import MovieItem, MovieDetailItem, MovieCommentItem
import scrapy
import json
import re

class MovieSpider(scrapy.Spider):
    name = 'movie'
    allowed_domains = ['movie.douban.com']
    start_urls = ['''https://movie.douban.com/j/search_subjects?
                        type=movie&
                        tag=%E7%83%AD%E9%97%A8&
                        sort=time&
                        page_limit=20&
                        page_start=0'''.replace('\n', '').replace(' ', '')]
#rules = ()
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
            yield scrapy.Request(url=i["url"], callback=self.parse_detail)
            #yield scrapy.Request(url=i["url"], callback=self.parse_comment)

        if self.page_count <= 25:
            next_url = '''https://movie.douban.com/j/search_subjects?
                        type=movie&
                        tag=%E7%83%AD%E9%97%A8&
                        sort=time&
                        page_limit=20&
                        page_start={0}'''\
                        .format((self.page_count * 20))\
                        .replace('\n', '').replace(' ', '')
            self.page_count += 1
            yield scrapy.Request(url=next_url, callback=self.parse)
        pass

    def parse_movie(self, response):
        li_list = response.xpath('//*[@id="content"]/div/div[1]/div/div[4]/div/a')
        for li in li_list:
            item = MovieItem()
            item['url'] = li.xpath('@href').extract_first()
            item['dbid'] = item['url'].split('/')[-2]
            item['title'] = li.xpath('p/text()').extract_first()
            item['score'] = li.xpath('p/strong/text()').extract_first()
            yield item

    def parse_detail(self, response):
        detailItem = MovieDetailItem()
        detailItem['dbid'] = response.url.split('/')[-2]
        detailItem['direct'] = "|".join(response.xpath('//*[@rel="v:directedBy"]/text()').extract())
        detailItem['vote_num'] = response.xpath('//*[@property="v:votes"]/text()').extract_first()
        detailItem['movie_time'] = response.xpath('//*[@property="v:initialReleaseDate"]/text()').extract_first()
        detailItem['movie_type'] = "|".join(response.xpath('//*[@property="v:genre"]/text()').extract())
        detailItem['five_star'] = response.xpath('//*[@id="interest_sectl"]/div[1]/div[3]/div[1]/span[2]/text()').extract_first()
        detailItem['four_star'] = response.xpath('//*[@id="interest_sectl"]/div/div[3]/div[2]/span[2]/text()').extract_first()
        detailItem['three_star'] = response.xpath('//*[@id="interest_sectl"]/div[1]/div[3]/div[3]/span[2]/text()').extract_first()
        detailItem['two_star'] = response.xpath('//*[@id="interest_sectl"]/div[1]/div[3]/div[4]/span[2]/text()').extract_first()
        detailItem['one_star'] = response.xpath('//*[@id="interest_sectl"]/div[1]/div[3]/div[5]/span[2]/text()').extract_first()
        content = "".join(response.xpath('//*[@id="info"]').extract())
        info = response.xpath('//*[@id="info"]/span').extract()
        if "又名" not in info:
            detailItem['other_title'] = None  # print("Null")#
        for i in range(0, len(info)):
            if "制片国家/地区" in info[i]:
                country = re.findall(r"<span class=\"pl\">制片国家/地区:</span>(.*?)<br>", content, re.S)
                detailItem['country'] = "".join(country).replace("\xa0", "").replace("\n", "").replace(" ", "")
            if "又名" in info[i]:
                other = re.findall(r"<span class=\"pl\">又名:</span>(.*?)<br>", content, re.S)
                detailItem['other_title'] = "".join(other).replace("\xa0", "").replace("\n", "").replace(" ", "")
        yield detailItem

    def parse_comment(self, response):
        commentItem = MovieCommentItem()
        for i in range(3):
            commentItem['dbid'] = response.url.split('/')[-2]
            commentItem['comment_people'] = response.xpath('//*[@id="hot-comments"]/div[{0}]/div/h3/span[2]/a/text()'.format(i+1)).extract_first()
            commentItem['comment_time'] = response.xpath('normalize-space(//*[@id="hot-comments"]/div[{0}]/div/h3/span[2]/span[3]/text())'.format(i+1)).extract_first()
            commentItem['comment_star'] = response.xpath('//*[@id="hot-comments"]/div[{0}]/div/h3/span[2]/span[2]/@title'.format(i+1)).extract_first()
            commentItem['content'] = response.xpath('//*[@id="hot-comments"]/div[{0}]/div/p/span/text()'.format(i+1)).extract_first()
            yield commentItem


