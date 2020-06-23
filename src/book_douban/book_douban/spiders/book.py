# -*- coding: utf-8 -*-
import scrapy
import re
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from book_douban.items import BookItem, CommentItem, CriticItem


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
        content = "".join(response.xpath('//*[@id="info"]').extract())
        tags = []
        for i in range(1, 5):
            tags.append(response.xpath("//*[@id='db-tags-section']/div/span[{0}]/a/text()".format(i)).extract()[0])
        item['ID'] = response.url.split('/')[-2]
        item['book_name'] = response.xpath("//div[@id='wrapper']/h1/span/text()").extract()[0]

        book_author = response.xpath("/html/body/div[3]/div[2]/div/div[1]/div[1]/div[1]/div[1]/div[2]/a[1]/text()") \
            .extract_first()
        if book_author is not None:
            item['book_author'] = book_author.replace(' ', '').replace('\n', '')
        else:
            item['book_author'] = None

        if "出版社" in content:
            publisher = re.findall(r"<span class=\"pl\">出版社:</span>(.*?)<br>", content, re.S)
            item['publisher'] = "".join(publisher).replace('\n', '').replace(' ', '').replace("\xa0", "")
        else:
            item['publisher'] = ""
        if "出版年" in content:
            date = re.findall(r"<span class=\"pl\">出版年:</span>(.*?)<br>", content, re.S)
            item['date'] = "".join(date).replace('\n', '').replace(' ', '').replace("\xa0", "")
        else:
            item['date'] = ""
        if "定价" in content:
            price = re.findall(r"<span class=\"pl\">定价:</span>(.*?)<br>", content, re.S)
            item['price'] = "".join(price).replace('\n', '').replace(' ', '').replace("\xa0", "")
        else:
            item['price'] = ""
        item['tags'] = "|".join(tags)
        item['intro'] = response.xpath("//*[@id=\"link-report\"]/span[1]/div/p[1]/text()").extract_first()
        item['rate'] = response.xpath("//*[@id=\"interest_sectl\"]/div/div[2]/strong/text()").extract_first()
        item['rate_pl'] = response.xpath("//*[@id=\"interest_sectl\"]/div/div[2]/div/div[2]/span/a/span/text()") \
            .extract_first()
        item['five_star'] = response.xpath("//*[@id=\"interest_sectl\"]/div/span[2]/text()").extract_first()
        item['four_star'] = response.xpath("//*[@id=\"interest_sectl\"]/div/span[4]/text()").extract_first()
        item['three_star'] = response.xpath("//*[@id=\"interest_sectl\"]/div/span[6]/text()").extract_first()
        item['two_star'] = response.xpath("//*[@id=\"interest_sectl\"]/div/span[8]/text()").extract_first()
        item['one_star'] = response.xpath("//*[@id=\"interest_sectl\"]/div/span[10]/text()").extract_first()
        yield item
        for i in range(3):
            comment = CommentItem()
            url = response.xpath("//*[@id=\"comments\"]/ul/li[{0}]/div/h3/span[2]/a/@href"
                                 .format(i + 1)).extract_first()
            if url is not None:
                url = response.urljoin(url)
                yield scrapy.Request(url, callback=self.parse_critic)
            comment['ID'] = response.url.split('/')[-2]
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
            yield comment

    def parse_critic(self, response):
        critic = CriticItem()
        critic['user_name'] = response.xpath("//*[@id=\"profile\"]/div/div[2]/div[1]/div/div/text()[1]").extract_first()
        critic['join_date'] = response.xpath("//*[@id=\"profile\"]/div/div[2]/div[1]/div/div/text()[2]").extract_first()
        critic['user_address'] = response.xpath("//*[@id=\"profile\"]/div/div[2]/div[1]/div/a/text()").extract_first()
        yield critic
