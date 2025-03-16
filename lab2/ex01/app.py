from flask import Flask, render_template ,request, json
from cipher.caesar import CaesarCipher

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/caesar")
def caesar():
    return render_template("caesar.html")

@app.route("/encrypt", methods=["POST"])
def caesar_encrypt():
    if request.method == "POST":
        text = request.form.get("InputPlainText", "").strip()  # Tránh KeyError
        key = int(request.form.get("InputKey", 0))

        Caesar = CaesarCipher()
        encrypted_text = Caesar.encrypt_text(text, key)

        return f"text: {text}<br/>key: {key} <br/> encrypted text: {encrypted_text}"
    else:
        return "Invalid request method", 400


@app.route("/decrypt", methods=["POST"])
def caesar_decrypt():
    text = request.form.get("inputCipherText", "").strip()  # Tránh lỗi KeyError
    key = request.form.get("InputKeyCipher", 0)

    try:
        key = int(key)  # Chuyển key thành số nguyên
    except ValueError:
        key = 0  # Nếu lỗi, đặt key về 0

    if not text:
        return "Error: No text received!", 400

    Caesar = CaesarCipher()
    decrypted_text = Caesar.decrypt_text(text, key)

    return f"text: {text}<br/>key: {key} <br/> decrypted text: {decrypted_text}"


#main function
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050, debug=True)