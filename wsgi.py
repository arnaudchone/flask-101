# wsgi.py
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello Dude!"

@app.route('/api/v1/products')
def hello():
    return "Hello Dude!"
