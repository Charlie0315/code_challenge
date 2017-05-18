# -*- coding: utf-8 -*-
import scrapy
import csv
import re
import json
from bs4 import BeautifulSoup
from articles.items import ArticlesItem
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class ArticlesSpider(CrawlSpider):
	name = 'articles'
	with open('articles.csv', 'rb') as f:
		start_urls = [row[0].replace('\'', '') for  row in csv.reader(f)]

	with open('crawler_setting.csv', 'rb') as f2:
		domain_router = dict(csv.reader(f2))

	def parse(self, response):
		soup = BeautifulSoup(response.body)
			
		print 'crawled',response.url

		for domain, attrs in self.domain_router.items():
			if domain in response.url:
				attrs = json.loads(attrs)          # attrs={"href":"/users/.+"}
				for key, value in attrs.items():  
					attrs[key] = re.compile(value)    # attrs={"class":re(object)}
				try: author = soup.find_all(attrs=attrs)[0].text.strip()
				except: author = ''
				finally: break
			else:
				author = ''

		'''
		print 'crawled',response.url
		if soup.select('.author_name'):
			author = soup.select('.author_name')[0].text.strip()  #class='author_name'
			rule = 1
		elif soup.select('.author'):
			author = soup.select('.author')[0].text.strip()
			rule = 2
		elif soup.select('.author-link'):    
			author = soup.select('.author-link')[0].text.strip()
			rule = 3
		elif soup.select('.byline__author'):
			author = soup.select('.byline__author')[0].text.strip()
			rule = 4
		elif soup.find_all(href=re.compile("/users/.+")):
			author = soup.find_all(href=re.compile("/users/.+"))[0].text.strip()
			rule = 5
		elif soup.select('.cat_desc'):
			author = soup.select('.cat_desc')[0].text.strip()
			rule = 6
		elif soup.select('.stat-author'):
			author = soup.select('.stat-author')[0].text.strip()
			rule = 7
		elif soup.select('.js-authors-list'):
			author = soup.select('.js-authors-list')[0].text
			rule = 12		
		elif soup.find_all(rel="author"):
			author = soup.find_all(rel="author")[0].text.strip()
			rule = 8
		elif soup.find_all(href=re.compile("/user/.+")):
			author = soup.find_all(href=re.compile("/user/.+"))[0].text.strip()
			rule = 9
		elif soup.select('.fn'):
			author = soup.select('.fn')[0].text.strip()
			rule = 10
		else:
			author = ''
			rule = 11
			#error_articles.appends('{}, '.format(response.url))
		'''
		
		item = ArticlesItem()
		item['url'] = response.url
		item['author'] = author
		return item