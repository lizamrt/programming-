from flask import Flask, jsonify, request, Response
import base64

app = Flask(__name__)

USERS_FILE = 'users.txt'

def load_users():
    users = {}
    with open(USERS_FILE, 'r') as file:
        for line in file:
            username, password = line.strip().split(':')
            users[username] = password
    return users

def authenticate():
    auth = request.headers.get('Authorization')
    if not auth:
        return False
    try:
        auth_type, credentials = auth.split()
        if auth_type != 'Basic':
            return False
        username, password = base64.b64decode(credentials).decode('utf-8').split(':')
        users = load_users()
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
    catalog = [
        {"id": 1, "name": "Chair", "price": 50, "material": "Wood"},
        {"id": 2, "name": "Desk", "price": 150, "material": "Metal"},
        {"id": 3, "name": "Lamp", "price": 30, "material": "Plastic"}
    ]
    return jsonify({"items": catalog})

@app.route('/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    if not authenticate():
        return Response(
            'Access Denied',
            status=401,
            headers={'WWW-Authenticate': 'Basic realm="Login Required"'}
        )
    catalog = [
        {"id": 1, "name": "Chair", "price": 50, "material": "Wood"},
        {"id": 2, "name": "Desk", "price": 150, "material": "Metal"},
        {"id": 3, "name": "Lamp", "price": 30, "material": "Plastic"}
    ]
    item = next((i for i in catalog if i["id"] == item_id), None)
    if item:
        return jsonify(item)
    else:
        return jsonify({"error": "Item not found"}), 404
    
if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=8000)