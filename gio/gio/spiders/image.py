# -*- coding: utf-8 -*-
import scrapy


class ImageSpider(scrapy.Spider):
    name = "image"
    allowed_domains = ["developers.google.com"]
    start_urls = (
        'http://www.developers.google.com/',
    )

    def parse(self, response):
        pass
