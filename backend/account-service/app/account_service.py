# account_service.py
from flask import Flask, jsonify, request

app = Flask(__name__)

users = []

@app.route('/account/register', methods=['POST'])
def register():
    data = request.get_json()
    if not data or not all(k in data for k in ("username", "password")):
        return jsonify({'message': 'Invalid data'}), 400
    
    new_user = {
        "id": len(users) + 1,
        "username": data["username"],
        "password": data["password"]
    }
    users.append(new_user)
    return jsonify(new_user), 201

@app.route('/account/login', methods=['POST'])
def login():
    data = request.get_json()
    user = next((u for u in users if u["username"] == data["username"] and u["password"] == data["password"]), None)
    if user:
        return jsonify({'message': 'Login successful'}), 200
    return jsonify({'message': 'Invalid credentials'}), 401

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
