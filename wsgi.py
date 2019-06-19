""" Simple REST API """
# wsgi.py
from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello Dude!"

@app.route('/api/v1/products')
def product_to_json():
    PRODUCTS = [
        {'id': 1, 'name': 'Skello'},
        {'id': 2, 'name': 'Socialive.tv'},
        {'id': 3, 'name': 'Product3'}
    ]
    return jsonify(PRODUCTS)
