# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from sahibinden.items import SahibindenItem
import logging

class SatilikArsalarSpider(scrapy.Spider):
    name = 'satilik-arsalar'
    allowed_domains = ['www.sahibinden.com']
    # Önce en yeni ilanı getir
    start_urls = ['https://www.sahibinden.com/satilik-arsa?pagingSize=50&sorting=date_desc']


    def parse(self, response):
        item_links = response.css('.classifiedTitle::attr(href)').extract()
        for a in item_links:
            yield scrapy.Request( "https://www.sahibinden.com" + a, callback=self.parse_detail_page)
        next_page_url = response.xpath('//li/a[text()="Sonraki "]/@href').extract_first()
        if next_page_url is not None:
            yield scrapy.Request(response.urljoin(next_page_url))

    def parse_detail_page(self, response):
        ilanid = str(response.xpath('.//span[@class="classifiedId"]/text()').extract_first()).strip()
        baslik = str(response.xpath('.//div[@class="classifiedDetailTitle"]/h1/text()').extract_first()).strip()
        boyut = str(response.xpath('.//strong[contains(text(),\'m²\')]/following::span[1]/text()').extract_first()).strip()
        fiyat = str(response.xpath('.//div[contains(@class, "classifiedInfo")]/h3/text()').extract_first()).strip()
        m2fiyat = str(response.xpath('.//strong[contains(text(),\'m² Fiyatı\')]/following::span[1]/text()').extract_first()).strip()
        il =str(response.xpath('.//div[contains(@class, "classifiedInfo")]/h2/a[1]/text()').extract_first()).strip()
        ilce =str(response.xpath('.//div[contains(@class, "classifiedInfo")]/h2/a[2]/text()').extract_first()).strip()
        imar = str(response.xpath('//strong[contains(text(),\'İmar Durumu\')]/following::span[1]/text()').extract_first()).strip()

        item = SahibindenItem()
        item['ilanid'] = ilanid
        item['baslik'] = baslik
        item['boyut'] = boyut
        item['fiyat'] = fiyat
        item['m2fiyat'] = m2fiyat
        item['il'] = il
        item['ilce'] = ilce
        item['imar'] = imar
        yield item
