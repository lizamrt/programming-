from flask import Flask, jsonify, request, Response
import base64

app = Flask(__name__)

users = {
    "admin": "liza12",
    "user": "lizauser"
}

catalog = [
    {"id": 1, "name": "Chair", "price": 50, "material": "Wood"},
    {"id": 2, "name": "Desk", "price": 150, "material": "Metal"},
    {"id": 3, "name": "Lamp", "price": 30, "material": "Plastic"}
]

def authenticate():
    auth = request.headers.get('Authorization')
    if not auth:
        return False
    try:
        auth_type, credentials = auth.split()
        if auth_type != 'Basic':
            return False
        username, password = base64.b64decode(credentials).decode('utf-8').split(':')
        return username in users and users[username] == password
    except Exception:
        return False

@app.route('/items', methods=['GET'])
def get_items():
    if not authenticate():
        return Response(
            'Access Denied', 
            status=401, 
            headers={'WWW-Authenticate': 'Basic realm="Login Required"'}
        )
    return jsonify({"items": catalog})

@app.route('/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    if not authenticate():
        return Response(
            'Access Denied', 
            status=401, 
            headers={'WWW-Authenticate': 'Basic realm="Login Required"'}
        )
    item = next((i for i in catalog if i["id"] == item_id), None)
    if item:
        return jsonify(item)
    else:
        return jsonify({"error": "Item not found"}), 404

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=8000)
