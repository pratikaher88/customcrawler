# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy import signals
from urllib.parse import urlparse

import re


class ToScrapeCSSSpider(CrawlSpider):
    name = "toscrapespiderax"

    def __init__(self, *args, **kwargs):
        self.job_data_id = kwargs.get('job_data_id', '1111')
        self.url = kwargs.get('url', "https://lovdata.no/")
        self.domain = urlparse(self.url).netloc
        self.start_urls = [self.url]
        self.allowed_domains = [self.domain]
        # self.custom_settings = {'CLOSESPIDER_PAGECOUNT': 10}
        self.regex_string = r'.*'+re.escape(self.domain)+ r'.*'
        ToScrapeCSSSpider.rules = [Rule(LinkExtractor(allow=(self.regex_string)), callback='parse_item', follow=True)]
        
        super(ToScrapeCSSSpider, self).__init__(*args, **kwargs)

    def parse_item(self, response):    
        yield {
            'extracted_url' : response.url
        }

    # @classmethod
    # def from_crawler(cls, crawler, *args, **kwargs):
    #     spider = super(ToScrapeCSSSpider, cls).from_crawler(crawler, *args, **kwargs)
    #     crawler.signals.connect(spider.spider_closed, signal=signals.spider_closed)
    #     return spider


    # def spider_closed(self, spider):

    #     print('Spider closed: %s', spider.name)
        

    # start_urls = [
    #     'https://lovdata.no/',
    # ]
    # allowed_domains = ['lovdata.no']
    
    # rules = [Rule(LinkExtractor(allow=(r'.*lovdata.no.*')), callback='parse_item', follow=True)]

    # custom_settings = {
    #     'CLOSESPIDER_PAGECOUNT': 400
    # }

    # def __init__(self, *args, **kwargs):
    #     self.start_urls = [self.url]
    #     self.allowed_domains = [self.domain]
        # ToScrapeCSSSpider.rules = [
        #    Rule(LinkExtractor(allow=(r'.*'+re.escape(self.domain)+'.*')), callback='parse_item', follow=True)],
        # ]

    # def parse_item(self, response):
        
    #     yield {
    #         'text' : response.url
    #     }

        # for quote in response.css("div.quote"):
        #     yield {
        #         'text': quote.css("span.text::text").extract_first(),
        #         'author': quote.css("small.author::text").extract_first(),
        #         'tags': quote.css("div.tags > a.tag::text").extract()
        #     }

        # next_page_url = response.css("li.next > a::attr(href)").extract_first()
        # if next_page_url is not None:
        #     yield scrapy.Request(response.urljoin(next_page_url))


