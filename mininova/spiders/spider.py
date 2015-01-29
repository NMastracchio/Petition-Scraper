from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from mininova.items import PetitionItem


class PetitionCrawler(CrawlSpider):
	name='petition'
	allowed_domains=['petitions.whitehouse.gov']
	start_urls=['https://petitions.whitehouse.gov/petitions/popular']
	#,'https://petitions.whitehouse.gov/petitions/more/popular/2/2/0/%20/'
	rules=[Rule(LinkExtractor(allow=['https:\/\/petitions.whitehouse.gov\/petition\/([\w-]*)\/\w*']),'parse_petition')]

	def parse_petition(self,response):
		self.item
		petition=PetitionItem()
		petition['url']=response.url
		petition['title']=response.xpath('//h1/text()').extract()
		petition['description']=response.xpath('//div[@id="petition-detail"]/div/p/text()').extract()
		petition['date']=response.xpath('//div[@id="petition-detail"]/div/div[@class="date"]/text()').extract()
		petition['issues']=response.xpath('//div[@id="petition-detail"]/div/div[@class="issues"]/a/text()').extract()
		petition['signatures']=response.xpath('//div[@id="total-on"]/div[@class="num-block num-block2"]/text()').extract()
		#petition['signaturesNeeded']
		#petition['currentSignatures']
		return petition
'''import scrapy
from mininova.items import DmozItem

class DmozSpider(scrapy.Spider):
	name='dmoz'
	allowed_domains=['dmoz.org']
	start_urls=[
		'http://www.dmoz.org/Computers/Programming/Languages/Python/Books/',
		'http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/'
	]

	def parse(self,response):
		for sel in response.xpath('//ul/li'):
			item=DmozItem()
			item['title']=sel.xpath('a/text()').extract()
			item['link']=sel.xpath('a/@href').extract()
			item['desc']=sel.xpath('text()').extract()
			yield item'''