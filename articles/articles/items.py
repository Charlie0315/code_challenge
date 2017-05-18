import scrapy


class ArticlesItem(scrapy.Item):

    url = scrapy.Field()
    author = scrapy.Field()