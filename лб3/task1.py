from flask import Flask, jsonify, request

app = Flask(__name__)

catalog = [
    {"id": 1, "name": "Chair", "price": 50, "material": "Wood"},
    {"id": 2, "name": "Desk", "price": 150, "material": "Metal"},
    {"id": 3, "name": "Lamp", "price": 30, "material": "Plastic"}
]

@app.route('/items', methods=['GET'])
def get_items():
    return jsonify({"items": catalog})

@app.route('/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    item = next((i for i in catalog if i["id"] == item_id), None)
    if item:
        return jsonify(item)
    else:
        return jsonify({"error": "Item not found"}), 404

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=8000)
