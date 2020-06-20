from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from music250.items import Music250Item, MusicDetailItem


class Music(CrawlSpider):
    name = 'music'
    allowed_domains = ['music.douban.com']
    start_urls = ['https://music.douban.com/top250/']
    rules = (
        Rule(LinkExtractor(allow=r"/subject/\d+/$"), callback='parse_detail', follow=True),
        Rule(LinkExtractor(allow=r"/?start=\d+"), callback='parse_top250', follow=True),
    )

    def parse_detail(self, response):
        detailItem = MusicDetailItem()
        detailItem["comment_number"] = response.xpath('//*[@property="v:average"]/text()').extract_first()
        yield detailItem

    def parse_top250(self, response):
        li_list = response.xpath('//*[@id="content"]/div/div[1]/div/table')
        for li in li_list:
            item = Music250Item()
            item['url'] = li.xpath('tr/td[1]/a/@href').extract_first()
            item['dbid'] = str(item['url']).split('/')[-2]
            item['music_news'] = li.xpath('tr/td[2]/div/p/text()').extract_first()
            item['music_name'] = li.xpath('tr/td[2]/div/a/text()').extract_first()
            yield item





