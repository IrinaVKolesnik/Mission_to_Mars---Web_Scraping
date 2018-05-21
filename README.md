# Mission to Mars - Web Scraping project

This project uses Pandas, requests, BeautifulSoup, splinter, selenium webdriver, MongoDB(Flask_pymongo), and Flask, to scrape data about Mars and display on the webpage.

## Step 1 - Scraping

### Mars News
Scrapes news title and paragraph text from most recent story at [NASA site](https://mars.nasa.gov/news/) using BeautifulSoup.

### Featured Image
Uses the web driver to scrape JPL's Featured Space Image from [JPL NASA site](https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars). 

### Mars Weather
Scrapes Mars weather from [Twitter](https://twitter.com/marswxreport?lang=en0).

### Mars Facts
Uses pandas html feature to scrape a Mars data table from the [Mars Facts webpage](http://space-facts.com/mars/).

### Mars Hemispheres
Obtains high resolution images for each of Mar's hemispheres from [USGS Astrogeology site](https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars).


## Step 2 - MongoDB and Flask Application
Creating a new HTML page that displays all of the information that was scraped from the URLs above using MongoDB with Flask templating.