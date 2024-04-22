import json
from flask import Blueprint, request, jsonify
from flask_restful import Api, Resource
from datetime import datetime

from model.highscores import HighScore  # Import the HighScore model

highscore_api = Blueprint('highscore_api', __name__, url_prefix='/api/highscores')
api = Api(highscore_api)

class HighScoreAPI:        
    class _CRUD(Resource):  
        def post(self): 
            body = request.get_json()
            name = body.get('player_name')
            game = body.get('game_name')
            score = body.get('player_score')

            if not all([name, game, score]):
                return {'message': 'Player name, game name, or score missing'}, 400

            try:
                high_score = HighScore(player_name=name, game_name=game, player_score=score)
                high_score.save()
                return {'message': 'High score added successfully'}, 201
            except Exception as e:
                return {'message': 'Error adding high score', 'error': str(e)}, 500

    api.add_resource(_CRUD, '/')
