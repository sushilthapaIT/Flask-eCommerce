from flask import Flask, render_template
from pymongo import MongoClient

app = Flask(__name__)

# Connect to MongoDB Atlas
client = MongoClient("mongodb+srv://thapasushilit:Vp3NxfMary7hE6Pt@cluster0.is8lh.mongodb.net/")

db = client.shop_db  # Connect to the 'shop_db' database
products_collection = db.products  # Connect to the 'products' collection


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/products')
def products():
    products_data = products_collection.find()  # Fetch all products
    return render_template('products.html', products=products_data)

if __name__ == '__main__':
    app.run(debug=True)
