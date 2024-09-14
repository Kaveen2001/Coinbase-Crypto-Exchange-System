from flask import Flask, render_template, jsonify

app = Flask(__name__)

# Home Route
@app.route('/')
def home():
    return render_template('index.html')

# API Endpoint to Get Market Data
@app.route('/api/market_data')
def market_data():
    # Sample data to represent market data from Coinbase
    data = {
        "BTC": {"price": "50000", "volume": "1500"},
        "ETH": {"price": "4000", "volume": "10000"}
    }
    return jsonify(data)

# API Endpoint for Trading
@app.route('/api/trade', methods=['POST'])
def trade():
    # Logic for trade execution (e.g., Buy/Sell orders)
    return jsonify({"message": "Trade executed successfully!"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)