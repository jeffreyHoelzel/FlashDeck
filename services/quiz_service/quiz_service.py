from flask import Flask, jsonify
from flask_cors import CORS
import random

# Classes needed to run FlashDeck
from Utilities.card import Card
from Utilities.deck import Deck
from Utilities.quiz import Quiz
from Utilities.database import db, DATABASE_URL

app = Flask(__name__)
CORS(app)

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URL

db.init_app(app)

@app.route("/quiz/quiz_deck/<int:deck_id>", methods=["GET"])
def start_quiz(deck_id):
    deck = Deck.query.get(deck_id)

    if not deck:
        return jsonify({"error": "Deck not found."}), 404

    flashcards = [{"id": card.id, "question": card.question, "answer": card.answer} for card in deck.cards]

    if not flashcards:
        return jsonify({"error": "This deck has no flashcards."}), 400

    random.shuffle(flashcards)

    return jsonify({"deck_id": deck.id, "deck_name": deck.name, "flashcards": flashcards}), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002, debug=True)
