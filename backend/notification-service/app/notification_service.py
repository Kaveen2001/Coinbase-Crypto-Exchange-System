# notification_service.py
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/notify', methods=['POST'])
def send_notification():
    data = request.get_json()
    if not data or not all(k in data for k in ("message", "recipient")):
        return jsonify({'message': 'Invalid data'}), 400
    
    # Simulate sending a notification
    return jsonify({'message': f"Notification sent to {data['recipient']}: {data['message']}"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5004)
