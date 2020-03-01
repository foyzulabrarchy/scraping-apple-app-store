import requests 
from bs4 import BeautifulSoup 
import csv 
import pandas as pd
URLS = pd.read_csv('links.csv', squeeze=True)
quotes=[]
for URL in URLS:
	r = requests.get(URL) 

	soup = BeautifulSoup(r.content, 'html5lib') 

	quote = {}
	quote['URL'] = URL

	try:
		data = soup.find('h1', attrs = {'class':'product-header__title app-header__title'}) 
		only_alpha = ""
		for char in data.text:
			if ord(char) >= 65 and ord(char) <= 90:
				only_alpha += char
			elif ord(char) >= 97 and ord(char) <= 122:
				only_alpha += char
			elif ord(char) == 32:
				only_alpha += char
		quote['AppName'] = only_alpha.strip()
	except Exception as e:
		quote['AppName'] = "n/a"
	
	
	

	try:
		data = soup.find('h2', attrs = {'class':'product-header__subtitle app-header__subtitle'}) 
		quote['Subtitle'] = data.text
	except Exception as e:
		quote['Subtitle'] = "n/a"
	try:
		data = soup.find('div', attrs = {'class':'we-customer-ratings__count small-hide medium-show'})
		quote['Total number of ratings'] = data.text.split(" Ratings",1)[0]
	except Exception as e:
		quote['Total number of ratings'] = "n/a"

	try:
		data = soup.find('div', attrs = {'class':'l-row l-row--peek'}) 
		row4 = data.findAll('figure', attrs = {'class':'we-star-rating ember-view we-customer-review__rating we-star-rating--large'})
		try:
			quote['rating1'] = row4[0].get('aria-label').split(" out of 5",1)[0]
		except Exception as e:
			quote['rating1'] = "n/a"
		try:
			quote['rating2'] = row4[1].get('aria-label').split(" out of 5",1)[0]
		except Exception as e:
			quote['rating2'] = "n/a"
		try:
			quote['rating3'] = row4[2].get('aria-label').split(" out of 5",1)[0]
		except Exception as e:
			quote['rating3'] = "n/a"
	except Exception as e:
		quote['rating1'] = "n/a"
		quote['rating2'] = "n/a"
		quote['rating3'] = "n/a"

	quotes.append(quote)
	



filename = 'rating.csv'
df=pd.DataFrame(quotes)
df.to_csv(filename,header=True, index=True)
print("Done Scraping.")









/*
new_r = requests.get(URL) 
			new_soup = BeautifulSoup(new_r.content, 'html5lib')








			*//*

try:
		html = requests.get(URL,
                            headers={'Cache-Control': 'no-cache'}).content
		df_list = pd.read_html(html)
		quotes = quotes.append(df_list[-1])
		time.sleep(2)
	except Exception as e:
		print("Error on this url "+ URL)
		#quotes = quotes.append([''])
		time.sleep(2)


*/