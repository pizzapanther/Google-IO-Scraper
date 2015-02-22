# -*- coding: utf-8 -*-
import scrapy
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor

from gio.items import GioItem

class Image1Spider (CrawlSpider):
  name = "image1"
  allowed_domains = [
    "developers.google.com",
    "developer.chrome.com",
    "developer.android.com",
    "cloud.google.com",
    "googledevelopers.blogspot.com",
    
    #"appurify.com",
    #"www.chromium.org",
    #"www.firebase.com",
    #"golang.org",
    #"www.html5rocks.com",
    #"www.stackdriver.com",
    
    "www.dartlang.org",
    "developer.nest.com",
    "www.polymer-project.org",
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
      
class Image2Spider (Image1Spider):
  name = "image2"
  allowed_domains = [
    #"angularjs.org",
    "www.dartlang.org",
    "developer.nest.com",
    "www.polymer-project.org",
  ]
  start_urls = (
    #'https://angularjs.org/',
    'https://www.dartlang.org/',
    'https://developer.nest.com/',
    'https://www.polymer-project.org/',
  )
  