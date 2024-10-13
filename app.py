from flask import Flask, render_template
from pymongo import MongoClient

app = Flask(__name__)

# MongoDB connection
connection_string = "mongodb+srv://thapasushilit:Vp3NxfMary7hE6Pt@cluster0.is8lh.mongodb.net/"
client = MongoClient("your_mongodb_atlas_connection_string")
db = client.shop_db
products_collection = db.products

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/products')
def products():
    products = products_collection.find()
    return render_template('products.html', products=products)

if __name__ == '__main__':
    app.run(debug=True)
