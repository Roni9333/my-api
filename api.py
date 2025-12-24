from flask import Flask, jsonify, request
import os

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"status": "API Running"})

@app.route("/hello")
def hello():
    name = request.args.get("name", "Roni")
    return jsonify({"message": f"Hello {name}"})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)