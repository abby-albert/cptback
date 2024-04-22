from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class HighScore(db.Model):
    """Model for high scores."""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    game = db.Column(db.String(100), nullable=False)
    score = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"<HighScore(name='{self.name}', game='{self.game}', score={self.score})>"

from flask import Flask

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///highscores.db'

db.init_app(app)

