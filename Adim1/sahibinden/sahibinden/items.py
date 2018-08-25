# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SahibindenItem(scrapy.Item):
    # define the fields for your item here like:
    imar = scrapy.Field()
    ilanid = scrapy.Field()
    baslik= scrapy.Field()
    boyut = scrapy.Field()
    fiyat = scrapy.Field()
    m2fiyat = scrapy.Field()
    il = scrapy.Field()
    ilce = scrapy.Field()
