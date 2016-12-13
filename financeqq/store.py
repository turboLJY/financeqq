#encoding: utf-8
from pymongo import MongoClient
from scrapy.conf import settings
client = MongoClient(
            settings['MONGODB_SERVER'],
            settings['MONGODB_PORT']
        )
News_qqDB = client[settings['MONGODB_DB']]
collect_qq_161212 = News_qqDB[settings['MONGODB_COLLECTION']]