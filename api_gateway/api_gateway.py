from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

SERVICE_URL = "http://localhost:5000"

@app.route("/api/<path:path>", methods=["GET", "POST", "PUT", "DELETE"])
def forward_request(path):
    url = f"{SERVICE_URL}/{path}"

    response = requests.request(
        method=request.method, 
        url=url, 
        headers={key: value for key, value in request.headers if key != "Host"}, 
        json=request.get_json(), 
        params=request.args
    )

    return jsonify(response.json()), response.status_code

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
