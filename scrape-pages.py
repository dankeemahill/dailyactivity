import csv
import glob
from bs4 import BeautifulSoup

'''
Create CSV of crimes reported on each daily activity log page downloaded with sacpd-scraper.py
'''

my_writer = csv.writer(open('crimes.csv', 'wb'), quoting=csv.QUOTE_MINIMAL)
my_writer.writerow(['Number', 'Crime', 'Address', 'Time', 'url'])

def readFile(nameOfFile):
    text = open(nameOfFile, 'r')
    text = text.read()
    return text

def scrapeSoup(soup, crime_count, url):
	ids = ['#northContent', '#centralContent', '#southContent']
	crime_count=0
	for div_id in ids:
		crime_grafs = soup.select(div_id)
		for graf in crime_grafs:
			crime_line = graf.select('p')
			for line in crime_line:
				crime_text = line.get_text()
				if "12-" in crime_text:
					print crime_text
					crime_list = crime_text.split(',')
					if len(crime_list) == 5:
						number = crime_list[0]
						crime = crime_list[1]
						address = crime_list[2]
						time = crime_list[3]
						try:
							my_writer.writerow([number, crime, address, time, url])
						except:
							my_writer.writerow(['', '', '', ''])
						crime_count += 1
	return crime_count
'''			crime_text = crime_line.get_text()
			crime_list = crime_text.split(',')
			number = crime_list[0]
			crime = crime_list[1]
			address = crime_list[2]
			time = crime_list[3]
			try:
				my_writer.writerow([number, crime, address, time, url])
			except:
				my_writer.writerow(['', '', '', ''])
	return crime_count'''

count=0

for url in glob.glob("pages/view.*"):
	soup = BeautifulSoup(readFile(url))
	count += scrapeSoup(soup, count, url)
	#scrapeSoup(soup, count, url)
print u'CRIME COUNT: %s' % (count)
