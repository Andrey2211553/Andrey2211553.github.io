from flask import Flask, jsonify, render_template, redirect, request, abort
from json import load, dump

app = Flask(__name__)

with open('orders.json', 'r+') as f:
    config = load(f)

@app.route('/<string:name>/<string:product>/<string:price>/<string:Discord>', methods=['POST'])
def create_task(name, product, price, Discord):
    config['LastOrder'] = f"Name: {name}, Product: {product}, Price: {price}, Discord: {Discord}"
    with open('orders.json', 'r+') as f:
        dump(config, f, ensure_ascii=False, indent=4)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
