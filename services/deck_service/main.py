from flask import Flask
from flask_cors import CORS
from adapters.outbound.database import db
from adapters.inbound.routes import routes
import os

def create_app():
    app = Flask(__name__)
    CORS(app)

    # Configuration
    db_path = os.path.join(os.path.dirname(__file__), "db")
    os.makedirs(db_path, exist_ok=True)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db/flashdeck.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)

    with app.app_context():
        db.create_all()

    app.register_blueprint(routes)

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
