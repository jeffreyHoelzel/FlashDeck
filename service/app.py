from flask import Flask
from flask_cors import CORS
from config import Config
from extensions import db
from routes.deck_routes import deck_bp
from routes.quiz_routes import quiz_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    CORS(app, origins=app.config["CORS_ORIGINS"])

    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["SQLALCHEMY_DATABASE_URI"] = app.config["DATABASE_URL"]
    db.init_app(app)

    with app.app_context():
        db.create_all()

    app.register_blueprint(deck_bp)
    app.register_blueprint(quiz_bp)

    return app


if __name__ == "__main__":
    create_app().run(host="0.0.0.0", port=5000, debug=True)
