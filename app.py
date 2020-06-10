from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

import pymongo
 
# Create an instance of Flask
app = Flask(__name__)

# # Use PyMongo to establish Mongo connection
# mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_app")

# # Setup connection to mongodb
# conn = "mongodb://localhost:27017"
# client = pymongo.MongoClient(conn)

# # Select database and collection to use
# db = client.mars_app
# facts = db.facts


# Route to render index.html template using data from Mongo
@app.route("/")
def home():

    # return("hi this is the homepage")
    # # Find one record of data from the mongo database
    # destination_data = mongo.db.collection.find_one()

    # Return template and data
    return render_template("index.html", facts)


# Route that will trigger the scrape function
@app.route("/scrape")
def scrape():

    # Run the scrape function
    #mars_data = scrape_mars.scrape_info()
    scrape_mars.scrape_info()

    # # Update the Mongo database using update and upsert=True
    # mongo.db.collection.update({}, mars_data, upsert=True)

    # write a statement that finds all the items in the db and sets it to a variable
    inventory = list(facts.find())
    print(inventory)

    # Redirect back to home page
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
