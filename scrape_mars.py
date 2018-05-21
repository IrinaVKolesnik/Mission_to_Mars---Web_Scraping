
# coding: utf-8

# In[1]:


# Imports
import pandas as pd
import requests
import re
import time
from splinter import Browser
from splinter.exceptions import ElementDoesNotExist
from bs4 import BeautifulSoup as bs
from selenium import webdriver
import pymongo

def init_browser():
	executable_path = {'executable_path': 'chromedriver.exe'}
	return Browser('chrome', **executable_path, headless=False)

# Scrape function
def scrape():
	browser = init_browser()
	mars_data = {}

# In[2]:

	# Scrape the NASA Mars News site
	url = "https://mars.nasa.gov/news/" 
	response = requests.get(url)


	# In[3]:


	# Collect news title and paragrapgh text
	soup = bs(response.text, 'html5lib')
	news_title = soup.find("div", class_="content_title").text
	news_p = soup.find("div", class_ = "rollover_description_inner").text
	print(news_title)
	print(news_p)


	# In[4]:


	#JPL Mars Space Images - Featured Image
	# visit the JPL website. Use splinter to navigate the site.
	executable_path = {'executable_path': 'chromedriver.exe'}
	browser = Browser('chrome', **executable_path, headless=False)
	jpl_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
	browser.visit(jpl_url)

	# Click each of the links to the hemispheres 
	# in order to find the image url to the full resolution image.
	time.sleep(10)
	browser.click_link_by_partial_text('FULL IMAGE')
	time.sleep(10)
	browser.click_link_by_partial_text('more info')
	time.sleep(10)

	# Create BeautifulSoup object; parse with 'html.parser'
	html = browser.html
	soup = bs(html, 'html.parser')

	# Scrape the featured image.
	results = soup.find('article')
	second_link = results.find('figure', 'lede').a['href']
	jpl_link = "https://www.jpl.nasa.gov"
	featured_image_url = jpl_link + second_link


	# In[5]:


	print(featured_image_url)


	# In[6]:


	#Mars Weather from Twitter
	executable_path = {'executable_path': 'chromedriver.exe'}
	browser = Browser('chrome', **executable_path, headless=False)
	weather_url='https://twitter.com/marswxreport?lang=en'
	browser.visit(weather_url)
	time.sleep(5)
	weather_html = browser.html
	weather_soup = bs(weather_html, 'html5lib')
	MarsWxReport = weather_soup.find('ol', class_='stream-items')
	mars_weather = MarsWxReport.find('p', class_="TweetTextSize").text


	# In[7]:


	print(mars_weather)


	# In[8]:


	#Mars Facts
	#Visit the Mars Facts webpage here and use Pandas to scrape the table containing facts about the planet including
	#Diameter, Mass, etc.
	url = 'https://space-facts.com/mars/'
	table = pd.read_html(url)
	table


	# In[9]:


	df = table[0]
	df.columns = ['0','1']
	df.rename(columns={'0':'Parameters', '1':'Values'}, inplace=True)
	df.set_index('Parameters', inplace=True)
	df


	# In[10]:


	#Use Pandas to convert the data to a HTML table string.
	mars_facts_html = df.to_html()
	mars_facts_html.replace('\n', '')
	print(mars_facts_html)


	# In[11]:


	facts_table = df.to_html('facts_table.html')
	
	# In[12]:


	# Mars Hemispheres
	#Visit the USGS Astrogeology site here to obtain high resolution images for each of Mar's hemispheres.

	url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
	browser.visit(url)
	html = browser.html
	soup = bs(html, 'html.parser')

	# Empty list of image urls
	hemisphere_image_urls = []

	products = soup.find("div", class_ = "result-list" )
	hemispheres = products.find_all("div", class_="item")

	for hemisphere in hemispheres:
	    title = hemisphere.find("h3").text
	#get rid of "Enhanced" in the titles    
	    title = title.replace("Enhanced", "")
	    second_link = hemisphere.find("a")["href"]
	    whole_link = "https://astrogeology.usgs.gov/" + second_link    
	    browser.visit(whole_link)
	    html = browser.html
	    soup=bs(html, "html.parser")
	    downloads = soup.find("div", class_="downloads")
	    image_url = downloads.find("a")["href"]
	    hemisphere_image_urls.append({"title": title, "img_url": image_url})
	   


	# In[13]:


	hemisphere_image_urls

	mars = {
	 "news_title": news_title,
	 "news_p": news_p,
	 "featured_image_url": featured_image_url,
	 "facts_table": mars_facts_html,
	 "mars_weather": mars_weather,
	 "hemisphere_image_urls": hemisphere_image_urls
	 }
	browser.quit()
	return mars