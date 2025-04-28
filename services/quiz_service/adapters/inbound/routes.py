from flask import Blueprint, request, jsonify
from adapters.outbound.sqlalchemy_quiz_repository import SQLAlchemyQuizRepository
from application.services.create_quiz_service import CreateQuizService
from adapters.outbound.database import db

routes = Blueprint("quiz_routes", __name__)

quiz_repo = SQLAlchemyQuizRepository()
create_quiz_service = CreateQuizService(quiz_repo)

@routes.route("/quiz/create_new_quiz", methods=["POST"])
def create_quiz():
    data = request.get_json()

    if not data or "name" not in data or "decks" not in data:
        return jsonify({"error": "Invalid input. 'name' and 'decks' fields are required."}), 400

    try:
        create_quiz_service.execute(data["name"], data["decks"])
        return jsonify({"message": "Quiz created successfully."}), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 409
