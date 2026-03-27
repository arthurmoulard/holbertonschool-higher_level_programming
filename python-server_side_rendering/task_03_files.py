from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)

# --- Functions to read data ---
def read_json():
    try:
        with open('products.json', 'r') as file:
            return json.load(file)
    except Exception as e:
        print("Error reading JSON:", e)
        return []

def read_csv():
    products = []
    try:
        with open('products.csv', 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                # Convert types
                row['id'] = int(row['id'])
                row['price'] = float(row['price'])
                products.append(row)
    except Exception as e:
        print("Error reading CSV:", e)
    return products

# --- Route ---
@app.route('/products')
def products():
    source = request.args.get('source', '').lower()
    id_param = request.args.get('id', None)

    error = None
    product_list = []

    # Choose data source
    if source == 'json':
        product_list = read_json()
    elif source == 'csv':
        product_list = read_csv()
    else:
        error = "Wrong source"
        product_list = []

    # Filter by id if provided
    if id_param and not error:
        try:
            id_int = int(id_param)
            filtered = [p for p in product_list if p['id'] == id_int]
            if not filtered:
                error = "Product not found"
            product_list = filtered
        except ValueError:
            error = "Invalid id"

    return render_template('product_display.html', products=product_list, error=error)

if __name__ == '__main__':
    app.run(debug=True, port=5000)