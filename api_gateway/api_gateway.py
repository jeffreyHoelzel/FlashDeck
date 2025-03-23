from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

SERVICES = {
    "deck": "http://deck-service:5001", 
    "quiz": "http://quiz-service:5002"
}

@app.route("/api/<service>/<path:path>", methods=["GET", "POST", "PUT", "DELETE"])
def forward_request(service, path):
    if service not in SERVICES:
        return jsonify({"error", "400 Bad Request"}), 400
    
    url = f"{SERVICES[service]}/{service}/{path}"

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
