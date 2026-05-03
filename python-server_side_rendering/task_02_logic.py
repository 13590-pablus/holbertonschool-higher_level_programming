from flask import Flask, render_template
import json
import os

app = Flask(__name__)

@app.route('/items')
def items():
    # JSON faylından məlumatları oxuyuruq
    items_list = []
    if os.path.exists('items.json'):
        with open('items.json', 'r') as file:
            data = json.load(file)
            items_list = data.get('items', [])

    # Məlumatları HTML şablonuna göndəririk
    return render_template('items.html', items=items_list)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
