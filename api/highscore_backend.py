from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///highscores.db'  # SQLite database file path
db = SQLAlchemy(app)

class HighScore(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    player_name = db.Column(db.String(50), nullable=False)
    game_name = db.Column(db.String(50), nullable=False)
    player_score = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"HighScore(player_name='{self.player_name}', game_name='{self.game_name}', player_score={self.player_score})"

@app.route('/api/highscores', methods=['POST'])
def add_high_score():
    data = request.json
    player_name = data.get('player_name')
    game_name = data.get('game_name')
    player_score = data.get('player_score')

    if not all([player_name, game_name, player_score]):
        return jsonify({'message': 'Incomplete data provided'}), 400

    high_score = HighScore(player_name=player_name, game_name=game_name, player_score=player_score)
    db.session.add(high_score)
    db.session.commit()

    return jsonify({'message': 'High score added successfully'}), 201

if __name__ == '__main__':
    db.create_all()  # Create database tables
    app.run(debug=True)
