# -*- coding: utf-8 -*-
import scrapy
import hashlib
import re

from scrapy.utils.python import to_bytes
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from book_douban.items import BookItem, CommentItem, CriticItem, PicItem


class BookSpider(CrawlSpider):
    name = 'book'
    allowed_domains = ['book.douban.com']
    start_urls = ['https://book.douban.com/tag/?view=cloud']
    rules = [
        Rule(LinkExtractor(allow='/tag/', restrict_xpaths="//div[@class='indent tag_cloud']"), follow=True),
        Rule(LinkExtractor(allow="\?start=\d+\&type=", restrict_xpaths="//div[@class='paginator']"), follow=True),
        Rule(LinkExtractor(allow="/subject/\d+/$", restrict_xpaths="//ul[@class='subject-list']"),
             callback='parse_item')
    ]

    def parse_item(self, response):
        item = BookItem()
        pic = PicItem()

        pic['pic_book_src'] = [response.xpath("//*[@id=\"mainpic\"]/a/img/@src").extract_first()]

        content = "".join(response.xpath('//*[@id="info"]').extract())
        tags = []
        for i in range(1, 5):
            tags.append(response.xpath("//*[@id='db-tags-section']/div/span[{0}]/a/text()".format(i)).extract()[0])
        item['id'] = response.url.split('/')[-2]
        item['book_name'] = response.xpath("//div[@id='wrapper']/h1/span/text()").extract()[0]

        #//*[@id="info"]/a[1]
        #//*[@id="info"]/span[1]/a
        book_author = response.xpath("//*[@id=\"info\"]/a[1]/text()").extract_first()
        if book_author is None:
            book_author = response.xpath("//*[@id=\"info\"]/span[1]/a[1]/text()").extract_first()
        if book_author is not None:
            item['book_author'] = book_author.replace(' ', '').replace('\n', '')
        else:
            item['book_author'] = None

        if "出版社" in content:
            publisher = re.findall(r"<span class=\"pl\">出版社:</span>(.*?)<br>", content, re.S)
            item['publisher'] = "".join(publisher).replace('\n', '').replace(' ', '').replace("\xa0", "")
        else:
            item['publisher'] = None
        if "出版年" in content:
            date = re.findall(r"<span class=\"pl\">出版年:</span>(.*?)<br>", content, re.S)
            item['date'] = "".join(date).replace('\n', '').replace(' ', '').replace("\xa0", "")
        else:
            item['date'] = None

        if "页数" in content:
            page = re.findall(r"<span class=\"pl\">页数:</span>(.*?)<br>", content, re.S)
            item['page'] = "".join(page).replace('\n', '').replace(' ', '').replace("\xa0", "")
        else:
            item['page'] = None

        if "ISBN" in content:
            isbn = re.findall(r"<span class=\"pl\">ISBN:</span>(.*?)<br>", content, re.S)
            item['isbn'] = "".join(isbn).replace('\n', '').replace(' ', '').replace("\xa0", "")
        else:
            item['isbn'] = None

        if "定价" in content:
            price = re.findall(r"<span class=\"pl\">定价:</span>(.*?)<br>", content, re.S)
            item['price'] = "".join(price).replace('\n', '').replace(' ', '').replace("\xa0", "")
        else:
            item['price'] = None
        item['tags'] = "|".join(tags)
        #//*[@id="link-report"]/div[1]/div/p[1]
        item['intro'] = response.xpath("//*[@id=\"link-report\"]/span[1]/div/p[1]/text()").extract_first()
        if item['intro'] is None:
            item['intro'] = response.xpath("//*[@id=\"link-report\"]/div[1]/div/p[1]/text()").extract_first()

        more_intro1 = response.xpath("//*[@id=\"link-report\"]/span[1]/div/p[2]/text()").extract_first()
        more_intro2 = response.xpath("//*[@id=\"link-report\"]/div[1]/div/p[2]/text()").extract_first()
        if more_intro1 is not None:
            item['intro'] += more_intro1
        elif more_intro2 is not None:
            item['intro'] += more_intro2
        item['rate'] = response.xpath("//*[@id=\"interest_sectl\"]/div/div[2]/strong/text()").extract_first()
        item['rate_pl'] = response.xpath("//*[@id=\"interest_sectl\"]/div/div[2]/div/div[2]/span/a/span/text()") \
            .extract_first()
        item['five_star'] = response.xpath("//*[@id=\"interest_sectl\"]/div/span[2]/text()").extract_first()
        item['four_star'] = response.xpath("//*[@id=\"interest_sectl\"]/div/span[4]/text()").extract_first()
        item['three_star'] = response.xpath("//*[@id=\"interest_sectl\"]/div/span[6]/text()").extract_first()
        item['two_star'] = response.xpath("//*[@id=\"interest_sectl\"]/div/span[8]/text()").extract_first()
        item['one_star'] = response.xpath("//*[@id=\"interest_sectl\"]/div/span[10]/text()").extract_first()
        item['pic'] = pic['pic_book_src'][0]
        item['pic_sha1'] = "full/%s.jpg" % (hashlib.sha1(to_bytes(pic['pic_book_src'][0])).hexdigest())

        yield pic
        yield item
        for i in range(3):
            comment = CommentItem()
            comment['id'] = response.url.split('/')[-2]
            critic = (response.xpath("//*[@id=\"comments\"]/ul/li[{0}]/div/h3/span[2]/a/text()"
                                     .format(i + 1)).extract_first())
            if critic is None:
                continue
            comment['critic'] = critic

            date = response.xpath("//*[@id=\"comments\"]/ul/li[{0}]/div/h3/span[2]/span[2]/text()"
                                  .format(i + 1)).extract_first()
            if date is None:
                continue
            comment['date'] = date

            comment['star_num'] = response.xpath("//*[@id=\"comments\"]/ul/li[{0}]/div/h3/span[2]/span[1]/@title"
                                                 .format(i + 1)).extract_first()
            comment['content'] = response.xpath("//*[@id=\"comments\"]/ul/li[{0}]/div/p/span/text()"
                                                .format(i + 1)).extract_first()
            url = response.xpath("//*[@id=\"comments\"]/ul/li[{0}]/div/h3/span[2]/a/@href"
                                 .format(i + 1)).extract_first()
            yield comment
            if url is not None:
                yield scrapy.http.Request(url=url, callback=self.parse_critic, dont_filter=True)

    def parse_critic(self, response):
        critic = CriticItem()
        critic['user_name'] = response.xpath("//*[@id=\"profile\"]/div/div[2]/div[1]/div/div/text()[1]").extract_first()
        critic['join_date'] = response.xpath("//*[@id=\"profile\"]/div/div[2]/div[1]/div/div/text()[2]").extract_first()
        critic['user_address'] = response.xpath("//*[@id=\"profile\"]/div/div[2]/div[1]/div/a/text()").extract_first()
        yield critic
