from splinter import Browser
from bs4 import BeautifulSoup
import pandas as pd
from pprint import pprint

executable_path = {'executable_path': 'chromedriver.exe'}
browser = Browser('chrome', **executable_path, headless=False)

url = 'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'
browser.visit(url)

#NASA Mars NEWS 
html = browser.html
mars_news_soup = BeautifulSoup(html, 'html.parser')

#Title 
news_title = mars_news_soup.find('div', class_='content_title').text
news_title

#1st paragraph
news_p = mars_news_soup.find('div', class_='article_teaser_body').text
news_p

# Mars Space Featured Image 
#URL
url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
browser.visit(url)

#Find image
browser.click_link_by_partial_text('FULL IMAGE')

#Parse
html = browser.html
image_soup = BeautifulSoup(html, 'html.parser')

#Scrape
feat_img_url = image_soup.find('figure', class_='lede').a['href']
feat_img_full_url = f'https://www.jpl.nasa.gov{feat_img_url}'
feat_img_full_url

# Mars Tweet
#URL
url = 'https://twitter.com/marswxreport?lang=en'
browser.visit(url)

#Parse
html = browser.html
tweet_soup = BeautifulSoup(html, 'html.parser')

#Scarpe
first_tweet = tweet_soup.find('p', class_='TweetTextSize').text
first_tweet

# Mars Facts
# Mars Facts
url = 'https://space-facts.com/mars/'
tables = pd.read_html(url)
tables

df = tables[0]
df

#Convert to HTML table
df.to_html()

# Mars Hemispheres
url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
browser.visit(url)

# HTML link
html_hemispheres = browser.html

# Parse
soup = BeautifulSoup(html_hemispheres, 'html.parser')

# Retreive items
items = soup.find_all('div', class_='item')

# Create empty list 
hemisphere_image_urls = []

# Main URL
hemispheres_main_url = 'https://astrogeology.usgs.gov'

# Loop through the items
for item in items: 
    title = item.find('h3').text
    
    # Store link to image website
    partial_img_url = item.find('a', class_='itemLink product-item')['href']
    
    # Visit the link with image
    browser.visit(hemispheres_main_url + partial_img_url)
    
    # HTML INFO
    partial_img_html = browser.html
    
    # Parse info
    soup = BeautifulSoup( partial_img_html, 'html.parser')
    
    # Retrieve full image source 
    img_url = hemispheres_main_url + soup.find('img', class_='wide-image')['src']
    
    # Store info in list 
    hemisphere_image_urls.append({"title" : title, "img_url" : img_url})
    

# Display hemisphere_image_urls
hemisphere_image_urls