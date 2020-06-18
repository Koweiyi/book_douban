# -*- coding: utf-8 -*-
import scrapy

from demo.items import DemoItem


class ScrapydSpider(scrapy.Spider):
    name = 'scrapyd'
    allowed_domains = ['lab.scrapyd.cn']
    start_urls = ['http://lab.scrapyd.cn/']

    def parse(self, response):
        quote = response.css("div.quote")

        item = DemoItem()

        for i in  quote:
            item['cont'] = i.css(".text::text").extract_first()
            tags = i.css(".tags .tag::text").extract()

            item['tag'] = ",".join(tags)

            yield item

        next_page = response.css("li.next a::attr(href)").extract_first()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield  scrapy.Request(next_page, callback=self.parse)
