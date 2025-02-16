from flask import Flask, request, jsonify
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

with app.app_context():
    db.create_all()

@app.route("/create_new_deck", methods=["POST"])
def create_deck():
    data = request.get_json()

    if not data or "name" not in data or "cards" not in data:
        return jsonify({"error": "Invalid input. 'name' and 'cards' fields are required."}), 400

    # Check if a deck with the same name already exists
    existing_deck = Deck.query.filter_by(name=data["name"]).first()
    if existing_deck:
        return jsonify({"error": "A deck with this name already exists."}), 409

    # Create a new deck
    new_deck = Deck(name=data["name"])
    db.session.add(new_deck)
    db.session.commit()

    for card_data in data["cards"]:
        question = card_data.get("question")
        answer = card_data.get("answer")
        if question and answer:
            new_card = Card(question=question, answer=answer, deck_id=new_deck.id)
            db.session.add(new_card)

    db.session.commit()

    return jsonify({"message": "Deck created successfully!", "deck_id": new_deck.id}), 201


#TODO: Add a way to delete entire decks
@app.route("/edit_existing_deck/<int:deck_id>", methods=["PUT"])
def edit_deck(deck_id):
    data = request.get_json()

    if not data:
        return jsonify({"error": "No data provided."}), 400

    deck = Deck.query.get(deck_id)
    if not deck:
        return jsonify({"error": "Deck not found."}), 404

    if "name" in data:
        deck.name = data["name"]

    if "cards" in data:
        for card_data in data["cards"]:
            card_id = card_data.get("id")
            question = card_data.get("question")
            answer = card_data.get("answer")

            if card_id:
                existing_card = Card.query.get(card_id)
                if existing_card:
                    existing_card.question = question
                    existing_card.answer = answer
            else:
                new_card = Card(question=question, answer=answer, deck_id=deck.id)
                db.session.add(new_card)

    db.session.commit()
    return jsonify({"message": "Deck updated successfully!"}), 200

@app.route("/delete_deck/<int:deck_id>", methods=["DELETE"])
def delete_deck(deck_id):
    try:
        deck = Deck.query.get(deck_id)

        if not deck:
            return jsonify({"error": "Deck not found."}), 404
        
        db.session.delete(deck)
        db.session.commit()

        return jsonify({"message": "Deck deleted successfully!"}), 200
    
    except Exception as e:
        db.session.rollback()
        print(f"Error deleting deck: {e}")
        return jsonify({"error": "Internal server error."}), 500

@app.route("/get_all_decks", methods=["GET"])
def get_all_decks():
    decks = Deck.query.all()
    deck_list = [{"id": deck.id, "name": deck.name} for deck in decks]

    return jsonify({"decks": deck_list}), 200

@app.route("/get_deck/<int:deck_id>", methods=["GET"])
def get_deck(deck_id):
    deck = Deck.query.get(deck_id)

    if not deck:
        return jsonify({"error": "Deck not found."}), 404

    cards = [{"id": card.id, "question": card.question, "answer": card.answer} for card in deck.cards]

    return jsonify({"id": deck.id, "name": deck.name, "cards": cards}), 200

@app.route("/quiz_deck/<int:deck_id>", methods=["GET"])
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
    app.run(host="0.0.0.0", port=5000, debug=True)
