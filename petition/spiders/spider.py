from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from petition.items import PetitionItem
import re


class PetitionCrawler(CrawlSpider):
	name = 'petition'
	allowed_domains = ['petitions.whitehouse.gov']
	start_urls = ['https://petitions.whitehouse.gov/petitions/more/popular/1/2/0/',
		'https://petitions.whitehouse.gov/petitions/more/popular/2/2/0/',
		'https://petitions.whitehouse.gov/petitions/more/popular/3/2/0/',
		'https://petitions.whitehouse.gov/petitions/more/popular/4/2/0/',
		'https://petitions.whitehouse.gov/petitions/more/popular/5/2/0/',
		'https://petitions.whitehouse.gov/petitions/more/popular/6/2/0/']

	#start_urls=['https://petitions.whitehouse.gov/petitions/popular']
	#,'https://petitions.whitehouse.gov/petitions/more/popular/2/2/0/%20/'
	def my_process_value(value):
		m = re.search(r"petition\\\/([\w-]+\\\/[\w]+)", value)
		if m:
			return m.group(1)

	def process_links(self, links):
		#print "LINKS: %r" % type(links[0])
		for link in links:
			sUrl = link.url
			sUrl = sUrl[:41] + "/" + sUrl[62:]
			sUrl = sUrl.replace("%5C", "")
			link.url = sUrl
		return links

	def parse_petition(self, response):
		#print self, response
		petition = PetitionItem()
		petition['url'] = response.url
		petition['title'] = response.xpath('//h1/text()').extract()
		petition['description'] = response.xpath('//div[@id = "petition-detail"]/div/p/text()').extract()
		petition['date'] = response.xpath('//div[@id = "petition-detail"]/div/div[@class = "date"]/text()').extract()
		petition['issues'] = response.xpath('//div[@id = "petition-detail"]/div/div[@class = "issues"]/a/text()').extract()
		petition['signatures'] = response.xpath('//div[@id = "total-on"]/div[@class = "num-block num-block2"]/text()').extract()
		#petition['signaturesNeeded']
		#petition['currentSignatures']
		return petition

	rules = [
		Rule(LinkExtractor(allow = (), process_value = my_process_value), 'parse_petition', process_links = 'process_links')
	]

	