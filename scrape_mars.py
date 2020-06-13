
# Dependencies
from bs4 import BeautifulSoup
import requests
import pymongo

import pandas as pd
from splinter import Browser
from selenium import webdriver
import time




def scrape_info():

    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)
    
    #NASA NEWS

    url = 'https://mars.nasa.gov/news/'

    browser.visit(url)
    browser.is_element_present_by_css('li.slide', wait_time=10)

    html = browser.html
    
    # Parse HTML with Beautiful Soup
    soup = BeautifulSoup(html, 'html.parser')
    article = soup.find('div', class_="article_teaser_body").text

    title = soup.find(class_ ="bottom_gradient")
    title = title.find('h3').text


    #JPL MARS SPACE IMAGE
    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url)

    html = browser.html
    soup = BeautifulSoup(html, 'lxml')
    footer = soup.find('footer')
    string_footer = str(footer)
    string_footer= string_footer.split('data-fancybox-href="')[1].split('" data-link')[0]
    featured_image_url = 'https://www.jpl.nasa.gov' + string_footer

    #MARS WEATHER TWITTER

    url = 'https://twitter.com/MarsWxReport'
    driver = webdriver.Chrome()
    driver.implicitly_wait(5) # seconds
    driver.get(url)

    element = driver.find_element_by_class_name("css-901oao")
    tweet = element.text
    

    # MARS FACTS

    url = "https://space-facts.com/mars/"
    tables = pd.read_html(url, index_col = 0)
    mars_facts_df = tables[0]
    html_table = mars_facts_df.to_html()

    # MARS HEMISHERES

    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url)

    html = browser.html
    # Parse HTML with Beautiful Soup
    soup = BeautifulSoup(html, 'html.parser')
    hemispheres = soup.find_all('h3')
    hemi_list = []
    link_list = []

    for h in hemispheres:
        hemi_text = h.text.strip('Enhanced')
        hemi_list.append(hemi_text)
        #Click on Hemisphere Link
        try:
                browser.click_link_by_partial_text(hemi_text)
        except:
                print("Scraping Complete")
        #Find image link
        link = browser.find_link_by_text('Original').first['href']
        link_list.append(link)
        #Go Back a Page
        browser.visit(url)


    #Hard coding values scraped earlier when the site was working
    hemi_list = ['Cerberus Hemisphere ', 'Schiaparelli Hemisphere ', 'Syrtis Major Hemisphere ', 'Valles Marineris Hemisphere ']
    link_list = ['https://astrogeology.usgs.gov/cache/images/f5e372a36edfa389625da6d0cc25d905_cerberus_enhanced.tif_full.jpg', 'https://astrogeology.usgs.gov/cache/images/3778f7b43bbbc89d6e3cfabb3613ba93_schiaparelli_enhanced.tif_full.jpg', 'https://astrogeology.usgs.gov/cache/images/555e6403a6ddd7ba16ddb0e471cadcf7_syrtis_major_enhanced.tif_full.jpg', 'https://astrogeology.usgs.gov/cache/images/b3c7c6c9138f57b4756be9b9c43e3a48_valles_marineris_enhanced.tif_full.jpg']


    #WRITE ALL TO DICT

    mars_dict = {"article_title": title, "article_excerpt": article, "feature_image": featured_image_url, "fact_table": html_table, "mars_weather": tweet,  "hemisphere_list": hemi_list, "hemisphere_pic": link_list}


    return(mars_dict)

