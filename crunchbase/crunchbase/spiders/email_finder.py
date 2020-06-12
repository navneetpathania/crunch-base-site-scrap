import scrapy
from bs4 import BeautifulSoup
import lxml
from selenium import webdriver
import time
from ..items import CrunchbaseItem
import csv





class EmailFinder(scrapy.Spider):
	name = 'emailfinder'
	# start_urls = ['https://www.crunchbase.com/search/principal.investors/a4a64455698861c30228725f3f9f09a4']

	def __init__(self,filename=None):
		if filename:
			with open(filename,'r') as r:
				self.start_urls = r.readlines()
				
				# urls.append(row[0])
		# self.driver = webdriver.Chrome()

	def parse(self,response):
		# item = CrunchbaseItem()
		# print(response.url)
		# time.sleep(1)
		# self.driver.get(response.url)
		soup = BeautifulSoup(response.text,'lxml')
		# print(soup.title)
		info_table = soup.findAll('fields-card',class_='ng-star-inserted')
		try:
			print(info_table[3].contents[0].contents[0].contents[1])
		except:
			pass
		# main_wrapper = soup.find('div',class_='body-wrapper')
		# # print(main_wrapper)
		# grid_rows = main_wrapper.findAll('grid-row')
		# # for row in grid_rows:
		# 	# print(grid_rows[0])
		# 	# .contents[0].contents[2].find('a')['href']
		# company_link = grid_rows[0].contents[1].contents[0].contents[1].contents[0].contents[0]['href']
		# print(company_link)
			# url = 'https://www.crunchbase.com' + company_link
			# print(url)
# 			item['comp_link'] = url

			# yield item
			# time.sleep(1)
			# driver.get(url)
			# yield 