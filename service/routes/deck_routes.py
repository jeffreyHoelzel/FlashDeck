from flask import Blueprint, request, jsonify
from controllers.deck_controller import *

deck_bp = Blueprint("deck", __name__, url_prefix="/decks")

@deck_bp.route("/create_new_deck", methods=["POST"])
def _create_deck():
    data = request.get_json()

    if not data or "name" not in data or "cards" not in data:
        return jsonify({"error": "Invalid input. 'name' and 'cards' fields are required."}), 400

    # Create a new deck
    new_deck = create_deck(data["name"], data["cards"])

    return jsonify({"message": "Deck created successfully!", "deck_id": new_deck.id}), 201

@deck_bp.route("edit_existing_deck/<int:deck_id>", methods=["PUT"])
def _edit_deck(deck_id):
    data = request.get_json()

    if not data:
        return jsonify({"error": "No data provided."}), 400
    
    deck = edit_deck(deck_id, name=data["name"], cards=data["cards"])

    if not deck:
        return jsonify({"error": "Deck not found."}), 404

    return jsonify({"message": "Deck updated successfully!"}), 200

@deck_bp.route("/delete_deck/<int:deck_id>", methods=["DELETE"])
def _delete_deck(deck_id):
    error = delete_deck(deck_id)

    if error == "No deck found":
        return jsonify({"error": "Deck not found."}), 404

    if error == "Error deleting deck":
        return jsonify({"error": "Internal server error."}), 500

    return jsonify({"message": "Deck deleted successfully!"}), 200

@deck_bp.route("/get_deck/<int:deck_id>", methods=["GET"])
def _get_deck(deck_id):
    deck = get_deck(deck_id)

    if not deck:
        return jsonify({"error": "Deck not found."}), 404

    return jsonify(deck), 200

@deck_bp.route("/get_all_decks", methods=["GET"])
def _get_all_decks():
    deck_list = get_all_decks()

    if not deck_list:
        return jsonify({"error": "Deck list not found"}), 404

    return jsonify({"decks": deck_list}), 200
