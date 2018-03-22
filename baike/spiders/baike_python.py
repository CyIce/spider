# -*- coding: utf-8 -*-
import scrapy

from baike.items import BaikeItem


class BaikePythonSpider(scrapy.Spider):
    # 爬虫名称
    name = 'baike_python'
    # 爬虫的允许域范围
    allowed_domains = ['baike.baidu.com']
    # 爬虫的起始地址
    start_urls = ['https://baike.baidu.com/item/Python/407313']
    # 网站的基础网址，用于补全短链接
    base_url = "https://baike.baidu.com"
    # 爬取网页的次数
    crawl_times=0

    def parse(self, response):
        # 当前爬取网页中满足条件的节点
        page_nodes = response.xpath("/html/body//div/a[@target='_blank' and @href]")
        # 储存每一次爬取的数据
        item = BaikeItem()
        for node in page_nodes:
            name = node.xpath("./text()").extract()
            url = node.xpath("./@href").extract()
            if len(name)<=0 or len(url)<=0 or (str)(url).find("http")!=-1:
                continue
            new_url = self.base_url + url[0]
            item["name"] = name[0]
            item["url"] = new_url
            print(item['url'])
            item["title"]=new_url
            yield item

            if self.crawl_times<=500:
                self.crawl_times += 1
                yield scrapy.Request(new_url,callback=self.parse)
