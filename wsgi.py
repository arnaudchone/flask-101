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

class Counter:
    def __init__(self):
        self.id = 3

    def next(self):
        self.id += 1
        return self.id

counter = Counter()

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
        return ('Deleted product', 204)
    else:
        return ('Product not found', 404)

@app.route('/api/v1/products/', methods=['POST'])
def create_product():
    body = request.get_json()
    next_val = counter.next()
    PRODUCTS_MAP[next_val] = {'id': next_val, 'name': body['name']}
    return ('', 200)


