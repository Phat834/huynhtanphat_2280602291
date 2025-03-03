from cipher.vigenere import VigenereCipher
from flask import Flask, request, jsonify

app = Flask(__name__)

vigenere_cipher = VigenereCipher()

@app.route('/api/vigenere/encrypt',methods=['POST'])
def vigenere_encrypt():
    data = request.json()
    plain_text = data['plain_text']
    key = data['key']
    encrypted_text = vigenere_cipher.vigenere_encrypt(plain_text, key)
    return jsonify({'encrypted_text': encrypted_text})

@app.route('/api/vigenere/decrypt',methods=['POST'])
def vigenere_decrypt():
    data = request.json()
    encrypted_text = data['encrypted_text']
    key = data['key']
    decrypted_text = vigenere_cipher.vigenere_decrypt(encrypted_text, key)
    return jsonify({'decrypted_text': decrypted_text})