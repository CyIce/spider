# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BaikeItem(scrapy.Item):
    # 姓名
    name = scrapy.Field()
    # 标题
    title = scrapy.Field()
    # 网页的URL地址
    url = scrapy.Field()
