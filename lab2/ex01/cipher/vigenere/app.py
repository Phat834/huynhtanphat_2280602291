from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/vigenere/encrypt', methods=['POST'])
def encrypt():
    data = request.get_json()
    if not data or 'plain_text' not in data or 'key' not in data:
        return jsonify({"error": "Invalid input"}), 400
    return jsonify({"message": "Encryption successful"})  # Placeholder

@app.route('/api/vigenere/decrypt', methods=['POST'])
def decrypt():
    data = request.get_json()
    if not data or 'cipher_text' not in data or 'key' not in data:
        return jsonify({"error": "Invalid input"}), 400
    return jsonify({"message": "Decryption successful"})  # Placeholder

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
