""" Simple REST API """
# wsgi.py
from flask import Flask, jsonify, abort, request
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

@app.route('/api/v1/products/')
def product_to_json():
    return jsonify(list(PRODUCTS_MAP.values()))

@app.route('/api/v1/products/<int:product_id>')
def get_product(product_id):
    # product = PRODUCTS_MAP.get(product_id)
    # if product is None:
    #     abort(404)
    # return jsonify(product)
    try:
        return jsonify(PRODUCTS_MAP[product_id])
    except KeyError:
        abort(404)

@app.route('/api/v1/products/<int:product_id>', methods=['DELETE'])
def del_product(product_id):
    if product_id in PRODUCTS_MAP:
        del PRODUCTS_MAP[product_id]
        return ('', 204)
    else:
        return ('Product not found', 404)

