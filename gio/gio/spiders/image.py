# -*- coding: utf-8 -*-
import scrapy
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor

from gio.items import GioItem

class ImageSpider (CrawlSpider):
  name = "image"
  allowed_domains = [
    "developers.google.com",
    "developer.chrome.com",
    "developer.android.com",
    "cloud.google.com",
    "googledevelopers.blogspot.com",
    "angularjs.org",
    "appurify.com",
    "www.chromium.org",
    "www.dartlang.org",
    "www.firebase.com",
    "golang.org",
    "www.html5rocks.com",
    "developer.nest.com",
    "www.polymer-project.org",
    "www.stackdriver.com",
  ]
  start_urls = (
    'https://developers.google.com/',
  )
  
  rules = [
  	Rule(LinkExtractor(allow=[r'.*']), callback='parse_item', follow=True)
  ]
  
  def parse_item (self, response):
    content = scrapy.Selector(response=response).xpath('//body')
    
    for node in content:
      item = GioItem()
      item['url'] = response.url
      item['image_urls'] = node.xpath('//img/@src').extract()
      
      yield item
      