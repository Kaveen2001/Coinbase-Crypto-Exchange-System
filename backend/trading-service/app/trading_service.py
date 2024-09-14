# trading_service.py
from flask import Flask, jsonify, request

app = Flask(__name__)

orders = []

@app.route('/trade', methods=['POST'])
def trade():
    data = request.get_json()
    if not data or not all(k in data for k in ("crypto", "amount", "side")):
        return jsonify({'message': 'Invalid data'}), 400
    
    new_order = {
        "id": len(orders) + 1,
        "crypto": data["crypto"],
        "amount": data["amount"],
        "side": data["side"],  # buy or sell
    }
    orders.append(new_order)
    return jsonify(new_order), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
