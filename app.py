from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

import pymongo
 
# Create an instance of Flask
app = Flask(__name__)

# # Use PyMongo to establish Mongo connection
mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_app")

# Route to render index.html template using data from Mongo
@app.route("/")
def home():

    #return("hi this is the homepage")
    # # Find one record of data from the mongo database
    mars_dict = mongo.db.facts.find_one()

    # Return template and data
    return render_template("index_empty.html", mars_dict=mars_dict)


# Route that will trigger the scrape function
@app.route("/scrape")
def scrape():

    # Run the scrape function
    mars_dict = scrape_mars.scrape_info()

    # # Update the Mongo database
    mongo.db.facts.update({}, mars_dict, upsert=True)
    print("scrape done")

    # Redirect back to home page
    return redirect("/scraped")

# Route to render index.html template using data from Mongo
@app.route("/scraped")
def scraped():

    # return("hi this is the homepage")
    # # Find one record of data from the mongo database
    mars_dict = mongo.db.facts.find_one()

    # Return template and data
    return render_template("index.html", mars_dict=mars_dict)
if __name__ == "__main__":
    app.run(debug=True)
