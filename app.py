from flask import Flask, render_template
from pymongo import MongoClient
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Get MongoDB credentials from environment variables
MONGODB_USERNAME = os.getenv('MONGODB_USERNAME')
MONGODB_PASSWORD = os.getenv('MONGODB_PASSWORD')
MONGODB_CLUSTER = os.getenv('MONGODB_CLUSTER')

# Connected to MongoDB Atlas using credentials from environment variables
mongo_uri = f"mongodb+srv://{MONGODB_USERNAME}:{MONGODB_PASSWORD}@{MONGODB_CLUSTER}/?retryWrites=true&w=majority"
client = MongoClient(mongo_uri)

# Connected to the 'shop_db' database and 'products' collection
db = client.shop_db
products_collection = db.products

print(db)

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/products')
def products():
    products_data = products_collection.find()  # Fetched all products
    return render_template('products.html', products=products_data)

if __name__ == '__main__':
    app.run(debug=True)
