from flask import Blueprint, jsonify
from controllers.quiz_controller import *

quiz_bp = Blueprint("quiz", __name__, url_prefix="/quizzes")

@quiz_bp.route("/quiz_deck/<int:deck_id>", methods=["GET"])
def _start_quiz(deck_id):
    data = start_quiz(deck_id)

    if data == "Deck not found":
        return jsonify({"error": "Deck not found."}), 404

    if data == "Flashcards not found":
        return jsonify({"error": "This deck has no flashcards."}), 400

    return jsonify(data), 200
