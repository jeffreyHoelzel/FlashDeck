from flask import Blueprint, request, jsonify
from adapters.outbound.sqlalchemy_deck_repository import SQLAlchemyDeckRepository
from application.services.create_deck_service import CreateDeckService
from adapters.outbound.database import db

routes = Blueprint("routes", __name__)

deck_repo = SQLAlchemyDeckRepository()
create_deck_service = CreateDeckService(deck_repo)

@routes.route("/deck/create_new_deck", methods=["POST"])
def create_deck():
    data = request.get_json()

    if not data or "name" not in data or "cards" not in data:
        return jsonify({"error": "Invalid input. 'name' and 'cards' fields are required."}), 400

    try:
        create_deck_service.execute(data["name"], data["cards"])
        return jsonify({"message": "Deck created successfully."}), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 409
