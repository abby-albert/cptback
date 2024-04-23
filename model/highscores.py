from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Initialize Flask app and database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///highscores.db'  # Adjust the database URI as needed
db = SQLAlchemy(app)

# Define the HighScore model
class HighScore(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    player_name = db.Column(db.String(100), nullable=False)
    game_name = db.Column(db.String(100), nullable=False)
    player_score = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'<HighScore {self.player_name} - {self.game_name}: {self.player_score}>'

    def save(self):
        db.session.add(self)
        db.session.commit()

# Import and register the highscore_api blueprint

from highscore.py import highscore_api
app.register_blueprint(highscore_api)

if __name__ == '__main__':
    app.run(debug=True)
