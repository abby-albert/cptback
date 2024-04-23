from flask_sqlalchemy import SQLAlchemy

# Create a SQLAlchemy instance
db = SQLAlchemy()

# Import the HighScore model so it can be accessed from other parts of the application
from .highscores import HighScore
