import os

class Config:
    DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///flashdeck.db")
    CORS_ORIGINS = ["*"]
