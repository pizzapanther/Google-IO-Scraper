# -*- coding: utf-8 -*-

# Scrapy settings for gio project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'pizzapanther'

SPIDER_MODULES = ['gio.spiders']
NEWSPIDER_MODULE = 'gio.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'PizzaPanther\'s Google IO Crawler paul.m.bailey@gmail.com'

LOG_LEVEL = 'INFO'
