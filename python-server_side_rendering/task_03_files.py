from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)

def read_json():
    try:
        with open('products.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def read_csv():
    products = []
    try:
        with open('products.csv', 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                products.append(row)
    except FileNotFoundError:
        pass
    return products

@app.route('/products')
def display_products():
    source = request.args.get('source')
    product_id = request.args.get('id')
    
    error_message = None
    products_list = []

    # 1. Source (Mənbə) yoxlanışı
    if source == 'json':
        products_list = read_json()
    elif source == 'csv':
        products_list = read_csv()
    else:
        error_message = "Wrong source"
        return render_template('product_display.html', error_message=error_message)

    # 2. ID yoxlanışı və filtrasiya
    if product_id:
        filtered_products = [p for p in products_list if str(p['id']) == str(product_id)]
        if not filtered_products:
            error_message = "Product not found"
            products_list = []
        else:
            products_list = filtered_products

    return render_template('product_display.html', products=products_list, error_message=error_message)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
