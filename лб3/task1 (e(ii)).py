from flask import Flask, jsonify

app = Flask(__name__)

CATALOG_FILE = 'Liza.txt'

def load_catalog():
    catalog = []
    try:
        with open(CATALOG_FILE, 'r') as file:
            for line in file:
                parts = line.strip().split(',')
                catalog.append({
                    "id": int(parts[0]),
                    "name": parts[1],
                    "price": float(parts[2]),
                    "material": parts[3]
                })
    except FileNotFoundError:
        pass
    return catalog

def save_catalog(catalog):
    with open(CATALOG_FILE, 'w') as file:
        for item in catalog:
            line = f"{item['id']},{item['name']},{item['price']},{item['material']}\n"
            file.write(line)

catalog = load_catalog()

@app.route('/items', methods=['GET'])
def get_items():
    return jsonify({"items": catalog})

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=8000)
