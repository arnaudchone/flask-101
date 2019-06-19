""" Simple REST API """
# wsgi.py
from flask import Flask, jsonify, abort
app = Flask(__name__)

PRODUCTS = [
    {'id': 1, 'name': 'Skello'},
    {'id': 2, 'name': 'Socialive.tv'},
    {'id': 3, 'name': 'Product3'}
]

PRODUCTS_MAP = {
    item['id']:item
    for item in PRODUCTS
}

@app.route('/')
def hello():
    return "Hello Dude!"

@app.route('/api/v1/products')
def product_to_json():
    return jsonify(PRODUCTS)

@app.route('/api/v1/products/<int:product_id>')
def get_product(product_id):
    try:
        return jsonify(PRODUCTS_MAP[product_id])
    except KeyError:
        abort(404)
# result = [item for item in PRODUCTS if item['id'] == product_id]
# if len(result) > 0:
# return jsonify(result)
# abort(404)

@app.route('/api/v1/products/<int:product_id>', methods=['DELETE'])
def del_product(product_id):
    result = [item for item in PRODUCTS if item['id'] == product_id]
    if type(result) != 'NoneType':
        return jsonify(result)
    abort(404)
