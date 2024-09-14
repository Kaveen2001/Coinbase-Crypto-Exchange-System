# wallet_service.py
from flask import Flask, jsonify, request

app = Flask(__name__)

wallets = []

@app.route('/wallet', methods=['POST'])
def create_wallet():
    data = request.get_json()
    if not data or "username" not in data:
        return jsonify({'message': 'Invalid data'}), 400
    
    new_wallet = {
        "username": data["username"],
        "balance_usd": 1000,  # Starting balance
    }
    wallets.append(new_wallet)
    return jsonify(new_wallet), 201

@app.route('/wallet/<username>', methods=['GET'])
def get_wallet(username):
    wallet = next((w for w in wallets if w["username"] == username), None)
    if wallet:
        return jsonify(wallet), 200
    return jsonify({'message': 'Wallet not found'}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003)
