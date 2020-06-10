# from splinter import Browser
# from bs4 import BeautifulSoup as bs
# import time

# Dependencies
from bs4 import BeautifulSoup
import requests
import pymongo

import pandas as pd
from splinter import Browser


def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {"executable_path": "/usr/local/bin/chromedriver"}
    return Browser("chrome", **executable_path, headless=False)


def scrape_info():

    #MARS FACTS

    url = "https://space-facts.com/mars/"
    tables = pd.read_html(url)
    mars_facts_df = tables[0]
    html_table = mars_facts_df.to_html()
    dict = {"fact_table": html_table}
    dummy = 1




    # browser = init_browser()

    # # Visit visitcostarica.herokuapp.com
    # url = "https://visitcostarica.herokuapp.com/"
    # browser.visit(url)

    # time.sleep(1)

    # # Scrape page into Soup
    # html = browser.html
    # soup = bs(html, "html.parser")

    # # Get the average temps
    # avg_temps = soup.find('div', id='weather')

    # # Get the min avg temp
    # min_temp = avg_temps.find_all('strong')[0].text

    # # Get the max avg temp
    # max_temp = avg_temps.find_all('strong')[1].text

    # # BONUS: Find the src for the sloth image
    # relative_image_path = soup.find_all('img')[2]["src"]
    # sloth_img = url + relative_image_path

    # # Store data in a dictionary
    # costa_data = {
    #     "sloth_img": sloth_img,
    #     "min_temp": min_temp,
    #     "max_temp": max_temp
    # }

    # # Close the browser after scraping
    # browser.quit()

    # # Return results
    # return costa_data




# TEST DB INSERT 

import pymongo
# Setup connection to mongodb
conn = "mongodb://localhost:27017"
client = pymongo.MongoClient(conn)

# Select database and collection to use
db = client.mars_app
facts = db.facts
print("db set up")

# Run the scrape function
#MARS FACTS

url = "https://space-facts.com/mars/"
tables = pd.read_html(url)
mars_facts_df = tables[0]
html_table = mars_facts_df.to_html()
dict = {"fact_table": html_table}

facts.insert(dict)

print("Data Uploaded!")