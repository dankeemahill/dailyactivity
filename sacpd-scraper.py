import os
import re
import requests
from bs4 import BeautifulSoup

'''
Downloads daily activity log web pages for 1/1/12-12/30/12. 
'''

ids = ['northContent', 'centralContent', 'southContent']

crimes = []

base_url = 'http://www.sacpd.org/dailyactivity/view.aspx?publish_date=2012'

months = {'01': range(2,31), '02': range(1,29), '03': range(1,31), '04': range(1,30), '05': range(1,31),
	'06': range(1,30), '07': range(1,31), '08': range(1,31), '09': range(1,30), '10': range(1,31), 
	'11': range(1,30), '12': range(1,31)}

# loops months dict to make dates in publish_date=20120102 format to request urls
def make_urls(months):
	urls = []
	for month in months:
		for day in months[month]:
			#ones place digits must have 0 in front to match publish_date=20120102 format
			if len(str(day)) == 1:
				urls.append(base_url + str(month) + '0' + str(day))
			else:
				urls.append(base_url + str(month) + str(day))
	return urls

# downloads html page to pages directory 
def scrape(url):
	wgetCommand = "cd pages/; wget " + url
	os.system(wgetCommand)


for url in make_urls(months):
	crimes.append(scrape(url))

#because the 12/31/12 log is in 2013... sigh...
last_url = "http://www.sacpd.org/dailyactivity/view.aspx?publish_date=20130101"
scrape(last_url)
