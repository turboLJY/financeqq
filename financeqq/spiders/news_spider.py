#encoding:utf-8
import scrapy
import re
from scrapy.selector import Selector
from financeqq.items import FinanceqqItem
from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.contrib.spiders import CrawlSpider,Rule

class ExampleSpider(CrawlSpider):
    name = "qqnews"
    allowed_domains = ["finance.qq.com"]
    start_urls = ['http://finance.qq.com/']
    rules=(
        Rule(LinkExtractor(allow=r"/([a-zA-Z]+)+/20161212+/*"),
        callback="parse_news",follow=True),
    )
    def printcn(suni):
        for i in uni:
            print uni.encode('utf-8')
    def parse_news(self,response):
        item = FinanceqqItem()
        item['news_thread']=response.url.strip().split('/')[-1][:-4]
        # self.get_thread(response,item)
        self.get_title(response,item)
        self.get_time(response,item)
        self.get_url(response,item)
        self.get_news_from(response,item)
        self.get_from_url(response,item)
        self.get_text(response,item)
        #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!remenber to Retrun Item after parse
        return item 
    def get_title(self,response,item):
        title=response.xpath("/html/head/title/text()").extract()
        if title:
            # print 'title:'+title[0][:-5].encode('utf-8')
            item['news_title']=title[0][:-7]

    def get_time(self,response,item):
        time=response.xpath("//div[@id='Main-Article-QQ']/div/div[1]/div[1]/div[1]/div/div[1]/span[2]/text()").extract()
        if time:
            # print 'time'+time[0][:-5].encode('utf-8')
            item['news_time']=time[0]

    def get_news_from(self,response,item):
        news_from=response.xpath("//div[@id='Main-Article-QQ']/div/div[1]/div[1]/div[1]/div/div[1]/span[1]/a/text()").extract()
        if news_from:
            # print 'from'+news_from[0].encode('utf-8')     
            item['news_from']=news_from[0]

    def get_from_url(self,response,item):
        from_url=response.xpath("//div[@id='Main-Article-QQ']/div/div[1]/div[1]/div[1]/div/div[1]/span[1]/a/@href").extract()
        if from_url:
            # print 'url'+from_url[0].encode('utf-8')       
            item['from_url']=from_url[0]    

    def get_text(self,response,item):
        news_body=response.xpath("//div[@id='Cnt-Main-Article-QQ']/p/text()").extract()
        if news_body:
            # for  entry in news_body:
            #   print entry.encode('utf-8')
            item['news_body']=news_body 
    def get_url(self,response,item):
        news_url=response.url
        if news_url:
            #print news_url 
            item['news_url']=news_url
