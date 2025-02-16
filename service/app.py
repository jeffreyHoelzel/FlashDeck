from flask import Flask, request, jsonify
from flask_cors import CORS

# Classes needed to run FlashDeck
from Utilities.card import Card
from Utilities.deck import Deck
from Utilities.quiz import Quiz
from Utilities.database import db, DATABASE_URL

app = Flask(__name__)
CORS(app)

app.config["SQLALCHEMY_TRACK_NOTIFICATIONS"] = False
app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URL

db.init_app(app)

with app.app_context():
    db.create_all()

# testing
@app.route("/", methods=["GET", "POST"])
def test():
    return jsonify({"message": "Hello, world!"}), 200

@app.route("/create_new_deck", methods=["GET"])
def create_deck():
    if request.method == "GET":
        pass

@app.route("/edit_existing_deck", methods=["GET"])
def edit_deck():
    pass

@app.route("/quiz_deck", methods=["GET"])
def start_quiz():
    pass

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
