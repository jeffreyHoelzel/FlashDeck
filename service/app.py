from flask import Flask
from flask_cors import CORS
from config import Config
from database import init_db
from controllers.deck_controller import deck_bp
from controllers.quiz_controller import quiz_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    CORS(app, origins=app.config["CORS_ORIGINS"])
    init_db(app)

    app.register_blueprint(deck_bp)
    app.register_blueprint(quiz_bp)

    return app

if __name__ == "__main__":
    create_app().run(host="0.0.0.0", port=5000, debug=True)
