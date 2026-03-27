from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route('/')
def home():
    return "Home page"

@app.route('/items')
def items():
    try:
        with open('items.json', 'r') as file:
            data = json.load(file)
            items_list = data.get("items", [])
    except Exception as e:
        print("Error reading JSON:", e)
        items_list = []

    return render_template('items.html', items=items_list)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
    from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route('/')
def home():
    return "Home page"

@app.route('/items')
def items():
    try:
        with open('items.json', 'r') as file:
            data = json.load(file)
            items_list = data.get("items", [])
    except Exception as e:
        print("Error reading JSON:", e)
        items_list = []

    return render_template('items.html', items=items_list)

if __name__ == '__main__':
    app.run(debug=True, port=5000)