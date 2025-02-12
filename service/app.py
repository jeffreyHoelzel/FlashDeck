from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# testing
@app.route("/", methods=["GET", "POST"])
def test():
    return jsonify({"message": "Hello, world!"}), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
