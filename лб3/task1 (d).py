from flask import Flask, jsonify, request

app = Flask(__name__)

catalog = [
    {"id": 1, "name": "Chair", "price": 50, "material": "Wood"},
    {"id": 2, "name": "Desk", "price": 150, "material": "Metal"},
    {"id": 3, "name": "Lamp", "price": 30, "material": "Plastic"}
]

@app.route('/items', methods=['GET'])
def get_items():
    return jsonify({"items": catalog}), 200

@app.route('/items', methods=['POST'])
def add_item():
    try:
        data = request.get_json()
        if not data or not all(k in data for k in ("id", "name", "price", "material")):
            return jsonify({"error": "Invalid data. Required fields: id, name, price, material"}), 400

        if any(item['id'] == data['id'] for item in catalog):
            return jsonify({"error": "Item with this ID already exists"}), 400

        catalog.append(data)
        return jsonify({"message": "Item added successfully", "item": data}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/items/<int:item_id>', methods=['GET', 'PUT', 'DELETE'])
def handle_item(item_id):
    item = next((i for i in catalog if i["id"] == item_id), None)

    if request.method == 'GET':
        if item:
            return jsonify(item), 200
        return jsonify({"error": "Item not found"}), 404

    if request.method == 'PUT':
        try:
            if not item:
                return jsonify({"error": "Item not found"}), 404

            data = request.get_json()
            if not data or not all(k in data for k in ("name", "price", "material")):
                return jsonify({"error": "Invalid data. Required fields: name, price, material"}), 400

            item.update(data)
            return jsonify({"message": "Item updated successfully", "item": item}), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    if request.method == 'DELETE':
        if not item:
            return jsonify({"error": "Item not found"}), 404

        catalog.remove(item)
        return jsonify({"message": "Item deleted successfully"}), 200

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=8000)
